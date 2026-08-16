#!/usr/bin/env python3
"""Validate Aramyst asset and page manifests against schema and repository rules."""

from __future__ import annotations

import csv
import json
import re
import sys
from collections.abc import Iterable
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import SchemaError
except ImportError:
    Draft202012Validator = None
    SchemaError = Exception

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "manifest.json"
CSV_PATH = ROOT / "ASSET_MANIFEST.csv"
MARKDOWN_PATH = ROOT / "docs" / "ASSET_MANIFEST.md"
SCHEMA_PATH = ROOT / "schemas" / "asset-manifest.schema.json"
FILESYSTEM_ALLOWLIST_PATH = ROOT / "schemas" / "filesystem-integrity-allowlist.json"
EXTERNAL_AUTHORITY_REGISTRY_PATH = ROOT / "schemas" / "external-authority-registry.json"
DEPENDENCY_CLASSIFICATION_PATH = ROOT / "schemas" / "dependency-classification-registry.json"
DEPENDENCY_CLASSIFICATION_SCHEMA_PATH = ROOT / "schemas" / "dependency-classification-registry.schema.json"

STATUSES = {
    "planned",
    "briefed",
    "in-progress",
    "review",
    "approved",
    "exported",
    "published",
    "superseded",
    "archived",
}

MATERIALIZED_STATUSES = {"review", "approved", "exported", "published"}

CATEGORY_CODES = {
    "cover": "COVER",
    "map": "MAP",
    "character": "CHAR",
    "faction": "FACT",
    "location": "LOC",
    "symbol": "SYM",
    "typography": "TYPE",
    "prompt": "PROMPT",
    "reference": "REF",
    "misc": "MISC",
}

ASSET_DIRECTORY_ROOTS = {
    "characters",
    "covers",
    "exports",
    "factions",
    "locations",
    "maps",
    "pages",
    "prompts",
    "references",
    "symbols",
    "typography",
}

ALLOWLIST_CLASSIFICATIONS = {"superseded", "provenance"}
PROSE_DEPENDENCY_CLASSIFICATIONS = {
    "title_bound_authority",
    "composite_gate",
    "long_term_prose_gate",
}

VERSION_RE = re.compile(r"^v\d{3}$")
ASSET_ID_RE = re.compile(r"^AST-(COVER|MAP|CHAR|FACT|LOC|SYM|TYPE|PROMPT|REF|MISC)-\d{3}$")
PAGE_PATH_RE = re.compile(r"^pages/(\d{3})_([a-z0-9]+(?:-[a-z0-9]+)*)\.[a-z0-9.]+$")
FILE_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*(?:-v\d{3})?(?:-[a-z0-9]+)*\.[a-z0-9.]+$")
EXACT_EXTERNAL_ID_RE = re.compile(r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$")
AUTHORITY_RANGE_RE = re.compile(r"^(.+)-(\d+)[–-](.+)-(\d+)$")

CSV_FIELDS = [
    "asset_id",
    "title",
    "category",
    "context",
    "purpose",
    "status",
    "version",
    "drive_file_id",
    "drive_url",
    "drive_path",
    "github_source_path",
    "github_export_path",
    "prompt_reference_path",
    "owner",
    "dependencies",
    "approval",
    "required_dimensions",
    "subjects",
    "notes",
]


def load_json(path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        with path.open(encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError:
        errors.append(f"Missing required file: {path.relative_to(ROOT)}")
        return {}
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return {}
    if not isinstance(data, dict):
        errors.append(f"{path.relative_to(ROOT)} must contain a JSON object")
        return {}
    return data


def format_json_path(path: Iterable[Any]) -> str:
    rendered = "$"
    for part in path:
        if isinstance(part, int):
            rendered += f"[{part}]"
        else:
            rendered += f".{part}"
    return rendered


def safe_repository_relative_path(path_value: str) -> bool:
    if not path_value or path_value.startswith("/") or "\\" in path_value:
        return False
    return ".." not in Path(path_value).parts


def validate_data_schema(data: dict[str, Any], schema: dict[str, Any], label: str, errors: list[str]) -> None:
    if Draft202012Validator is None:
        errors.append(
            "Missing validation dependency: jsonschema. "
            "Install requirements-validation.txt before running the validator."
        )
        return
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        message = getattr(exc, "message", str(exc))
        errors.append(f"Invalid JSON Schema for {label}: {message}")
        return
    validator = Draft202012Validator(schema)
    schema_errors = sorted(
        validator.iter_errors(data),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    for error in schema_errors:
        path = format_json_path(error.absolute_path)
        errors.append(f"{label} schema violation at {path}: {error.message}")


def validate_json_schema(manifest: dict[str, Any], schema: dict[str, Any], errors: list[str]) -> None:
    validate_data_schema(manifest, schema, "manifest.json", errors)


def validate_project(project: Any, errors: list[str]) -> None:
    expected = {
        "id": "aramyst-book-assets",
        "format": "fixed-layout",
        "width_inches": 6,
        "height_inches": 9,
        "dpi": 300,
        "github_repository": "JamesJedi420/aramyst-book-assets",
        "google_drive_root_id": "1IBbWIFfAuJpB7I9jc7yrjb461mPnuGnq",
    }
    if not isinstance(project, dict):
        errors.append("project must be an object")
        return
    for key, value in expected.items():
        if project.get(key) != value:
            errors.append(f"project.{key} must equal {value!r}")
    if not isinstance(project.get("title"), str) or not project["title"].strip():
        errors.append("project.title must be a non-empty string")


def validate_asset(asset: Any, index: int, errors: list[str]) -> str | None:
    label = f"assets[{index}]"
    if not isinstance(asset, dict):
        errors.append(f"{label} must be an object")
        return None
    required = {
        "asset_id", "title", "category", "context", "purpose", "subjects",
        "required_dimensions", "status", "version", "drive_file_id", "drive_url",
        "drive_path", "github_source_path", "github_export_path", "prompt_reference_path",
        "owner", "dependencies", "approval", "notes",
    }
    missing = sorted(required - set(asset))
    if missing:
        errors.append(f"{label} missing fields: {', '.join(missing)}")
        return None
    asset_id = asset.get("asset_id")
    if not isinstance(asset_id, str) or not ASSET_ID_RE.fullmatch(asset_id):
        errors.append(f"{label}.asset_id has invalid format: {asset_id!r}")
        return None
    category = asset.get("category")
    if category not in CATEGORY_CODES:
        errors.append(f"{asset_id}: invalid category {category!r}")
    elif asset_id.split("-")[1] != CATEGORY_CODES[category]:
        errors.append(f"{asset_id}: ID category code does not match category {category!r}")
    for field in ("title", "context", "purpose", "subjects", "required_dimensions", "owner", "approval"):
        if not isinstance(asset.get(field), str) or not asset[field].strip():
            errors.append(f"{asset_id}: {field} must be a non-empty string")
    if asset.get("status") not in STATUSES:
        errors.append(f"{asset_id}: invalid status {asset.get('status')!r}")
    if not isinstance(asset.get("version"), str) or not VERSION_RE.fullmatch(asset["version"]):
        errors.append(f"{asset_id}: invalid version {asset.get('version')!r}")
    dependencies = asset.get("dependencies")
    if not isinstance(dependencies, list) or any(not isinstance(item, str) for item in dependencies):
        errors.append(f"{asset_id}: dependencies must be a list of strings")
    elif len(dependencies) != len(set(dependencies)):
        errors.append(f"{asset_id}: dependencies contain duplicates")
    drive_id = asset.get("drive_file_id", "")
    drive_url = asset.get("drive_url", "")
    github_source = asset.get("github_source_path", "")
    github_export = asset.get("github_export_path", "")
    if bool(drive_id) != bool(drive_url):
        errors.append(f"{asset_id}: drive_file_id and drive_url must be provided together")
    if drive_url and drive_id not in drive_url:
        errors.append(f"{asset_id}: drive_url does not contain drive_file_id")
    if not drive_id and not github_source:
        errors.append(f"{asset_id}: requires a Drive source or GitHub source path")
    if asset.get("status") in {"exported", "published"} and not github_export:
        errors.append(f"{asset_id}: exported or published assets require github_export_path")
    for path_field in ("github_source_path", "github_export_path"):
        path_value = asset.get(path_field, "")
        if path_value and not safe_repository_relative_path(path_value):
            errors.append(f"{asset_id}: {path_field} must be a safe repository-relative path")
        if path_value and not path_value.endswith("/") and not path_value.startswith("pages/"):
            filename = Path(path_value).name
            if not FILE_NAME_RE.fullmatch(filename):
                errors.append(f"{asset_id}: filename violates lowercase kebab-case rules: {filename}")
    return asset_id


def validate_pages(pages: Any, asset_ids: set[str], errors: list[str]) -> None:
    if not isinstance(pages, list):
        errors.append("pages must be an array")
        return
    numbers: set[int] = set()
    paths: set[str] = set()
    for index, page in enumerate(pages):
        label = f"pages[{index}]"
        if not isinstance(page, dict):
            errors.append(f"{label} must be an object")
            continue
        required = {"page_number", "page_slug", "file_path", "asset_id", "status", "version"}
        missing = sorted(required - set(page))
        if missing:
            errors.append(f"{label} missing fields: {', '.join(missing)}")
            continue
        number = page["page_number"]
        path = page["file_path"]
        if not isinstance(number, int) or not 1 <= number <= 999:
            errors.append(f"{label}.page_number must be an integer from 1 to 999")
        elif number in numbers:
            errors.append(f"Duplicate page number: {number}")
        else:
            numbers.add(number)
        if not isinstance(path, str) or not PAGE_PATH_RE.fullmatch(path):
            errors.append(f"{label}.file_path has invalid format: {path!r}")
        else:
            if path in paths:
                errors.append(f"Duplicate page path: {path}")
            paths.add(path)
            expected_prefix = f"{number:03d}_" if isinstance(number, int) else ""
            if expected_prefix and not Path(path).name.startswith(expected_prefix):
                errors.append(f"{label}: page number and filename prefix disagree")
        if page.get("asset_id") not in asset_ids:
            errors.append(f"{label}: unknown asset_id {page.get('asset_id')!r}")
        if page.get("status") not in STATUSES:
            errors.append(f"{label}: invalid status {page.get('status')!r}")
        if not isinstance(page.get("version"), str) or not VERSION_RE.fullmatch(page["version"]):
            errors.append(f"{label}: invalid version {page.get('version')!r}")
        if page.get("status") in {"exported", "published"} and isinstance(path, str) and not (ROOT / path).is_file():
            errors.append(f"{label}: exported page file is missing: {path}")


def read_csv(errors: list[str]) -> dict[str, dict[str, str]]:
    try:
        with CSV_PATH.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != CSV_FIELDS:
                errors.append("ASSET_MANIFEST.csv header mismatch. Expected: " + ",".join(CSV_FIELDS))
            rows: dict[str, dict[str, str]] = {}
            for line_number, row in enumerate(reader, start=2):
                asset_id = row.get("asset_id", "")
                if not asset_id:
                    errors.append(f"ASSET_MANIFEST.csv line {line_number}: missing asset_id")
                    continue
                if asset_id in rows:
                    errors.append(f"ASSET_MANIFEST.csv duplicate asset_id: {asset_id}")
                rows[asset_id] = row
            return rows
    except FileNotFoundError:
        errors.append("Missing required file: ASSET_MANIFEST.csv")
        return {}


def compare_csv(assets: list[dict[str, Any]], csv_rows: dict[str, dict[str, str]], errors: list[str]) -> None:
    manifest_rows = {asset["asset_id"]: asset for asset in assets if isinstance(asset, dict) and "asset_id" in asset}
    if set(manifest_rows) != set(csv_rows):
        missing_csv = sorted(set(manifest_rows) - set(csv_rows))
        missing_json = sorted(set(csv_rows) - set(manifest_rows))
        if missing_csv:
            errors.append("Assets missing from CSV: " + ", ".join(missing_csv))
        if missing_json:
            errors.append("Assets missing from JSON: " + ", ".join(missing_json))
    fields = [
        "title", "category", "context", "purpose", "status", "version", "drive_file_id",
        "drive_url", "drive_path", "github_source_path", "github_export_path",
        "prompt_reference_path", "owner", "approval", "required_dimensions", "subjects", "notes",
    ]
    for asset_id in sorted(set(manifest_rows) & set(csv_rows)):
        asset = manifest_rows[asset_id]
        row = csv_rows[asset_id]
        for field in fields:
            if str(asset.get(field, "")) != row.get(field, ""):
                errors.append(f"{asset_id}: JSON/CSV mismatch for {field}")
        csv_dependencies = [item.strip() for item in row.get("dependencies", "").split(";") if item.strip()]
        if asset.get("dependencies") != csv_dependencies:
            errors.append(f"{asset_id}: JSON/CSV mismatch for dependencies")


def validate_markdown(asset_ids: set[str], errors: list[str]) -> None:
    try:
        text = MARKDOWN_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append("Missing required file: docs/ASSET_MANIFEST.md")
        return
    for asset_id in sorted(asset_ids):
        if asset_id not in text:
            errors.append(f"docs/ASSET_MANIFEST.md is missing {asset_id}")


def load_filesystem_allowlist(errors: list[str], root: Path = ROOT) -> dict[str, dict[str, str]]:
    path = root / "schemas" / "filesystem-integrity-allowlist.json"
    try:
        with path.open(encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError:
        errors.append("Missing required file: schemas/filesystem-integrity-allowlist.json")
        return {}
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON in schemas/filesystem-integrity-allowlist.json: {exc}")
        return {}
    if not isinstance(data, dict):
        errors.append("schemas/filesystem-integrity-allowlist.json must contain a JSON object")
        return {}
    if data.get("version") != 1:
        errors.append("filesystem integrity allowlist version must equal 1")
    entries = data.get("allowed_unregistered_files")
    if not isinstance(entries, list):
        errors.append("filesystem integrity allowlist must contain allowed_unregistered_files array")
        return {}
    allowlist: dict[str, dict[str, str]] = {}
    for index, entry in enumerate(entries):
        label = f"filesystem allowlist entry {index}"
        if not isinstance(entry, dict):
            errors.append(f"{label} must be an object")
            continue
        path_value = entry.get("path")
        classification = entry.get("classification")
        reason = entry.get("reason")
        if not isinstance(path_value, str) or not safe_repository_relative_path(path_value):
            errors.append(f"{label}: path must be a safe repository-relative path")
            continue
        if Path(path_value).parts[0] not in ASSET_DIRECTORY_ROOTS:
            errors.append(f"{label}: path must be inside an asset-owned directory")
        if classification not in ALLOWLIST_CLASSIFICATIONS:
            errors.append(f"{label}: classification must be one of {sorted(ALLOWLIST_CLASSIFICATIONS)}")
        if not isinstance(reason, str) or not reason.strip():
            errors.append(f"{label}: reason must be a non-empty string")
        if path_value in allowlist:
            errors.append(f"Duplicate filesystem allowlist path: {path_value}")
            continue
        allowlist[path_value] = {"classification": str(classification), "reason": reason if isinstance(reason, str) else ""}
        if not (root / path_value).is_file():
            errors.append(f"Allowlisted provenance file is missing: {path_value}")
    return allowlist


def validate_registered_dependencies(assets: list[dict[str, Any]], asset_ids: set[str], errors: list[str]) -> None:
    for asset in assets:
        if not isinstance(asset, dict):
            continue
        asset_id = asset.get("asset_id", "<unknown asset>")
        dependencies = asset.get("dependencies", [])
        if not isinstance(dependencies, list):
            continue
        for dependency in dependencies:
            if not isinstance(dependency, str) or not dependency.startswith("AST-"):
                continue
            if not ASSET_ID_RE.fullmatch(dependency):
                errors.append(f"{asset_id}: malformed registered Asset-ID dependency: {dependency}")
            elif dependency not in asset_ids:
                errors.append(f"{asset_id}: dangling registered Asset-ID dependency: {dependency}")


def _authority_range_resolves(dependency: str, ranges: list[dict[str, Any]]) -> bool:
    match = AUTHORITY_RANGE_RE.fullmatch(dependency)
    if not match:
        return False
    left_prefix, left_num, right_prefix, right_num = match.groups()
    if left_prefix != right_prefix or len(left_num) != len(right_num):
        return False
    start = int(left_num)
    end = int(right_num)
    if start > end:
        return False
    return any(
        entry.get("prefix") == left_prefix
        and entry.get("width") == len(left_num)
        and isinstance(entry.get("start"), int)
        and isinstance(entry.get("end"), int)
        and entry["start"] <= start
        and end <= entry["end"]
        for entry in ranges
        if isinstance(entry, dict)
    )


def validate_dependency_governance(
    assets: list[dict[str, Any]],
    asset_ids: set[str],
    authority_registry: dict[str, Any],
    classification_registry: dict[str, Any],
    errors: list[str],
    root: Path = ROOT,
) -> None:
    """Enforce objective dependency-policy admission rules without interpreting prose."""
    exact_entries = authority_registry.get("exact_authorities", [])
    range_entries = authority_registry.get("authority_ranges", [])
    if not isinstance(exact_entries, list) or not isinstance(range_entries, list):
        errors.append("external authority registry must contain exact_authorities and authority_ranges arrays")
        exact_entries = []
        range_entries = []
    exact_ids = {
        entry.get("id")
        for entry in exact_entries
        if isinstance(entry, dict) and isinstance(entry.get("id"), str)
    }
    records = classification_registry.get("prose_dependencies", [])
    if not isinstance(records, list):
        errors.append("dependency classification registry must contain prose_dependencies array")
        records = []
    classification_by_dependency: dict[str, dict[str, Any]] = {}
    for record in records:
        if not isinstance(record, dict):
            continue
        dependency = record.get("dependency")
        if not isinstance(dependency, str):
            continue
        if dependency in classification_by_dependency:
            errors.append(f"Duplicate dependency classification record: {dependency}")
            continue
        classification_by_dependency[dependency] = record
        classification = record.get("classification")
        if classification not in PROSE_DEPENDENCY_CLASSIFICATIONS:
            errors.append(f"Invalid prose dependency classification for {dependency}: {classification!r}")
        evidence_path = record.get("evidence_path")
        if not isinstance(evidence_path, str) or not safe_repository_relative_path(evidence_path):
            errors.append(f"Dependency classification {dependency}: invalid evidence_path")
        elif not (root / evidence_path).is_file():
            errors.append(f"Dependency classification {dependency}: evidence file is missing: {evidence_path}")

    actual_prose_uses: dict[str, set[str]] = {}
    for asset in assets:
        if not isinstance(asset, dict):
            continue
        asset_id = asset.get("asset_id", "<unknown asset>")
        dependencies = asset.get("dependencies", [])
        if not isinstance(dependencies, list):
            continue
        for dependency in dependencies:
            if not isinstance(dependency, str):
                continue
            if dependency.startswith("AST-"):
                if not ASSET_ID_RE.fullmatch(dependency):
                    errors.append(f"{asset_id}: malformed registered Asset-ID dependency: {dependency}")
                elif dependency not in asset_ids:
                    errors.append(f"{asset_id}: dangling registered Asset-ID dependency: {dependency}")
                continue
            if dependency in exact_ids:
                continue
            if AUTHORITY_RANGE_RE.fullmatch(dependency):
                if not _authority_range_resolves(dependency, range_entries):
                    errors.append(f"{asset_id}: unresolved external authority range: {dependency}")
                continue
            if EXACT_EXTERNAL_ID_RE.fullmatch(dependency):
                errors.append(f"{asset_id}: unresolved external authority ID: {dependency}")
                continue
            actual_prose_uses.setdefault(dependency, set()).add(str(asset_id))
            record = classification_by_dependency.get(dependency)
            if record is None:
                errors.append(f"{asset_id}: unclassified prose dependency: {dependency}")
                continue
            allowed_assets = record.get("applies_to_asset_ids", [])
            if not isinstance(allowed_assets, list) or asset_id not in allowed_assets:
                errors.append(f"{asset_id}: prose dependency is not classified for this asset: {dependency}")

    for dependency, record in classification_by_dependency.items():
        declared_assets = record.get("applies_to_asset_ids", [])
        declared_set = {item for item in declared_assets if isinstance(item, str)} if isinstance(declared_assets, list) else set()
        actual_set = actual_prose_uses.get(dependency, set())
        if declared_set != actual_set:
            errors.append(
                f"Dependency classification asset set mismatch for {dependency}: "
                f"declared={sorted(declared_set)}, actual={sorted(actual_set)}"
            )
        unknown_assets = sorted(declared_set - asset_ids)
        if unknown_assets:
            errors.append(f"Dependency classification {dependency} references unknown assets: {', '.join(unknown_assets)}")


def concrete_registered_paths(assets: list[dict[str, Any]], pages: list[dict[str, Any]]) -> set[str]:
    paths: set[str] = set()
    for asset in assets:
        if not isinstance(asset, dict):
            continue
        for field in ("github_source_path", "github_export_path"):
            value = asset.get(field)
            if isinstance(value, str) and value and not value.endswith("/"):
                paths.add(value)
    for page in pages:
        if not isinstance(page, dict):
            continue
        value = page.get("file_path")
        if isinstance(value, str) and value:
            paths.add(value)
    return paths


def validate_registered_filesystem_paths(
    assets: list[dict[str, Any]], pages: list[dict[str, Any]], allowlist: dict[str, dict[str, str]],
    errors: list[str], root: Path = ROOT,
) -> None:
    assets_by_id = {
        asset.get("asset_id"): asset
        for asset in assets
        if isinstance(asset, dict) and isinstance(asset.get("asset_id"), str)
    }
    for asset in assets:
        if not isinstance(asset, dict):
            continue
        asset_id = asset.get("asset_id", "<unknown asset>")
        status = asset.get("status")
        for field in ("github_source_path", "github_export_path"):
            path_value = asset.get(field)
            if not isinstance(path_value, str) or not path_value or path_value.endswith("/"):
                continue
            if status in MATERIALIZED_STATUSES and not (root / path_value).is_file():
                errors.append(f"{asset_id}: {field} must exist for {status} asset: {path_value}")
            if status in MATERIALIZED_STATUSES and path_value in allowlist:
                errors.append(f"{asset_id}: active {field} points to superseded/provenance allowlist file: {path_value}")
    for index, page in enumerate(pages):
        if not isinstance(page, dict):
            continue
        path_value = page.get("file_path")
        status = page.get("status")
        if isinstance(path_value, str) and status in MATERIALIZED_STATUSES and not (root / path_value).is_file():
            errors.append(f"pages[{index}]: file must exist for {status} page: {path_value}")
        asset_id = page.get("asset_id")
        asset = assets_by_id.get(asset_id)
        if asset and isinstance(path_value, str):
            export_path = asset.get("github_export_path")
            if isinstance(export_path, str) and export_path and export_path != path_value:
                errors.append(f"pages[{index}]: file_path disagrees with {asset_id} github_export_path")


def validate_asset_directory_files(
    assets: list[dict[str, Any]], pages: list[dict[str, Any]], allowlist: dict[str, dict[str, str]],
    errors: list[str], root: Path = ROOT,
) -> None:
    registered_paths = concrete_registered_paths(assets, pages)
    allowlisted_paths = set(allowlist)
    for path_value in sorted(registered_paths & allowlisted_paths):
        errors.append(
            f"Filesystem allowlist path is also registered as an active/history path; remove redundant allowlist entry: {path_value}"
        )
    for root_name in sorted(ASSET_DIRECTORY_ROOTS):
        directory = root / root_name
        if not directory.exists():
            continue
        if not directory.is_dir():
            errors.append(f"Asset-owned path must be a directory: {root_name}")
            continue
        for candidate in sorted(directory.rglob("*")):
            if not candidate.is_file() or candidate.name == ".gitkeep":
                continue
            relative = candidate.relative_to(root).as_posix()
            if relative in registered_paths or relative in allowlisted_paths:
                continue
            errors.append(f"Unregistered asset-directory file: {relative}")


def validate_filesystem_integrity(
    assets: list[dict[str, Any]], pages: list[dict[str, Any]], asset_ids: set[str],
    allowlist: dict[str, dict[str, str]], errors: list[str], root: Path = ROOT,
) -> None:
    validate_registered_dependencies(assets, asset_ids, errors)
    validate_registered_filesystem_paths(assets, pages, allowlist, errors, root)
    validate_asset_directory_files(assets, pages, allowlist, errors, root)


def main() -> int:
    errors: list[str] = []
    manifest = load_json(MANIFEST_PATH, errors)
    schema = load_json(SCHEMA_PATH, errors)
    authority_registry = load_json(EXTERNAL_AUTHORITY_REGISTRY_PATH, errors)
    classification_registry = load_json(DEPENDENCY_CLASSIFICATION_PATH, errors)
    classification_schema = load_json(DEPENDENCY_CLASSIFICATION_SCHEMA_PATH, errors)
    if schema:
        validate_json_schema(manifest, schema, errors)
    if classification_registry and classification_schema:
        validate_data_schema(
            classification_registry,
            classification_schema,
            "schemas/dependency-classification-registry.json",
            errors,
        )
    validate_project(manifest.get("project"), errors)
    assets = manifest.get("assets")
    asset_ids: set[str] = set()
    if not isinstance(assets, list):
        errors.append("assets must be an array")
        assets = []
    else:
        for index, asset in enumerate(assets):
            asset_id = validate_asset(asset, index, errors)
            if asset_id:
                if asset_id in asset_ids:
                    errors.append(f"Duplicate asset_id: {asset_id}")
                asset_ids.add(asset_id)
    pages = manifest.get("pages")
    validate_pages(pages, asset_ids, errors)
    if not isinstance(pages, list):
        pages = []
    csv_rows = read_csv(errors)
    compare_csv(assets, csv_rows, errors)
    validate_markdown(asset_ids, errors)
    validate_dependency_governance(
        assets, asset_ids, authority_registry, classification_registry, errors
    )
    filesystem_allowlist = load_filesystem_allowlist(errors)
    validate_filesystem_integrity(assets, pages, asset_ids, filesystem_allowlist, errors)
    if errors:
        print("Aramyst manifest validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        f"Validated schema contract, {len(asset_ids)} assets, {len(pages)} pages, "
        "dependency governance, registered dependencies, and asset filesystem integrity."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

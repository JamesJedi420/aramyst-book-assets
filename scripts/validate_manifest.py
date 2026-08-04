#!/usr/bin/env python3
"""Validate Aramyst asset and page manifests without external dependencies."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "manifest.json"
CSV_PATH = ROOT / "ASSET_MANIFEST.csv"
MARKDOWN_PATH = ROOT / "docs" / "ASSET_MANIFEST.md"
SCHEMA_PATH = ROOT / "schemas" / "asset-manifest.schema.json"

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

VERSION_RE = re.compile(r"^v\d{3}$")
ASSET_ID_RE = re.compile(r"^AST-(COVER|MAP|CHAR|FACT|LOC|SYM|TYPE|PROMPT|REF|MISC)-\d{3}$")
PAGE_PATH_RE = re.compile(r"^pages/(\d{3})_([a-z0-9]+(?:-[a-z0-9]+)*)\.[a-z0-9.]+$")
FILE_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*(?:-v\d{3})?(?:-[a-z0-9]+)*\.[a-z0-9.]+$")

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
        "asset_id",
        "title",
        "category",
        "context",
        "purpose",
        "subjects",
        "required_dimensions",
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
        "notes",
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
        if path_value.startswith("/") or "\\" in path_value or ".." in Path(path_value).parts:
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

        if page.get("status") in {"exported", "published"} and isinstance(path, str):
            if not (ROOT / path).is_file():
                errors.append(f"{label}: exported page file is missing: {path}")


def read_csv(errors: list[str]) -> dict[str, dict[str, str]]:
    try:
        with CSV_PATH.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != CSV_FIELDS:
                errors.append(
                    "ASSET_MANIFEST.csv header mismatch. Expected: " + ",".join(CSV_FIELDS)
                )
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
        "approval",
        "required_dimensions",
        "subjects",
        "notes",
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


def main() -> int:
    errors: list[str] = []
    manifest = load_json(MANIFEST_PATH, errors)
    load_json(SCHEMA_PATH, errors)

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

    validate_pages(manifest.get("pages"), asset_ids, errors)
    csv_rows = read_csv(errors)
    compare_csv(assets, csv_rows, errors)
    validate_markdown(asset_ids, errors)

    if errors:
        print("Aramyst manifest validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(asset_ids)} assets and {len(manifest.get('pages', []))} pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate machine-readable provenance sidecars for approved Aramyst assets."""

from __future__ import annotations

import base64
import hashlib
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "manifest.json"
SCHEMA_PATH = ROOT / "schemas" / "approved-asset-provenance.schema.json"
PROVENANCE_DIR = ROOT / "provenance"
CONTROLLED_STATUSES = {"approved", "exported", "published"}


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def git_blob_sha1(path: Path) -> str:
    payload = path.read_bytes()
    header = f"blob {len(payload)}\0".encode("ascii")
    return hashlib.sha1(header + payload).hexdigest()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_base64_decoded(path: Path) -> str:
    encoded = path.read_bytes()
    payload = base64.b64decode(encoded, validate=True)
    return hashlib.sha256(payload).hexdigest()


def verify_hash(binding: dict[str, Any], path: Path, label: str, errors: list[str]) -> None:
    algorithm = binding.get("algorithm")
    expected = binding.get("value")
    if not path.is_file():
        errors.append(f"{label}: bound repository file is missing: {path.relative_to(ROOT)}")
        return
    if algorithm == "git-blob-sha1":
        actual = git_blob_sha1(path)
    elif algorithm == "sha256":
        actual = sha256(path)
    elif algorithm == "sha256-base64-decoded":
        try:
            actual = sha256_base64_decoded(path)
        except Exception as exc:
            errors.append(f"{label}: unable to decode/hash base64 file: {exc}")
            return
    else:
        errors.append(f"{label}: unsupported hash algorithm: {algorithm!r}")
        return
    if actual != expected:
        errors.append(f"{label}: hash mismatch: expected {expected}, actual {actual}")


def validate_repository(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    manifest = load_json(root / "manifest.json")
    schema = load_json(root / "schemas" / "approved-asset-provenance.schema.json")
    Draft202012Validator.check_schema(schema)
    schema_validator = Draft202012Validator(schema)

    assets = manifest.get("assets", [])
    assets_by_id = {
        asset.get("asset_id"): asset
        for asset in assets
        if isinstance(asset, dict) and isinstance(asset.get("asset_id"), str)
    }
    controlled_ids = {
        asset_id
        for asset_id, asset in assets_by_id.items()
        if asset.get("status") in CONTROLLED_STATUSES
    }

    provenance_dir = root / "provenance"
    sidecar_paths = sorted(provenance_dir.glob("*.json")) if provenance_dir.is_dir() else []
    sidecars_by_id: dict[str, tuple[Path, dict[str, Any]]] = {}

    for path in sidecar_paths:
        try:
            sidecar = load_json(path)
        except Exception as exc:
            errors.append(f"{path.relative_to(root)}: invalid JSON: {exc}")
            continue
        schema_errors = sorted(schema_validator.iter_errors(sidecar), key=lambda error: list(error.absolute_path))
        for error in schema_errors:
            location = ".".join(str(part) for part in error.absolute_path) or "$"
            errors.append(f"{path.relative_to(root)} schema violation at {location}: {error.message}")
        asset_id = sidecar.get("asset_id")
        if not isinstance(asset_id, str):
            continue
        if asset_id in sidecars_by_id:
            errors.append(f"Duplicate approved provenance sidecar for {asset_id}")
            continue
        sidecars_by_id[asset_id] = (path, sidecar)

    missing = sorted(controlled_ids - set(sidecars_by_id))
    unexpected = sorted(set(sidecars_by_id) - controlled_ids)
    if missing:
        errors.append("Approved/exported/published assets missing provenance sidecars: " + ", ".join(missing))
    if unexpected:
        errors.append("Provenance sidecars exist for assets not in an approved/exported/published state: " + ", ".join(unexpected))

    for asset_id in sorted(controlled_ids & set(sidecars_by_id)):
        path, sidecar = sidecars_by_id[asset_id]
        asset = assets_by_id[asset_id]
        label = str(path.relative_to(root))

        for field in ("asset_id", "version", "status", "drive_file_id", "github_source_path", "github_export_path"):
            if sidecar.get(field) != asset.get(field):
                errors.append(f"{label}: {field} disagrees with manifest.json")

        approval_date = sidecar.get("approval_date")
        try:
            date.fromisoformat(approval_date)
        except Exception:
            errors.append(f"{label}: approval_date must be a valid ISO date")
            approval_date = None

        evidence_path = sidecar.get("approval_evidence_path")
        evidence_text = ""
        if isinstance(evidence_path, str):
            evidence_file = root / evidence_path
            if not evidence_file.is_file():
                errors.append(f"{label}: approval evidence file is missing: {evidence_path}")
            else:
                evidence_text = evidence_file.read_text(encoding="utf-8", errors="replace")
        if approval_date:
            manifest_approval_text = f"{asset.get('approval', '')}\n{asset.get('notes', '')}"
            if approval_date not in manifest_approval_text and approval_date not in evidence_text:
                errors.append(
                    f"{label}: approval_date is not corroborated by manifest approval/notes or controlled evidence"
                )

        master = sidecar.get("master", {})
        if isinstance(master, dict):
            master_system = master.get("system")
            master_hash = master.get("hash")
            if master_system == "google_drive":
                if master.get("drive_file_id") != asset.get("drive_file_id"):
                    errors.append(f"{label}: Drive-master file ID disagrees with manifest.json")
                if not isinstance(master_hash, dict) or master_hash.get("algorithm") != "sha256":
                    errors.append(f"{label}: Drive masters must carry an expected SHA-256 binding")
                elif len(str(master_hash.get("value", ""))) != 64:
                    errors.append(f"{label}: Drive-master SHA-256 must contain 64 hex characters")
            elif master_system == "github":
                github_path = master.get("github_path")
                if github_path != asset.get("github_source_path"):
                    errors.append(f"{label}: GitHub master path disagrees with manifest github_source_path")
                if isinstance(github_path, str) and isinstance(master_hash, dict):
                    verify_hash(master_hash, root / github_path, f"{label} master", errors)

        source_hash = sidecar.get("source_hash")
        source_path = asset.get("github_source_path")
        if isinstance(source_hash, dict):
            if not isinstance(source_path, str) or not source_path or source_path.endswith("/"):
                errors.append(f"{label}: source_hash requires a concrete manifest github_source_path")
            else:
                verify_hash(source_hash, root / source_path, f"{label} source", errors)

        export_hash = sidecar.get("export_hash")
        export_path = asset.get("github_export_path")
        if isinstance(export_path, str) and export_path and not export_path.endswith("/"):
            if not isinstance(export_hash, dict):
                errors.append(f"{label}: concrete github_export_path requires export_hash")
            else:
                verify_hash(export_hash, root / export_path, f"{label} export", errors)
        elif isinstance(export_hash, dict):
            errors.append(f"{label}: export_hash present without a concrete manifest github_export_path")

    return errors


def main() -> int:
    errors = validate_repository()
    if errors:
        print("Approved asset provenance validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    count = len(list(PROVENANCE_DIR.glob("*.json"))) if PROVENANCE_DIR.is_dir() else 0
    print(f"Validated {count} approved asset provenance sidecars.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

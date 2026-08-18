#!/usr/bin/env python3
"""Check objective asset-governance invariants that supplement manifest validation."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "manifest.json"

PROMOTED_STATUSES = {"approved", "exported", "published"}
VERSION_TOKEN_RE = re.compile(r"(?:^|-)v(\d{3})(?=[.-])")


def explicit_version_token(path_value: str) -> str | None:
    if not path_value or path_value.endswith("/"):
        return None
    match = VERSION_TOKEN_RE.search(Path(path_value).name)
    return f"v{match.group(1)}" if match else None


def validate_asset_governance(assets: list[dict[str, Any]], errors: list[str]) -> None:
    """Enforce only objective end-state rules; do not infer creative or approval semantics."""
    for asset in assets:
        if not isinstance(asset, dict):
            continue
        asset_id = str(asset.get("asset_id", "<unknown asset>"))
        drive_id = asset.get("drive_file_id", "")
        drive_url = asset.get("drive_url", "")
        drive_path = asset.get("drive_path", "")
        status = asset.get("status")
        version = asset.get("version")
        approval = asset.get("approval", "")

        if drive_id or drive_url or drive_path:
            if not all(isinstance(value, str) and value.strip() for value in (drive_id, drive_url, drive_path)):
                errors.append(
                    f"{asset_id}: Drive-backed asset requires drive_file_id, drive_url, and drive_path together"
                )
            elif isinstance(drive_url, str):
                parsed = urlparse(drive_url)
                if parsed.scheme != "https" or parsed.hostname not in {"docs.google.com", "drive.google.com"}:
                    errors.append(f"{asset_id}: drive_url must use an approved Google Drive host")
                elif str(drive_id) not in parsed.path:
                    errors.append(f"{asset_id}: drive_url path does not identify drive_file_id")

        if status in PROMOTED_STATUSES and isinstance(approval, str):
            if "not approved" in approval.casefold():
                errors.append(
                    f"{asset_id}: {status} status contradicts approval text containing 'not approved'"
                )

        if isinstance(version, str):
            for field in ("github_source_path", "github_export_path"):
                path_value = asset.get(field, "")
                if not isinstance(path_value, str):
                    continue
                token = explicit_version_token(path_value)
                if token is not None and token != version:
                    errors.append(
                        f"{asset_id}: {field} version token {token} disagrees with manifest version {version}"
                    )


def main() -> int:
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"Asset governance check could not load manifest.json: {exc}", file=sys.stderr)
        return 1

    assets = manifest.get("assets")
    if not isinstance(assets, list):
        print("Asset governance check requires manifest assets array", file=sys.stderr)
        return 1

    errors: list[str] = []
    validate_asset_governance(assets, errors)
    if errors:
        print("Asset governance validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated objective governance invariants for {len(assets)} assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

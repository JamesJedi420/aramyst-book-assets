import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts import validate_manifest


class JsonSchemaEnforcementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(validate_manifest.MANIFEST_PATH.read_text(encoding="utf-8"))
        cls.schema = json.loads(validate_manifest.SCHEMA_PATH.read_text(encoding="utf-8"))

    def test_current_manifest_satisfies_schema(self) -> None:
        errors: list[str] = []
        validate_manifest.validate_json_schema(self.manifest, self.schema, errors)
        self.assertEqual([], errors)

    def test_schema_rejects_undeclared_top_level_property(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["unexpected_control_field"] = True
        errors: list[str] = []
        validate_manifest.validate_json_schema(manifest, self.schema, errors)
        self.assertTrue(
            any("schema violation" in error and "Additional properties" in error for error in errors),
            errors,
        )


class FilesystemIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(validate_manifest.MANIFEST_PATH.read_text(encoding="utf-8"))

    def test_current_repository_passes_filesystem_integrity(self) -> None:
        errors: list[str] = []
        allowlist = validate_manifest.load_filesystem_allowlist(errors)
        assets = self.manifest["assets"]
        pages = self.manifest["pages"]
        asset_ids = {asset["asset_id"] for asset in assets}
        validate_manifest.validate_filesystem_integrity(
            assets,
            pages,
            asset_ids,
            allowlist,
            errors,
        )
        self.assertEqual([], errors)

    def test_missing_active_source_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "maps").mkdir()
            assets = [
                {
                    "asset_id": "AST-MAP-999",
                    "status": "approved",
                    "github_source_path": "maps/missing-v001.svg",
                    "github_export_path": "",
                    "dependencies": [],
                }
            ]
            errors: list[str] = []
            validate_manifest.validate_registered_filesystem_paths(
                assets,
                [],
                {},
                errors,
                root,
            )
            self.assertTrue(any("must exist for approved asset" in error for error in errors), errors)

    def test_planned_future_export_may_be_unmaterialized(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            assets = [
                {
                    "asset_id": "AST-COVER-999",
                    "status": "planned",
                    "github_source_path": "covers/",
                    "github_export_path": "pages/999_future-cover.png.b64",
                    "dependencies": [],
                }
            ]
            pages = [
                {
                    "asset_id": "AST-COVER-999",
                    "status": "planned",
                    "file_path": "pages/999_future-cover.png.b64",
                }
            ]
            errors: list[str] = []
            validate_manifest.validate_registered_filesystem_paths(
                assets,
                pages,
                {},
                errors,
                root,
            )
            self.assertEqual([], errors)

    def test_dangling_registered_asset_dependency_is_rejected(self) -> None:
        assets = [
            {
                "asset_id": "AST-COVER-999",
                "dependencies": ["AST-SYM-999"],
            }
        ]
        errors: list[str] = []
        validate_manifest.validate_registered_dependencies(
            assets,
            {"AST-COVER-999"},
            errors,
        )
        self.assertTrue(any("dangling registered Asset-ID dependency" in error for error in errors), errors)

    def test_unregistered_asset_directory_file_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            maps = root / "maps"
            maps.mkdir()
            (maps / "orphan-v001.svg").write_text("<svg/>", encoding="utf-8")
            errors: list[str] = []
            validate_manifest.validate_asset_directory_files(
                [],
                [],
                {},
                errors,
                root,
            )
            self.assertEqual(["Unregistered asset-directory file: maps/orphan-v001.svg"], errors)

    def test_documented_provenance_file_is_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            maps = root / "maps"
            maps.mkdir()
            (maps / "historical-v001.svg").write_text("<svg/>", encoding="utf-8")
            allowlist = {
                "maps/historical-v001.svg": {
                    "classification": "superseded",
                    "reason": "historical test fixture",
                }
            }
            errors: list[str] = []
            validate_manifest.validate_asset_directory_files(
                [],
                [],
                allowlist,
                errors,
                root,
            )
            self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()

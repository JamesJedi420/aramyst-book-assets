import json
import tempfile
import unittest
from pathlib import Path

from scripts import validate_approved_provenance


class ApprovedProvenanceTests(unittest.TestCase):
    def test_current_repository_passes(self) -> None:
        self.assertEqual([], validate_approved_provenance.validate_repository())

    def _fixture_root(self) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "schemas").mkdir()
        (root / "provenance").mkdir()
        (root / "symbols").mkdir()
        (root / "exports").mkdir()
        schema = json.loads(validate_approved_provenance.SCHEMA_PATH.read_text(encoding="utf-8"))
        (root / "schemas" / "approved-asset-provenance.schema.json").write_text(
            json.dumps(schema), encoding="utf-8"
        )
        source = root / "symbols" / "test-v001.md"
        source.write_text("approval 2026-08-18\n", encoding="utf-8")
        manifest = {
            "assets": [
                {
                    "asset_id": "AST-SYM-999",
                    "version": "v001",
                    "status": "approved",
                    "drive_file_id": "drive-999",
                    "github_source_path": "symbols/test-v001.md",
                    "github_export_path": "",
                    "approval": "Approved 2026-08-18",
                    "notes": "",
                }
            ]
        }
        (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        return root

    def test_missing_sidecar_is_rejected(self) -> None:
        root = self._fixture_root()
        errors = validate_approved_provenance.validate_repository(root)
        self.assertTrue(any("missing provenance sidecars" in error for error in errors), errors)

    def test_manifest_binding_mismatch_is_rejected(self) -> None:
        root = self._fixture_root()
        source = root / "symbols" / "test-v001.md"
        sidecar = {
            "asset_id": "AST-SYM-999",
            "version": "v002",
            "status": "approved",
            "approval_date": "2026-08-18",
            "approval_evidence_path": "symbols/test-v001.md",
            "drive_file_id": "drive-999",
            "github_source_path": "symbols/test-v001.md",
            "github_export_path": "",
            "master": {
                "system": "github",
                "github_path": "symbols/test-v001.md",
                "hash": {
                    "algorithm": "git-blob-sha1",
                    "value": validate_approved_provenance.git_blob_sha1(source),
                },
            },
        }
        (root / "provenance" / "ast-sym-999-v001.json").write_text(
            json.dumps(sidecar), encoding="utf-8"
        )
        errors = validate_approved_provenance.validate_repository(root)
        self.assertTrue(any("version disagrees with manifest.json" in error for error in errors), errors)

    def test_repository_hash_mismatch_is_rejected(self) -> None:
        root = self._fixture_root()
        sidecar = {
            "asset_id": "AST-SYM-999",
            "version": "v001",
            "status": "approved",
            "approval_date": "2026-08-18",
            "approval_evidence_path": "symbols/test-v001.md",
            "drive_file_id": "drive-999",
            "github_source_path": "symbols/test-v001.md",
            "github_export_path": "",
            "master": {
                "system": "github",
                "github_path": "symbols/test-v001.md",
                "hash": {"algorithm": "git-blob-sha1", "value": "0" * 40},
            },
        }
        (root / "provenance" / "ast-sym-999-v001.json").write_text(
            json.dumps(sidecar), encoding="utf-8"
        )
        errors = validate_approved_provenance.validate_repository(root)
        self.assertTrue(any("hash mismatch" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()

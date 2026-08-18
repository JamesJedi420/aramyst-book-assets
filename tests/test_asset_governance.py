import copy
import json
import unittest

from scripts import check_asset_governance


class AssetGovernanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(check_asset_governance.MANIFEST_PATH.read_text(encoding="utf-8"))

    def test_current_manifest_passes_asset_governance(self) -> None:
        errors: list[str] = []
        check_asset_governance.validate_asset_governance(self.manifest["assets"], errors)
        self.assertEqual([], errors)

    def test_drive_backed_asset_requires_drive_path(self) -> None:
        asset = copy.deepcopy(self.manifest["assets"][2])
        asset["drive_path"] = ""
        errors: list[str] = []
        check_asset_governance.validate_asset_governance([asset], errors)
        self.assertTrue(any("requires drive_file_id, drive_url, and drive_path together" in e for e in errors), errors)

    def test_drive_url_requires_google_drive_host(self) -> None:
        asset = copy.deepcopy(self.manifest["assets"][2])
        asset["drive_url"] = f"https://example.com/{asset['drive_file_id']}"
        errors: list[str] = []
        check_asset_governance.validate_asset_governance([asset], errors)
        self.assertTrue(any("approved Google Drive host" in e for e in errors), errors)

    def test_promoted_status_rejects_not_approved_text(self) -> None:
        asset = copy.deepcopy(self.manifest["assets"][2])
        asset["status"] = "approved"
        asset["approval"] = "Not approved"
        errors: list[str] = []
        check_asset_governance.validate_asset_governance([asset], errors)
        self.assertTrue(any("contradicts approval text" in e for e in errors), errors)

    def test_explicit_path_version_must_match_manifest_version(self) -> None:
        asset = copy.deepcopy(self.manifest["assets"][2])
        asset["version"] = "v001"
        asset["github_source_path"] = "maps/example-source-v002.svg"
        errors: list[str] = []
        check_asset_governance.validate_asset_governance([asset], errors)
        self.assertTrue(any("version token v002 disagrees with manifest version v001" in e for e in errors), errors)

    def test_path_without_version_token_is_allowed(self) -> None:
        asset = copy.deepcopy(self.manifest["assets"][2])
        asset["github_source_path"] = "maps/example-source.svg"
        asset["github_export_path"] = ""
        errors: list[str] = []
        check_asset_governance.validate_asset_governance([asset], errors)
        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()

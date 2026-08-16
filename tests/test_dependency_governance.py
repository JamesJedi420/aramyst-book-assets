import copy
import json
import unittest

from jsonschema import Draft202012Validator

from scripts import validate_manifest


class DependencyGovernanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(validate_manifest.MANIFEST_PATH.read_text(encoding="utf-8"))
        cls.authorities = json.loads(
            validate_manifest.EXTERNAL_AUTHORITY_REGISTRY_PATH.read_text(encoding="utf-8")
        )
        cls.classifications = json.loads(
            validate_manifest.DEPENDENCY_CLASSIFICATION_PATH.read_text(encoding="utf-8")
        )
        cls.classification_schema = json.loads(
            validate_manifest.DEPENDENCY_CLASSIFICATION_SCHEMA_PATH.read_text(encoding="utf-8")
        )

    def test_classification_registry_satisfies_schema(self) -> None:
        Draft202012Validator.check_schema(self.classification_schema)
        errors = list(
            Draft202012Validator(self.classification_schema).iter_errors(self.classifications)
        )
        self.assertEqual([], errors)

    def test_current_manifest_passes_dependency_governance(self) -> None:
        assets = self.manifest["assets"]
        asset_ids = {asset["asset_id"] for asset in assets}
        errors: list[str] = []
        validate_manifest.validate_dependency_governance(
            assets,
            asset_ids,
            self.authorities,
            self.classifications,
            errors,
        )
        self.assertEqual([], errors)

    def test_unclassified_prose_dependency_is_rejected(self) -> None:
        assets = copy.deepcopy(self.manifest["assets"])
        assets[0]["dependencies"].append("Unreviewed future gate")
        asset_ids = {asset["asset_id"] for asset in assets}
        errors: list[str] = []
        validate_manifest.validate_dependency_governance(
            assets,
            asset_ids,
            self.authorities,
            self.classifications,
            errors,
        )
        self.assertTrue(any("unclassified prose dependency" in error for error in errors), errors)

    def test_unresolved_external_authority_id_is_rejected(self) -> None:
        assets = copy.deepcopy(self.manifest["assets"])
        assets[0]["dependencies"].append("SCN-UNKNOWN-999")
        asset_ids = {asset["asset_id"] for asset in assets}
        errors: list[str] = []
        validate_manifest.validate_dependency_governance(
            assets,
            asset_ids,
            self.authorities,
            self.classifications,
            errors,
        )
        self.assertTrue(any("unresolved external authority ID" in error for error in errors), errors)

    def test_unresolved_external_authority_range_is_rejected(self) -> None:
        assets = copy.deepcopy(self.manifest["assets"])
        assets[0]["dependencies"].append("GEO-000002–GEO-000099")
        asset_ids = {asset["asset_id"] for asset in assets}
        errors: list[str] = []
        validate_manifest.validate_dependency_governance(
            assets,
            asset_ids,
            self.authorities,
            self.classifications,
            errors,
        )
        self.assertTrue(any("unresolved external authority range" in error for error in errors), errors)

    def test_prose_dependency_use_requires_asset_specific_classification(self) -> None:
        assets = copy.deepcopy(self.manifest["assets"])
        cover = next(asset for asset in assets if asset["asset_id"] == "AST-COVER-001")
        cover["dependencies"].append("Scene 01 canon")
        asset_ids = {asset["asset_id"] for asset in assets}
        errors: list[str] = []
        validate_manifest.validate_dependency_governance(
            assets,
            asset_ids,
            self.authorities,
            self.classifications,
            errors,
        )
        self.assertTrue(
            any("prose dependency is not classified for this asset" in error for error in errors),
            errors,
        )

    def test_dangling_asset_edge_is_rejected_by_governance(self) -> None:
        assets = copy.deepcopy(self.manifest["assets"])
        assets[0]["dependencies"].append("AST-SYM-999")
        asset_ids = {asset["asset_id"] for asset in assets}
        errors: list[str] = []
        validate_manifest.validate_dependency_governance(
            assets,
            asset_ids,
            self.authorities,
            self.classifications,
            errors,
        )
        self.assertTrue(any("dangling registered Asset-ID dependency" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()

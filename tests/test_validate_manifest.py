import copy
import json
import unittest

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


if __name__ == "__main__":
    unittest.main()

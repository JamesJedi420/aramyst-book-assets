import json
import re
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "schemas" / "external-authority-registry.json"
SCHEMA_PATH = ROOT / "schemas" / "external-authority-registry.schema.json"
MANIFEST_PATH = ROOT / "manifest.json"

EXACT_ID_RE = re.compile(r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$")
RANGE_RE = re.compile(r"^(.+)-(\d+)[–-](.+)-(\d+)$")


class ExternalAuthorityRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        cls.exact = {entry["id"]: entry for entry in cls.registry["exact_authorities"]}
        cls.ranges = cls.registry["authority_ranges"]

    def test_registry_satisfies_schema(self) -> None:
        Draft202012Validator.check_schema(self.schema)
        errors = list(Draft202012Validator(self.schema).iter_errors(self.registry))
        self.assertEqual([], errors)

    def test_registry_identifiers_are_unique_and_range_sources_resolve(self) -> None:
        ids = [entry["id"] for entry in self.registry["exact_authorities"]]
        self.assertEqual(len(ids), len(set(ids)), ids)
        range_keys = [
            (entry["prefix"], entry["start"], entry["end"], entry["width"])
            for entry in self.ranges
        ]
        self.assertEqual(len(range_keys), len(set(range_keys)), range_keys)
        for entry in self.ranges:
            self.assertLessEqual(entry["start"], entry["end"], entry)
            self.assertIn(entry["source_authority_id"], self.exact, entry)

    def test_map_env_product_is_distinct_from_asset(self) -> None:
        entry = self.exact["MAP-ENV-001"]
        self.assertEqual("map_product", entry["kind"])
        self.assertEqual("AST-MAP-003", entry["implemented_by_asset_id"])
        self.assertEqual("distinct_from_asset", entry["identity_rule"])

    def _range_resolves(self, dependency: str) -> bool:
        match = RANGE_RE.fullmatch(dependency)
        if not match:
            return False
        left_prefix, left_num, right_prefix, right_num = match.groups()
        if left_prefix != right_prefix or len(left_num) != len(right_num):
            return False
        start = int(left_num)
        end = int(right_num)
        if start > end:
            return False
        for entry in self.ranges:
            if (
                entry["prefix"] == left_prefix
                and entry["width"] == len(left_num)
                and entry["start"] <= start
                and end <= entry["end"]
            ):
                return True
        return False

    def test_every_id_shaped_non_asset_dependency_resolves(self) -> None:
        unresolved = []
        for asset in self.manifest["assets"]:
            for dependency in asset["dependencies"]:
                if dependency.startswith("AST-"):
                    continue
                if self._range_resolves(dependency):
                    continue
                if EXACT_ID_RE.fullmatch(dependency):
                    if dependency not in self.exact:
                        unresolved.append((asset["asset_id"], dependency))
        self.assertEqual([], unresolved)

    def test_descriptive_gates_are_not_forced_into_registry(self) -> None:
        self.assertNotIn("Scene 01 canon", self.exact)
        self.assertNotIn("Final publishing specifications", self.exact)
        self.assertNotIn("Approved cover direction", self.exact)


if __name__ == "__main__":
    unittest.main()

import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from resolve_skill import resolve
from validate_repo import validate

class SkillContractTests(unittest.TestCase):
    def test_repository_contracts_validate(self):
        self.assertEqual(validate(strict=True), 0)

    def test_codex_claude_portability(self):
        codex = resolve("governed-execution", "codex")
        claude = resolve("governed-execution", "claude")
        self.assertEqual(codex["source"]["sha256"], claude["source"]["sha256"])
        self.assertEqual(codex["contract_hash"], claude["contract_hash"])
        self.assertEqual(codex["authority"], claude["authority"])
        self.assertFalse(codex["authority"]["grants_authority"])
        self.assertNotEqual(codex["runtime"], claude["runtime"])
    def test_wf60_binding_is_explicit(self):
        bundle = resolve("outcome-verification", "wf60", output_format="wf60")
        binding = bundle["skill_bindings"][0]
        self.assertFalse(binding["authority"]["grants_authority"])
        self.assertTrue(binding["source"]["path"].startswith("skills/"))
        self.assertEqual(len(binding["source"]["sha256"]), 64)

if __name__ == "__main__":
    unittest.main()

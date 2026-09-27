import sys
import tempfile
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from resolve_skill import resolve
from text_hash import canonical_text_sha256
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

    def test_text_hash_is_portable_across_line_endings(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            lf = root / "lf.md"
            crlf = root / "crlf.md"
            lf.write_bytes(b"# Skill\nline two\n")
            crlf.write_bytes(b"# Skill\r\nline two\r\n")
            self.assertEqual(canonical_text_sha256(lf), canonical_text_sha256(crlf))

if __name__ == "__main__":
    unittest.main()

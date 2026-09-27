#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

from resolve_skill import resolve

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence" / "portability-proof.json"

def build_proof():
    codex = resolve("governed-execution", "codex")
    claude = resolve("governed-execution", "claude")
    invariant_fields = {
        "same_source_hash": codex["source"]["sha256"] == claude["source"]["sha256"],
        "same_contract_hash": codex["contract_hash"] == claude["contract_hash"],
        "same_authority": codex["authority"] == claude["authority"],
        "authority_not_granted": not codex["authority"]["grants_authority"],
    }
    passed = all(invariant_fields.values()) and codex["runtime"] != claude["runtime"]
    return {
        "work_item": "PCA-209",
        "skill_id": "governed-execution",
        "runtimes": ["codex", "claude"],
        "invariants": invariant_fields,
        "result": "PASS" if passed else "FAIL",
        "codex_binding": codex,
        "claude_binding": claude,
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    proof = build_proof()
    if args.write:
        EVIDENCE.parent.mkdir(parents=True, exist_ok=True)
        EVIDENCE.write_text(json.dumps(proof, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(proof, indent=2))
    if args.check and proof["result"] != "PASS":
        raise SystemExit(1)

if __name__ == "__main__":
    main()

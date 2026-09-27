#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import sys

import yaml

from text_hash import canonical_text_sha256

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "https://github.com/jjuniper-dev/skills"

def sha256_file(path):
    return canonical_text_sha256(path)

def load_registry():
    return yaml.safe_load((ROOT / "registry.yaml").read_text(encoding="utf-8"))

def resolve(skill_id, runtime, revision=None, output_format="binding"):
    registry = load_registry()
    entries = {item["id"]: item for item in registry["skills"]}
    if skill_id not in entries:
        raise ValueError(f"unknown skill: {skill_id}")
    entry = entries[skill_id]
    if runtime not in entry["runtimes"]:
        raise ValueError(f"runtime {runtime!r} is not declared for {skill_id}")
    source_path = ROOT / entry["source_path"]
    actual_hash = sha256_file(source_path)
    if actual_hash != entry["source_sha256"]:
        raise ValueError(f"source hash mismatch for {skill_id}")
    contract_hash = actual_hash
    if entry.get("contract_path"):
        contract_hash = sha256_file(ROOT / entry["contract_path"])
    binding = {
        "skill_id": entry["id"],
        "version": entry["version"],
        "runtime": runtime,
        "contract_version": entry["contract_version"],
        "source": {
            "repository": REPOSITORY,
            "path": entry["source_path"],
            "revision": revision or entry["source_revision"],
            "sha256": actual_hash,
        },
        "contract_hash": contract_hash,
        "authority": {
            "class": entry["authority_class"],
            "grants_authority": False,
            "mutation_level": entry["mutation_level"],
        },
        "capabilities": entry["capabilities"],
        "evidence_requirements": entry["evidence_requirements"],
    }
    return {"skill_bindings": [binding]} if output_format == "wf60" else binding

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", required=True)
    parser.add_argument("--runtime", required=True)
    parser.add_argument("--revision")
    parser.add_argument("--format", choices=["binding", "wf60"], default="binding")
    args = parser.parse_args()
    try:
        print(json.dumps(resolve(args.skill, args.runtime, args.revision, args.format), indent=2))
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(2)

if __name__ == "__main__":
    main()

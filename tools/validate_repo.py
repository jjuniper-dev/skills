#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

import jsonschema
import yaml

from text_hash import canonical_text_sha256

ROOT = Path(__file__).resolve().parents[1]

def repo_files(pattern):
    return [p for p in ROOT.rglob(pattern) if ".git" not in p.parts and "__pycache__" not in p.parts]

def sha256_file(path):
    return canonical_text_sha256(path)

def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))

def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def validate(strict=False):
    errors = []
    counts = {"json": 0, "yaml": 0, "python": 0, "skills": 0, "v2_contracts": 0}
    for path in repo_files("*.json"):
        counts["json"] += 1
        try:
            load_json(path)
        except Exception as exc:
            errors.append(f"invalid JSON {path.relative_to(ROOT)}: {exc}")

    for pattern in ("*.yaml", "*.yml"):
        for path in repo_files(pattern):
            counts["yaml"] += 1
            try:
                load_yaml(path)
            except Exception as exc:
                errors.append(f"invalid YAML {path.relative_to(ROOT)}: {exc}")

    for path in repo_files("*.py"):
        counts["python"] += 1
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except Exception as exc:
            errors.append(f"invalid Python {path.relative_to(ROOT)}: {exc}")

    for rel in [
        "README.md", "registry.yaml", "schemas/skill-contract-v2.schema.json",
        "schemas/skill-registry.schema.json", "tools/resolve_skill.py",
        ".github/workflows/validate.yml"
    ]:
        if not (ROOT / rel).exists():
            errors.append(f"missing required path: {rel}")
    registry_path = ROOT / "registry.yaml"
    if registry_path.exists():
        try:
            registry = load_yaml(registry_path)
            registry_schema = load_json(ROOT / "schemas/skill-registry.schema.json")
            jsonschema.validate(registry, registry_schema)
            entries = {item["id"]: item for item in registry["skills"]}
            skill_dirs = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
            counts["skills"] = len(skill_dirs)
            dir_ids = {p.name for p in skill_dirs}
            if set(entries) != dir_ids:
                errors.append(
                    "registry/skills directory mismatch: "
                    f"missing={sorted(dir_ids-set(entries))} extra={sorted(set(entries)-dir_ids)}"
                )

            contract_schema = load_json(ROOT / "schemas/skill-contract-v2.schema.json")
            for skill_id, entry in entries.items():
                source = ROOT / entry["source_path"]
                if not source.exists():
                    errors.append(f"{skill_id}: source_path does not exist")
                    continue
                actual = sha256_file(source)
                if actual != entry["source_sha256"]:
                    errors.append(f"{skill_id}: source_sha256 mismatch")
                if entry["contract_version"] == "2.0":
                    counts["v2_contracts"] += 1
                    contract_rel = entry.get("contract_path")
                    if not contract_rel:
                        errors.append(f"{skill_id}: missing contract_path")
                        continue
                    contract_path = ROOT / contract_rel
                    if not contract_path.exists():
                        errors.append(f"{skill_id}: contract_path does not exist")
                        continue
                    contract = load_yaml(contract_path)
                    try:
                        jsonschema.validate(contract, contract_schema)
                    except Exception as exc:
                        errors.append(f"{skill_id}: invalid v2 contract: {exc}")
                        continue
                    if contract["id"] != skill_id:
                        errors.append(f"{skill_id}: contract id mismatch")
                    if contract["authority"]["grants_authority"] is not False:
                        errors.append(f"{skill_id}: skill illegally grants authority")
                    if entry["source_revision"] != registry["release_revision"]:
                        errors.append(f"{skill_id}: revision differs from registry release")
        except Exception as exc:
            errors.append(f"registry validation failed: {exc}")

    result = {"status": "PASS" if not errors else "FAIL", "counts": counts, "errors": errors}
    print(json.dumps(result, indent=2))
    if strict and errors:
        return 1
    return 0 if not errors else 1
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    raise SystemExit(validate(strict=args.strict))

if __name__ == "__main__":
    main()

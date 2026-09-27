#!/usr/bin/env python3
import hashlib
import re
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
RELEASE = "v2.0.0"

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def skill_name(text, slug):
    match = re.search(r"^# Skill:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else slug.replace("-", " ").title()

def main():
    entries = []
    for directory in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        slug = directory.name
        md_path = directory / "SKILL.md"
        if not md_path.exists():
            continue
        md = md_path.read_text(encoding="utf-8")
        contract_path = directory / "skill.yaml"
        if contract_path.exists():
            contract = yaml.safe_load(contract_path.read_text(encoding="utf-8"))
            entry = {
                "id": slug,
                "name": contract["name"],
                "version": contract["version"],
                "status": contract["status"],
                "contract_version": "2.0",
                "source_path": f"skills/{slug}/SKILL.md",
                "contract_path": f"skills/{slug}/skill.yaml",
                "source_revision": RELEASE,
                "source_sha256": sha256(md_path),
                "runtimes": contract["runtimes"],
                "authority_class": contract["authority"]["class"],
                "mutation_level": "none" if contract["allowed_mutations"] == ["none"] else "bounded",
                "capabilities": contract["capabilities"],
                "evidence_requirements": contract["evidence"],
            }
        else:
            status = "deprecated" if slug == "powerpoint-arb-deck" else "legacy"
            entry = {
                "id": slug,
                "name": skill_name(md, slug),
                "version": "1.0.0",
                "status": status,
                "contract_version": "1.0",
                "source_path": f"skills/{slug}/SKILL.md",
                "source_revision": RELEASE,
                "source_sha256": sha256(md_path),
                "runtimes": ["chatgpt", "claude", "codex"],
                "authority_class": "none",
                "mutation_level": "none",
                "capabilities": ["legacy-library"],
                "evidence_requirements": ["Result as defined by SKILL.md"],
            }
        entries.append(entry)

    registry = {
        "schema_version": "2.0",
        "repository": "https://github.com/jjuniper-dev/skills",
        "release_revision": RELEASE,
        "skills": entries,
    }
    (ROOT / "registry.yaml").write_text(
        yaml.safe_dump(registry, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    print(f"registered={len(entries)}")

if __name__ == "__main__":
    main()

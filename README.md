# Skills

Canonical portable skill library for reusable, governed AI and enterprise-architecture capabilities.

## Authority boundary

This repository defines **capability procedure**, not execution authority. A skill cannot create work authority, tool authority, credential authority, leases, merge approval, publication approval, or production authority. Governed consumers such as PCA/WF60 must supply those controls externally.

## Skill Contract v2

V2 skills pair human guidance (`SKILL.md`) with a machine-readable contract (`skill.yaml`) using:

**Intent → Preconditions → Inputs → Authority → Procedure → Allowed Mutations → Evidence → Success Criteria → Stop Conditions → Handoff**

See `docs/skill-contract-v2.md`.

## Registry and provenance

`registry.yaml` is the canonical discovery surface. Every registered skill includes repository path, release revision, SHA-256 source hash, declared runtimes, authority class, mutation level, capability mappings, and evidence requirements.

Resolve a governed binding with:

```bash
python tools/resolve_skill.py --skill governed-execution --runtime codex --format wf60
```
## Production v2 skills

- `architecture-diagram`
- `work-package-orchestration`
- `governed-execution`
- `agent-dispatch`
- `outcome-verification`
- `runtime-evidence`
- `credential-authority`
- `evidence-engineering`
- `session-handover`
- `ea-delivery-pipeline`
- `qa-recording-evidence`

Existing v1 skills remain registered as `legacy` until deliberately migrated. `powerpoint-arb-deck` is retained as deprecated history.

## Validation

```bash
python -m pip install -r requirements-dev.txt
python tools/build_registry.py
python tools/validate_repo.py --strict
python -m unittest discover -s tests -v
python tools/portability_proof.py --check
```

GitHub Actions runs the validation and test spine on pull requests and `main`.
## Repository structure

```text
.github/workflows/validate.yml
registry.yaml
schemas/
  skill-contract-v2.schema.json
  skill-registry.schema.json
skills/<skill>/
  SKILL.md
  skill.yaml          # v2 skills only
tools/
  build_registry.py
  validate_repo.py
  resolve_skill.py
  portability_proof.py
docs/
  skill-contract-v2.md
  wf60-integration.md
  baseline-v2.json
evidence/
  portability-proof.json
```

## Governance

- Prefer reusable mechanisms over project-specific instructions.
- Keep transient tickets, run IDs, leases, branches, secret paths, and current runtime state out of skill definitions.
- Pin governed skill use to an immutable revision or release plus source hash.
- Preserve independent verification and retained human gates.
- Skill possession never grants tool or mutation authority.

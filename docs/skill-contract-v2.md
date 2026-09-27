# Skill Contract v2

Skill Contract v2 separates reusable procedure from execution authority. A skill describes how a capability is performed; it never authorizes work, tools, credentials, mutation, merge, publication, or production access.

## Canonical contract

Every v2 skill has a human-readable `SKILL.md` and a machine-readable `skill.yaml`.

The machine contract contains the following ordered concerns:

1. **Intent** — the durable outcome the skill exists to produce.
2. **Preconditions** — facts that must already be true.
3. **Inputs** — required and optional information.
4. **Authority** — required authority class and explicit constraints.
5. **Procedure** — deterministic execution steps.
6. **Allowed Mutations** — the maximum side effects the skill may request.
7. **Evidence** — proof the procedure actually ran.
8. **Success Criteria** — observable conditions for completion.
9. **Stop Conditions** — conditions that force fail-closed behavior.
10. **Handoff** — what is returned to the caller or next governed stage.

## Authority rule

`authority.grants_authority` is permanently `false` in the schema.

An orchestrator may select a skill only after its own work-authority, policy, lease, credential, and human-gate requirements are satisfied. Loading a skill cannot widen any of those permissions.

## Version and provenance

Governed consumers resolve a skill through `registry.yaml` and retain:

- repository URL
- skill path
- release revision
- SHA-256 of the human-readable skill
- contract hash
- runtime binding

Mutable URLs are discovery surfaces, not governed execution authority. Release tags or commit SHAs are the normal pinning mechanism.

## Legacy skills

Existing v1 skills remain registered as `legacy` until deliberately migrated. They remain discoverable but do not receive a v2 machine contract merely by being present in the repository.

The `architecture-diagram` skill is the reference migration used to prove the v2 schema.

# Skill: Governed Execution
**Version**: 2.0.0 | **Status**: Production | **Contract**: Skill Contract v2

## Intent
Execute an already-authorized bounded work package while preserving authority, mutation ceilings, evidence, and fail-closed behavior.
## Preconditions
- A governing work request or bounded user intent exists.
- Required external authority is resolved outside this skill.
## Inputs
- **work_request** (required): Bounded outcome or governed work package.
- **context** (required): Pinned or attributable context required to perform the skill.
## Authority
Authority class: **bounded-mutation**. This skill never grants authority. External governance must enforce work authorization, tools, credentials, leases, human gates, and production boundaries.
## Procedure
1. Revalidate work authority and readiness.
2. Verify lease or equivalent mutation authority.
3. Materialize pinned context and skills.
4. Execute only the bounded change.
5. Run deterministic verification.
6. Package evidence for independent review.
## Allowed Mutations
- authorized repository files within the work package
- bounded branch and pull-request state
## Evidence
- request and authority identity
- files changed
- tests and verification
- branch and pull-request lineage
## Success Criteria
- Requested outcome is verified within scope.
- Evidence is sufficient for downstream acceptance.
- Human gates remain intact.
## Stop Conditions
- Authority or lease is absent or ambiguous.
- Scope expands unexpectedly.
- Credentials fail or evidence cannot be verified.
## Handoff
- verification-ready evidence
- remaining blockers
- human decision if retained
## Runtime Portability
Declared runtimes: chatgpt, claude, codex, wf60. Runtime choice may change mechanics but cannot change scope or authority.

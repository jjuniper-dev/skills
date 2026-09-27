# Skill: Outcome Verification
**Version**: 2.0.0 | **Status**: Production | **Contract**: Skill Contract v2

## Intent
Independently determine whether an executed change produced the intended observable outcome.
## Preconditions
- A governing work request or bounded user intent exists.
- Required external authority is resolved outside this skill.
## Inputs
- **work_request** (required): Bounded outcome or governed work package.
- **context** (required): Pinned or attributable context required to perform the skill.
## Authority
Authority class: **read**. This skill never grants authority. External governance must enforce work authorization, tools, credentials, leases, human gates, and production boundaries.
## Procedure
1. Load the expected outcome and verification plan.
2. Observe current state independently of the implementer.
3. Run deterministic checks.
4. Classify evidence as healthy, regression, or inconclusive.
5. Return a machine-readable verdict with provenance.
## Allowed Mutations
- none
## Evidence
- verification plan
- observations
- test results
- verdict provenance
## Success Criteria
- Verdict is VERIFIED_HEALTHY, REGRESSION_DETECTED, or INCONCLUSIVE.
- Every verdict is supported by evidence.
## Stop Conditions
- Target cannot be observed safely.
- Required evidence source is unavailable.
- Verification would require unauthorized mutation.
## Handoff
- verification verdict
- evidence references
- recommended next governed state
## Runtime Portability
Declared runtimes: chatgpt, claude, codex, wf60. Runtime choice may change mechanics but cannot change scope or authority.

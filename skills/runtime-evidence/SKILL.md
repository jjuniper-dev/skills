# Skill: Runtime Evidence
**Version**: 2.0.0 | **Status**: Production | **Contract**: Skill Contract v2

## Intent
Collect read-only runtime, service, container, version, and health evidence with provenance and no target mutation.
## Preconditions
- A governing work request or bounded user intent exists.
- Required external authority is resolved outside this skill.
## Inputs
- **work_request** (required): Bounded outcome or governed work package.
- **context** (required): Pinned or attributable context required to perform the skill.
## Authority
Authority class: **read**. This skill never grants authority. External governance must enforce work authorization, tools, credentials, leases, human gates, and production boundaries.
## Procedure
1. Resolve the authorized observation target.
2. Capture server and service identity and versions.
3. Capture container or process state.
4. Collect bounded health evidence.
5. Normalize results into an evidence envelope.
## Allowed Mutations
- none
## Evidence
- target identity
- server and service status
- versions
- container or process state
- health observations
## Success Criteria
- Evidence is attributable and sufficient for outcome verification.
- No target mutation occurred.
## Stop Conditions
- Target identity is ambiguous.
- Observation requires privileged mutation.
- Sensitive output cannot be safely redacted.
## Handoff
- runtime evidence envelope
- gaps or inconclusive observations
## Runtime Portability
Declared runtimes: chatgpt, claude, codex, wf60. Runtime choice may change mechanics but cannot change scope or authority.

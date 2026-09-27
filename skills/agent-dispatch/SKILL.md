# Skill: Agent Dispatch
**Version**: 2.0.0 | **Status**: Production | **Contract**: Skill Contract v2

## Intent
Select and launch an eligible agent runtime for bounded work without allowing runtime choice to alter scope or authority.
## Preconditions
- A governing work request or bounded user intent exists.
- Required external authority is resolved outside this skill.
## Inputs
- **work_request** (required): Bounded outcome or governed work package.
- **context** (required): Pinned or attributable context required to perform the skill.
## Authority
Authority class: **read**. This skill never grants authority. External governance must enforce work authorization, tools, credentials, leases, human gates, and production boundaries.
## Procedure
1. Classify the work package.
2. Check runtime and tool readiness.
3. Select the best eligible runtime for the task.
4. Bind immutable context and skill references.
5. Record the selected runtime and constraints.
6. Dispatch only when external authority permits.
## Allowed Mutations
- none
## Evidence
- runtime selection rationale
- readiness result
- pinned execution input
## Success Criteria
- A qualified runtime is selected deterministically.
- Runtime selection does not widen authority.
## Stop Conditions
- No eligible runtime is ready.
- Required tool or model is unavailable.
- Dispatch authority is absent.
## Handoff
- runtime binding
- execution input
- dispatch blocker when not authorized
## Runtime Portability
Declared runtimes: chatgpt, claude, codex, wf60. Runtime choice may change mechanics but cannot change scope or authority.

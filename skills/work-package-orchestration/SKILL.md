# Skill: Work Package Orchestration
**Version**: 2.0.0 | **Status**: Production | **Contract**: Skill Contract v2

## Intent
Turn an authorized outcome into bounded, sequenced work packages without creating competing workers or shadow authority.
## Preconditions
- A governing work request or bounded user intent exists.
- Required external authority is resolved outside this skill.
## Inputs
- **work_request** (required): Bounded outcome or governed work package.
- **context** (required): Pinned or attributable context required to perform the skill.
## Authority
Authority class: **read**. This skill never grants authority. External governance must enforce work authorization, tools, credentials, leases, human gates, and production boundaries.
## Procedure
1. Resolve the governing work item and desired outcome.
2. Decompose it into bounded packages with dependencies.
3. Assign one owner per mutating package.
4. Identify safe parallel read or review lanes.
5. Return an execution plan with stop conditions.
## Allowed Mutations
- none
## Evidence
- work-package graph
- dependency and ownership map
- authority references
## Success Criteria
- Every package has one outcome, owner, dependencies, and acceptance criteria.
- No overlapping mutation ownership is created.
## Stop Conditions
- No authoritative work item exists.
- Scope cannot be bounded.
- A competing mutation owner already exists.
## Handoff
- bounded work packages
- recommended runtime assignments
- retained human gates
## Runtime Portability
Declared runtimes: chatgpt, claude, codex, wf60. Runtime choice may change mechanics but cannot change scope or authority.

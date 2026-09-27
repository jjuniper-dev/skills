# Skill: EA Delivery Pipeline
**Version**: 2.0.0 | **Status**: Production | **Contract**: Skill Contract v2

## Intent
Move enterprise architecture work from governed intake through authored artifacts, evidence, review, and publication-ready output.
## Preconditions
- A governing work request or bounded user intent exists.
- Required external authority is resolved outside this skill.
## Inputs
- **work_request** (required): Bounded outcome or governed work package.
- **context** (required): Pinned or attributable context required to perform the skill.
## Authority
Authority class: **human-gated-mutation**. This skill never grants authority. External governance must enforce work authorization, tools, credentials, leases, human gates, and production boundaries.
## Procedure
1. Resolve intake and architecture outcome.
2. Author working architecture in the collaboration plane.
3. Create controlled technical artifacts in Git.
4. Run quality and evidence checks.
5. Route for required review and approval.
6. Publish only after the retained human gate.
## Allowed Mutations
- bounded architecture artifacts and workflow state when separately authorized
## Evidence
- work-item lineage
- artifact source and render
- CI and QA results
- review decision
## Success Criteria
- Architecture artifact is reproducible reviewable and publication-ready.
- Decision rationale and evidence remain linked.
## Stop Conditions
- Architecture authority is unclear.
- Required review is missing.
- Publication would exceed the approved scope.
## Handoff
- review or publication package
- decision record
- remaining gaps
## Runtime Portability
Declared runtimes: chatgpt, claude, codex, wf60. Runtime choice may change mechanics but cannot change scope or authority.

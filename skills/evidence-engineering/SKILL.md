# Skill: Evidence Engineering
**Version**: 2.0.0 | **Status**: Production | **Contract**: Skill Contract v2

## Intent
Create durable, traceable evidence that proves what was attempted, what changed, what was observed, and what remains uncertain.
## Preconditions
- A governing work request or bounded user intent exists.
- Required external authority is resolved outside this skill.
## Inputs
- **work_request** (required): Bounded outcome or governed work package.
- **context** (required): Pinned or attributable context required to perform the skill.
## Authority
Authority class: **read**. This skill never grants authority. External governance must enforce work authorization, tools, credentials, leases, human gates, and production boundaries.
## Procedure
1. Identify the claim that requires proof.
2. Select primary evidence sources.
3. Capture immutable identifiers and timestamps.
4. Separate observed facts from generated conclusions.
5. Package evidence with lineage.
6. Return gaps explicitly rather than inferring success.
## Allowed Mutations
- none
## Evidence
- source references
- commit run or artifact identifiers
- verification outputs
## Success Criteria
- Claims can be traced to primary evidence.
- Evidence distinguishes fact, inference, and judgment.
## Stop Conditions
- Primary evidence is unavailable.
- Evidence provenance cannot be established.
- Collection would expose secrets.
## Handoff
- evidence package
- claim-to-evidence map
- unresolved gaps
## Runtime Portability
Declared runtimes: chatgpt, claude, codex, wf60. Runtime choice may change mechanics but cannot change scope or authority.

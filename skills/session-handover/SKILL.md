# Skill: Session Handover
**Version**: 2.0.0 | **Status**: Production | **Contract**: Skill Contract v2

## Intent
Reconstruct and transfer execution state from authoritative systems so a new session can continue without relying on conversational memory.
## Preconditions
- A governing work request or bounded user intent exists.
- Required external authority is resolved outside this skill.
## Inputs
- **work_request** (required): Bounded outcome or governed work package.
- **context** (required): Pinned or attributable context required to perform the skill.
## Authority
Authority class: **read**. This skill never grants authority. External governance must enforce work authorization, tools, credentials, leases, human gates, and production boundaries.
## Procedure
1. Resolve the governing work item.
2. Read current repository pull-request and CI state.
3. Identify active leases or workers.
4. Summarize completed evidence and open blockers.
5. Record explicit next actions and retained gates.
## Allowed Mutations
- none
## Evidence
- current work-item status
- repository pull-request and CI references
- active owner or lease state
## Success Criteria
- A new worker can resume from authoritative state without repeating completed work.
## Stop Conditions
- Authoritative systems disagree materially.
- Active mutation ownership cannot be determined.
## Handoff
- bounded state summary
- next executable action
- human gates
## Runtime Portability
Declared runtimes: chatgpt, claude, codex, wf60. Runtime choice may change mechanics but cannot change scope or authority.

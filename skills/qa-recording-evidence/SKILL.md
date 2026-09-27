# Skill: QA Recording Evidence
**Version**: 2.0.0 | **Status**: Production | **Contract**: Skill Contract v2

## Intent
Produce a concise recording that demonstrates a bug, reproduction path, verified behavior, or executive-friendly how-to as QA evidence.
## Preconditions
- A governing work request or bounded user intent exists.
- Required external authority is resolved outside this skill.
## Inputs
- **work_request** (required): Bounded outcome or governed work package.
- **context** (required): Pinned or attributable context required to perform the skill.
## Authority
Authority class: **read**. This skill never grants authority. External governance must enforce work authorization, tools, credentials, leases, human gates, and production boundaries.
## Procedure
1. Define the behavior to demonstrate.
2. Prepare a sanitized reproducible scenario.
3. Record only the bounded sequence.
4. Capture expected versus observed outcome.
5. Store the recording with metadata and link it to the governing work item.
## Allowed Mutations
- none
## Evidence
- MP4 recording
- recording metadata
- reproduction or verification steps
## Success Criteria
- A reviewer can understand the behavior without recreating the entire environment.
- Recording contains no secrets or unrelated sensitive content.
## Stop Conditions
- Recording would expose credentials or sensitive data.
- Scenario cannot be reproduced safely.
## Handoff
- QA recording artifact
- short executive-friendly description
- verification context
## Runtime Portability
Declared runtimes: chatgpt, claude, codex, wf60. Runtime choice may change mechanics but cannot change scope or authority.

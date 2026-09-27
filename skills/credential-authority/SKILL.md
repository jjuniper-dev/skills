# Skill: Credential Authority
**Version**: 2.0.0 | **Status**: Production | **Contract**: Skill Contract v2

## Intent
Use governed credentials only within their declared scope while preventing secrets from becoming content, evidence, or ambient authority.
## Preconditions
- A governing work request or bounded user intent exists.
- Required external authority is resolved outside this skill.
## Inputs
- **work_request** (required): Bounded outcome or governed work package.
- **context** (required): Pinned or attributable context required to perform the skill.
## Authority
Authority class: **human-gated-mutation**. This skill never grants authority. External governance must enforce work authorization, tools, credentials, leases, human gates, and production boundaries.
## Procedure
1. Identify the required operation and minimum credential scope.
2. Resolve the approved credential source.
3. Verify identity and expiry without exposing secret material.
4. Use the credential only for the authorized operation.
5. Record non-secret audit evidence.
6. Revoke or release temporary authority when required.
## Allowed Mutations
- credential lifecycle operations only when separately authorized
## Evidence
- credential source identifier
- scope or role
- non-secret verification result
- audit reference
## Success Criteria
- Operation uses least privilege.
- No secret value appears in repository, prompt, log, or evidence.
## Stop Conditions
- Credential source is ambiguous.
- Requested scope exceeds authorization.
- Secret material would be exposed.
## Handoff
- verified credential readiness or blocker
- non-secret audit evidence
## Runtime Portability
Declared runtimes: chatgpt, claude, codex, wf60. Runtime choice may change mechanics but cannot change scope or authority.

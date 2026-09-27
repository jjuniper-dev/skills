# WF60 integration contract

Skills Repository v2 is a portable capability source. WF60 remains a governed consumer, not a subordinate authority of this repository.

## Binding pattern

A governed consumer resolves a skill to a binding containing:

```json
{
  "skill_id": "governed-execution",
  "version": "2.0.0",
  "runtime": "codex",
  "source": {
    "repository": "https://github.com/jjuniper-dev/skills",
    "path": "skills/governed-execution/SKILL.md",
    "revision": "v2.0.0",
    "sha256": "<verified sha256>"
  },
  "authority": {
    "class": "bounded-mutation",
    "grants_authority": false
  }
}
```

## WF60 rules

- Resolve by registry ID, never by unpinned mutable URL for governed execution.
- Preserve the Jira/work request identity outside the skill.
- Revalidate readiness and authority before any mutation.
- Skill bindings may shape planning, context loading, procedure, verification, and evidence packaging.
- A skill may not mint a lease, grant credentials, approve a merge, authorize production, or declare business completion.
- Reviewer and implementer bindings remain separate when independence is required.

`tools/resolve_skill.py --format wf60` emits the portable binding shape used for PCA-209 verification.

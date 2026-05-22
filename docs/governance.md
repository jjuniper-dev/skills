# Skills Library Governance

## Purpose

This document establishes governance standards for the skills library to ensure consistency, quality, and maintainability across all skill definitions.

## Skill Versioning

### Semantic Versioning
Each skill follows semantic versioning: `MAJOR.MINOR.PATCH`
- **MAJOR**: Significant change to purpose, inputs, or outputs (not backward compatible)
- **MINOR**: New features, templates, or examples (backward compatible)
- **PATCH**: Bug fixes, clarifications, corrections (no functional changes)

### Version Format
Versions are tracked in `SKILL.md` header:
```markdown
# Skill: Presentation Deck
**Version**: 1.2.0 | **Last Updated**: 2026-05-22 | **Status**: Production
```

## Quality Standards

### Skill Definition Quality

Each skill definition must pass these checks:

| Criterion | Standard | Validation |
|-----------|----------|-----------|
| **Purpose** | Clear, single-sentence statement | No jargon, specific use case |
| **When to Use** | 3-5 concrete scenarios | Covers different audience types |
| **Inputs** | Complete list of required/optional inputs | Data types specified |
| **Outputs** | Specific output formats and structure | Examples included |
| **Constraints** | Explicit limitations and boundaries | Safety/quality guardrails |
| **Workflow** | Step-by-step process (5-8 steps) | Ordered, testable |
| **Quality Checks** | Measurable acceptance criteria | Checkbox list (minimum 5) |
| **Examples** | At least one complete example | Real-world scenario |

### Template Quality

Templates must include:
- ✅ Use case description
- ✅ Complete section structure
- ✅ Placeholder text with guidance
- ✅ Speaker notes or usage tips
- ✅ Visual notes (if applicable)

### Example Quality

Examples must include:
- ✅ Input description
- ✅ Complete output/result
- ✅ Configuration (if applicable)
- ✅ Explanation of choices/patterns
- ✅ Quality checklist

## Review Process

### Skill Addition

1. **Author** creates skill in feature branch
2. **Self-review** against quality standards
3. **Pull request** with clear description
4. **Technical review** (architect, domain expert)
5. **Merge** to main branch
6. **Tag** release if MAJOR or MINOR version bump

### Skill Update

- **PATCH updates**: Direct merge after review
- **MINOR updates**: Feature branch → pull request → merge
- **MAJOR updates**: Extended review, deprecation notice if replacing

### Deprecation

When replacing a skill:
1. Add deprecation notice to old skill
2. Mark version as "Deprecated"
3. Link to replacement
4. Keep in repository for 6 months (for reference)
5. Archive to separate folder after 6 months

**Example:**
```markdown
# Skill: PowerPoint ARB Deck
**Status**: Deprecated | **Replaced by**: Presentation Deck (v1.0+)

⚠️ This skill is deprecated. Please use the generic Presentation Deck skill instead.
Reason: ARB-specific version superseded by more flexible generic skill.
```

## Naming Conventions

### Skill Names
- Use title case: `Presentation Deck`, `Neo4j Graph Builder`
- Avoid acronyms unless universally known
- Be descriptive: `Social Feed & News Integration` not `Feed Integration`

### File/Directory Names
- Use kebab-case: `presentation-deck`, `neo4j-graph-builder`
- Match skill name (converted to kebab-case)

### Document Types
- `SKILL.md`: Main skill definition (required)
- `templates/`: Reusable templates
- `examples/`: Real-world examples
- `integration-patterns/`: Code samples, integration guides
- `schemas/`: JSON/YAML schema examples
- `validators/`: Quality check scripts
- `docs/`: Additional documentation

## Maintenance Schedule

| Task | Frequency | Owner |
|------|-----------|-------|
| **Review** outdated examples | Quarterly | Skill maintainer |
| **Update** templates based on feedback | As needed | Skill maintainer |
| **Audit** quality standards | Annually | Architecture team |
| **Deprecate** outdated skills | As needed | Architecture lead |
| **Archive** deprecated content | Annually | Repository admin |

## Feedback & Evolution

### Collecting Feedback
- User feedback recorded in GitHub issues (skill-request, skill-feedback labels)
- Monthly review of feedback trends
- Track "most used" and "needs improvement" skills

### Making Changes
1. **Minor improvements**: Update template, add example (PATCH)
2. **New capability**: Add new template or example (MINOR)
3. **Significant changes**: Create new skill version (MAJOR)

### Deprecation Triggers
- Skill not used for 12+ months
- Skill replaced by better alternative
- Constraint no longer valid (e.g., tool discontinued)

## Compliance & Governance

### Security
- No sensitive credentials in examples
- Glossaries/templates must not expose PII
- Code samples follow security best practices

### Accessibility
- All slide templates must be WCAG 2.1 AA compliant
- Architecture diagrams use colorblind-safe palettes
- Text content readable (no images of text)

### Confidentiality
- Examples use realistic but non-sensitive data
- Government/health Canada examples do not contain real data
- Clearly mark "fictional example" where needed

### Auditability
- All changes tracked in git history
- Version numbers link to commits
- Change log maintained in README updates

## Integration Standards

### Code Samples (Python/JavaScript)
- Follow PEP 8 (Python) or ESLint (JavaScript)
- Include docstrings/JSDoc comments
- Provide requirements.txt or package.json
- Tested examples only

### Configuration Files
- YAML or JSON format
- Document all required fields
- Provide example values
- Include comments explaining non-obvious settings

### API Integration
- Clear authentication requirements
- Rate limits and quotas noted
- Error handling examples
- Retry logic documented

## Version Control

### Branch Naming
- Feature: `skill/skill-name` or `skill-name/enhancement`
- Bug: `skill/skill-name/bug-description`

### Commit Messages
- Format: `[SKILL] Commit message`
- Example: `[presentation-deck] Add executive strategy template`

### Tags
- Format: `v{major}.{minor}.{patch}`
- Example: `v1.2.0` (in context of individual skill)

## Maintenance Contacts

| Skill | Maintainer | Backup |
|-------|-----------|--------|
| Presentation Deck | [Name] | [Name] |
| Architecture Diagram | [Name] | [Name] |
| Neo4j Graph Builder | [Name] | [Name] |
| Social Feed Integration | [Name] | [Name] |
| GCTranslate Integration | [Name] | [Name] |
| Briefing Note | [Name] | [Name] |

## FAQ

**Q: Can I create a skill variant for a specific use case?**
A: Create a new skill if it has distinct inputs/outputs. If it's the same skill with different templates, add a template instead.

**Q: How do I propose a new skill?**
A: File an issue with the `skill-request` label. Include use case, inputs, outputs, and proposed examples.

**Q: When should I deprecate vs. update?**
A: Deprecate if replacing with a better alternative. Update if improving the existing skill.

**Q: Can I modify an example after it's merged?**
A: Yes, improvements are always welcome. File a PR with the `skill-improvement` label.

# Skill: Prompts Layer

## Purpose
Define, manage, and version system prompts and task-specific prompt templates for AI agents and LLM-based workflows.

## When to use
- Building AI agent workflows (multi-step tasks)
- Standardizing LLM interactions across projects
- Creating reusable prompt libraries
- Fine-tuning model behavior and consistency
- Implementing governance and auditability
- Versioning prompts with code
- A/B testing prompt effectiveness

## Inputs
- Skill definition (what the skill does)
- User intent/request (what they want to accomplish)
- Context (documents, data, prior conversation)
- Optional: constraints (budget, quality, safety)
- Optional: examples (few-shot learning)

## Outputs
- System prompt (instructs the model on role/behavior)
- Task prompt (specific instruction for this task)
- Formatted prompt text (ready to send to LLM)
- Validation feedback (prompt quality assessment)
- Example outputs (demonstrate expected results)

## Constraints
- Prompts must be version-controlled (in git)
- System prompts separate from task prompts
- Clear delineation of roles and responsibilities
- No secrets or credentials in prompts
- Compliance with responsible AI principles
- Auditability (can trace which prompt version was used)
- Tested and validated before production use
- Clear documentation of prompt purpose and limitations

## Prompt structure

### System Prompt
Role-based instruction that persists across the conversation.

```
You are an expert [role] with [X years] of experience in [domain].

Your responsibilities:
- [Responsibility 1]
- [Responsibility 2]
- [Responsibility 3]

Guidelines:
- [Guideline 1]
- [Guideline 2]

Constraints:
- [Constraint 1]
- [Constraint 2]

Output format:
- [Format specification]

Tone:
- [Tone/style description]
```

### Task Prompt
Specific instruction for a single task or conversation turn.

```
I need you to [specific task].

Context:
[Relevant context, documents, data]

Requirements:
- [Requirement 1]
- [Requirement 2]

Format:
[Output format specification]

Example:
[If applicable, provide example of expected output]
```

## Workflow
1. **Define skill** - What capability are we building?
2. **Write system prompt** - Role, expertise, guidelines
3. **Write task template** - How users will invoke the skill
4. **Add examples** - Few-shot examples for context
5. **Test prompt** - Validate with real inputs
6. **Iterate** - Refine based on outputs
7. **Version** - Commit to git with version number
8. **Document** - Link to skill definition
9. **Monitor** - Track performance in production
10. **Update** - Improve based on feedback

## Quality checks
- ✅ System prompt clearly defines role
- ✅ Task prompt is specific and actionable
- ✅ Examples demonstrate expected output quality
- ✅ Constraints are explicit and enforceable
- ✅ No secrets or credentials in prompts
- ✅ Prompt is version-controlled
- ✅ Output format matches spec
- ✅ Tested with representative inputs
- ✅ Performance benchmarked (accuracy, speed, cost)

## Output formats
- Text file (plain prompts)
- JSON (structured prompt config)
- YAML (prompt + metadata)
- Python dataclass (type-safe prompts)
- Prompt management system (Prompt Hub, LangChain)

## Example: Briefing Note Generator Prompts

### System Prompt
```
You are an expert government communications specialist with 15 years of experience 
writing executive briefing notes for senior leaders.

Your role:
- Translate complex information into concise, actionable briefs
- Identify key decisions and recommendations
- Anticipate leader concerns and questions
- Ensure accuracy and evidence-based recommendations

Guidelines:
- Be concise: 1-2 pages maximum
- Be clear: No jargon without explanation
- Be balanced: Present alternatives fairly
- Be actionable: Clear recommendation with next steps

Output format:
- Issue (1-2 sentences)
- Background (2-3 paragraphs)
- Considerations (3-5 key points)
- Risks (2-3 risks + mitigations)
- Recommendation (clear, specific)

Tone: Professional, neutral, evidence-based
```

### Task Prompt
```
Write a briefing note for the Deputy Minister on [TOPIC].

Context:
[Key documents, data, recent events]

Decision needed:
[What decision is required?]

Timeline:
[When is decision needed?]

Audience:
[Who will read this? What's their background?]

Requirements:
- Include 2-3 supporting data points
- Flag any controversial aspects
- Suggest next steps after decision

Example of good note:
[Link to previous example or template]
```

## Versioning
```
prompts/
├── system/
│   ├── analyst.v1.md
│   ├── analyst.v2.md (improvements based on feedback)
│   ├── executive-writer.v1.md
│   └── diagram-architect.v1.md
└── task/
    ├── briefing-note-generator.v1.md
    ├── briefing-note-generator.v2.md (refined)
    ├── architecture-diagram-creator.v1.md
    └── graph-builder.v1.md
```

## Git workflow
```bash
# Create new prompt version
git checkout -b prompts/briefing-note-v2

# Edit prompt
vim prompts/task/briefing-note-generator.v2.md

# Commit with context
git commit -m "Improve briefing note prompt: add decision deadline handling

- Clearer decision framing
- Better risk mitigation guidance
- Tested with 10 examples (90% quality target)"

# Tag release
git tag prompts/briefing-note@v2.0
```

## Monitoring & iteration
- Track prompt performance (accuracy, user satisfaction)
- A/B test prompt variants
- Collect feedback from users
- Update based on failure cases
- Document lessons learned
- Share improvements with team

## Integration with skills
Each skill can reference one or more prompts:

```markdown
# Skill: Briefing Note

## Prompts Used
- System: `prompts/system/executive-writer.v2.md`
- Task: `prompts/task/briefing-note-generator.v2.md`
- Examples: `prompts/examples/briefing-notes/*.md`

## Performance
- Avg quality score: 4.2/5
- User satisfaction: 85%
- Cost per generation: $0.02
```

## Related skills
- **Presentation Deck** - Prompts for slide generation
- **Briefing Note** - Executive writing prompts
- **Architecture Diagram** - Diagram generation prompts
- **Neo4j Graph Builder** - Graph schema creation prompts

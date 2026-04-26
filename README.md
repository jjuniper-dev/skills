# Skills

Reusable skill definitions, artifact-production rules, prompt templates, schemas, and validation patterns for architecture, briefing, PowerPoint, and governance-oriented AI workflows.

## Purpose

This repository is a versioned capability library. It is intended to make repeated work easier, more consistent, and more auditable by turning high-value prompts and production standards into reusable skills.

The repo is designed for:

- Enterprise architecture artifact production
- ARB / executive PowerPoint support
- Briefing notes and government-style written artifacts
- Strategic screening and governance review
- Accessible presentation production
- Agent-supported workflows and future automation

## Repository structure

```text
skills/
├── README.md
├── skills/
│   ├── architecture-diagram/
│   │   ├── SKILL.md
│   │   ├── examples/
│   │   └── templates/
│   ├── briefing-note/
│   │   ├── SKILL.md
│   │   ├── examples/
│   │   └── templates/
│   ├── powerpoint-arb-deck/
│   │   ├── SKILL.md
│   │   ├── examples/
│   │   └── templates/
│   ├── strategic-screening/
│   │   ├── SKILL.md
│   │   └── rubrics/
│   └── accessible-pptx/
│       ├── SKILL.md
│       └── validators/
├── schemas/
│   ├── skill.schema.json
│   └── artifact-request.schema.json
├── prompts/
│   ├── system/
│   └── task/
└── docs/
    ├── governance.md
    ├── naming-conventions.md
    └── usage-patterns.md
```

## Skill format

Each skill should define:

- Purpose
- When to use it
- Inputs
- Outputs
- Constraints
- Workflow
- Quality checks
- Examples

## Initial MVP skills

1. Architecture Diagram
2. PowerPoint ARB Deck
3. Strategic Screening
4. Briefing Note
5. Accessible PPTX

## Design principles

- Prefer reusable patterns over one-off prompts.
- Keep artifacts traceable, versioned, and reviewable.
- Separate production rules from project-specific content.
- Make governance and accessibility checks explicit.
- Support both human use and future agent use.

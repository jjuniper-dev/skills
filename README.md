# Skills

Reusable skill definitions, artifact-production rules, prompt templates, schemas, and validation patterns for architecture, briefing, PowerPoint, and governance-oriented AI workflows.

## Purpose

This repository is a versioned capability library. It is intended to make repeated work easier, more consistent, and more auditable by turning high-value prompts and production standards into reusable skills.

The repo is designed for:

- Enterprise architecture artifact production
- Executive presentation and decision support
- Multi-language content and localization
- Briefing notes and government-style written artifacts
- Strategic screening and governance review
- Knowledge graph construction and relationship mapping
- Real-time intelligence and news aggregation
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
│   ├── presentation-deck/
│   │   ├── SKILL.md
│   │   ├── examples/
│   │   ├── templates/
│   │   └── validators/
│   ├── strategic-screening/
│   │   ├── SKILL.md
│   │   └── rubrics/
│   ├── powerpoint-arb-deck/
│   │   ├── SKILL.md
│   │   ├── examples/
│   │   └── templates/
│   ├── neo4j-graph-builder/
│   │   ├── SKILL.md
│   │   ├── examples/
│   │   ├── schemas/
│   │   └── queries/
│   ├── social-feed-news-integration/
│   │   ├── SKILL.md
│   │   ├── examples/
│   │   └── integration-patterns/
│   ├── gctranslate-integration/
│   │   ├── SKILL.md
│   │   ├── examples/
│   │   ├── glossaries/
│   │   └── integration-patterns/
│   └── accessible-pptx/
│       ├── SKILL.md
│       └── validators/
├── schemas/
│   ├── skill.schema.json
│   ├── artifact-request.schema.json
│   └── architecture.schema.json
├── prompts/
│   ├── system/
│   └── task/
└── docs/
    ├── governance.md
    ├── naming-conventions.md
    ├── usage-patterns.md
    └── hc-template-guide.md
```

## Core Skills

### Presentation & Storytelling
- **Presentation Deck** - Generic PPTX production for executive, governance, and business communications (ARB, strategy, briefings)
- **Briefing Note** - Structured government-style briefings for policy, program, or architecture decisions
- **PowerPoint ARB Deck** - [Legacy] Specialized ARB submission decks

### Architecture & Design
- **Architecture Diagram** - Clean, executive-ready architecture diagrams from text or structured input
- **Neo4j Graph Builder** - Graph database schema generation, Cypher queries, knowledge graph modeling

### Intelligence & Integration
- **Social Feed & News Integration** - Real-time aggregation and normalization of social feeds and news sources
- **Google Cloud Translate** - Multi-language content translation with glossary support and localization workflows

### Governance & Analysis
- **Strategic Screening** - Opportunity screening and governance evaluation framework
- **Accessible PPTX** - Accessibility validation and remediation for PowerPoint presentations

## Docker images

- **Claude Code**: `docker/claude-code/` contains a small Alpine-based Docker image and Compose entrypoint for running Claude Code in a container against a mounted repository.

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

## Design principles

- Prefer reusable patterns over one-off prompts
- Keep artifacts traceable, versioned, and reviewable
- Separate production rules from project-specific content
- Make governance and accessibility checks explicit
- Support both human use and future agent use
- Integrate with enterprise systems and workflows
- Document integration points and API contracts

## Recent enhancements

- **Presentation Deck**: Generalized from ARB-only to support any organizational context
- **Architecture Diagram**: Added diagram type guidance and enhanced quality criteria
- **Neo4j Graph Builder**: New skill for graph database modeling
- **Social Feed Integration**: New skill for real-time intelligence aggregation
- **GCTranslate Integration**: New skill for multi-language support

## Usage patterns

[See docs/usage-patterns.md for workflow examples]

## Governance & Naming

[See docs/governance.md and docs/naming-conventions.md for standards]

## HC Template Guide

[See docs/hc-template-guide.md for template specification and integration]

# Skill: Architecture Diagram

## Purpose
Generate clean, executive-ready architecture diagrams from structured or natural language input.

## When to use
- Creating EA visuals for ARB or executive decks
- Translating architecture descriptions into diagrams

## Inputs
- Plain language description OR structured JSON
- Optional constraints (style, layout, audience)

## Outputs
- Mermaid / PlantUML / SVG / PPTX-ready diagram

## Workflow
1. Parse input systems and relationships
2. Normalize into components and flows
3. Apply layout rules (layered, network, etc.)
4. Generate diagram code
5. Validate readability and completeness

## Quality checks
- Clear flow direction
- No orphan nodes
- Consistent naming
- Executive readability

## Notes
Default style: clean, government-friendly, WCAG-legible

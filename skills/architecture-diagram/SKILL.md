# Skill: Architecture Diagram

## Purpose
Generate clean, executive-ready architecture diagrams from structured or natural language input. Transform architecture descriptions into visually compelling, accessible diagrams suitable for governance, decision-making, or technical documentation.

## When to use
- Creating EA visuals for ARB or executive decks
- Translating architecture descriptions into diagrams
- Technical documentation and design reviews
- Solution architecture visualization
- System dependency mapping
- Data flow and integration diagrams
- Infrastructure and deployment architectures

## Inputs
- Plain language description OR structured JSON/YAML
- Diagram type hint (system context, C4, layered, network, flow)
- Optional: style, color palette, layout preferences
- Optional: audience (executive, technical, mixed)
- Optional: existing templates or base diagrams

## Outputs
- Mermaid / PlantUML / SVG source code
- PPTX-ready diagram (image + metadata)
- HTML/web-ready version
- Accessibility annotations (alt text, color info)
- Legend and notation guide

## Constraints
- Clear flow direction (left-to-right or top-to-bottom)
- No orphan nodes without relationships
- Consistent naming conventions
- Color choices meet WCAG contrast requirements
- Executive readability (readable at 50% zoom)
- No more than 15-20 major elements per diagram
- Relationships clearly labeled

## Diagram types
- **System Context** - High-level system and external actors
- **Container** - Major containers/components and their connections
- **Component** - Internal structure of a container
- **Code** - Classes, interfaces, detailed relationships
- **Flow** - Process flows, data flows, user journeys
- **Network/Infrastructure** - Cloud resources, deployments, topology
- **Dependency Graph** - Service/module dependencies

## Workflow
1. **Parse input** - Extract entities, relationships, and constraints
2. **Select diagram type** - Match input to appropriate pattern
3. **Normalize elements** - Standardize naming, remove duplication
4. **Apply layout rules** - Use appropriate layout (layered, network, hierarchical)
5. **Generate diagram code** - Mermaid, PlantUML, or custom format
6. **Validate readability** - Check flow, spacing, label clarity
7. **Apply styling** - Colors, typography, branding
8. **Generate accessible output** - Alt text, color values, accessible fonts
9. **Embed in PPTX** - Create slide-ready version if needed

## Quality checks
- Clear flow direction (no cycles or confusing paths)
- All nodes have at least one relationship (no orphans)
- Consistent naming across all elements
- Executive readability (zoom test at 50%)
- WCAG AA color contrast achieved
- Relationships are typed and meaningful
- Diagram fits in standard slide/page (no excessive width/height)
- Legend clear and complete

## Output formats
- Mermaid syntax (editable, version-controllable)
- PlantUML (detailed, customizable rendering)
- SVG (scalable, embeddable, styleable)
- PNG/PDF (distribution, print-ready)
- PPTX slide (presentation-ready with speaker notes)
- JSON schema representation

## Style options
- Clean government-friendly (default)
- Modern tech/startup aesthetic
- Corporate/enterprise formal
- Dark mode
- Color-blind safe palette

## Templates
- Control Plane Architecture (governance/security layer)
- Microservices mesh
- Data warehouse/lake
- Event-driven system
- Cloud-native deployment
- Integration/middleware
- API ecosystem

## Notes
- Default: clean, government-friendly, WCAG-legible
- Support both C4 model and UML-style diagrams
- Can generate from architecture decision records (ADRs)
- Integrates with diagram-as-code tools

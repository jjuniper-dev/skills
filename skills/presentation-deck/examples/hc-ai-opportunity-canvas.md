# Example: HC/PHAC AI Opportunity Canvas

## Overview

This example demonstrates how to programmatically generate an HC/PHAC branded Opportunity Canvas for an AI initiative at Health Canada.

## Context

The Health Canada/Public Health Agency of Canada (HC/PHAC) is exploring AI opportunities to enhance public health and regulatory work. This canvas captures the strategic opportunity.

## Usage

### Quick Start (Python)

```python
from hc_canvas_generator import OpportunityCanvas

# Define your opportunity
data = {
    "target_users": [
        "HC/PHAC analysts, scientists, inspectors",
        "Decision‑makers in public health/regulatory",
        "Canadian public via improved services"
    ],
    "problems": [
        "Manual analysis slows health threat response",
        "Fragmented data impedes insights",
        "High regulatory workload"
    ],
    # ... (see full data below)
}

# Generate presentation
canvas = OpportunityCanvas("Opportunity Canvas — AI at HC/PHAC")
path = canvas.build(data)
print(f"Created: {path}")
```

## Canvas Data Structure

### Target Users and Customers
```python
"target_users": [
    "HC/PHAC analysts, scientists, inspectors",
    "Decision‑makers in public health/regulatory",
    "Canadian public via improved services"
]
```

**Key insights**:
- Internal users (analysts, scientists)
- Decision-makers (ADM, DM-level)
- External beneficiaries (public health outcomes)

### User Problems and Needs
```python
"problems": [
    "Manual analysis slows health threat response",
    "Fragmented data impedes insights",
    "High regulatory workload"
]
```

**Validation**:
- Speed: Threat detection needs to be sub-day
- Integration: Data lives in multiple silos
- Capacity: Review backlogs evident across programs

### Current Alternatives
```python
"alternatives": [
    "Excel/Access databases, manual reports",
    "Ad hoc automation, not enterprise‑grade",
    "Heavy reliance on SMEs for repetition"
]
```

**Gap analysis**:
- Current tools are not scalable
- No consistent automation framework
- Bottleneck: SME availability

### Usage Contexts (Highest-Value Use Cases)
```python
"contexts": [
    "National outbreak detection – early threat spotting",
    "Drug & medical device review – faster safe approvals",
    "Climate‑health impact mapping – predict, mitigate risk",
    "Inspection targeting – focus on highest risk areas",
    "Policy intelligence scanning – rapid global insight"
]
```

**Prioritization**:
1. Outbreak detection (life safety, political priority)
2. Regulatory approval speed (competitive advantage)
3. Climate health (emerging priority)
4. Inspection efficiency (operational)
5. Intelligence (strategic)

### Solution Ideas and Scope
```python
"solution": [
    "Enterprise AI platform via PATH",
    "AI‑native productivity and delivery tools",
    "AI‑enablers (MLOps, RAG, model serving)",
    "Integration of spatial data/geomatics intelligence",
    "Leverage Justice (Otto) and NRC AI assets to accelerate and de‑risk delivery",
    "Incorporate Developer Copilot for secure, compliant code acceleration"
]
```

**Architecture**:
- Platform: PATH (Government of Canada cloud platform)
- Approach: Enterprise-grade, reusable AI services
- Reuse: Existing GC assets (Justice Otto, NRC)
- Acceleration: Developer tooling (GitHub Copilot)

### User Value Proposition
```python
"value_prop": [
    "50% faster decisions",
    "Improved accuracy and consistency",
    "Free up time for high‑value work"
]
```

**Benefits**:
- Speed: Outbreak response: 24h → 12h
- Accuracy: Reduce false positives in screening
- Morale: Analysts focus on judgment, not data entry

### Adoption Strategy
```python
"adoption": [
    "Start with highest‑value, lowest‑risk priorities",
    "AI literacy and ethics training",
    "Transparent evaluation and AIA compliance for ADM/DM assurance"
]
```

**Phased approach**:
1. **Pilot**: Outbreak detection (high value, tractable data)
2. **Scale**: Regulatory review (clear success metrics)
3. **Expand**: Climate health, inspection (broader scope)
4. **Culture**: Training, transparency, governance

### Success Metrics
```python
"metrics": [
    "≥90% AIA before production",
    "≥80% reuse of PATH AI services",
    "≥50% faster time‑to‑insight"
]
```

**Definition of success**:
- Governance: All models pass Algorithmic Impact Assessment
- Efficiency: Leverage existing solutions (reduce duplication)
- Impact: Measurable speed improvement in key workflows

### Business Value
```python
"business_value": [
    "Stronger health readiness",
    "Faster regulatory processing",
    "Higher productivity and morale",
    "Better spatial awareness for decisions",
    "Increased public trust",
    "Accelerated outcomes via reuse of GC solutions",
    "Reduced delivery timelines via Developer Copilot"
]
```

**Strategic outcomes**:
- Mission: Better protect public health
- Operations: Faster decision-making
- Culture: More engaging, high-value work
- Trust: Transparent, ethical AI
- Cost: Accelerated delivery, reduced risk

### Costs & Constraints
```python
"costs": [
    "PATH infrastructure investment",
    "Compliance with GC/TBS/privacy",
    "Non‑goal: replacing human expertise"
]
```

**Critical guardrails**:
- Funding: PATH platform cost (shared across GC)
- Governance: AIA, privacy, Treasury Board compliance
- Philosophy: AI augments expertise, doesn't replace

### Risks & Assumptions
```python
"risks": [
    "Risk: Low adoption if trust lacking",
    "Risk: Data quality limits value",
    "Assumption: PATH scales with demand"
]
```

**Mitigation**:
- Trust: Early wins, transparent communication
- Data: Data quality assessment in pilot
- Scale: Phased rollout, feedback loops

### Open Questions
```python
"questions": [
    "Which highest‑value, lowest‑risk priorities first?",
    "How to sustain governance capacity long‑term?",
    "Next: formalize roadmap, align with ADM/DM priorities"
]
```

**Decision gates**:
1. Q2 2026: Prioritize use cases with stakeholders
2. Q3 2026: Pilot design and approval
3. Q4 2026: Pilot launch and evaluation

## Color Legend

The canvas uses HC/PHAC brand colors:

- **Neutral Gray** (left column): Context, problems, current state
- **Light Blue** (middle column): Solution, approach, value
- **Light Green** (right column): Business value, outcomes, decisions

## Generating Variations

### Healthcare Program Example
```python
canvas = OpportunityCanvas("AI for Patient Monitoring")
data = {
    "target_users": ["Healthcare providers", "Patients"],
    "problems": ["Slow diagnosis", "Manual monitoring"],
    # ... customize for your use case
}
canvas.build(data)
```

### Regulatory Process Automation
```python
canvas = OpportunityCanvas("Regulatory AI")
data = {
    "target_users": ["Regulatory inspectors", "Applicants"],
    "problems": ["Slow approvals", "Inconsistent standards"],
    # ... customize
}
canvas.build(data)
```

## Integration with Presentation Decks

Use canvas as part of larger strategy deck:

```python
from slide_generator import DeckBuilder

builder = DeckBuilder("HC AI Strategy", "Author Name")

# Add canvas slide
canvas_slide = SlideGenerator.create_opportunity_canvas(
    "AI Opportunity Canvas",
    opportunity_data
)

# Build complete deck
presentation = builder.build_executive_briefing(
    situation={"headline": "Health Canada AI Initiative"},
    options=[...],
    recommendation={...},
    # ... other sections
)
```

## Output

**File**: `Opportunity_Canvas_AI_HC_PHAC.pptx`

**Slide dimensions**: 17" × 11" (landscape, fits 12 cards)

**Layout**: 3 columns × 4-5 rows of rounded rectangle cards

**Branding**: HC/PHAC colors, professional typography

## Customization

### Colors
```python
from hc_canvas_generator import HC_COLORS

# Use HC colors in your code
title_color = HC_COLORS["primary"]    # Dark blue
card_blue = HC_COLORS["secondary"]    # Light blue
card_green = HC_COLORS["tertiary"]    # Light green
```

### Add Custom Cards
```python
canvas = OpportunityCanvas("My Canvas")

# Add a custom card to any position
canvas.add_card(
    title="Custom Card",
    lines=["Point 1", "Point 2"],
    x=12.0,  # inches from left
    y=2.0,   # inches from top
    width=4.5,
    height=2.0,
    fill_color=HC_COLORS["neutral"]
)

canvas.save("custom-canvas.pptx")
```

## Quality Checklist

✅ Canvas is complete (all sections filled)
✅ Content is concise (max 5-6 lines per card)
✅ Assumptions are explicit ("Assumption: ...")
✅ Risks have mitigations ("Risk: ... Mitigation: ...")
✅ Success metrics are measurable and specific
✅ Open questions frame next decisions
✅ Colors match HC/PHAC branding
✅ Fonts are readable (sans-serif, bold titles)

## Next Steps

After creating the canvas:

1. **Socialize with stakeholders** (analysts, leadership)
2. **Refine based on feedback** (iterate on data)
3. **Formalize into strategy** (transition to executive briefing deck)
4. **Set up governance** (AIA, ethics review)
5. **Plan implementation** (roadmap, phasing)

## Related Skills

- **Presentation Deck**: For full strategy presentation (slide-generator.py)
- **Briefing Note**: For executive summary (1-2 pages)
- **Architecture Diagram**: For system design (how to build it)
- **Neo4j Graph Builder**: For stakeholder/dependency mapping

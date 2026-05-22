# Template: Task Prompt

## Instructions

Use this template to create task prompts for specific requests within a conversation. Task prompts are paired with system prompts to provide complete instructions for AI agents.

---

## Template

```
I need you to [SPECIFIC TASK].

**Context & Background:**
[Relevant situation, prior decisions, constraints]

**Key Information:**
- [Fact 1]
- [Fact 2]
- [Fact 3]

**Requirements:**
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

**Constraints:**
- [Constraint 1]
- [Constraint 2]
- Budget/timeline: [if applicable]

**Success Criteria:**
- [Criterion 1]
- [Criterion 2]
- [How you'll know it's successful]

**Format:**
[Specify output format, length, structure]

**Audience:**
[Who will read/use this? What's their background?]

**Examples:**
[If helpful, provide 1-2 examples of good output]

**Questions to Address:**
- [Question 1]
- [Question 2]
```

---

## Example 1: Policy Analysis Task

```
I need you to write a policy analysis of the proposed national AI governance framework.

**Context & Background:**
- Treasury Board released a draft framework in April 2026
- Cabinet is reviewing for potential approval in June
- This analysis is for the Deputy Minister of Innovation, Science and Technology
- There are competing concerns about innovation speed vs. safety

**Key Information:**
- Framework proposes mandatory AI impact assessments for government AI
- Compliance timeline: 18 months for all departments
- Estimated implementation cost: $50-100M

**Requirements:**
- Analyze feasibility of 18-month timeline
- Identify trade-offs between compliance requirements and innovation
- Assess international alignment (compare to UK, EU approaches)
- Recommend option for Cabinet consideration

**Constraints:**
- Do not take a position on whether framework is "good" or "bad"
- Present options fairly
- Assume Cabinet wants to be world leaders AND responsible
- Budget: within existing IT transformation funds

**Success Criteria:**
- Policy options are clearly differentiated
- Trade-offs are explicit (not hidden)
- Recommendation is justified with evidence
- Document addresses Cabinet's known concerns

**Format:**
- 3-4 pages (briefing memo style)
- Use headings: Issue | Options | Analysis | Recommendation
- Include 1-page summary at start

**Audience:**
- Deputy Ministers (policy/technical literacy, political awareness)
- Will brief full Cabinet

**Questions to Address:**
- Is 18-month timeline realistic?
- What are implementation risks?
- How does this compare to other jurisdictions?
- What's the political downside of each option?

**Example:**
[Link to previous governance briefing memo, or inline example]
```

---

## Example 2: Emergency Response Communication Task

```
I need you to draft public health messaging for a new communicable disease threat.

**Context & Background:**
- Novel variant detected in 2 provinces (Ontario, Quebec)
- 15 confirmed cases, no deaths
- Media is asking questions (uncertainty is high)
- Public is concerned but not panicked (yet)
- We want to maintain trust and transparency

**Key Information:**
- Transmission mode: respiratory droplets
- Severity: moderate (hospitalization rate ~5%)
- Vaccine effectiveness: unknown (estimated 60-80%)
- Incubation period: 3-5 days

**Requirements:**
- Calm and informative (not alarming)
- Accurate but humble about uncertainties
- Actionable for public (what should people do?)
- Suitable for social media, news releases, and website

**Constraints:**
- Do NOT overstate confidence in estimates
- Must align with WHO statements
- Cannot commit to specific vaccination timelines
- Must acknowledge that situation may change

**Success Criteria:**
- Public feels informed (not panicked)
- Media quotes are positive and accurate
- Messaging is consistent across channels
- Builds confidence in health authority

**Format:**
- Main statement (100 words) — for press release + social media
- FAQ (5-7 Q&As) — for website
- Talking points for health officials (bullet format)

**Audience:**
- General public (no medical background)
- Media (looking for conflict or reassurance)
- Health officials (need consistent messaging)

**Examples:**
- [Link to previous outbreak messaging]
- [Example FAQ structure from 2023 incident]
```

---

## Example 3: Technical Architecture Task

```
I need you to design a data architecture for a health data integration platform.

**Context & Background:**
- Health Canada needs to integrate data from 10+ provincial health systems
- Data includes: case reports, vaccination records, lab results, hospitalizations
- Privacy is critical (PIPEDA compliance required)
- Some provinces have legacy systems (XML/CSV), others have APIs

**Key Information:**
- Data volume: ~50M records/year
- Query latency requirement: <5 seconds
- Availability: 99.9% (health-critical system)
- Security: must support role-based access control (RBAC)

**Requirements:**
- Design supports real-time data ingestion
- Supports ad hoc analysis queries
- Provides audit trail of all data access
- Handles schema evolution (provinces add new fields over time)

**Constraints:**
- Budget: $2-5M for first year
- Infrastructure: must use Canadian cloud providers
- Timeline: production in 12 months
- Cannot require changes to provincial systems

**Success Criteria:**
- Processes all daily provincial reports within 2 hours
- Supports analyst queries without IT mediation
- Zero security breaches in pilot
- Accepted by 5+ provinces for pilot

**Format:**
- Architecture diagram (C4 context + container view)
- Data model (entity relationship diagram)
- Component decisions (technology choices + justification)
- Risk & mitigation plan

**Audience:**
- Technical architecture review board
- Provincial health IT directors
- Security/privacy officers

**Questions to Address:**
- How do we handle schema differences across provinces?
- What's the backup/disaster recovery strategy?
- How do we audit data access?
- What's the data retention policy?
```

---

## Customization Checklist

### Define the Task
- [ ] Specific action verb ("write", "design", "analyze", "compare")
- [ ] Clear scope (not too broad, not too narrow)
- [ ] Success criteria are measurable

### Provide Context
- [ ] What led to this task?
- [ ] What decisions are pending?
- [ ] What's the political/business context?

### Share Key Information
- [ ] Facts needed to complete task
- [ ] Constraints (budget, timeline, scope)
- [ ] Known limitations of data

### Specify Requirements
- [ ] What must be included
- [ ] What should NOT be included
- [ ] Any non-negotiables

### Set Success Criteria
- [ ] How will you know it's good?
- [ ] Quality metrics (accuracy, completeness, clarity)
- [ ] Customer satisfaction

### Specify Format
- [ ] Length (pages, word count)
- [ ] Structure (headings, sections)
- [ ] Output format (memo, slide, code, diagram)

### Identify Audience
- [ ] Who will read/use this?
- [ ] What's their background?
- [ ] What do they care about?
- [ ] How will they use it?

### Provide Examples
- [ ] Good example of similar work
- [ ] Example output structure
- [ ] Tone/style model

---

## Testing Your Task Prompt

### Clarity Test
- Could someone complete this task from your prompt alone?
- Are all undefined terms explained?
- Is the scope clear?

### Specificity Test
- Would two people produce the same output?
- Are success criteria measurable?
- Does format specification match requirements?

### Completeness Test
- Is all needed context provided?
- Are assumptions stated?
- Is the audience clear?

---

## Combining System + Task Prompts

System Prompt → Task Prompt = Complete Instructions

**Example:**

System Prompt (Policy Analyst role, guidelines, standards)
+
Task Prompt (Analyze AI governance framework, Cabinet audience, specific requirements)
=
Complete instructions for AI-powered policy analysis

---

## Version Control

Save task prompts with version:

```
# Task Prompt: Policy Analysis
**Version**: 1.0 | **Date**: 2026-05-22 | **For**: AI Governance Framework

I need you to write a policy analysis...
```

Update version when:
- v1.1: Clarifications to requirements or format
- v2.0: Major changes to scope or success criteria

---

## Common Patterns

### For Analytical Tasks
```
I need you to analyze [topic].

Context: [situation]
Requirements: Evidence-based, multiple perspectives, clear trade-offs
Format: [structure]
Success: Stakeholders understand options and trade-offs
```

### For Generative Tasks
```
I need you to create [deliverable].

Context: [purpose, audience, constraints]
Requirements: [specific elements to include]
Format: [length, structure]
Success: [how you'll know it's good]
Examples: [reference materials]
```

### For Advisory Tasks
```
I need you to recommend [action/decision].

Context: [situation, stakeholders]
Requirements: Actionable, evidence-based, considers constraints
Success: [stakeholder satisfaction, decision quality]
Risks: [what could go wrong]
```

---

## Related Resources

- System Prompt Template: `system-prompt-template.md`
- Prompt Versioning: `prompts/SKILL.md`
- Workflow: `prompts/SKILL.md` (Workflow section)

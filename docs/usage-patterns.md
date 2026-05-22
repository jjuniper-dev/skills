# Usage Patterns & Workflows

Common workflows for using skills in various contexts.

## Presentation Deck Skill

### Workflow: Executive Strategy Briefing

**When**: Making a strategic recommendation to C-suite or board

**Process**:
1. Start with `executive-strategy-briefing.md` template
2. Develop narrative: situation → challenge → recommendation → investment → risks → next steps
3. Use speaker notes to develop talking points
4. Create 1 visual per slide (chart, diagram, or image)
5. Time for 15-minute delivery (1 min per slide)
6. Get peer review before presenting

**Output**: PPTX with speaker notes

**Tools**: PowerPoint, Google Slides, or python `slide-generator.py`

### Workflow: Board-Level Update

**When**: Quarterly or annual business update to board

**Process**:
1. Use `executive-strategy-briefing` template as base
2. Focus on: performance, key decisions, risks, forward outlook
3. Include financial summaries and metrics
4. 12-18 slides typical
5. Prepare for Q&A (detailed backup slides)

**Tips**:
- Keep main story to 8-10 slides
- Use backup slides (started with divider) for detailed Q&A
- Bold visuals for engagement
- Time for 15-20 min + 10 min Q&A

### Workflow: Stakeholder Alignment

**When**: Aligning multiple teams on direction/change

**Process**:
1. Customize `executive-strategy-briefing` template
2. Start with "why" (situation that affects everyone)
3. Show "what" (recommended approach)
4. Show "how" (implementation, timeline, roles)
5. Address concerns/risks directly
6. Clear call to action

**Tips**:
- Multiple small sessions better than one large
- Get feedback in advance from key stakeholders
- Allow time for discussion
- Send slides afterward with detailed notes

## Architecture Diagram Skill

### Workflow: Design Review Diagram

**When**: Presenting new architecture to technical team

**Process**:
1. Start with natural language description or existing architecture doc
2. Create system context diagram (high-level, all systems)
3. Create container diagram (major components)
4. Create component diagram (internal structure, if needed)
5. Use `architecture-diagram` examples as templates
6. Validate: no orphans, clear flows, consistent naming
7. Export to Mermaid/SVG for embedding in docs

**Output**: Mermaid diagram code + visual export (SVG/PNG)

**Tools**: Draw.io, Mermaid, PlantUML, or custom with Mermaid CLI

### Workflow: Documentation Diagram

**When**: Including architecture in technical documentation

**Process**:
1. Use `cloud-deployment-topology.md` example as reference
2. Describe architecture in natural language first
3. Create Mermaid diagram
4. Include diagram in README/docs alongside description
5. Keep diagram source in version control
6. Update diagram whenever architecture changes

**Tips**:
- Keep diagrams simple (< 15 major elements)
- Use consistent shapes and colors
- Group by concern (network, compute, data)
- Add legend explaining notation

### Workflow: Multi-Region/High-Availability Diagram

**When**: Showing resilience and failover architecture

**Process**:
1. Use `cloud-deployment-topology.md` as starting template
2. Show primary and secondary regions clearly
3. Highlight replication/sync relationships (dotted lines)
4. Include monitoring and alerting layer
5. Add RTO/RPO annotations
6. Make failover path obvious

**Output**: Diagram with resilience strategy explained

## Neo4j Graph Builder Skill

### Workflow: Organizational Structure Graph

**When**: Building knowledge graph of org structure

**Process**:
1. Document org structure in natural language
2. Identify node types: Person, Team, Role, Organization
3. Identify relationships: REPORTS_TO, MEMBER_OF, LEADS, HAS_SKILL
4. Use `org-hierarchy-graph.md` example as template
5. Create Cypher DDL (CREATE INDEX, CREATE CONSTRAINT)
6. Populate with sample data
7. Create common queries: hierarchy, teams, skills, dependencies
8. Set up periodic snapshots for auditing

**Output**: Cypher DDL + sample data + query library

**Tools**: Neo4j Browser, python `graph-query-builder.py`

### Workflow: Service Dependency Graph

**When**: Mapping service architecture and dependencies

**Process**:
1. List all services and their tech stack
2. Identify service-to-service dependencies
3. Identify service ownership (team)
4. Use Cypher to model: (Service)-[:DEPENDS_ON]->(Service)
5. Query for circular dependencies
6. Query for cross-team dependencies
7. Use for impact analysis (change propagation)

**Output**: Graph schema + dependency queries + impact analysis script

### Workflow: Knowledge Graph for Search/Discovery

**When**: Building searchable knowledge base

**Process**:
1. Identify entity types: Person, Document, Topic, Project, Skill
2. Define relationships: CREATED, REFERENCES, HAS_SKILL, WORKS_ON
3. Populate graph from various data sources
4. Create queries for common searches
5. Expose via API or search interface
6. Maintain data quality through regular validation

**Output**: Graph model + search queries + API

## Social Feed & News Integration Skill

### Workflow: Brand Sentiment Dashboard

**When**: Real-time monitoring of brand mentions

**Process**:
1. Define sources: Twitter/X, LinkedIn, Reddit, news APIs
2. Define keywords: brand name, competitors, key topics
3. Set up aggregation service (batch or streaming)
4. Configure sentiment analysis (Google NLP or similar)
5. Define alert rules and thresholds
6. Create dashboard: sentiment trends, top posts, volume
7. Set up Slack alerts for anomalies
8. Track metrics daily

**Output**: Real-time dashboard + alert rules + Slack integration

**Tools**: `brand-sentiment-monitoring.md` example, Slack, data viz tool

### Workflow: Crisis Detection

**When**: Monitoring for crisis signals (outages, security issues, PR problems)

**Process**:
1. Define crisis keywords: "outage", "down", "security", "data breach"
2. Monitor volume and sentiment spikes
3. Set high-sensitivity thresholds (crisis = immediate alert)
4. Route critical alerts to crisis team channel
5. Create tickets automatically for critical events
6. Log for post-incident review

**Output**: Crisis alert pipeline + incident tickets

### Workflow: Competitive Intelligence

**When**: Tracking competitor announcements and sentiment

**Process**:
1. Define competitor keywords and social accounts
2. Monitor news and social mentions
3. Categorize by announcement type: product, hiring, partnerships
4. Track sentiment toward competitors
5. Create weekly summary report
6. Share insights with product and strategy teams

**Output**: Weekly reports + aggregated feeds + trend analysis

## Google Cloud Translate Skill

### Workflow: Multi-Language Documentation

**When**: Translating product docs into multiple languages

**Process**:
1. Prepare English documentation (source)
2. Create glossaries: brand terms, technical terms
3. Configure Google Cloud Translate (advanced model)
4. Batch translate documentation
5. Validate translations (confidence > 0.85)
6. Flag low-confidence segments for review
7. Have native speakers review flagged segments
8. Publish translated docs

**Output**: Multi-language documentation set

**Tools**: `multi-language-product-docs.md` example, GCP Translate API, python script

### Workflow: Real-Time Chat Translation

**When**: Supporting multi-language customer support chat

**Process**:
1. Detect language of incoming message
2. If not English, translate to English for processing
3. Respond in English
4. Translate response back to customer's language
5. Cache translations for repeated phrases
6. Monitor translation quality

**Output**: Translated chat messages + quality metrics

### Workflow: Accessibility Translations

**When**: Creating accessibility features (captions, alt text, etc.)

**Process**:
1. Auto-generate English captions/alt text from video/image
2. Translate to multiple languages
3. Create subtitle files for each language
4. Validate accessibility (readability, sync)
5. Publish with language picker

**Output**: Multi-language captions and alt text

## Briefing Note Skill

### Workflow: Policy Decision Brief

**When**: Requesting leadership decision on policy/strategy

**Process**:
1. Define the issue clearly (1-2 sentences)
2. Write background (what got us here, current state)
3. List considerations (pros/cons of options)
4. Identify risks and mitigations
5. Write clear recommendation
6. Use `policy-decision-brief.md` template
7. Keep to 1-2 pages
8. Get peer review before sharing

**Output**: 1-2 page briefing note

### Workflow: Risk/Opportunity Assessment

**When**: Escalating risk or opportunity for decision

**Process**:
1. Issue: What is the risk or opportunity?
2. Background: How did we get here? Why now?
3. Considerations: Impact, likelihood, precedent
4. Risks: If we act (or don't act)
5. Recommendation: What should leadership decide?

**Output**: Concise brief for leadership review

### Workflow: Executive Summary

**When**: Summarizing a complex topic for executives

**Process**:
1. Don't just copy the long document
2. Synthesize into 1-2 key points
3. Use briefing note format
4. Include data that supports recommendation
5. Be specific about next steps and timeline

## Multi-Skill Workflows

### Workflow: End-to-End Strategic Initiative

**When**: Launching a significant strategic initiative (e.g., digital transformation)

**Steps**:

1. **Architecture Diagram** (internal)
   - Create current-state and target-state diagrams
   - Identify components, systems, data flows
   - Validate with technical team

2. **Neo4j Graph**
   - Model service/team dependencies
   - Identify cross-team impacts
   - Plan implementation sequence

3. **Briefing Note** (for leadership approval)
   - Issue: What are we doing and why?
   - Background: Market context, competitive pressure
   - Considerations: Risks, investment, timeline
   - Recommendation: Approve project with $X investment

4. **Presentation Deck** (board/stakeholder presentation)
   - Use briefing note as input
   - Expand to 12-15 slides
   - Add visuals: architecture diagram, timeline, investment breakdown
   - Include risk matrix and success metrics

5. **Social Feed Integration** (post-launch comms)
   - Monitor brand sentiment around announcement
   - Track customer and market reaction
   - Alert on issues or opportunities

6. **GCTranslate** (global comms)
   - Translate marketing material into key languages
   - Localize messaging for different regions

**Timeline**: 2-3 weeks from brief to board presentation

### Workflow: Crisis Response

**When**: Responding to operational crisis (outage, security, data issue)

**Steps**:

1. **Social Feed Integration** (immediate)
   - Monitor spike in mentions
   - Detect sentiment about issue
   - Identify key narratives
   - Send alert to crisis team via Slack

2. **Briefing Note** (for escalation)
   - Issue: What happened?
   - Background: Why?
   - Considerations: Customer impact, media coverage
   - Recommendation: Action to take (comms, remediation, etc.)

3. **Presentation Deck** (post-mortem or status update)
   - What happened
   - Root cause
   - Actions taken
   - Prevention measures

4. **GCTranslate** (global communication)
   - Translate crisis statement into customer languages
   - Ensure consistent messaging globally

**Timeline**: Minutes to hours depending on severity

## Best Practices

1. **Start with the briefing note**: Clarifies thinking before diving into deck or diagram
2. **Create diagrams early**: Helps align on what you're talking about
3. **Build examples first**: Templates are guides, examples show what good looks like
4. **Review with diverse audience**: Technical person reviews diagram, comms person reviews deck
5. **Version everything**: Diffs show what changed and why
6. **Keep it simple**: Fewer elements done well beats overcomplicated
7. **Update regularly**: Keep examples and templates current
8. **Document decisions**: Note why choices were made for future reference

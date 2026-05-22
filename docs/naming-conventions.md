# Naming Conventions

This document establishes consistent naming standards across the skills library.

## Skill Names

### Format
- Title Case: `Presentation Deck`, `Neo4j Graph Builder`
- Describe the capability, not the tool
- Keep concise (2-3 words maximum)

### Examples
✅ **Good**
- Presentation Deck
- Architecture Diagram
- Neo4j Graph Builder
- Social Feed & News Integration
- Google Cloud Translate Integration

❌ **Avoid**
- PPTX Generator (tool-specific)
- Slide Creator (too vague)
- Neo4j (just the tool name)
- Feed (too generic)

## Directory Names

### Format
- Kebab-case: `presentation-deck`, `neo4j-graph-builder`
- Match skill name (converted to kebab-case)
- All lowercase

### Structure
```
skills/
├── skill-name/
│   ├── SKILL.md                    # Main definition
│   ├── templates/                  # Reusable templates
│   ├── examples/                   # Real-world examples
│   ├── integration-patterns/       # Code samples
│   ├── schemas/                    # Data schemas
│   ├── validators/                 # QA scripts
│   └── docs/                       # Additional docs
```

## File Naming

### Template Files
- Pattern: `{use-case}-{template-type}.md`
- Examples:
  - `executive-strategy-briefing.md`
  - `policy-decision-brief.md`
  - `incident-response-alert.md`

### Example Files
- Pattern: `{domain/use-case}-{example-name}.md`
- Examples:
  - `microservices-system-context.md`
  - `cloud-deployment-topology.md`
  - `org-hierarchy-graph.md`
  - `brand-sentiment-monitoring.md`
  - `multi-language-product-docs.md`

### Code Samples
- Pattern: `{tool/service}-{function-name}.{ext}`
- Examples:
  - `slack-alert-handler.py`
  - `graph-query-builder.py`
  - `slide-generator.py`
  - `api-client.js`

### Schema Files
- Pattern: `{entity-name}.schema.json` or `.yml`
- Examples:
  - `org-hierarchy.schema.json`
  - `sentiment-alert.schema.json`
  - `slide-deck.schema.json`

### Validator Scripts
- Pattern: `validate-{aspect}.py` or `.js`
- Examples:
  - `validate-presentation-accessibility.py`
  - `validate-diagram-readability.py`
  - `validate-json-schema.py`

## Document Naming

### README Files
- `README.md`: Repository or section overview
- `SKILL.md`: Skill definition (required, always at root of skill dir)

### Documentation Files
- `{topic}.md` in `docs/` folder
- Examples:
  - `governance.md`
  - `naming-conventions.md`
  - `usage-patterns.md`
  - `hc-template-guide.md`

## Configuration Naming

### YAML/JSON Config Files
- Pattern: `{tool/service}-{purpose}.{yml|json}`
- Examples:
  - `slack-config.yml`
  - `gcp-translate-config.json`
  - `neo4j-connection.yml`

### Environment Variables
- UPPERCASE_SNAKE_CASE
- Prefix with component name
- Examples:
  - `SLACK_BOT_TOKEN`
  - `GCP_PROJECT_ID`
  - `NEO4J_DRIVER_URL`
  - `PRESENTATION_TEMPLATE_PATH`

## Code/Class Naming

### Python
- Classes: `PascalCase` (e.g., `SlackAlertHandler`, `GraphQueryBuilder`)
- Functions: `snake_case` (e.g., `send_sentiment_alert`, `get_organizational_hierarchy`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`, `DEFAULT_TIMEOUT`)

### JavaScript/TypeScript
- Classes: `PascalCase` (e.g., `SlackAlertHandler`)
- Functions: `camelCase` (e.g., `sendSentimentAlert`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`)
- Interfaces: `PascalCase` with `I` prefix (optional): `IAlertConfig`

## Data Field Naming

### JSON/API Fields
- camelCase: `firstName`, `isActive`, `sentimentScore`
- Avoid dashes or spaces
- Be descriptive: `user_id` not `uid`

### Database Naming
- Table names: `snake_case` (e.g., `sentiment_alerts`, `graph_nodes`)
- Column names: `snake_case` (e.g., `user_id`, `created_at`)
- Relationships: `descriptive_verb` (e.g., `REPORTS_TO`, `DEPENDS_ON`)

### CSV Headers
- Space-separated or snake_case: `First Name` or `first_name`
- Consistent with domain conventions

## Glossary/Terminology Naming

### Terms
- Use consistent capitalization
- Examples:
  - "Executive briefing" (not "executive brief" or "exec brief")
  - "Sentiment score" (not "sentiment value" or "score")
  - "Service dependency" (not "dependency" or "relation")

### Acronyms
- Define on first use: "Architecture Review Board (ARB)"
- Use consistently thereafter
- Preferred: spell out over acronyms when possible

## Version Naming

### Semantic Versioning
- Format: `MAJOR.MINOR.PATCH`
- Examples: `1.0.0`, `1.2.0`, `2.0.0`
- Record in skill header: `**Version**: 1.2.0`

### Release Tags
- Format: `v{major}.{minor}.{patch}`
- Example: `v1.2.0`
- Create tag on main branch after merge

## Example Consistency

When creating examples, use consistent naming:

### Organization/Company Names
- Use fictional: `MyCompany`, `TechCorp`, `DataFlow`
- Avoid real company names (unless public case study)

### Person Names
- Use diverse, realistic names
- Pattern: `{FirstName} {LastName}`
- Examples: `Alice Chen`, `Bob Kumar`, `Carol Martinez`, `Diana Park`

### Email Addresses
- Pattern: `{first}@company.com` or `{first}.{last}@company.com`
- Example: `alice@company.com` or `alice.chen@company.com`

### URLs
- Pattern: `https://{service}.example.com` or `https://{service}.example.{domain}`
- Example: `https://dashboard.example.com`, `https://api.example.io`

### Dates
- Format: ISO 8601 (`YYYY-MM-DD`)
- Example: `2026-05-22`

### Time
- Format: ISO 8601 with UTC (`YYYY-MM-DDTHH:MM:SSZ`)
- Example: `2026-05-22T14:30:00Z`

## Label & Tag Naming

### GitHub Labels
- Format: `{type}-{subject}` (lowercase, hyphens)
- Examples:
  - `skill-request`: New skill proposal
  - `skill-improvement`: Enhancement to existing skill
  - `skill-bug`: Bug in skill definition
  - `template-feedback`: Feedback on templates
  - `documentation`: Documentation updates

### File Tags/Categories
- Prefix: `@{skill-name}`
- Example: `@presentation-deck`, `@architecture-diagram`

## Checklist for Naming

When creating new skill content, verify:

- [ ] Skill name is descriptive, not tool-specific
- [ ] Directory name matches skill name (kebab-case)
- [ ] File names follow pattern and are lowercase
- [ ] Code uses appropriate language conventions
- [ ] Example data uses fictional, realistic names
- [ ] Dates are ISO 8601 format
- [ ] URLs are example.com domain
- [ ] Version numbers follow semantic versioning
- [ ] Terminology is consistent with this guide

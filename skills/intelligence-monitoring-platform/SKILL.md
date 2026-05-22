# Skill: Intelligence Monitoring Platform

## Purpose
Build an enterprise intelligence pipeline that ingests feeds from 10 strategic sources, scores relevance to organizational priorities (AI governance, enterprise strategy, community/policy signals), and routes curated intelligence to decision-makers via daily briefings, alerts, and structured archives.

## When to use
- Daily executive intelligence briefings (AI/governance/policy trends)
- Real-time threat/opportunity detection (regulatory, competitive, technology shifts)
- Evidence gathering for strategic planning and policy research
- Compliance monitoring (data protection, AI regulation, sector-specific rules)
- Automated research feeds for analysts and program managers
- Crisis detection and early warning triggers
- Multi-stakeholder knowledge synthesis (bilingual, cross-department)

## Inputs
- 10 feed categories (newsletters, APIs, RSS, social platforms, regulatory sources, geopolitical monitors)
- Organizational context (HC/PHAC priorities, threat models, policy windows)
- Scoring weights (strategic relevance, novelty, organizational alignment, PCA impact)
- Routing rules (who gets what via Obsidian, Airtable, Teams, audio briefing, email digest)
- User feedback (relevance ratings for continuous calibration)

## Outputs
- Daily executive briefing (top 3-5 intelligence items + context)
- Scored feed items (relevance 0-100, with reasoning)
- Structured archives (Obsidian vault, Airtable base, searchable index)
- Real-time alerts (policy threats, regulatory changes, technology breakthroughs)
- Audio briefings (narrated summaries for leaders on the move)
- Bilingual summaries (EN/FR with GCTranslate integration)
- Feed health dashboard (coverage gaps, source quality, staleness metrics)

## Constraints
- Respect source ToS, copyright, and rate limits
- Validate information quality (avoid misinformation, verify sources)
- Preserve attribution and links
- Handle duplicates and near-duplicates across sources
- Support bilingual workflows (EN/FR)
- Archive completeness for audit and compliance
- Low false-positive alert rates (high precision)
- User-configurable scoring and routing

## Workflow
1. **Ingest** - Pull from 10 feed categories every 4-6 hours
2. **Dedupe** - Hash-based deduplication within 48-hour window
3. **Score** - Calculate relevance (AI governance, enterprise strategy, policy/community signals, PCA impact)
4. **Route** - Distribute to Obsidian, Airtable, Teams, audio, email based on score and category
5. **Summarize** - Generate 1-2 sentence summaries for daily brief
6. **Archive** - Store in Obsidian/Airtable with full metadata
7. **Alert** - Trigger real-time notifications on high-signal events
8. **Refresh** - Daily digest generation at 6:00 AM (before leadership standup)
9. **Bilingual** - Translate key items via GCTranslate for EN/FR audiences
10. **Feedback** - Track user engagement to improve scoring

## Feed Taxonomy (10 tiers)

### Tier 1: AI & Governance Intelligence (Daily refresh)
- **OpenAI Blog & Releases** - Product launches, policy positions, safety research
- **DeepSeek Research** - Chinese AI capability signals, geopolitical implications
- **Anthropic Research Papers** - Claude model updates, safety/alignment research
- **Hugging Face Hub** - Open model releases, dataset trends, MCP server patterns
- **Stanford HAI & MIT-IBM** - Academic research, policy frameworks
- **AI Policy Tracker** (https://theaiindependent.org, Center for AI Policy) - Regulatory tracking (US, EU, CA)

**Purpose**: Monitor AI capability frontier, policy risks, and organizational technology roadmap alignment.

### Tier 2: Canadian Governance & Policy (Daily refresh)
- **GovInfo RSS** (https://www.gcpedia.gc.ca) - Health Canada announcements, PHAC updates
- **House of Commons Bills** (Bill C-X tracking: AI, data protection, cybersecurity)
- **Senate Committee Hearings** (e.g., AGOAF on AI governance)
- **Ministerial Mandate Letters** - Deputy Minister priorities (from Treasury Board)
- **Treasury Board Circular Updates** - Policy direction, procurement, digital standards

**Purpose**: Track regulatory landscape, HC/PHAC policy windows, and government AI strategy.

### Tier 3: Health & Public Health Policy (3x weekly)
- **PHAC Epidemiology Reports** - Disease surveillance, health emergencies
- **WHO Health Alerts** - Global health threats, emerging diseases
- **Health Affairs & JAMA** - Academic health policy and implementation science
- **Canadian Medical Association Journal** - Healthcare policy, physician perspectives
- **Provincial Health Ministry Bulletins** - Provincial policy alignment

**Purpose**: Detect health system shocks, policy opportunities, and operational risks.

### Tier 4: Enterprise Architecture & Cloud Strategy (2x weekly)
- **Gartner Hype Cycle Reports** - Technology maturity cycles
- **AWS / Azure / GCP Blog** - Cloud capability releases relevant to government
- **NIST Cybersecurity Framework Updates** - Security and AI standards
- **Cloud Security Alliance Reports** - Enterprise risks
- **IDC Market Intelligence** - Digital transformation trends

**Purpose**: Inform HC/PHAC platform roadmap and procurement decisions.

### Tier 5: Geopolitical & Risk Intelligence (3x weekly)
- **Foreign Affairs Canada Travel Advisories** - Real-time threat assessment
- **Stratfor & Council on Foreign Relations** - Geopolitical risk analysis
- **Reuters World Desk** - Breaking international news
- **The Diplomat & Asia-Pacific Security** - Regional tension monitoring
- **NATO Strategic Communications** - Collective security signals

**Purpose**: Early warning on geopolitical shocks affecting health/emergency response.

### Tier 6: Social Signals & Community Intelligence (Daily refresh)
- **Reddit (r/Health, r/Canada, r/AskCanada)** - Public sentiment, grassroots policy feedback
- **Bluesky/X Policy & Health Communities** - Thought leader discussion, advocacy signals
- **Twitter/X Search (health + policy hashtags)** - Breaking news amplification
- **LinkedIn Public Posts** (health tech leaders, policy makers) - Industry perspective
- **Community Health Worker Networks** (Slack/Discord monitoring) - Frontline signals

**Purpose**: Detect public sentiment, advocacy pressure, and community-level risk signals.

### Tier 7: Long-Form & Investigative (Weekly digest)
- **The Intercept / ProPublica** - Investigative reporting (government accountability)
- **Inside Higher Ed** - Academic and research policy trends
- **MuckRack / Journalism Research Feeds** - Fact-checking and investigative journalism
- **Medium (policy + tech)** - Long-form analysis from practitioners
- **Substack (health + AI policy)** - Specialist newsletters (e.g., Zvi Mowshowitz, Helen Toner)

**Purpose**: Deep contextual analysis for strategic planning and policy development.

### Tier 8: API-Driven Intelligence (Continuous)
- **NewsAPI** (filtered by: health, AI, Canada, policy) - Aggregated news API
- **EventRegistry API** - Event detection and clustering
- **Semantic Scholar API** - Academic paper discovery (AI + health policy)
- **Twitter v2 Academic API** - Real-time policy discussion tracking
- **GitHub Trending** - Open-source AI/security projects

**Purpose**: Structured, machine-readable intelligence for automated analysis.

### Tier 9: Regulatory Filings & Official Records (Weekly)
- **SEC EDGAR** (relevant companies: tech, healthcare, AI vendors)
- **Privacy Commissioner of Canada Reports** - Data protection enforcement
- **PIPEDA Complaint Database** - Privacy breach trends
- **BC FIPPA / Ontario FOI** - Provincial data governance
- **Hansard (Parliament records)** - MP questions, legislative history

**Purpose**: Compliance and risk monitoring via official records.

### Tier 10: GCTranslate-Integrated Bilingual Feeds (Daily, EN/FR)
- **Substack FR (santé + politique)** - French-language health/policy analysis
- **Medias Sociaux FR (health + tech)** - French social sentiment
- **Radio Canada / TVA News** - Canadian French-language breaking news
- **Senat du Canada (sessions)** - French parliamentary records
- **European AI Act Monitoring (FR resources)** - Regulatory trends in francophone jurisdictions

**Purpose**: Bilingual coverage for HC/PHAC's bilingual leadership and public-facing needs.

## Scoring Model

### Relevance Score (0-100)
- **AI Governance Alignment (0-25)**: Does this relate to AI regulation, responsible AI, enterprise AI strategy? (e.g., "Health Canada proposes AI liability framework" = 25)
- **Enterprise Strategy (0-25)**: Impact on HC/PHAC platform roadmap, capability building, digital transformation? (e.g., "AWS releases new health compliance module" = 20)
- **Policy/Community Signal (0-25)**: Policy window opening, public pressure, stakeholder advocacy? (e.g., "Senate committee hearing on health data" = 22)
- **PCA Impact (0-25)**: Direct relevance to Privacy Commissioner Act enforcement, data governance, PIPEDA? (e.g., "New privacy-tech standard released" = 20)

**Relevance Threshold**: 50+ = Route to daily briefing; 30-49 = Archive only; <30 = Discard (unless alert triggered)

### Novelty Score (0-100)
- **First mention**: 100 (new story, policy, or research)
- **Follow-up within 24h**: 50 (adds context, different angle)
- **Repeat/echo**: 10 (same story from multiple sources)
- **Duplicate content**: 0 (exact duplicate, discard)

### Quality Score (0-100)
- **Source credibility**: Reuters/AP = 90; industry blog = 40; social media unverified = 10
- **Editorial process**: Peer-reviewed journal = 100; news outlet = 80; personal blog = 30
- **Fact-check status**: Verified = 100; disputed = 30; unverified = 60
- **Completeness**: Full article with sources = 100; headline only = 40

**Combined Score** = (0.4 × Relevance) + (0.3 × Novelty) + (0.3 × Quality)

## Routing Rules

| Score Range | Action | Destination | Frequency |
|-------------|--------|-------------|-----------|
| 85-100 | Alert + Brief | Teams + Email + Obsidian | Real-time |
| 70-84 | Daily Brief | Daily digest + Airtable | 6 AM briefing |
| 50-69 | Archive | Obsidian vault + search index | No active notification |
| <50 | Discard | Deleted, searchable archive only | On-demand |

## Data Model

```json
{
  "id": "intel-2026-05-22-001",
  "timestamp": "2026-05-22T14:30:00Z",
  "source": {
    "feed": "AI Policy Tracker",
    "tier": 1,
    "url": "https://theaiindependent.org/news/123",
    "name": "Center for AI Policy"
  },
  "content": {
    "title": "Health Canada proposes AI liability framework",
    "summary": "HC's new framework establishes liability for high-risk AI in healthcare.",
    "body": "Full article text...",
    "language": "en",
    "published_date": "2026-05-22",
    "updated_date": "2026-05-22T14:30:00Z"
  },
  "metadata": {
    "relevance_score": 92,
    "relevance_breakdown": {
      "ai_governance": 25,
      "enterprise_strategy": 15,
      "policy_community": 20,
      "pca_impact": 18
    },
    "novelty_score": 100,
    "quality_score": 95,
    "combined_score": 94,
    "entities": ["Health Canada", "AI liability", "healthcare"],
    "keywords": ["AI governance", "regulation", "healthcare"],
    "bilingual": {
      "title_fr": "Santé Canada propose un cadre de responsabilité en IA",
      "summary_fr": "Le cadre de SC établit la responsabilité...",
      "language_detected": "en"
    },
    "routing": {
      "alert": true,
      "daily_brief": true,
      "obsidian": true,
      "airtable": true,
      "teams": true,
      "email": true
    }
  },
  "processing": {
    "duplicate_count": 0,
    "duplicate_of": null,
    "ingested_at": "2026-05-22T14:35:00Z",
    "scored_at": "2026-05-22T14:36:00Z",
    "routed_at": "2026-05-22T14:37:00Z"
  }
}
```

## Quality Checks

- ✅ All sources are active and producing content
- ✅ No duplicates across the 10 tiers (hash deduplication within 48h)
- ✅ Score calibration validated against user feedback monthly
- ✅ Tier distribution balanced (no single tier dominates daily brief)
- ✅ Bilingual coverage verified for FR feeds
- ✅ Alert accuracy tracked (precision >90%, recall >70%)
- ✅ Archive completeness audited weekly
- ✅ Feed health metrics (uptime, freshness, coverage) monitored

## Integration Examples

1. **Daily Executive Briefing** - Top 3-5 items scored >70, formatted for 6 AM read
2. **Real-Time Crisis Alert** - Policy threat (e.g., "Health data breach in provincial system") triggers instant Teams alert
3. **Research Evidence Base** - Analyst queries Obsidian vault for AI governance precedents
4. **Compliance Dashboard** - Privacy officer monitors PIPEDA violations via Airtable automated summary
5. **Bilingual Brief** - HC leadership receives EN/FR briefing via email + Obsidian
6. **Policy Development** - Geopolitical intelligence feeds into HC strategic planning cycle

## Output Formats

- **JSON** - Full scored feed items for integration/processing
- **Daily Digest Markdown** - Executive summary (Teams/Email)
- **Airtable Base** - Queryable intelligence archive
- **Obsidian Vault** - Linked, searchable knowledge base
- **Teams Message** - Real-time alerts with context
- **Audio Briefing** - MP3 narration for car commute (bilingual)
- **CSV Export** - Analysis/research exports

## Related Skills
- **n8n Intelligence Automation** - Workflow orchestration, scoring logic, routing
- **HC/PHAC Intelligence Stack** - Reference implementation, daily briefing example
- **Briefing Note** - Executive summary generation from intelligence
- **GCTranslate Integration** - Bilingual content workflow

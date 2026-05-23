# Skill: HC/PHAC Intelligence Stack — Daily Briefing Reference Implementation

## Purpose
End-to-end reference implementation of the Intelligence Monitoring Platform + n8n Automation for HC/PHAC leadership. This example demonstrates:
- Daily AI/governance intelligence briefing (6:00 AM for 7:30 AM standup)
- Real-time crisis alerts (policy threats, health emergencies)
- Bilingual coverage (EN/FR for HC/PHAC's bilingual leadership)
- Integration with Obsidian knowledge vault, Airtable archive, and Teams channels

## When to use
- Deploying intelligence pipeline for HC/PHAC (or similar government organization)
- Creating daily executive briefing workflows
- Setting up real-time alert monitoring
- Establishing bilingual intelligence infrastructure
- Integrating with Teams/Outlook/SharePoint ecosystem

## Inputs
- **Feed sources**: All 10 tiers from Intelligence Monitoring Platform
- **Scoring weights**: HC/PHAC-specific (AI governance regulation, enterprise health platform, policy/community, PIPEDA/PCA)
- **Leadership context**: Policy windows, strategic priorities, threat models
- **Obsidian vault path**: `/users/hc-phac/library/Intelligence/`
- **Airtable base**: HC/PHAC Intelligence Archive
- **Teams channels**: `#intelligence-briefing`, `#intelligence-alerts`
- **Email**: `intelligence-briefing@hc-sc.gc.ca`, `leadership-intelligence@hc-sc.gc.ca`

## Outputs
- **6:00 AM Brief**: Top 3-5 intelligence items (AI policy, enterprise strategy, health system risk)
- **Real-time Alerts**: High-priority items (score >85, e.g., "PHAC announces new AI governance")
- **Obsidian vault**: Daily notes linked by topic
- **Airtable archive**: Searchable, queryable intelligence base
- **Bilingual coverage**: EN/FR summaries via GCTranslate
- **Weekly digest**: 7-day summary of key intelligence (optional)

## Configuration for HC/PHAC

### Feed Tier Customization

#### Tier 1: AI & Governance (HC-specific)
- **Health Canada AI Policy Tracker** - HC announcements, AI strategy updates
- **PHAC Digital Transformation** - Public health emergency preparedness, digital resilience
- **Treasury Board Digital Strategy** - Government AI/tech procurement, cloud strategy
- **Senate Committee on Social Affairs** - Health policy hearings, AI in healthcare
- **Anthropic/Claude releases** - Enterprise AI capability signals (HC evaluating Claude API)

#### Tier 2: Canadian Governance (PHAC-specific)
- **GovInfo - Health Canada** - HC policy announcements
- **House of Commons Health Committee** - Health legislation (Bill C-X on health data)
- **Provincial Health Ministers** - Healthcare system signals, pandemic preparedness
- **Ministerial Mandate Letters** - Deputy Minister priorities
- **Public Health Agency Notices** - PHAC emergency alerts, disease surveillance

#### Tier 3: Health & Public Health
- **PHAC Epidemiology Reports** - Disease surveillance, health emergencies
- **WHO Health Alerts** - Emerging diseases, pandemic signals
- **Canadian Medical Association Journal** - Healthcare policy, implementation science
- **Health Affairs & JAMA** - Evidence-based policy research
- **Provincial Ministry of Health News** - Provincial health system news

**Scoring Weights for HC/PHAC:**
- **AI Governance**: 30% (regulatory landscape, HC AI strategy alignment)
- **Enterprise Strategy**: 25% (HC/PHAC platform roadmap, digital modernization)
- **Policy/Community**: 20% (legislative change, public pressure, advocacy)
- **PCA/PIPEDA**: 25% (privacy, health data protection, compliance)

### Example Scoring Calculation

**Article**: "Health Canada proposes new AI liability framework for high-risk medical devices"

```
Relevance Breakdown:
- AI Governance: 30 (direct impact on HC regulation)
- Enterprise Strategy: 15 (affects HC procurement of AI tools)
- Policy/Community: 20 (legislative development phase)
- PCA/PIPEDA: 20 (health data liability implications)
- Total Relevance: 85/100

Novelty: 95 (published today)
Quality: 95 (Reuters source, regulatory authority)

Combined Score: (0.4 × 85) + (0.3 × 95) + (0.3 × 95) = 34 + 28.5 + 28.5 = 91

Routing: ALERT + DAILY_BRIEF (Team message + 6 AM briefing + Obsidian + Airtable)
```

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Feed Ingestion Layer                      │
│  (NewsAPI, RSS, APIs, Social platforms, Regulatory sources) │
└────────┬────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│                  n8n Orchestration Layer                     │
│  01-Ingest  → 02-Score  → 03-Archive  ↓ 04-Alerts ↓ 05-Brief│
│     ↓           ↓           ↓          ↓          ↓          │
│   Dedupe    Relevance    Obsidian    Teams      Email 6 AM   │
│   4-hourly   scoring      vault    real-time    briefing     │
└────────┬────────────────────────────────────────────────────┘
         │
    ┌────┴──────────────────────────────────────┐
    │                                            │
    ▼                                            ▼
┌─────────────────────┐           ┌──────────────────────┐
│  Obsidian Vault     │           │  Airtable Base       │
│  /Intelligence/     │           │  Feed Items table    │
│  └Sources/          │           │  Alerts table        │
│  └Topics/           │           │  Daily Briefing      │
│  └Archives/         │           │  Feed Health         │
└─────────────────────┘           └──────────────────────┘
    │                                    │
    └────────────────┬───────────────────┘
                     │
         ┌───────────┴──────────────┐
         │                          │
         ▼                          ▼
    ┌──────────────┐        ┌────────────────┐
    │Teams Channel │        │ Email & Audio  │
    │#intelligence │        │    Briefing    │
    │-alerts       │        │   6:00 AM      │
    │#intelligence │        │   (bilingual)  │
    │-briefing     │        └────────────────┘
    └──────────────┘
```

## Daily Workflow Timeline

```
00:00  → Workflow 01 (Ingest & Dedupe) runs
        └─ Fetches all 10 feed tiers
        └─ Deduplicates against 48h window
        └─ Triggers Score & Route

04:00  → Workflow 01 runs again

06:00  → Workflow 05 (Daily Briefing) triggers
        └─ Fetches items scored 70-84 from past 24h
        └─ Groups by category (AI, policy, health, etc.)
        └─ Generates markdown summary
        └─ Sends email to leadership-intelligence@
        └─ Posts to Teams #intelligence-briefing
        └─ Archives to Airtable

06:30  → Leadership receives briefing (before 7:30 standup)

07:00  → Workflow 06 (Feed Health) runs
        └─ Checks feed freshness
        └─ Alerts admin if feed stale >48h

[Throughout day] → Real-time alerts for score >85 items
                 └─ Teams message to #intelligence-alerts
                 └─ Email to leadership-intelligence@
                 └─ Archived to Obsidian + Airtable
```

## Obsidian Vault Structure

```
Intelligence/
├── Sources/
│   ├── 1-AI-Governance/
│   │   ├── 2026-05-22-15-30-health-canada-ai-liability.md
│   │   ├── 2026-05-21-09-15-openai-safety-report.md
│   │   └── ...
│   ├── 2-Canadian-Policy/
│   │   ├── 2026-05-22-10-00-bill-c-27-privacy.md
│   │   └── ...
│   └── 3-Health-Public/
│       └── ...
├── Topics/
│   ├── AI-Governance.md (hub linking all AI governance items)
│   ├── Health-Data-Privacy.md
│   ├── Enterprise-Platform.md
│   └── Policy-Windows.md
├── Archives/
│   ├── 2026-05-briefing.md (daily digest)
│   └── 2026-week-21.md (weekly summary)
└── README.md (guide to intelligence vault)
```

## Airtable Base Structure

### Table 1: Feed Items
- **ID** (primary)
- Title
- Summary
- Source
- Link
- Published Date
- Ingested At
- Relevance Score
- Novelty Score
- Quality Score
- Combined Score
- Routing Decision
- Obsidian Path
- Language (EN/FR)
- Status (PENDING, SCORED, ARCHIVED, DELETED)

### Table 2: Alerts
- **ID** (primary)
- Feed Item ID
- Title
- Score
- Alert Sent At
- Teams Message TS
- Email Sent At
- Status

### Table 3: Daily Briefing
- **Date** (primary)
- Item Count
- Top 3 Items
- Markdown Content
- Sent At
- Recipients
- Teams Channel Posted

### Table 4: Feed Health
- **Date** (primary)
- Total Sources Active
- Total Items (7 days)
- Avg Score
- Stale Feeds Count
- Report
- Status

## Teams & Email Configuration

### Teams Channels

**#intelligence-alerts** (for real-time alerts, score >85)
- Adaptive card format with score breakdown
- Link to article and Obsidian note
- Emoji indicators (🔴 critical, 🟡 high, 🟢 medium)

**#intelligence-briefing** (for daily 6 AM digest)
- Markdown formatted summary
- Grouped by category
- Includes link to full Obsidian notes
- Pinned at top for 24h reference

### Email Recipients

- **leadership-intelligence@hc-sc.gc.ca**: Daily briefing (6:00 AM) + Real-time alerts
- **intelligence-team@hc-sc.gc.ca**: Weekly digest + Health metrics
- **deputy-minister@hc-sc.gc.ca**: Daily briefing summary (optional VIP channel)

## Bilingual Workflow (EN/FR)

1. **Items ingested in English** (primary language)
2. **Scored and routed** (same process)
3. **Daily brief generation**:
   - English summary auto-generated
   - Top N items translated to French via GCTranslate
   - Create parallel bilingual email/Teams message
4. **Archive in Obsidian**:
   - English note with FR translation in metadata
   - Bilingual tags: `#ai-governance` and `#ia-gouvernance`

**GCTranslate Integration**:
```
Input (EN): "Health Canada proposes new AI liability framework"
Output (FR): "Santé Canada propose un nouveau cadre de responsabilité en IA"
```

## Quality Metrics & Monitoring

### Daily Checklist
- ✅ All 10 feed tiers active and producing content
- ✅ Deduplication working (no duplicate items in briefing)
- ✅ Scoring calibrated (leadership feedback on relevance)
- ✅ Alert precision >90% (few false positives)
- ✅ Daily briefing delivered by 6:00 AM
- ✅ No feed stale >48 hours

### Weekly Review
- Relevance weight calibration (based on user clicks/engagement)
- Alert true-positive rate (e.g., "How many alerts led to action?")
- Coverage gaps (any important sources being missed?)
- Bilingual quality (French translation accuracy)
- Obsidian vault cleanliness (old notes archived)

### Monthly Review
- Feed tier utilization (which tiers are most useful?)
- Score distribution (are scores well-calibrated?)
- User feedback integration
- Tool chain optimization (any bottlenecks in pipeline?)

## Deployment Checklist

- [ ] **Airtable Setup**
  - [ ] Create base "HC/PHAC Intelligence"
  - [ ] Create 4 tables (Feed Items, Alerts, Daily Briefing, Feed Health)
  - [ ] Share base with n8n service account
  - [ ] Generate API key and save to n8n credentials

- [ ] **n8n Deployment**
  - [ ] Import 6 workflows from json files
  - [ ] Configure credentials (Airtable, Teams, Email, GCTranslate, NewsAPI)
  - [ ] Update environment variables (.env or n8n Cloud)
  - [ ] Test Workflow 01 manually (ingest)
  - [ ] Verify Workflow 02 scoring logic
  - [ ] Test Workflow 04 alert delivery
  - [ ] Activate cron schedules (workflows 01, 05, 06)

- [ ] **Obsidian Setup**
  - [ ] Create vault at /Intelligence/
  - [ ] Create folder structure (Sources/, Topics/, Archives/)
  - [ ] Install Obsidian Git plugin (optional, for auto-sync)
  - [ ] Configure n8n to write to vault via HTTP API

- [ ] **Teams Setup**
  - [ ] Create channels #intelligence-briefing, #intelligence-alerts
  - [ ] Generate Incoming Webhook URLs
  - [ ] Add URLs to n8n credentials
  - [ ] Test message delivery

- [ ] **Email Setup**
  - [ ] Configure SendGrid or Outlook SMTP
  - [ ] Verify email addresses (leadership-intelligence@)
  - [ ] Test email delivery

- [ ] **GCTranslate Setup** (if bilingual)
  - [ ] Enable GCTranslate integration
  - [ ] Add API key to n8n
  - [ ] Test EN→FR translation

- [ ] **Monitoring & Alerts**
  - [ ] Set up Feed Health dashboard (Airtable views)
  - [ ] Configure admin alerts for stale feeds
  - [ ] Test alert thresholds

## Next Steps

1. **Customize feed sources** based on HC/PHAC priorities
2. **Calibrate scoring weights** with leadership feedback (1-week trial)
3. **Establish feedback loop** (weekly relevance review)
4. **Document institutional knowledge** (handoff to operations team)
5. **Monitor and iterate** (monthly optimization reviews)

## Related Skills
- **Intelligence Monitoring Platform** - Core scoring model, feed taxonomy
- **n8n Intelligence Automation** - Workflow orchestration
- **GCTranslate Integration** - Bilingual content workflow
- **Briefing Note** - Executive summary generation

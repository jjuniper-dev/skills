# Skill: n8n Intelligence Automation

## Purpose
Orchestrate the intelligence pipeline (ingest → dedupe → score → route → archive) using n8n workflows that integrate with 10 feed sources, apply scoring logic, and distribute intelligence to Obsidian, Airtable, Teams, and email.

## When to use
- Automating daily intelligence briefings (set-it-and-forget-it)
- Real-time feed ingestion from 10 strategic sources
- Deduplication and scoring at scale
- Routing scored items to multiple destinations (Obsidian, Airtable, Teams, email)
- Bilingual summarization with GCTranslate
- Crisis detection and alert triggering
- Weekly/monthly intelligence summaries
- Archive maintenance and cleanup

## Inputs
- Feed URLs (RSS, APIs, web scrape targets)
- Scoring weights (AI governance, strategy, policy, PCA impact)
- Routing thresholds (alert >85, brief >70, archive >50)
- Obsidian vault path and markdown template
- Airtable base ID, table ID, field mappings
- Teams webhook URL and channel
- Email recipient list and GCTranslate API key

## Outputs
- Scored feed items stored in Airtable
- Markdown notes in Obsidian vault (auto-linked)
- Daily briefing digest (Teams + Email)
- Real-time alerts (Teams + Email)
- Archive metadata (timestamps, dedup records)
- Bilingual summaries (EN/FR)
- Feed health metrics

## Constraints
- n8n self-hosted or cloud deployment
- Respect feed source rate limits (backoff strategy)
- Atomic deduplication (no race conditions)
- Idempotent routing (duplicate sends prevented)
- Graceful error handling (feed failures don't block pipeline)
- Audit trail for all routing decisions
- Secure credential storage (API keys, tokens)

## Workflow Architecture

```
[Feed Sources] → [HTTP Fetch] → [Parse & Normalize] → [Dedupe] → [Score] → [Route Decision] → [Multi-Destination Output]
```

### Stage 1: Ingest
- Fetch from 10 feed categories via HTTP, RSS, or API
- Parse JSON/XML responses
- Normalize to common schema (title, summary, link, date, source)

### Stage 2: Dedupe
- Hash (SHA256) of title + source URL
- Check against Airtable dedup table (48-hour window)
- If duplicate: log, increment counter, skip further routing
- If novel: continue to scoring

### Stage 3: Score
- Calculate relevance (AI governance, strategy, policy, PCA)
- Calculate novelty (0-100 based on publish date)
- Calculate quality (source credibility + editorial process)
- Combine: (0.4 × rel) + (0.3 × novelty) + (0.3 × quality)
- Store score in Airtable

### Stage 4: Route
- If score >85: Alert (Teams + Email immediate)
- If score 70-84: Daily brief queue (digest at 6 AM)
- If score 50-69: Archive only (Obsidian + Airtable)
- If score <50: Delete (or archive searchable)

### Stage 5: Archive
- Write to Obsidian vault with markdown formatting
- Create Airtable record with full metadata
- Auto-link related items by keyword/topic
- Maintain audit trail (ingested_at, scored_at, routed_at)

### Stage 6: Summarize & Deliver
- Group daily brief items by category
- Generate executive summary (3-5 sentences)
- Translate key items to French (GCTranslate)
- Send via Teams channel + Email
- Log delivery metadata

## Ready-to-Import Workflows

### Workflow 1: Ingest & Dedupe
**File**: `workflows/01-ingest-dedupe.json`
- Fetch from all 10 feed categories
- Parse RSS/JSON/XML
- Check Airtable dedup table
- Log duplicates
- Pass novel items to scoring stage

**Cron**: Every 4 hours (00:00, 04:00, 08:00, 12:00, 16:00, 20:00 UTC)

### Workflow 2: Score & Route
**File**: `workflows/02-score-route.json`
- Iterate over novel items from Ingest workflow
- Calculate relevance score (4 dimensions)
- Calculate novelty score (time-based)
- Calculate quality score (source credibility)
- Combine scores
- Decide routing (alert, brief, archive, delete)
- Update Airtable with scores

**Trigger**: Webhook from Ingest workflow (dedup pass)

### Workflow 3: Archive to Obsidian
**File**: `workflows/03-archive-obsidian.json`
- Read routed items from Airtable (score >50)
- Create markdown file in Obsidian vault
- Format: `YYYY-MM-DD-HH-mm-source-slug.md`
- Include frontmatter (title, score, source, date, tags)
- Auto-link by keyword/topic
- Commit to Git (optional: Obsidian Git plugin)

**Trigger**: Webhook from Route decision

### Workflow 4: Real-Time Alerts (Teams + Email)
**File**: `workflows/04-alerts-teams-email.json`
- Monitor items with score >85
- Format Teams message (title + context + link)
- Send to Teams channel
- Send to email alert list
- Log alert delivery
- Track user engagement (Teams reactions)

**Trigger**: Webhook from Route decision (alert threshold)

### Workflow 5: Daily Briefing Digest
**File**: `workflows/05-daily-briefing-digest.json`
- Run at 6:00 AM UTC
- Collect items from past 24h with score 70-84
- Group by category (AI, policy, health, etc.)
- Generate executive summary (LLM-powered or template)
- Translate to French (GCTranslate)
- Format as Teams message + Email
- Send to leadership distribution list

**Cron**: Daily 06:00 UTC

### Workflow 6: Feed Health & Metrics
**File**: `workflows/06-feed-health-metrics.json`
- Run daily
- Check freshness of each feed (last update <24h = ✅)
- Check item count per feed (baseline trend)
- Calculate coverage gaps
- Log to dashboard/Airtable
- Alert if feed is stale >48h

**Cron**: Daily 07:00 UTC

## Configuration Guide

### Step 1: Set Up Credentials
In n8n, create credentials for:
- **Airtable API Token** (Personal access token, base read/write)
- **Teams Webhook URL** (Incoming Webhook connector)
- **Email SMTP** (Gmail, Outlook, or SendGrid)
- **GCTranslate API Key** (Bilingual translation)
- **GitHub Token** (Optional: for Obsidian Git sync)

### Step 2: Configure Feed Sources
Edit `workflows/01-ingest-dedupe.json`:
- Update RSS feed URLs for each tier
- Add NewsAPI key and search queries
- Configure API endpoints (Twitter v2, EventRegistry, etc.)
- Set rate limits per feed (backoff strategy)

### Step 3: Configure Airtable
- Create base with tables:
  - `Feed Items` (title, summary, source, score, routing_decision, etc.)
  - `Dedup Ledger` (hash, source, first_seen, duplicate_count)
  - `Alerts` (score, alert_id, teams_message_ts, email_sent_at)
  - `Daily Briefing` (date, items, sent_to, engagement_metrics)
- Share API credentials with n8n

### Step 4: Configure Obsidian Vault
- Create local folder: `/path/to/vault/Intelligence/`
- Subdirectories: `Sources/`, `Topics/`, `Archives/`
- Update workflow with vault path
- Enable Obsidian Git plugin for auto-sync

### Step 5: Configure Teams & Email
- Create Teams channel: `#intelligence-briefing`
- Create Teams channel: `#intelligence-alerts`
- Create email list: `leadership-intelligence@hc-sc.gc.ca`
- Update workflow with channel IDs and email list

### Step 6: Test & Deploy
- Import each workflow JSON into n8n
- Trigger Ingest workflow manually (test feed parsing)
- Verify Airtable records created
- Test Alert workflow with score >85 item
- Verify Teams message and email delivery
- Activate cron schedule after validation

## Data Flow Example

```
Input: NewsAPI result for "Health Canada AI strategy"
  ↓
Parse: title, summary, source, date
  ↓
Hash: SHA256(title + source) = abc123...
  ↓
Lookup Dedup Table: NOT found (novel)
  ↓
Score:
  - Relevance: AI governance (25), strategy (15), policy (20), PCA (18) = 78
  - Novelty: Published 2h ago = 100
  - Quality: NewsAPI source = 95
  - Combined: (0.4×78) + (0.3×100) + (0.3×95) = 31.2 + 30 + 28.5 = 89.7
  ↓
Route Decision: score 89.7 > 85 → Alert
  ↓
Output:
  1. Store in Airtable (Feed Items table)
  2. Create Teams message (channel #intelligence-alerts)
  3. Send email alert (leadership-intelligence@)
  4. Create Obsidian note (Sources/newsapi/2026-05-22-health-canada-ai.md)
  5. Log routing metadata
```

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Feed parsing fails | Invalid RSS/JSON | Check feed URL, add error handling in HTTP node |
| Dedup not working | Airtable lookup timeout | Increase timeout, add retry logic |
| Scores always low | Relevance weights miscalibrated | Adjust weights based on sample feedback |
| Teams alerts spam | Threshold too low | Increase alert threshold to >85 |
| Obsidian notes not linking | Keyword mismatch | Use exact phrase matching in front matter |
| Bilingual translation slow | GCTranslate rate limit | Add queue/batch logic, translate async |

## Related Skills
- **Intelligence Monitoring Platform** - Feed taxonomy, scoring model, routing rules
- **HC/PHAC Intelligence Stack** - End-to-end reference implementation
- **GCTranslate Integration** - Bilingual workflow patterns

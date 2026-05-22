# Skill: Social Feed & News Integration

## Purpose
Aggregate, normalize, and integrate social media feeds and news sources into structured data for analysis, dashboard display, sentiment tracking, or alert triggering.

## When to use
- Real-time monitoring (brand, topics, competitors, threats)
- Competitive intelligence gathering
- Sentiment analysis and trend tracking
- Crisis detection and response
- Social proof and testimonial collection
- News and market intelligence feeds
- Executive dashboards and briefings

## Inputs
- Social platforms (Twitter/X, LinkedIn, Reddit, etc.)
- News sources (RSS, API, specific outlets)
- Search keywords, hashtags, or handle lists
- Filter criteria (date range, language, sentiment threshold)
- Optional: credential configuration for APIs

## Outputs
- Normalized feed data (JSON/structured format)
- Aggregation query logic
- Sentiment/topic classification
- Alert rules and triggers
- Dashboard-ready summary metrics
- Archive and retrieval patterns

## Constraints
- Respect API rate limits and ToS
- Preserve source attribution and links
- Handle authentication securely
- Normalize timestamps to UTC
- Handle missing or incomplete data
- Remove duplicate entries
- Filter for relevance to avoid noise

## Workflow
1. **Define sources** - Identify platforms, keywords, and feeds
2. **Configure credentials** - Secure API keys and auth tokens
3. **Normalize data** - Map different APIs to common schema
4. **Filter & enrich** - Apply relevance filters, add metadata
5. **Aggregate & dedupe** - Merge duplicates, sort by relevance
6. **Extract insights** - Sentiment, sentiment trends, top themes
7. **Store & retrieve** - Archive for analysis, expose via query interface
8. **Alert triggers** - Set rules for threshold-based notifications

## Quality checks
- All entries have proper source attribution
- Timestamps are consistent and correct
- Duplicate detection working effectively
- Sentiment/classification accuracy validated
- API connectivity tested
- Rate limits respected
- Data freshness meets SLA (real-time vs. daily batch)
- Archive completeness for audit trail

## Output formats
- JSON structured data
- CSV export for analysis
- Real-time streaming (websocket, event bus)
- Aggregation dashboard JSON
- Alert payload
- Archive query interface

## Integrations
- Slack/Teams alerts
- Dashboard ingestion (Tableau, Power BI)
- Analytics platforms (Splunk, DataDog)
- Threat detection systems
- Incident management (PagerDuty, Jira)

## Examples
- Brand sentiment tracking dashboard
- Competitive intelligence feed
- Crisis keyword monitoring
- Customer feedback aggregation
- Market trend alerts
- Threat/security news monitoring

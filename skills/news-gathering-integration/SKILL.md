# Skill: News Gathering & Integration

## Purpose
Aggregate, normalize, and integrate news from multiple sources (RSS, APIs, web) into structured data for analysis, monitoring, and decision support.

## When to use
- Competitive intelligence gathering
- Industry trend monitoring
- Threat/risk detection
- Executive briefings and market updates
- Policy research and evidence gathering
- Regulatory tracking
- Real-time alerting on topic mentions

## Inputs
- News sources (RSS feeds, news APIs, specific outlets)
- Search keywords, topics, or categories
- Filter criteria (date range, language, relevance threshold)
- Optional: source priority/credibility weights
- Optional: custom parsing rules for specific sources

## Outputs
- Normalized news items (JSON/structured format)
- Aggregated summaries (by topic, source, date)
- Metadata (source, date, sentiment, relevance score)
- Alert triggers (threshold-based)
- Archived news for historical analysis
- Trend analysis and topic clustering

## Constraints
- Respect source terms of service and robots.txt
- Preserve source attribution and links
- Handle rate limits and API quotas
- Validate news quality (avoid misinformation)
- Remove duplicates and near-duplicates
- Handle missing or incomplete metadata
- Respect embargo periods for press releases

## Workflow
1. **Configure sources** - Define feeds, APIs, keywords, filters
2. **Fetch content** - Pull from RSS, APIs, web sources
3. **Parse & normalize** - Extract title, body, date, source, author
4. **Deduplicate** - Remove duplicates within time window
5. **Enrich metadata** - Add sentiment, language, relevance score
6. **Filter & rank** - Apply relevance filters, rank by importance
7. **Aggregate** - Group by topic, time period, source
8. **Store & archive** - Persist to database, maintain history
9. **Alert** - Trigger notifications on threshold events
10. **Deliver** - Expose via dashboard, API, email digest

## Quality checks
- No duplicate articles (deduplication working)
- All articles have source attribution and link
- Dates are consistent and parseable
- Relevance scores calibrated to user feedback
- Sentiment classification validated
- Language detection accurate
- Feed connectivity and freshness verified
- Alert accuracy (no false positives)
- Archive completeness for audit trail

## Output formats
- JSON (structured article objects)
- CSV (spreadsheet export for analysis)
- RSS (repurposing aggregated feed)
- Dashboard JSON (summary metrics + top articles)
- Email digest (markdown or HTML)
- Alert payloads (webhook, Slack, email)

## Integration examples
- News APIs: NewsAPI, Guardian, NYTimes, Financial Times
- RSS feeds: Industry publications, blogs, regulatory bodies
- Web scraping: Press release pages, regulatory notices
- Real-time platforms: Twitter/X, LinkedIn, Reddit (via APIs)
- Analytics: Trend analysis, sentiment tracking, topic modeling

## Data model
```json
{
  "id": "news-2026-05-22-001",
  "timestamp": "2026-05-22T14:30:00Z",
  "source": {
    "name": "Reuters",
    "type": "news_api",
    "url": "https://reuters.com/article/123"
  },
  "content": {
    "title": "Health Canada announces new AI strategy",
    "summary": "HC/PHAC launching enterprise AI platform...",
    "body": "Full article text...",
    "language": "en",
    "published_date": "2026-05-22",
    "last_updated": "2026-05-22T14:30:00Z"
  },
  "metadata": {
    "sentiment": "positive",
    "sentiment_confidence": 0.87,
    "relevance_score": 0.92,
    "keywords": ["health canada", "AI", "public health"],
    "category": "health",
    "duplicate_count": 2
  },
  "extraction": {
    "entities": [
      {"type": "ORG", "value": "Health Canada"},
      {"type": "PRODUCT", "value": "AI platform"}
    ],
    "topics": ["artificial intelligence", "government", "health"]
  }
}
```

## Examples
- Executive news brief (health sector)
- Competitor monitoring dashboard
- Regulatory compliance tracking
- Real-time threat detection
- Industry trend analysis
- Policy development research

## Related skills
- **Social Feed & News Integration** - Real-time social media + news combined
- **Briefing Note** - Summarize top news into executive brief
- **Presentation Deck** - Create dashboard/report from news analysis

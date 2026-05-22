# Example: Health News Monitoring Dashboard

## Scenario

A government health organization needs to monitor global health news to detect emerging health threats, track regulatory updates, and identify policy-relevant trends.

## Configuration

### Data Sources

```yaml
rss_feeds:
  - BBC Health & Science
  - Reuters Health
  - WHO Alerts
  - Health Canada News

news_apis:
  - NewsAPI (health category)
  - Guardian API (science section)

web_sources:
  - Health Canada press releases
  - WHO situation reports
```

### Filtering Rules

```yaml
include_keywords:
  - "pandemic"
  - "epidemic"
  - "outbreak"
  - "vaccine"
  - "drug approval"
  - "health regulation"

exclude_keywords:
  - "sports medicine"
  - "celebrity health"
  - "alternative medicine"

regions:
  - "Canada"
  - "North America"
  - "Global threats"
```

## Data Model

### Individual Article

```json
{
  "id": "health-2026-05-22-001",
  "timestamp": "2026-05-22T14:30:00Z",
  "source": {
    "name": "Reuters Health",
    "type": "news_api",
    "credibility_score": 0.95,
    "url": "https://reuters.com/health/health-canada-approves..."
  },
  "content": {
    "title": "Health Canada Approves New Treatment for Pandemic Variant",
    "summary": "Regulatory approval granted for antiviral treatment showing 80% efficacy in trials",
    "body": "Full article text...",
    "language": "en",
    "published_date": "2026-05-22",
    "last_updated": "2026-05-22T14:30:00Z",
    "image_url": "https://example.com/image.jpg"
  },
  "metadata": {
    "sentiment": 0.72,
    "sentiment_label": "positive",
    "relevance_score": 0.94,
    "keywords": ["health canada", "antiviral", "approval", "pandemic"],
    "category": "regulatory",
    "entities": [
      { "type": "ORG", "value": "Health Canada" },
      { "type": "ORG", "value": "WHO" },
      { "type": "PRODUCT", "value": "antiviral treatment" }
    ],
    "topics": ["public health", "regulation", "treatment"]
  },
  "alert_flags": {
    "is_crisis_alert": false,
    "is_new_threat": false,
    "high_engagement": true,
    "regulatory_relevance": "high"
  }
}
```

### Daily Digest Output

```json
{
  "date": "2026-05-22",
  "summary": {
    "total_articles": 47,
    "sources": 8,
    "languages": ["en", "fr"],
    "sentiment_distribution": {
      "positive": 0.53,
      "neutral": 0.35,
      "negative": 0.12
    }
  },
  "trending_topics": [
    {
      "topic": "pandemic variant surveillance",
      "mentions": 12,
      "trend": "increasing",
      "articles": ["health-2026-05-22-001", "health-2026-05-22-003"]
    },
    {
      "topic": "vaccine effectiveness",
      "mentions": 8,
      "trend": "stable",
      "articles": ["health-2026-05-22-002"]
    },
    {
      "topic": "health equity",
      "mentions": 5,
      "trend": "increasing",
      "articles": ["health-2026-05-22-004"]
    }
  ],
  "high_priority_articles": [
    {
      "rank": 1,
      "title": "Health Canada Approves New Treatment",
      "source": "Reuters Health",
      "relevance": 0.94,
      "sentiment": "positive",
      "summary": "Regulatory approval granted for antiviral treatment..."
    },
    {
      "rank": 2,
      "title": "WHO Updates Pandemic Response Guidelines",
      "source": "WHO Alerts",
      "relevance": 0.89,
      "sentiment": "neutral",
      "summary": "New interim recommendations for member states..."
    }
  ],
  "crisis_alerts": [],
  "regulatory_updates": [
    {
      "type": "approval",
      "jurisdiction": "Canada",
      "description": "Health Canada approves antiviral for pandemic variant",
      "impact": "high"
    }
  ]
}
```

## Dashboard Metrics

### Real-Time Display

```
┌─────────────────────────────────────────────────────────┐
│ HEALTH NEWS MONITORING DASHBOARD                         │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Last Updated: 2026-05-22 14:30 UTC                    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐  │
│  │ TODAY'S ARTICLES                                 │  │
│  │ ─────────────────────────────────────────────── │  │
│  │ Total: 47                                        │  │
│  │ High relevance (>0.8): 12                       │  │
│  │ New sources: 2                                  │  │
│  │ Positive sentiment: 53%                         │  │
│  └─────────────────────────────────────────────────┘  │
│                                                          │
│  ┌─────────────────────────────────────────────────┐  │
│  │ TRENDING TOPICS (Last 7 days)                   │  │
│  │ ─────────────────────────────────────────────── │  │
│  │ 🔴 Pandemic variant surveillance ↑↑ (12 mentions) │
│  │ 🟡 Vaccine effectiveness → (8 mentions)        │  │
│  │ 🟢 Health equity ↑ (5 mentions)                │  │
│  └─────────────────────────────────────────────────┘  │
│                                                          │
│  ┌─────────────────────────────────────────────────┐  │
│  │ CRISIS ALERTS                                    │  │
│  │ ─────────────────────────────────────────────── │  │
│  │ None                                             │  │
│  └─────────────────────────────────────────────────┘  │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

## Alert Rules

### Crisis Detection

```python
# Trigger when mentions spike >5x normal
normal_volume = 4  # articles/day on "pandemic"
spike_threshold = normal_volume * 5  # 20 articles

if articles_last_hour > spike_threshold:
    send_alert(
        severity="critical",
        type="crisis_detection",
        message="Unusual spike in pandemic-related news"
    )
```

### Regulatory Alerts

```python
# Alert on regulatory news from key sources
regulatory_keywords = ["approval", "regulation", "ban", "policy"]

if article.category == "regulatory" and article.relevance > 0.85:
    send_alert(
        severity="high",
        type="regulatory_update",
        message=f"New regulatory development: {article.title}",
        recipients=["policy-team@organization.ca"]
    )
```

### Sentiment Shift

```python
# Track sentiment changes on key topics
yesterday_sentiment = 0.65  # positive
today_sentiment = 0.35      # neutral

if abs(yesterday_sentiment - today_sentiment) > 0.3:
    send_alert(
        severity="medium",
        type="sentiment_shift",
        message="Significant sentiment change on health equity topic"
    )
```

## Integration: Email Digest

### HTML Template

```html
<html>
<head>
  <title>Health News Digest - 2026-05-22</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6;">

<h1 style="color: #003D68;">Health News Digest</h1>
<p>Daily summary: <strong>May 22, 2026</strong></p>

<hr style="border: 1px solid #ddd;">

<h2 style="color: #1a7c3f;">Top Stories</h2>

<div style="background: #f5f5f5; padding: 15px; margin: 10px 0; border-left: 4px solid #003D68;">
  <h3 style="margin-top: 0;">Health Canada Approves New Treatment</h3>
  <p><strong>Source:</strong> Reuters Health | <strong>Relevance:</strong> 94%</p>
  <p>Regulatory approval granted for antiviral treatment showing 80% efficacy in trials for pandemic variant...</p>
  <p><a href="https://reuters.com/health/..." style="color: #003D68;">Read full article →</a></p>
</div>

<div style="background: #f5f5f5; padding: 15px; margin: 10px 0; border-left: 4px solid #1a7c3f;">
  <h3 style="margin-top: 0;">WHO Updates Pandemic Response</h3>
  <p><strong>Source:</strong> WHO Alerts | <strong>Relevance:</strong> 89%</p>
  <p>New interim recommendations for member states addressing pandemic variant management...</p>
  <p><a href="https://who.int/..." style="color: #003D68;">Read full article →</a></p>
</div>

<hr style="border: 1px solid #ddd;">

<h2 style="color: #1a7c3f;">Trending Topics</h2>
<ul>
  <li><strong>Pandemic variant surveillance</strong> (12 mentions, ↑ trending up)</li>
  <li><strong>Vaccine effectiveness</strong> (8 mentions, → stable)</li>
  <li><strong>Health equity</strong> (5 mentions, ↑ trending up)</li>
</ul>

<hr style="border: 1px solid #ddd;">

<p style="color: #666; font-size: 12px;">
  This digest was generated automatically by the Health News Monitoring system.
  <a href="https://dashboard.organization.ca/news">View full dashboard →</a>
</p>

</body>
</html>
```

## Performance Metrics

### Processing

```
Pipeline Performance (2026-05-22)
─────────────────────────────────
Fetch time:        2.3s  (47 articles from 8 sources)
Parse time:        0.8s  (extract, normalize metadata)
Deduplication:     0.4s  (47 → 44 unique articles)
Enrichment time:   1.2s  (sentiment, entities, keywords)
Summarization:     3.1s  (BART model inference)
Alert evaluation:  0.2s  (check rules)
Total:             8.0s

Throughput:        5.9 articles/second
───────────────────────────────────
```

### Quality Metrics

```
Quality Report (May 22, 2026)
──────────────────────────────
Deduplication effectiveness:  93.6% (removed 3 near-duplicates)
Source credibility (avg):     0.89/1.0
Sentiment accuracy (sample):  87% (compared to manual review)
Entity extraction recall:     0.91 (91% of entities found)
Alert false positive rate:    2% (1 out of 50 alerts was duplicate)
Customer satisfaction:        4.2/5.0 (from feedback survey)
──────────────────────────────
```

## Monitoring & Governance

### SLA Target

- **Response time**: News alerts within 15 minutes of publication
- **Accuracy**: ≥90% relevance for high-priority alerts
- **Availability**: 99.5% uptime
- **Freshness**: Update every 15 minutes (incremental), hourly full refresh

### Audit Trail

```json
{
  "article_id": "health-2026-05-22-001",
  "processing_log": {
    "fetched_at": "2026-05-22T14:25:00Z",
    "source": "reuters_health_api",
    "deduplicated": false,
    "enrichment": {
      "sentiment_model": "distilbert-v3",
      "entities_extracted": 3,
      "keywords_extracted": 5
    },
    "alerts_triggered": ["regulatory_update"],
    "delivered_to": ["policy-team@organization.ca"],
    "delivered_at": "2026-05-22T14:27:15Z"
  }
}
```

## Related Skills

- **Social Feed & News Integration**: Real-time social media + news combined
- **Briefing Note**: Summarize top news into executive brief
- **Presentation Deck**: Create dashboard/report from news analysis

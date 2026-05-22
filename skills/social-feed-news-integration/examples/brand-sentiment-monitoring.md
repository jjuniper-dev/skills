# Example: Brand Sentiment Monitoring Dashboard

## Context
Real-time monitoring of brand mentions across Twitter/X, LinkedIn, Reddit, and news outlets with sentiment analysis and alert triggers.

## Configuration

```yaml
sources:
  - platform: twitter
    keywords: ["@mycompany", "#mycompany", "mycompany"]
    filters:
      languages: [en, fr]
      min_followers: 100
      exclude_retweets: false
    credentials: twitter_api_v2
    
  - platform: reddit
    subreddits: ["r/tech", "r/startups", "r/myindustry"]
    keywords: ["mycompany"]
    filters:
      min_score: 1
    
  - platform: news
    sources: ["techcrunch.com", "forbes.com", "bloomberg.com"]
    keywords: ["mycompany"]
    filters:
      date_range: last_7_days
    api: newsapi
    
  - platform: linkedin
    search_terms: ["mycompany", "company_name"]
    filters:
      post_types: [company_updates, news, articles]

aggregation:
  dedup_window: 3600  # seconds
  group_by: [source, keyword, author]
  sort_by: relevance
  
sentiment_analysis:
  model: google_natural_language
  min_confidence: 0.7
  categories: [positive, neutral, negative, ambiguous]
  
storage:
  type: postgresql
  retention: 90  # days
  archive_to_s3: true
  
cache:
  type: redis
  ttl: 3600
```

## Data Model (JSON)

```json
{
  "feed_entry": {
    "id": "entry-20260522-001",
    "timestamp": "2026-05-22T14:30:00Z",
    "source": {
      "platform": "twitter",
      "account": "@techcrunch",
      "url": "https://twitter.com/techcrunch/status/123456789"
    },
    "content": {
      "text": "MyCompany just launched their new AI platform. Impressive architecture decisions.",
      "lang": "en",
      "has_media": true,
      "media_type": ["image"]
    },
    "author": {
      "id": "user-techcrunch",
      "name": "TechCrunch",
      "followers": 5000000,
      "verified": true,
      "influence_score": 0.95
    },
    "engagement": {
      "likes": 2500,
      "retweets": 1200,
      "replies": 340,
      "views": 50000
    },
    "sentiment": {
      "label": "positive",
      "confidence": 0.92,
      "score": 0.85,
      "entities": [
        {
          "text": "MyCompany",
          "type": "ORG",
          "sentiment": "positive",
          "confidence": 0.96
        },
        {
          "text": "AI platform",
          "type": "PRODUCT",
          "sentiment": "positive",
          "confidence": 0.88
        }
      ]
    },
    "keywords_matched": ["mycompany", "AI", "platform"],
    "duplicate_of": null,
    "archived": false,
    "metadata": {
      "processing_time_ms": 245,
      "duplicate_count": 0,
      "is_reply": false,
      "is_quote": false
    }
  }
}
```

## Alert Rules

```yaml
alerts:
  - id: alert-001
    name: "Negative mention spike"
    description: "Alert when negative sentiment mentions exceed threshold"
    trigger:
      metric: sentiment_count
      dimension: sentiment
      value: negative
      window: 3600  # 1 hour
      threshold: 10
      operator: gte
    actions:
      - slack_channel: "#crisis-response"
        message: "🚨 Negative sentiment spike detected"
      - pagerduty_severity: warning
      - create_ticket:
          system: jira
          project: CX
          issue_type: Incident
    
  - id: alert-002
    name: "High-influence negative post"
    description: "Alert on negative posts from influencers"
    trigger:
      metric: influence_score
      condition:
        - sentiment: negative
        - influence_score: gte 0.8
      threshold: 1
    actions:
      - slack_channel: "#comms-team"
        message: "⚠️ High-influence account posted negative mention"
      - pagerduty_severity: critical
    
  - id: alert-003
    name: "Trending topic"
    description: "Alert when a keyword trends"
    trigger:
      metric: mention_volume
      window: 1800  # 30 min
      trend_change: 300  # % increase
    actions:
      - slack_channel: "#marketing"
        message: "📈 Trending topic detected"
      - dashboard_pin: true

  - id: alert-004
    name: "Product mention with low sentiment"
    description: "Alert on new product mentions with neutral/negative sentiment"
    trigger:
      metric: product_sentiment
      products: ["new-ai-platform"]
      sentiment_threshold: 0.5
      operator: lt
      window: 1800
    actions:
      - slack_channel: "#product"
        message: "⚠️ Low sentiment mention of AI Platform"
```

## Dashboard Metrics (Real-time)

```json
{
  "dashboard": {
    "timestamp": "2026-05-22T15:00:00Z",
    "period": "last_24_hours",
    "summary": {
      "total_mentions": 4527,
      "unique_sources": 1823,
      "reach": 125000000,
      "avg_sentiment_score": 0.71,
      "sentiment_distribution": {
        "positive": 0.62,
        "neutral": 0.28,
        "negative": 0.10
      }
    },
    "trends": {
      "volume_trend": {
        "direction": "up",
        "change_pct": 15.3,
        "change_direction": "📈"
      },
      "sentiment_trend": {
        "direction": "stable",
        "change_pct": 2.1,
        "change_direction": "➡️"
      }
    },
    "top_keywords": [
      {"keyword": "mycompany", "mentions": 2841, "sentiment": 0.74},
      {"keyword": "ai-platform", "mentions": 1203, "sentiment": 0.81},
      {"keyword": "announcement", "mentions": 945, "sentiment": 0.68}
    ],
    "top_sources": [
      {"source": "twitter", "mentions": 2100, "reach": 45000000},
      {"source": "reddit", "mentions": 1200, "reach": 3000000},
      {"source": "news", "mentions": 800, "reach": 50000000}
    ],
    "top_posts": [
      {
        "text": "MyCompany launches AI platform...",
        "platform": "twitter",
        "engagement": 9523,
        "sentiment": 0.92,
        "influence_score": 0.87
      }
    ],
    "alerts_triggered": 3,
    "active_issues": 1
  }
}
```

## Integration Points

### Slack Integration
```json
{
  "type": "slack_alert",
  "channel": "#comms-team",
  "message": {
    "blocks": [
      {
        "type": "section",
        "text": {
          "type": "mrkdwn",
          "text": "🚨 *Negative sentiment spike detected*\n10+ negative mentions in the last hour"
        }
      },
      {
        "type": "section",
        "fields": [
          {"type": "mrkdwn", "text": "*Volume*\n10 mentions"},
          {"type": "mrkdwn", "text": "*Avg Sentiment*\n-0.72"},
          {"type": "mrkdwn", "text": "*Reach*\n125K"},
          {"type": "mrkdwn", "text": "*Status*\n⚠️ Active"}
        ]
      },
      {
        "type": "actions",
        "elements": [
          {"type": "button", "text": "View Dashboard", "url": "https://dashboard.example.com"},
          {"type": "button", "text": "Create Ticket", "action_id": "create_ticket"}
        ]
      }
    ]
  }
}
```

### Dashboard Export (CSV)
```csv
timestamp,platform,author,engagement_score,sentiment,reach,text
2026-05-22T14:30:00Z,twitter,@techcrunch,4040,positive,5000000,"MyCompany just launched..."
2026-05-22T14:35:00Z,linkedin,@johnsmith,245,neutral,50000,"Check out MyCompany's new..."
2026-05-22T14:40:00Z,reddit,r/tech,156,positive,2000,"MyCompany's architecture is..."
```

## Maintenance & Operations

- **Update frequency**: Real-time (streaming) or 5-minute batches
- **Retry logic**: Exponential backoff for API failures
- **Deduplication**: Hash-based (text + source + author) with 1-hour window
- **Archive**: 90-day hot storage (postgres), then S3 cold storage
- **SLA**: 99.5% uptime, <5 minute latency from post to alert

## Quality Checks
- ✅ No duplicate entries across sources
- ✅ Sentiment confidence above threshold
- ✅ All entries have source attribution
- ✅ Timestamps normalized to UTC
- ✅ Reach calculations verified
- ✅ Alert thresholds tested

"""
News Aggregation Engine
Fetch, normalize, and aggregate news from multiple sources
"""

from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
from enum import Enum
import json
import logging
import hashlib

logger = logging.getLogger(__name__)


class Sentiment(Enum):
    """Sentiment levels"""
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"


@dataclass
class NewsSource:
    """News source metadata"""
    name: str
    url: str
    source_type: str  # "rss", "api", "web"
    category: str
    language: str
    priority: int = 1
    credibility_score: float = 0.5

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class NewsArticle:
    """Normalized news article"""
    id: str
    title: str
    url: str
    published_date: datetime
    source: NewsSource

    # Content
    summary: str
    body: Optional[str] = None
    image_url: Optional[str] = None

    # Metadata
    language: str = "en"
    last_updated: datetime = None
    sentiment: float = 0.0  # -1.0 to 1.0
    sentiment_label: str = "neutral"
    relevance_score: float = 0.5  # 0.0 to 1.0
    keywords: List[str] = None
    entities: List[Dict[str, str]] = None

    def __post_init__(self):
        if self.last_updated is None:
            self.last_updated = datetime.utcnow()
        if self.keywords is None:
            self.keywords = []
        if self.entities is None:
            self.entities = []

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data['source'] = self.source.to_dict()
        data['published_date'] = self.published_date.isoformat()
        data['last_updated'] = self.last_updated.isoformat()
        data['sentiment_label'] = self.sentiment_label
        return data

    def get_hash(self) -> str:
        """Generate hash for deduplication"""
        text = f"{self.title}:{self.source.name}".lower()
        return hashlib.sha256(text.encode()).hexdigest()


@dataclass
class NewsDigest:
    """Aggregated news digest"""
    date: datetime
    total_articles: int
    sources_count: int
    trending_topics: List[Dict[str, Any]]
    high_priority_articles: List[NewsArticle]
    crisis_alerts: List[Dict[str, Any]] = None
    sentiment_distribution: Dict[str, float] = None

    def __post_init__(self):
        if self.crisis_alerts is None:
            self.crisis_alerts = []
        if self.sentiment_distribution is None:
            self.sentiment_distribution = {
                'positive': 0.0,
                'neutral': 0.0,
                'negative': 0.0
            }

    def to_dict(self) -> Dict[str, Any]:
        return {
            'date': self.date.isoformat(),
            'total_articles': self.total_articles,
            'sources_count': self.sources_count,
            'trending_topics': self.trending_topics,
            'high_priority_articles': [a.to_dict() for a in self.high_priority_articles],
            'crisis_alerts': self.crisis_alerts,
            'sentiment_distribution': self.sentiment_distribution
        }


class NewsAggregator:
    """Aggregate and normalize news"""

    def __init__(self):
        self.articles: List[NewsArticle] = []
        self.dedup_window = timedelta(days=7)
        self.processed_hashes = set()

    def add_article(self, article: NewsArticle) -> bool:
        """Add article if not duplicate"""
        article_hash = article.get_hash()

        if article_hash in self.processed_hashes:
            logger.debug(f"Duplicate article: {article.title}")
            return False

        self.processed_hashes.add(article_hash)
        self.articles.append(article)
        return True

    def add_articles(self, articles: List[NewsArticle]) -> int:
        """Add multiple articles, return count added"""
        count = 0
        for article in articles:
            if self.add_article(article):
                count += 1
        return count

    def filter_by_relevance(self, threshold: float = 0.5) -> List[NewsArticle]:
        """Filter articles above relevance threshold"""
        return [a for a in self.articles if a.relevance_score >= threshold]

    def filter_by_sentiment(self, min_score: float, max_score: float) -> List[NewsArticle]:
        """Filter articles by sentiment range"""
        return [a for a in self.articles
                if min_score <= a.sentiment <= max_score]

    def filter_by_date(self, start_date: datetime, end_date: datetime) -> List[NewsArticle]:
        """Filter articles by date range"""
        return [a for a in self.articles
                if start_date <= a.published_date <= end_date]

    def get_trending_topics(self, top_n: int = 5) -> List[Dict[str, Any]]:
        """Extract trending topics from keywords"""
        topic_counts: Dict[str, int] = {}

        for article in self.articles:
            for keyword in article.keywords:
                topic_counts[keyword] = topic_counts.get(keyword, 0) + 1

        # Sort by frequency
        sorted_topics = sorted(topic_counts.items(), key=lambda x: x[1], reverse=True)

        return [
            {'topic': topic, 'mentions': count}
            for topic, count in sorted_topics[:top_n]
        ]

    def get_sentiment_distribution(self) -> Dict[str, float]:
        """Calculate sentiment distribution"""
        if not self.articles:
            return {'positive': 0.0, 'neutral': 0.0, 'negative': 0.0}

        positive = sum(1 for a in self.articles if a.sentiment > 0.3)
        negative = sum(1 for a in self.articles if a.sentiment < -0.3)
        neutral = len(self.articles) - positive - negative

        total = len(self.articles)
        return {
            'positive': round(positive / total, 2),
            'neutral': round(neutral / total, 2),
            'negative': round(negative / total, 2)
        }

    def detect_crisis(self, spike_threshold: int = 5) -> List[Dict[str, Any]]:
        """Detect crisis conditions (unusual topic spikes)"""
        alerts = []
        topic_counts = {}

        for article in self.articles:
            for keyword in article.keywords:
                topic_counts[keyword] = topic_counts.get(keyword, 0) + 1

        # Check for spikes (simplified—real system would compare to historical baseline)
        for topic, count in topic_counts.items():
            if count >= spike_threshold:
                alerts.append({
                    'type': 'topic_spike',
                    'topic': topic,
                    'mentions': count,
                    'severity': 'high' if count >= spike_threshold * 2 else 'medium'
                })

        return alerts

    def generate_digest(self, top_articles: int = 5) -> NewsDigest:
        """Generate news digest"""
        high_priority = sorted(
            self.articles,
            key=lambda a: a.relevance_score,
            reverse=True
        )[:top_articles]

        digest = NewsDigest(
            date=datetime.utcnow(),
            total_articles=len(self.articles),
            sources_count=len(set(a.source.name for a in self.articles)),
            trending_topics=self.get_trending_topics(),
            high_priority_articles=high_priority,
            crisis_alerts=self.detect_crisis(),
            sentiment_distribution=self.get_sentiment_distribution()
        )

        return digest

    def export_json(self, output_path: str) -> str:
        """Export articles as JSON"""
        data = [a.to_dict() for a in self.articles]
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        return output_path

    def export_csv(self, output_path: str) -> str:
        """Export articles as CSV"""
        import csv

        fieldnames = [
            'published_date', 'title', 'source', 'category',
            'sentiment', 'relevance_score', 'url'
        ]

        with open(output_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for article in self.articles:
                writer.writerow({
                    'published_date': article.published_date.isoformat(),
                    'title': article.title,
                    'source': article.source.name,
                    'category': article.source.category,
                    'sentiment': round(article.sentiment, 2),
                    'relevance_score': round(article.relevance_score, 2),
                    'url': article.url
                })

        return output_path


class NewsEnricher:
    """Enrich articles with metadata"""

    @staticmethod
    def calculate_sentiment(text: str) -> float:
        """Calculate sentiment (-1.0 to 1.0)"""
        # Simplified sentiment—real implementation uses trained model
        positive_words = ['good', 'great', 'positive', 'approved', 'success']
        negative_words = ['bad', 'poor', 'negative', 'failed', 'risk']

        score = 0.0
        text_lower = text.lower()

        for word in positive_words:
            score += text_lower.count(word) * 0.2

        for word in negative_words:
            score -= text_lower.count(word) * 0.2

        return max(-1.0, min(1.0, score))

    @staticmethod
    def set_sentiment_label(sentiment_score: float) -> str:
        """Convert score to label"""
        if sentiment_score > 0.3:
            return Sentiment.POSITIVE.value
        elif sentiment_score < -0.3:
            return Sentiment.NEGATIVE.value
        else:
            return Sentiment.NEUTRAL.value

    @staticmethod
    def extract_keywords(text: str, max_keywords: int = 10) -> List[str]:
        """Extract keywords from text (simplified)"""
        # Real implementation uses NLP (YAKE, TF-IDF, etc.)
        words = text.lower().split()
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'of', 'is'}
        keywords = [w for w in words if len(w) > 3 and w not in stop_words]
        return list(set(keywords))[:max_keywords]

    @staticmethod
    def extract_entities(text: str) -> List[Dict[str, str]]:
        """Extract named entities (simplified)"""
        # Real implementation uses NER models (spaCy, BERT, etc.)
        entities = []
        org_keywords = ['health canada', 'who', 'cdc', 'department']
        person_keywords = ['dr.', 'minister']

        for keyword in org_keywords:
            if keyword.lower() in text.lower():
                entities.append({'type': 'ORG', 'value': keyword.title()})

        for keyword in person_keywords:
            if keyword.lower() in text.lower():
                entities.append({'type': 'PERSON', 'value': 'Unknown'})

        return entities


# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Create sample articles
    source = NewsSource(
        name="Reuters Health",
        url="https://reuters.com",
        source_type="api",
        category="health",
        language="en",
        credibility_score=0.95
    )

    articles = [
        NewsArticle(
            id="news-001",
            title="Health Canada Approves New Treatment",
            url="https://reuters.com/article/1",
            published_date=datetime.utcnow(),
            source=source,
            summary="New antiviral treatment approved",
            sentiment=0.8,
            sentiment_label="positive",
            relevance_score=0.94,
            keywords=["health canada", "antiviral", "approval"]
        ),
        NewsArticle(
            id="news-002",
            title="WHO Updates Pandemic Guidelines",
            url="https://who.int/article/2",
            published_date=datetime.utcnow(),
            source=source,
            summary="WHO releases updated recommendations",
            sentiment=0.2,
            sentiment_label="neutral",
            relevance_score=0.89,
            keywords=["who", "pandemic", "guidelines"]
        )
    ]

    # Aggregate
    aggregator = NewsAggregator()
    count = aggregator.add_articles(articles)
    print(f"Added {count} articles")

    # Generate digest
    digest = aggregator.generate_digest()
    print(f"\nDigest: {len(digest.high_priority_articles)} top articles")
    print(f"Trending: {digest.trending_topics}")
    print(f"Sentiment: {digest.sentiment_distribution}")

    # Export
    aggregator.export_json("/tmp/news.json")
    print("\nExported to /tmp/news.json")

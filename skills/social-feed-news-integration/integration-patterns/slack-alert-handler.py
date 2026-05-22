"""
Slack Alert Handler for Social Feed Integration
Sends real-time sentiment alerts and aggregated reports to Slack channels
"""

import json
import logging
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logger = logging.getLogger(__name__)


class SlackAlertHandler:
    """Handle Slack notifications for social feed events"""

    def __init__(self, slack_token: str, default_channel: str = "#comms-team"):
        """
        Initialize Slack client

        Args:
            slack_token: Slack bot token (starts with xoxb-)
            default_channel: Default channel for alerts
        """
        self.client = WebClient(token=slack_token)
        self.default_channel = default_channel

    def send_sentiment_alert(
        self,
        sentiment: str,
        mentions_count: int,
        avg_sentiment_score: float,
        top_posts: List[Dict],
        channel: Optional[str] = None,
        severity: str = "warning"
    ) -> bool:
        """
        Send sentiment alert to Slack

        Args:
            sentiment: "positive", "negative", or "neutral"
            mentions_count: Number of mentions in window
            avg_sentiment_score: Average sentiment score (-1 to 1)
            top_posts: List of top posts with engagement
            channel: Target channel (uses default if not provided)
            severity: "info", "warning", or "critical"

        Returns:
            True if successful, False otherwise
        """
        channel = channel or self.default_channel

        # Emoji based on sentiment
        emoji_map = {
            "positive": "😊",
            "neutral": "➡️",
            "negative": "😡"
        }
        emoji = emoji_map.get(sentiment, "ℹ️")

        # Color for severity
        color_map = {
            "info": "#36a64f",
            "warning": "#ff9900",
            "critical": "#ff0000"
        }
        color = color_map.get(severity, "#808080")

        # Build blocks
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"{emoji} {sentiment.capitalize()} Sentiment Alert"
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Mentions*\n{mentions_count}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Avg Sentiment*\n{avg_sentiment_score:.2f}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Severity*\n{severity.capitalize()}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Time*\n{datetime.now().strftime('%H:%M UTC')}"
                    }
                ]
            }
        ]

        # Add top posts
        if top_posts:
            blocks.append({"type": "divider"})
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Top Posts*"
                }
            })

            for i, post in enumerate(top_posts[:3], 1):
                text = post.get("text", "")[:200]
                engagement = post.get("engagement", {})
                source = post.get("source", {})

                blocks.append({
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"{i}. {text}...\n"
                               f"_<{source.get('url', '#')}|{source.get('platform', 'unknown')}>_ "
                               f"• 👍 {engagement.get('likes', 0)} "
                               f"• 🔄 {engagement.get('retweets', 0)}"
                    }
                })

        # Add action buttons
        blocks.append({"type": "divider"})
        blocks.append({
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "View Dashboard"
                    },
                    "url": "https://dashboard.example.com/sentiment",
                    "style": "primary"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Create Ticket"
                    },
                    "action_id": "create_incident_ticket",
                    "style": "danger" if severity == "critical" else None
                }
            ]
        })

        try:
            response = self.client.chat_postMessage(
                channel=channel,
                blocks=blocks,
                text=f"{sentiment.capitalize()} sentiment alert: {mentions_count} mentions"
            )
            logger.info(f"Sent alert to {channel}: {response['ts']}")
            return True
        except SlackApiError as e:
            logger.error(f"Slack API error: {e.response['error']}")
            return False

    def send_daily_summary(
        self,
        summary_data: Dict,
        channel: Optional[str] = None
    ) -> bool:
        """
        Send daily summary report to Slack

        Args:
            summary_data: Dictionary with summary metrics
            channel: Target channel

        Returns:
            True if successful
        """
        channel = channel or self.default_channel

        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "📊 Daily Social Feed Summary"
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Total Mentions*\n{summary_data.get('total_mentions', 0):,}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Reach*\n{summary_data.get('total_reach', 0):,}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Positive Sentiment*\n{summary_data.get('positive_pct', 0):.1f}%"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Negative Sentiment*\n{summary_data.get('negative_pct', 0):.1f}%"
                    }
                ]
            }
        ]

        # Top keywords section
        top_keywords = summary_data.get('top_keywords', [])
        if top_keywords:
            blocks.append({"type": "divider"})
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Trending Keywords*"
                }
            })

            keyword_text = "\n".join([
                f"• *{kw['keyword']}* ({kw['mentions']} mentions, "
                f"sentiment: {kw['sentiment']:.2f})"
                for kw in top_keywords[:5]
            ])

            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": keyword_text
                }
            })

        try:
            self.client.chat_postMessage(
                channel=channel,
                blocks=blocks,
                text="Daily summary"
            )
            return True
        except SlackApiError as e:
            logger.error(f"Failed to send summary: {e}")
            return False

    def send_crisis_alert(
        self,
        crisis_type: str,
        description: str,
        affected_count: int,
        recommended_action: str,
        channel: Optional[str] = None
    ) -> bool:
        """
        Send critical crisis alert

        Args:
            crisis_type: Type of crisis (data_breach, security_issue, etc.)
            description: Description of the crisis
            affected_count: Number of affected mentions/users
            recommended_action: Recommended action to take
            channel: Target channel (defaults to #crisis-response)

        Returns:
            True if successful
        """
        channel = channel or "#crisis-response"

        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "🚨 CRISIS ALERT 🚨",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{crisis_type.replace('_', ' ').title()}*\n{description}"
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Affected Mentions*\n{affected_count}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Time*\n{datetime.now().strftime('%Y-%m-%d %H:%M UTC')}"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Recommended Action*\n{recommended_action}"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Activate Crisis Team"
                        },
                        "action_id": "activate_crisis_team",
                        "style": "danger"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "View Full Context"
                        },
                        "url": "https://dashboard.example.com/crisis",
                        "style": "primary"
                    }
                ]
            }
        ]

        try:
            self.client.chat_postMessage(
                channel=channel,
                blocks=blocks,
                text="CRISIS ALERT"
            )
            # Also send mention
            self.client.chat_postMessage(
                channel=channel,
                text="<!here> Crisis alert - check message above"
            )
            return True
        except SlackApiError as e:
            logger.error(f"Failed to send crisis alert: {e}")
            return False


# Example usage
if __name__ == "__main__":
    handler = SlackAlertHandler(slack_token="xoxb-your-token")

    # Send sentiment alert
    handler.send_sentiment_alert(
        sentiment="negative",
        mentions_count=15,
        avg_sentiment_score=-0.65,
        top_posts=[
            {
                "text": "Disappointed with recent MyCompany service outage...",
                "source": {"platform": "twitter", "url": "https://twitter.com/user/status/123"},
                "engagement": {"likes": 245, "retweets": 89}
            }
        ],
        severity="warning"
    )

    # Send daily summary
    handler.send_daily_summary(
        summary_data={
            "total_mentions": 4527,
            "total_reach": 125000000,
            "positive_pct": 62.0,
            "negative_pct": 10.0,
            "top_keywords": [
                {"keyword": "mycompany", "mentions": 2841, "sentiment": 0.74},
                {"keyword": "ai-platform", "mentions": 1203, "sentiment": 0.81}
            ]
        }
    )

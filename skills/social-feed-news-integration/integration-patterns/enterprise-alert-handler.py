"""
Enterprise Alert Handler for Social Feed & News Integration
Sends alerts and reports to Microsoft Teams, SharePoint, and ServiceNow
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from enum import Enum
from datetime import datetime
import requests
import logging

logger = logging.getLogger(__name__)


class AlertSeverity(Enum):
    """Alert severity levels"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass
class AlertMessage:
    """Alert message to send"""
    title: str
    description: str
    severity: AlertSeverity
    source: str
    timestamp: datetime
    data: Dict[str, Any]
    tags: List[str] = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []


class TeamsAlertHandler:
    """Send alerts to Microsoft Teams channels"""

    def __init__(self, webhook_url: str):
        """
        Initialize Teams handler

        Args:
            webhook_url: Teams incoming webhook URL
        """
        self.webhook_url = webhook_url
        self.severity_colors = {
            AlertSeverity.CRITICAL: "ff0000",  # Red
            AlertSeverity.HIGH: "ff9900",      # Orange
            AlertSeverity.MEDIUM: "ffff00",    # Yellow
            AlertSeverity.LOW: "0099cc"        # Blue
        }

    def send_alert(self, alert: AlertMessage) -> bool:
        """
        Send sentiment alert to Teams

        Args:
            alert: Alert message to send

        Returns:
            Success status
        """
        payload = {
            "@type": "MessageCard",
            "@context": "https://schema.org/extensions",
            "summary": alert.title,
            "themeColor": self.severity_colors[alert.severity],
            "sections": [
                {
                    "activityTitle": alert.title,
                    "activitySubtitle": f"[{alert.severity.value.upper()}] {alert.source}",
                    "text": alert.description,
                    "facts": [
                        {"name": "Severity", "value": alert.severity.value},
                        {"name": "Source", "value": alert.source},
                        {"name": "Time", "value": alert.timestamp.isoformat()},
                    ] + [
                        {"name": k, "value": str(v)}
                        for k, v in list(alert.data.items())[:5]  # Limit to 5 fields
                    ],
                    "markdown": True
                }
            ],
            "potentialAction": [
                {
                    "@type": "ViewAction",
                    "name": "View Details",
                    "target": [alert.data.get("url", "#")]
                }
            ]
        }

        try:
            response = requests.post(self.webhook_url, json=payload, timeout=10)
            if response.status_code == 200:
                logger.info(f"Teams alert sent: {alert.title}")
                return True
            else:
                logger.error(f"Teams API error: {response.status_code}")
                return False
        except requests.RequestException as e:
            logger.error(f"Failed to send Teams alert: {e}")
            return False

    def send_daily_summary(self, summary: Dict[str, Any], channel: str = "General") -> bool:
        """
        Send daily summary report to Teams

        Args:
            summary: Summary data with metrics
            channel: Target channel (optional)

        Returns:
            Success status
        """
        payload = {
            "@type": "MessageCard",
            "@context": "https://schema.org/extensions",
            "summary": "Daily Social & News Summary",
            "themeColor": "0078d4",
            "sections": [
                {
                    "activityTitle": "📊 Daily Social & News Summary",
                    "activitySubtitle": datetime.utcnow().strftime("%Y-%m-%d"),
                    "text": f"Summary Report - {summary.get('total_items', 0)} items processed",
                    "facts": [
                        {"name": "Total Items", "value": str(summary.get('total_items', 0))},
                        {"name": "High Priority", "value": str(summary.get('high_priority', 0))},
                        {"name": "Sentiment", "value": summary.get('sentiment', 'neutral')},
                        {"name": "Trending Topics", "value": ", ".join(summary.get('trending', [])[:3])},
                    ],
                    "markdown": True
                }
            ]
        }

        try:
            response = requests.post(self.webhook_url, json=payload, timeout=10)
            if response.status_code == 200:
                logger.info("Daily summary sent to Teams")
                return True
            else:
                logger.error(f"Teams API error: {response.status_code}")
                return False
        except requests.RequestException as e:
            logger.error(f"Failed to send Teams summary: {e}")
            return False

    def send_crisis_alert(self, crisis_data: Dict[str, Any]) -> bool:
        """
        Send critical crisis alert to Teams with elevated visibility

        Args:
            crisis_data: Crisis details

        Returns:
            Success status
        """
        payload = {
            "@type": "MessageCard",
            "@context": "https://schema.org/extensions",
            "summary": "🚨 CRISIS ALERT",
            "themeColor": "ff0000",
            "sections": [
                {
                    "activityTitle": "🚨 CRISIS DETECTED",
                    "activitySubtitle": "Immediate attention required",
                    "text": crisis_data.get("description", ""),
                    "facts": [
                        {"name": "Topic", "value": crisis_data.get("topic", "Unknown")},
                        {"name": "Severity", "value": "CRITICAL"},
                        {"name": "Mentions", "value": str(crisis_data.get("mention_count", 0))},
                        {"name": "Trend", "value": crisis_data.get("trend", "rapid increase")},
                    ]
                }
            ],
            "potentialAction": [
                {
                    "@type": "ViewAction",
                    "name": "View Crisis Dashboard",
                    "target": [crisis_data.get("dashboard_url", "#")]
                },
                {
                    "@type": "OpenUri",
                    "name": "Escalate",
                    "targets": [
                        {
                            "os": "default",
                            "uri": crisis_data.get("escalation_url", "#")
                        }
                    ]
                }
            ]
        }

        try:
            response = requests.post(self.webhook_url, json=payload, timeout=10)
            if response.status_code == 200:
                logger.critical("Crisis alert sent to Teams")
                return True
            else:
                logger.error(f"Teams API error: {response.status_code}")
                return False
        except requests.RequestException as e:
            logger.error(f"Failed to send crisis alert: {e}")
            return False


class SharePointListHandler:
    """Save alerts and reports to SharePoint lists"""

    def __init__(self, site_url: str, list_name: str, access_token: str):
        """
        Initialize SharePoint handler

        Args:
            site_url: SharePoint site URL (e.g., https://org.sharepoint.com/sites/analytics)
            list_name: Target list name
            access_token: Azure AD access token
        """
        self.site_url = site_url
        self.list_name = list_name
        self.access_token = access_token
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def save_alert(self, alert: AlertMessage) -> bool:
        """
        Save alert to SharePoint list

        Args:
            alert: Alert to save

        Returns:
            Success status
        """
        # Get list ID
        list_url = f"{self.site_url}/_api/web/lists/getByTitle('{self.list_name}')"

        # Create item
        item_data = {
            "fields": {
                "Title": alert.title,
                "Description": alert.description,
                "Severity": alert.severity.value,
                "Source": alert.source,
                "Tags": ";".join(alert.tags),
                "Timestamp": alert.timestamp.isoformat(),
                "DataJson": str(alert.data)
            }
        }

        try:
            response = requests.post(
                f"{list_url}/items",
                json=item_data,
                headers=self.headers,
                timeout=10
            )
            if response.status_code == 201:
                logger.info(f"Alert saved to SharePoint: {alert.title}")
                return True
            else:
                logger.error(f"SharePoint API error: {response.status_code}")
                return False
        except requests.RequestException as e:
            logger.error(f"Failed to save alert to SharePoint: {e}")
            return False

    def save_report(self, report: Dict[str, Any], report_type: str = "Daily Summary") -> bool:
        """
        Save report to SharePoint list

        Args:
            report: Report data
            report_type: Type of report

        Returns:
            Success status
        """
        list_url = f"{self.site_url}/_api/web/lists/getByTitle('{self.list_name}')"

        item_data = {
            "fields": {
                "Title": f"{report_type} - {datetime.utcnow().strftime('%Y-%m-%d')}",
                "Description": report.get("summary", ""),
                "Severity": "normal",
                "Source": "automated_report",
                "DataJson": str(report)
            }
        }

        try:
            response = requests.post(
                f"{list_url}/items",
                json=item_data,
                headers=self.headers,
                timeout=10
            )
            if response.status_code == 201:
                logger.info(f"Report saved to SharePoint: {report_type}")
                return True
            else:
                logger.error(f"SharePoint API error: {response.status_code}")
                return False
        except requests.RequestException as e:
            logger.error(f"Failed to save report to SharePoint: {e}")
            return False


class ServiceNowIncidentHandler:
    """Create and manage incidents in ServiceNow"""

    def __init__(self, instance_url: str, api_key: str):
        """
        Initialize ServiceNow handler

        Args:
            instance_url: ServiceNow instance URL (e.g., https://org.service-now.com)
            api_key: ServiceNow API authentication key
        """
        self.instance_url = instance_url
        self.headers = {
            "Authorization": f"Basic {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def create_incident(self, alert: AlertMessage) -> Optional[str]:
        """
        Create incident in ServiceNow from alert

        Args:
            alert: Alert message

        Returns:
            Incident number or None
        """
        # Map severity to ServiceNow urgency
        severity_map = {
            AlertSeverity.CRITICAL: "1",
            AlertSeverity.HIGH: "2",
            AlertSeverity.MEDIUM: "3",
            AlertSeverity.LOW: "4"
        }

        incident_data = {
            "short_description": alert.title,
            "description": alert.description,
            "urgency": severity_map[alert.severity],
            "impact": "2" if alert.severity in [AlertSeverity.CRITICAL, AlertSeverity.HIGH] else "3",
            "category": "Social Media" if "social" in alert.source.lower() else "News & Intelligence",
            "assigned_to": self._get_on_call_user(alert.severity),
            "assignment_group": "Communications & Intelligence",
            "correlation_id": f"{alert.source}:{alert.timestamp.isoformat()}"
        }

        try:
            response = requests.post(
                f"{self.instance_url}/api/now/v2/table/incident",
                json=incident_data,
                headers=self.headers,
                timeout=10
            )
            if response.status_code == 201:
                incident_num = response.json()["result"]["number"]
                logger.info(f"ServiceNow incident created: {incident_num}")
                return incident_num
            else:
                logger.error(f"ServiceNow API error: {response.status_code}")
                return None
        except requests.RequestException as e:
            logger.error(f"Failed to create ServiceNow incident: {e}")
            return None

    def update_incident(self, incident_id: str, status: str, notes: str) -> bool:
        """
        Update incident in ServiceNow

        Args:
            incident_id: Incident number or sys_id
            status: New status (new, in_progress, resolved, closed)
            notes: Update notes

        Returns:
            Success status
        """
        update_data = {
            "state": self._map_status(status),
            "work_notes": notes
        }

        try:
            response = requests.patch(
                f"{self.instance_url}/api/now/v2/table/incident/{incident_id}",
                json=update_data,
                headers=self.headers,
                timeout=10
            )
            if response.status_code == 200:
                logger.info(f"ServiceNow incident updated: {incident_id}")
                return True
            else:
                logger.error(f"ServiceNow API error: {response.status_code}")
                return False
        except requests.RequestException as e:
            logger.error(f"Failed to update ServiceNow incident: {e}")
            return False

    def _get_on_call_user(self, severity: AlertSeverity) -> str:
        """Get on-call user based on severity"""
        if severity == AlertSeverity.CRITICAL:
            return "manager"  # Escalate to manager
        elif severity == AlertSeverity.HIGH:
            return "lead_analyst"
        else:
            return "analyst"

    def _map_status(self, status: str) -> str:
        """Map status to ServiceNow state"""
        mapping = {
            "new": "1",
            "in_progress": "2",
            "resolved": "6",
            "closed": "7"
        }
        return mapping.get(status, "1")


# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Teams example
    teams_handler = TeamsAlertHandler(webhook_url="https://outlook.webhook.office.com/webhookb2/...")

    alert = AlertMessage(
        title="High negative sentiment spike on AI governance",
        description="Twitter mentions dropped 20% in sentiment score over 2 hours",
        severity=AlertSeverity.HIGH,
        source="twitter",
        timestamp=datetime.utcnow(),
        data={
            "mentions": 450,
            "sentiment_change": -0.20,
            "trending_keywords": ["governance", "regulation", "risk"]
        },
        tags=["AI", "governance", "sentiment"]
    )

    teams_handler.send_alert(alert)

    # ServiceNow example
    sn_handler = ServiceNowIncidentHandler(
        instance_url="https://org.service-now.com",
        api_key="base64_encoded_key"
    )

    incident_id = sn_handler.create_incident(alert)
    if incident_id:
        sn_handler.update_incident(
            incident_id,
            status="in_progress",
            notes="Alert reviewed. Monitoring social channels."
        )

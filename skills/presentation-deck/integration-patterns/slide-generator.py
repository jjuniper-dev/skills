"""
Presentation Slide Generator
Create PPTX-ready slide structures from narrative inputs
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum
import json
import logging

logger = logging.getLogger(__name__)


class SlideType(Enum):
    """Slide types in standard presentation deck"""
    COVER = "cover"
    TITLE = "title"
    CONTENT = "content"
    TWO_COL = "two_column"
    IMAGE_FULL = "image_full"
    CHART = "chart"
    QUOTE = "quote"
    CALLOUT = "callout"
    SECTION_BREAK = "section_break"
    BACKUP = "backup"


@dataclass
class Slide:
    """Representation of a single slide"""
    id: str
    type: SlideType
    title: str
    subtitle: Optional[str] = None
    content: Optional[List[str]] = None
    speaker_notes: Optional[str] = None
    visual: Optional[Dict[str, Any]] = None
    layout: str = "default"
    timing_seconds: int = 60

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON export"""
        data = asdict(self)
        data['type'] = self.type.value
        return data


@dataclass
class Presentation:
    """Representation of a complete presentation"""
    title: str
    subtitle: str
    author: str
    slides: List[Slide]
    target_duration_minutes: int = 15
    audience: str = "executive"
    theme: str = "professional"

    def add_slide(self, slide: Slide) -> None:
        """Add a slide to the presentation"""
        self.slides.append(slide)

    def get_total_duration(self) -> float:
        """Calculate total duration in minutes"""
        return sum(s.timing_seconds for s in self.slides) / 60

    def to_json(self) -> str:
        """Export as JSON"""
        data = {
            'title': self.title,
            'subtitle': self.subtitle,
            'author': self.author,
            'audience': self.audience,
            'theme': self.theme,
            'target_duration_minutes': self.target_duration_minutes,
            'actual_duration_minutes': round(self.get_total_duration(), 1),
            'slide_count': len(self.slides),
            'slides': [s.to_dict() for s in self.slides]
        }
        return json.dumps(data, indent=2, default=str)


class SlideGenerator:
    """Generate standardized slide structures"""

    # HC/PHAC Brand Colors
    HC_COLORS = {
        "primary": (0, 61, 104),        # Dark Blue
        "secondary": (237, 246, 255),  # Light Blue
        "tertiary": (229, 255, 239),   # Light Green
        "neutral": (247, 249, 251),    # Light Gray
        "border": (148, 163, 184),     # Slate
        "text_dark": (17, 24, 39),     # Dark Gray
        "text_white": (255, 255, 255), # White
    }

    @staticmethod
    def create_cover_slide(
        title: str,
        subtitle: str,
        author: str,
        date: str
    ) -> Slide:
        """Create cover slide"""
        return Slide(
            id="slide-cover",
            type=SlideType.COVER,
            title=title,
            subtitle=subtitle,
            speaker_notes=f"Welcome the audience. Introduce {author}. "
                          f"State the purpose of this presentation.",
            timing_seconds=60,
            content=[author, date]
        )

    @staticmethod
    def create_agenda_slide(
        agenda_items: List[str],
        timing: int = 60
    ) -> Slide:
        """Create agenda/outline slide"""
        return Slide(
            id="slide-agenda",
            type=SlideType.CONTENT,
            title="Agenda",
            content=agenda_items,
            speaker_notes="Walk through each agenda item. "
                         "Estimate timing for each section.",
            timing_seconds=timing
        )

    @staticmethod
    def create_situation_slide(
        headline: str,
        key_points: List[str],
        supporting_data: Optional[Dict] = None
    ) -> Slide:
        """Create situation/context slide"""
        speaker_notes = (
            f"Open with: {headline}\n"
            f"Key points:\n"
        )
        for point in key_points:
            speaker_notes += f"- {point}\n"

        return Slide(
            id="slide-situation",
            type=SlideType.CONTENT,
            title="Current Situation",
            subtitle=headline,
            content=key_points,
            speaker_notes=speaker_notes,
            timing_seconds=90,
            visual=supporting_data or {
                'type': 'chart',
                'data_series': ['Current', 'Trend'],
                'note': 'Add chart visual here'
            }
        )

    @staticmethod
    def create_options_slide(
        options: List[Dict[str, str]],
        highlight_recommended: Optional[int] = None
    ) -> Slide:
        """Create options/alternatives slide"""
        content = []
        speaker_notes = "Compare options:\n"

        for i, option in enumerate(options):
            content.append(f"Option {i+1}: {option['title']}")
            if option.get('description'):
                speaker_notes += f"\nOption {i+1}: {option['description']}\n"

        if highlight_recommended is not None:
            speaker_notes += (
                f"\nRecommended: Option {highlight_recommended + 1} because...\n"
            )

        return Slide(
            id="slide-options",
            type=SlideType.TWO_COL,
            title="Strategic Options",
            content=content,
            speaker_notes=speaker_notes,
            timing_seconds=120
        )

    @staticmethod
    def create_recommendation_slide(
        recommendation: str,
        rationale_points: List[str],
        expected_outcomes: Optional[List[str]] = None
    ) -> Slide:
        """Create recommendation slide"""
        content = [
            "Recommendation:",
            recommendation,
            "",
            "Rationale:"
        ]
        content.extend([f"• {point}" for point in rationale_points])

        speaker_notes = f"Recommend: {recommendation}\n\nRationale:\n"
        speaker_notes += "\n".join([f"- {point}" for point in rationale_points])

        if expected_outcomes:
            speaker_notes += "\n\nExpected outcomes:\n"
            speaker_notes += "\n".join(
                [f"- {outcome}" for outcome in expected_outcomes]
            )

        return Slide(
            id="slide-recommendation",
            type=SlideType.CALLOUT,
            title="Recommendation",
            content=content,
            speaker_notes=speaker_notes,
            timing_seconds=120
        )

    @staticmethod
    def create_timeline_slide(
        timeline_phases: List[Dict[str, str]]
    ) -> Slide:
        """Create project timeline/roadmap slide"""
        content = []
        speaker_notes = "Project timeline:\n"

        for phase in timeline_phases:
            content.append(f"{phase['name']}: {phase['duration']}")
            speaker_notes += f"- {phase['name']} ({phase['duration']}): "
            speaker_notes += phase.get('description', '') + "\n"

        return Slide(
            id="slide-timeline",
            type=SlideType.CHART,
            title="Implementation Timeline",
            content=content,
            speaker_notes=speaker_notes,
            timing_seconds=90,
            visual={
                'type': 'gantt_chart',
                'phases': timeline_phases
            }
        )

    @staticmethod
    def create_investment_slide(
        total_investment: str,
        cost_breakdown: Dict[str, str],
        payback_period: str = "TBD"
    ) -> Slide:
        """Create investment/financial slide"""
        content = [
            f"Total Investment: {total_investment}",
            "",
            "Cost Breakdown:"
        ]

        for category, amount in cost_breakdown.items():
            content.append(f"• {category}: {amount}")

        content.append(f"\nPayback Period: {payback_period}")

        speaker_notes = (
            f"Total investment required: {total_investment}\n\n"
            f"Cost breakdown:\n"
        )
        speaker_notes += "\n".join(
            [f"- {cat}: {amt}" for cat, amt in cost_breakdown.items()]
        )

        return Slide(
            id="slide-investment",
            type=SlideType.CHART,
            title="Investment Summary",
            content=content,
            speaker_notes=speaker_notes,
            timing_seconds=90,
            visual={
                'type': 'waterfall_chart',
                'categories': list(cost_breakdown.keys()),
                'amounts': list(cost_breakdown.values())
            }
        )

    @staticmethod
    def create_risks_slide(
        risks: List[Dict[str, str]]
    ) -> Slide:
        """Create risks and mitigations slide"""
        content = []
        speaker_notes = "Key risks and mitigations:\n"

        for risk in risks:
            content.append(f"• {risk['risk']}")
            speaker_notes += f"\nRisk: {risk['risk']}\n"
            speaker_notes += f"Mitigation: {risk['mitigation']}\n"

        return Slide(
            id="slide-risks",
            type=SlideType.CONTENT,
            title="Key Risks & Mitigations",
            content=content,
            speaker_notes=speaker_notes,
            timing_seconds=90
        )

    @staticmethod
    def create_next_steps_slide(
        decision_needed: str,
        timeline: str,
        approval_path: Optional[List[str]] = None
    ) -> Slide:
        """Create next steps / call to action slide"""
        content = [
            f"Decision: {decision_needed}",
            f"Timeline: {timeline}"
        ]

        if approval_path:
            content.append("Approval Path:")
            content.extend([f"→ {step}" for step in approval_path])

        speaker_notes = (
            f"Decision needed: {decision_needed}\n"
            f"Timeline: {timeline}\n"
        )

        if approval_path:
            speaker_notes += "Approval path:\n"
            speaker_notes += " → ".join(approval_path) + "\n"

        speaker_notes += "\nAre we ready to move forward? Questions?"

        return Slide(
            id="slide-next-steps",
            type=SlideType.CALLOUT,
            title="Next Steps",
            subtitle="Decision & Timeline",
            content=content,
            speaker_notes=speaker_notes,
            timing_seconds=120
        )


    @staticmethod
    def create_opportunity_canvas(
        title: str,
        canvas_data: Dict[str, List[str]]
    ) -> Slide:
        """
        Create Opportunity Canvas slide (Lean Canvas variant)

        Args:
            title: Slide title
            canvas_data: Dict with keys like target_users, problems, solution, etc.

        Returns:
            Slide with canvas layout
        """
        content = [
            f"**Target Users**: {', '.join(canvas_data.get('target_users', ['TBD'])[:1])}",
            f"**Problems**: {', '.join(canvas_data.get('problems', ['TBD'])[:1])}",
            f"**Solution**: {', '.join(canvas_data.get('solution', ['TBD'])[:1])}",
            f"**Value Prop**: {', '.join(canvas_data.get('value_prop', ['TBD'])[:1])}",
            f"**Success Metrics**: {', '.join(canvas_data.get('metrics', ['TBD'])[:1])}"
        ]

        speaker_notes = "Opportunity Canvas:\n\n"
        for key, values in canvas_data.items():
            speaker_notes += f"{key.replace('_', ' ').title()}:\n"
            speaker_notes += "\n".join([f"- {v}" for v in values[:3]]) + "\n\n"

        return Slide(
            id="slide-canvas",
            type=SlideType.CONTENT,
            title=title,
            subtitle="Canvas Framework",
            content=content,
            speaker_notes=speaker_notes,
            timing_seconds=120,
            layout="canvas"
        )

    @staticmethod
    def create_business_model_canvas(
        canvas_data: Dict[str, List[str]]
    ) -> Slide:
        """Create Business Model Canvas slide"""
        content = [
            f"**Partners**: {', '.join(canvas_data.get('key_partners', ['TBD'])[:1])}",
            f"**Activities**: {', '.join(canvas_data.get('key_activities', ['TBD'])[:1])}",
            f"**Value**: {', '.join(canvas_data.get('value_propositions', ['TBD'])[:1])}",
            f"**Customers**: {', '.join(canvas_data.get('customer_segments', ['TBD'])[:1])}",
            f"**Revenue**: {', '.join(canvas_data.get('revenue_streams', ['TBD'])[:1])}"
        ]

        return Slide(
            id="slide-bm-canvas",
            type=SlideType.CHART,
            title="Business Model Canvas",
            content=content,
            timing_seconds=120,
            layout="canvas"
        )


class DeckBuilder:
    """Build complete presentations from narrative"""

    def __init__(self, title: str, author: str, audience: str = "executive"):
        """Initialize presentation"""
        self.presentation = Presentation(
            title=title,
            subtitle="",
            author=author,
            audience=audience,
            slides=[]
        )

    def build_executive_briefing(
        self,
        situation: Dict[str, Any],
        options: List[Dict[str, Any]],
        recommendation: Dict[str, Any],
        investment: Dict[str, Any],
        risks: List[Dict[str, str]],
        next_steps: Dict[str, Any]
    ) -> Presentation:
        """Build complete executive briefing deck"""

        # Cover
        self.presentation.add_slide(
            SlideGenerator.create_cover_slide(
                self.presentation.title,
                situation.get('subtitle', ''),
                self.presentation.author,
                situation.get('date', '')
            )
        )

        # Agenda
        self.presentation.add_slide(
            SlideGenerator.create_agenda_slide([
                "Current Situation",
                "Strategic Options",
                "Recommendation",
                "Investment & Timeline",
                "Risks & Mitigations",
                "Next Steps"
            ])
        )

        # Situation
        self.presentation.add_slide(
            SlideGenerator.create_situation_slide(
                situation.get('headline', ''),
                situation.get('key_points', []),
                situation.get('data')
            )
        )

        # Options
        self.presentation.add_slide(
            SlideGenerator.create_options_slide(options)
        )

        # Recommendation
        self.presentation.add_slide(
            SlideGenerator.create_recommendation_slide(
                recommendation.get('recommendation', ''),
                recommendation.get('rationale', []),
                recommendation.get('outcomes')
            )
        )

        # Investment
        self.presentation.add_slide(
            SlideGenerator.create_investment_slide(
                investment.get('total', ''),
                investment.get('breakdown', {}),
                investment.get('payback_period')
            )
        )

        # Risks
        if risks:
            self.presentation.add_slide(
                SlideGenerator.create_risks_slide(risks)
            )

        # Next Steps
        self.presentation.add_slide(
            SlideGenerator.create_next_steps_slide(
                next_steps.get('decision', ''),
                next_steps.get('timeline', ''),
                next_steps.get('approval_path')
            )
        )

        return self.presentation


# Example usage
if __name__ == "__main__":
    builder = DeckBuilder(
        title="Digital Transformation Strategy",
        author="Alice Chen, CTO",
        audience="executive"
    )

    presentation = builder.build_executive_briefing(
        situation={
            'headline': 'Market is shifting. Our competitors are moving faster.',
            'subtitle': 'Strategic Initiative Briefing',
            'date': '2026-05-22',
            'key_points': [
                'Customer preference for digital-first: 68%',
                'Competitors\' digital revenue growth: +35% YoY',
                'Our digital revenue growth: +8% YoY',
                'Compliance gap: NIST framework now mandates zero-trust'
            ]
        },
        options=[
            {'title': 'Option A: Zero-Trust Full Migration', 'description': 'Complete architecture redesign...'},
            {'title': 'Option B: Enhanced VPN & MFA', 'description': 'Incremental improvements...'},
            {'title': 'Option C: Hybrid Approach', 'description': 'Phased modernization...'}
        ],
        recommendation={
            'recommendation': 'Pursue Option C: Hybrid approach with phased migration',
            'rationale': [
                'Balances risk and investment',
                'Allows parallel operations during transition',
                'Reduces disruption to users'
            ],
            'outcomes': ['25% digital revenue by 2028', 'NIST framework compliance', 'Improved NPS']
        },
        investment={
            'total': '$18M',
            'breakdown': {
                'Platform Modernization': '$9M',
                'New Product Development': '$6M',
                'Team Upskilling': '$3M'
            },
            'payback_period': '2.5 years'
        },
        risks=[
            {'risk': 'Implementation delays', 'mitigation': 'Phased rollout with experienced vendor'},
            {'risk': 'User adoption resistance', 'mitigation': 'Early communication and training'}
        ],
        next_steps={
            'decision': 'Approve $18M investment',
            'timeline': 'Board decision by June 30',
            'approval_path': ['CFO Review', 'Board Finance Committee', 'Full Board']
        }
    )

    # Export as JSON
    print(presentation.to_json())
    print(f"\nTotal slides: {len(presentation.slides)}")
    print(f"Presentation duration: {presentation.get_total_duration():.1f} minutes")

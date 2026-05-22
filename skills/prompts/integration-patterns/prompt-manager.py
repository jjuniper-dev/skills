"""
Prompt Manager
Version control, testing, and performance tracking for LLM prompts
"""

from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
from enum import Enum
import json
import logging
import hashlib

logger = logging.getLogger(__name__)


class PromptType(Enum):
    """Prompt types"""
    SYSTEM = "system"
    TASK = "task"
    FEW_SHOT = "few_shot"


class PromptStatus(Enum):
    """Prompt lifecycle status"""
    DRAFT = "draft"
    TESTING = "testing"
    PRODUCTION = "production"
    DEPRECATED = "deprecated"


@dataclass
class PromptVersion:
    """A versioned prompt"""
    name: str
    version: str  # semantic: major.minor.patch
    prompt_type: PromptType
    content: str
    status: PromptStatus
    created_at: datetime
    updated_at: datetime
    author: str

    # Metadata
    description: str = ""
    tags: List[str] = None
    related_skills: List[str] = None
    test_results: Dict[str, Any] = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.related_skills is None:
            self.related_skills = []
        if self.test_results is None:
            self.test_results = {}

    def get_hash(self) -> str:
        """Generate content hash for change detection"""
        return hashlib.sha256(self.content.encode()).hexdigest()

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data['prompt_type'] = self.prompt_type.value
        data['status'] = self.status.value
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data


@dataclass
class PromptTest:
    """Test case for a prompt"""
    name: str
    input_text: str
    expected_output_criteria: List[str]  # What good output should contain
    actual_output: Optional[str] = None
    passed: bool = False
    score: float = 0.0  # 0-1
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class PromptPerformance:
    """Performance metrics for a prompt in production"""
    prompt_version: str
    metric_date: datetime
    total_uses: int
    average_latency_ms: float
    user_satisfaction: float  # 1-5 scale
    error_rate: float  # 0-1
    output_quality_score: float  # 0-1 (manual review)

    def to_dict(self) -> Dict[str, Any]:
        return {
            'prompt_version': self.prompt_version,
            'metric_date': self.metric_date.isoformat(),
            'total_uses': self.total_uses,
            'average_latency_ms': round(self.average_latency_ms, 1),
            'user_satisfaction': round(self.user_satisfaction, 2),
            'error_rate': round(self.error_rate, 3),
            'output_quality_score': round(self.output_quality_score, 2)
        }


class PromptManager:
    """Manage prompt versions and testing"""

    def __init__(self):
        self.prompts: Dict[str, List[PromptVersion]] = {}
        self.performance_history: List[PromptPerformance] = []

    def create_prompt(
        self,
        name: str,
        version: str,
        prompt_type: PromptType,
        content: str,
        author: str,
        description: str = "",
        tags: List[str] = None
    ) -> PromptVersion:
        """Create a new prompt version"""
        prompt = PromptVersion(
            name=name,
            version=version,
            prompt_type=prompt_type,
            content=content,
            status=PromptStatus.DRAFT,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            author=author,
            description=description,
            tags=tags or []
        )

        if name not in self.prompts:
            self.prompts[name] = []

        self.prompts[name].append(prompt)
        logger.info(f"Created prompt: {name} v{version}")
        return prompt

    def get_prompt(self, name: str, version: Optional[str] = None) -> Optional[PromptVersion]:
        """Get a specific prompt version (default: latest production)"""
        if name not in self.prompts:
            return None

        versions = self.prompts[name]

        if version:
            # Get specific version
            for v in versions:
                if v.version == version:
                    return v
        else:
            # Get latest production version
            production_versions = [v for v in versions if v.status == PromptStatus.PRODUCTION]
            if production_versions:
                return sorted(production_versions, key=lambda v: v.updated_at)[-1]

        return None

    def list_versions(self, name: str) -> List[PromptVersion]:
        """List all versions of a prompt"""
        return self.prompts.get(name, [])

    def promote_to_production(self, name: str, version: str) -> bool:
        """Promote a prompt to production status"""
        prompt = self.get_prompt(name, version)
        if not prompt:
            logger.error(f"Prompt not found: {name} v{version}")
            return False

        prompt.status = PromptStatus.PRODUCTION
        prompt.updated_at = datetime.utcnow()
        logger.info(f"Promoted to production: {name} v{version}")
        return True

    def deprecate_prompt(self, name: str, version: str) -> bool:
        """Mark prompt as deprecated"""
        prompt = self.get_prompt(name, version)
        if not prompt:
            return False

        prompt.status = PromptStatus.DEPRECATED
        prompt.updated_at = datetime.utcnow()
        logger.info(f"Deprecated: {name} v{version}")
        return True

    def compare_versions(self, name: str, v1: str, v2: str) -> Dict[str, Any]:
        """Compare two prompt versions"""
        prompt1 = self.get_prompt(name, v1)
        prompt2 = self.get_prompt(name, v2)

        if not prompt1 or not prompt2:
            return {}

        return {
            'v1': v1,
            'v2': v2,
            'v1_hash': prompt1.get_hash(),
            'v2_hash': prompt2.get_hash(),
            'content_identical': prompt1.content == prompt2.content,
            'v1_status': prompt1.status.value,
            'v2_status': prompt2.status.value,
            'change_type': self._detect_change_type(prompt1, prompt2)
        }

    def _detect_change_type(self, old: PromptVersion, new: PromptVersion) -> str:
        """Detect what type of change was made"""
        if old.content == new.content:
            return "metadata_only"

        old_len = len(old.content.split())
        new_len = len(new.content.split())

        if new_len > old_len * 1.2:
            return "expansion"
        elif new_len < old_len * 0.8:
            return "compression"
        else:
            return "refinement"

    def export_to_json(self, output_path: str) -> str:
        """Export all prompts to JSON"""
        data = {}
        for name, versions in self.prompts.items():
            data[name] = [v.to_dict() for v in versions]

        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2, default=str)

        return output_path

    def track_performance(self, performance: PromptPerformance) -> None:
        """Track performance metrics"""
        self.performance_history.append(performance)

    def get_performance_trend(self, prompt_name: str, days: int = 30) -> List[PromptPerformance]:
        """Get performance trend for a prompt"""
        cutoff = datetime.utcnow() - timedelta(days=days)
        return [
            p for p in self.performance_history
            if p.prompt_version.startswith(prompt_name) and p.metric_date > cutoff
        ]


class PromptTester:
    """Test prompts before production"""

    def __init__(self, prompt: PromptVersion):
        self.prompt = prompt
        self.tests: List[PromptTest] = []
        self.results: Dict[str, Any] = {}

    def add_test(self, test: PromptTest) -> None:
        """Add a test case"""
        self.tests.append(test)

    def run_test(self, test: PromptTest, output: str) -> Tuple[bool, float]:
        """Evaluate output against test criteria"""
        test.actual_output = output

        # Check if output contains expected criteria
        output_lower = output.lower()
        matched_criteria = 0

        for criterion in test.expected_output_criteria:
            if criterion.lower() in output_lower:
                matched_criteria += 1

        test.score = matched_criteria / len(test.expected_output_criteria) if test.expected_output_criteria else 0.0
        test.passed = test.score >= 0.8  # 80% threshold

        return test.passed, test.score

    def run_all_tests(self) -> Dict[str, Any]:
        """Run all tests and generate report"""
        passed = 0
        failed = 0
        avg_score = 0.0

        for test in self.tests:
            if test.passed:
                passed += 1
            else:
                failed += 1
            avg_score += test.score

        avg_score = avg_score / len(self.tests) if self.tests else 0.0

        self.results = {
            'prompt_version': f"{self.prompt.name} v{self.prompt.version}",
            'test_count': len(self.tests),
            'passed': passed,
            'failed': failed,
            'pass_rate': round(passed / len(self.tests), 2) if self.tests else 0.0,
            'average_score': round(avg_score, 2),
            'test_details': [t.to_dict() for t in self.tests]
        }

        return self.results

    def export_results(self, output_path: str) -> str:
        """Export test results"""
        if not self.results:
            self.run_all_tests()

        with open(output_path, 'w') as f:
            json.dump(self.results, f, indent=2, default=str)

        return output_path


# Example usage
if __name__ == "__main__":
    from datetime import timedelta

    logging.basicConfig(level=logging.INFO)

    # Create manager
    manager = PromptManager()

    # Create system prompt
    system_prompt = manager.create_prompt(
        name="Policy Analyst",
        version="1.0",
        prompt_type=PromptType.SYSTEM,
        content="You are an expert policy analyst...",
        author="Alice Chen",
        description="System prompt for government policy analysis"
    )

    # Create task prompt
    task_prompt = manager.create_prompt(
        name="Policy Analysis - AI Governance",
        version="1.0",
        prompt_type=PromptType.TASK,
        content="I need you to analyze the AI governance framework...",
        author="Alice Chen"
    )

    # Create tests
    tester = PromptTester(system_prompt)

    test1 = PromptTest(
        name="Policy Analysis Test 1",
        input_text="Analyze the proposed AI governance framework",
        expected_output_criteria=["options", "trade-offs", "recommendation"]
    )
    test1.actual_output = "Here are the options: Option A has benefits. Trade-offs: cost vs risk. Recommendation: Option B"
    tester.run_test(test1, test1.actual_output)
    tester.add_test(test1)

    # Run tests
    results = tester.run_all_tests()
    print(f"Test Results: {results['passed']}/{results['test_count']} passed")
    print(f"Average Score: {results['average_score']}")

    # Track performance
    perf = PromptPerformance(
        prompt_version="Policy Analyst v1.0",
        metric_date=datetime.utcnow(),
        total_uses=150,
        average_latency_ms=1200,
        user_satisfaction=4.3,
        error_rate=0.02,
        output_quality_score=0.87
    )
    manager.track_performance(perf)

    # Export
    manager.export_to_json("/tmp/prompts.json")
    print("\nExported to /tmp/prompts.json")

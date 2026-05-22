# Outputs Directory Pattern

## Purpose

Standardized directory structure and artifact persistence strategy for generated deliverables, caches, and outputs from skills.

## Directory Structure

```
outputs/
├── {skill-name}/
│   ├── {run-date}/
│   │   ├── manifest.json              # Metadata about generated artifacts
│   │   ├── {artifact-name}.pptx       # Deliverables
│   │   ├── {artifact-name}.md
│   │   ├── {artifact-name}.json
│   │   └── logs/
│   │       ├── processing.log         # Execution logs
│   │       ├── errors.log
│   │       └── warnings.log
│   ├── latest -> {most-recent-date}/  # Symbolic link to latest
│   └── archive/
│       ├── {older-date}/
│       └── {oldest-date}/
│
├── cache/
│   ├── presentation-deck/
│   │   ├── template.pptx              # Cached templates
│   │   └── brand-assets/
│   ├── news-gathering/
│   │   ├── rss-feeds.json             # Cached feed lists
│   │   └── api-configs.yaml
│   └── prompts/
│       ├── system/
│       └── task/
│
└── .gitignore                         # Don't commit generated artifacts
```

## Manifest File (manifest.json)

Each skill run generates a manifest documenting artifacts:

```json
{
  "skill": "presentation-deck",
  "version": "2.1",
  "run_id": "run-2026-05-22-143000",
  "timestamp": "2026-05-22T14:30:00Z",
  "user": "alice@organization.ca",
  "status": "success",
  "duration_seconds": 45,
  
  "input": {
    "template": "executive-strategy-briefing",
    "audience": "executive",
    "topic": "Digital Transformation Strategy",
    "language": "en"
  },
  
  "artifacts": [
    {
      "name": "Digital_Transformation_Strategy.pptx",
      "type": "pptx",
      "size_bytes": 2450000,
      "format": "PowerPoint 2016+",
      "pages": 15,
      "accessibility": "WCAG 2.1 AA",
      "hash": "sha256:abc123...",
      "generated_at": "2026-05-22T14:30:35Z"
    },
    {
      "name": "slide-content.json",
      "type": "json",
      "size_bytes": 45000,
      "schema": "presentation-deck-v2",
      "hash": "sha256:def456..."
    },
    {
      "name": "speaker-notes.md",
      "type": "markdown",
      "size_bytes": 15000,
      "hash": "sha256:ghi789..."
    }
  ],
  
  "processing": {
    "template_rendering": { "duration_ms": 1200, "status": "success" },
    "content_generation": { "duration_ms": 18500, "status": "success" },
    "accessibility_check": { "duration_ms": 3200, "status": "success", "issues": 0 },
    "export": { "duration_ms": 22100, "status": "success" }
  },
  
  "quality_metrics": {
    "accessibility_score": 1.0,
    "content_completeness": 0.98,
    "visual_consistency": 1.0,
    "spell_check": "passed"
  },
  
  "dependencies": {
    "skills": ["accessible-pptx/v1.0"],
    "templates": ["executive-strategy-briefing/v1.md"],
    "brand_assets": ["hc-colors/v2.0"]
  },
  
  "retention": {
    "policy": "keep_7_days",
    "expires_at": "2026-05-29T14:30:00Z",
    "archive_after_days": 7
  },
  
  "provenance": {
    "generated_by": "skill:presentation-deck",
    "triggered_by": "user",
    "source_branch": "main",
    "source_commit": "a1b2c3d"
  }
}
```

## Python Integration Pattern

### ArtifactManager Class

```python
from pathlib import Path
from datetime import datetime, timedelta
import json
import hashlib
import logging

logger = logging.getLogger(__name__)


class ArtifactManager:
    """Manage skill output artifacts"""

    def __init__(self, skill_name: str, base_path: str = "outputs"):
        self.skill_name = skill_name
        self.base_path = Path(base_path)
        self.run_date = datetime.utcnow().strftime("%Y-%m-%d")
        self.run_time = datetime.utcnow().strftime("%H%M%S")
        self.run_id = f"run-{self.run_date}-{self.run_time}"
        
        # Create directories
        self.skill_dir = self.base_path / skill_name
        self.run_dir = self.skill_dir / self.run_id
        self.run_dir.mkdir(parents=True, exist_ok=True)
        
        self.artifacts = []
        self.logs = {
            'processing': [],
            'errors': [],
            'warnings': []
        }

    def save_artifact(self, filename: str, content: bytes, artifact_type: str = "generic") -> dict:
        """Save artifact and record metadata"""
        artifact_path = self.run_dir / filename
        
        # Write file
        with open(artifact_path, 'wb') as f:
            f.write(content)
        
        # Calculate hash
        file_hash = hashlib.sha256(content).hexdigest()
        
        # Record metadata
        metadata = {
            'name': filename,
            'type': artifact_type,
            'size_bytes': len(content),
            'hash': f"sha256:{file_hash}",
            'generated_at': datetime.utcnow().isoformat() + 'Z'
        }
        
        self.artifacts.append(metadata)
        logger.info(f"Saved artifact: {filename} ({len(content)} bytes)")
        return metadata

    def log_processing(self, stage: str, duration_ms: int, status: str = "success", details: dict = None):
        """Log processing stage"""
        log_entry = {
            'stage': stage,
            'duration_ms': duration_ms,
            'status': status,
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        }
        if details:
            log_entry.update(details)
        
        self.logs['processing'].append(log_entry)

    def log_error(self, error_type: str, message: str, context: dict = None):
        """Log error"""
        error_entry = {
            'type': error_type,
            'message': message,
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        }
        if context:
            error_entry['context'] = context
        
        self.logs['errors'].append(error_entry)
        logger.error(f"[{error_type}] {message}")

    def generate_manifest(self, status: str, input_params: dict, quality_metrics: dict = None) -> dict:
        """Generate manifest.json"""
        manifest = {
            'skill': self.skill_name,
            'run_id': self.run_id,
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'status': status,
            'input': input_params,
            'artifacts': self.artifacts,
            'processing': self.logs['processing'],
            'quality_metrics': quality_metrics or {}
        }
        
        # Save manifest
        manifest_path = self.run_dir / 'manifest.json'
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        logger.info(f"Manifest saved to {manifest_path}")
        return manifest

    def save_manifest(self):
        """Save manifest.json"""
        manifest_path = self.run_dir / 'manifest.json'
        manifest = {
            'skill': self.skill_name,
            'run_id': self.run_id,
            'artifacts': self.artifacts,
            'logs': self.logs
        }
        
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)

    def cleanup_old_artifacts(self, keep_days: int = 7):
        """Remove artifacts older than keep_days"""
        cutoff = datetime.utcnow() - timedelta(days=keep_days)
        
        for run_path in self.skill_dir.iterdir():
            if run_path.is_dir() and run_path.name.startswith('run-'):
                # Parse date from run-YYYY-MM-DD-HHMMSS
                try:
                    run_date_str = run_path.name[4:13]  # Extract YYYY-MM-DD
                    run_date = datetime.strptime(run_date_str, '%Y-%m-%d')
                    
                    if run_date < cutoff:
                        logger.info(f"Removing old artifacts: {run_path}")
                        import shutil
                        shutil.rmtree(run_path)
                except Exception as e:
                    logger.error(f"Error cleaning up {run_path}: {e}")

    def get_artifact_path(self, filename: str) -> Path:
        """Get path to saved artifact"""
        return self.run_dir / filename

    def list_artifacts(self) -> list:
        """List all artifacts in run"""
        return [
            self.run_dir / a['name']
            for a in self.artifacts
        ]
```

### Usage Example

```python
# Initialize
manager = ArtifactManager("presentation-deck")

# Generate presentation
start = time.time()
pptx_content = generate_presentation(template="executive-brief", audience="C-suite")
duration = (time.time() - start) * 1000
manager.log_processing("content_generation", int(duration), status="success")

# Save artifact
manager.save_artifact(
    "Digital_Transformation.pptx",
    pptx_content,
    artifact_type="pptx"
)

# Quality checks
accessibility_score = check_accessibility(pptx_content)
manager.log_processing("accessibility_check", 3200, "success", {"issues": 0})

# Generate manifest
manifest = manager.generate_manifest(
    status="success",
    input_params={'template': 'executive-brief', 'audience': 'C-suite'},
    quality_metrics={'accessibility': accessibility_score}
)

# Cleanup old artifacts
manager.cleanup_old_artifacts(keep_days=7)

print(f"Artifacts saved to: {manager.run_dir}")
print(f"Manifest: {manifest}")
```

## Caching Strategy

### What to Cache

```
Cache (keep indefinitely):
├── Templates (PPTX master slides, HTML templates)
├── Brand assets (colors, logos, fonts)
├── Configuration files (API keys, source lists)
├── Model weights (ML models for sentiment analysis)
└── Reference data (mapping tables, dictionaries)

Don't cache:
├── Generated presentations (store as output, not cache)
├── News feed content (changes frequently)
├── User-specific data (privacy)
└── Transient data (temporary processing)
```

### Cache Invalidation

```
Templates: Invalidate on version change (major only)
Brand assets: Invalidate on brand update or quarterly
Config files: Invalidate on config change (immediate)
Reference data: Invalidate monthly
```

## Retention Policy

### Default Policy

```
Outputs (Generated Artifacts):
- Recent (0-7 days): Keep in outputs/{skill}/{run-id}/
- Archive (7-90 days): Move to archive/ subdirectory
- Expired (>90 days): Delete

Caches:
- Keep indefinitely unless version/expiry specified
- Review quarterly for cleanup

Logs:
- Keep 30 days in outputs/logs/
- Archive after 30 days
```

### Example: Flexible Retention

```json
{
  "retention": {
    "policy": "custom",
    "keep_days": 30,
    "archive_days": 7,
    "expires_at": "2026-06-22T14:30:00Z",
    "reason": "Large PPTX files (2.4MB)"
  }
}
```

## .gitignore Configuration

```
# Don't commit generated outputs
outputs/*/run-*/**/*
outputs/*/latest -> # Don't symlinks either

# Keep manifests only (for audit trail)
!outputs/**/manifest.json

# Cache can be committed if small, else ignore
# cache/**.pptx       # Ignore large PPTX templates
!cache/**.json       # Keep config JSON files

# Logs
logs/*.log
!logs/README.md
```

## Monitoring & Metrics

### Success Rate

```
Track per skill:
- Total runs: 150
- Successful: 148 (98.7%)
- Failed: 2 (1.3%)
- Average duration: 45.2 seconds
```

### Storage Usage

```
outputs/ total size: 45.3 GB
├── presentation-deck: 32.1 GB
├── news-gathering: 8.9 GB
├── architecture-diagram: 3.2 GB
└── prompts: 1.1 GB

Cache size: 2.4 GB
```

## Integration with Skills

Each skill should:

1. **Initialize ArtifactManager** at start
2. **Log processing stages** as work progresses
3. **Save artifacts** with proper metadata
4. **Generate manifest** at completion
5. **Cleanup old** artifacts based on policy

Example in skill code:

```python
# At skill execution start
from artifact_manager import ArtifactManager

manager = ArtifactManager("my-skill")

try:
    # Do work...
    manager.log_processing("stage1", duration)
    # ... more work
    
    manager.generate_manifest(
        status="success",
        input_params=input_dict,
        quality_metrics=metrics_dict
    )
finally:
    # Cleanup
    manager.cleanup_old_artifacts()
```

## Version Control

- **Commit**: manifest.json (audit trail)
- **Don't commit**: Generated PPTX, PDFs, large files
- **Optional commit**: Small cache files (config JSON)

## Related Documentation

- Skill definitions: `skills/*/SKILL.md`
- Integration patterns: `skills/*/integration-patterns/`
- Cache management: `docs/caching-strategy.md`

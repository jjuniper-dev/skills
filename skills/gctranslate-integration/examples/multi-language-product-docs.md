# Example: Multi-Language Product Documentation

## Context
Translating English product documentation into 5 languages (French, Spanish, German, Japanese, Simplified Chinese) using Google Cloud Translate with custom glossary and brand terminology.

## Configuration

```yaml
gcp:
  project_id: "my-company-translation"
  credentials_file: "gcp-credentials.json"
  location: "us-central1"

translation:
  source_language: en
  target_languages:
    - fr  # French
    - es  # Spanish
    - de  # German
    - ja  # Japanese
    - zh  # Chinese (Simplified)
  
  mode: advanced  # Use advanced translation model
  
  glossary:
    - name: tech-glossary
      file: glossary-tech-terms.csv
      languages:
        source: en
        targets: [fr, es, de, ja, zh]
    
    - name: brand-glossary
      file: glossary-brand-terms.csv
      languages:
        source: en
        targets: [fr, es, de, ja, zh]

content:
  source_directory: "docs/en"
  output_directory: "docs/"
  formats: [md, html]
  exclude_patterns: ["*.tmp", "draft-*.md"]
  
processing:
  batch_size: 100  # characters per API call
  max_concurrent_requests: 10
  retry_count: 3
  cache_enabled: true
  cache_ttl: 86400

quality:
  min_confidence_score: 0.8
  require_review_below: 0.85
  preserve_formatting: true
  preserve_code_blocks: true
```

## Glossary Files

### Brand Terms (glossary-brand-terms.csv)
```csv
English,French,Spanish,German,Japanese,Chinese
MyCompany,MyCompany,MyCompany,MyCompany,マイカンパニー,我的公司
MyCloud Platform,Plateforme MyCloud,Plataforma MyCloud,MyCloud-Plattform,MyCloudプラットフォーム,MyCloud平台
Data Workspace,Espace de travail des données,Espacio de trabajo de datos,Datenbasis,データワークスペース,数据工作区
```

### Technical Terms (glossary-tech-terms.csv)
```csv
English,French,Spanish,German,Japanese,Chinese
API Gateway,Passerelle API,Puerta de API,API-Gateway,APIゲートウェイ,API网关
Microservices,Microservices,Microservicios,Mikrodienste,マイクロサービス,微服务
Kubernetes,Kubernetes,Kubernetes,Kubernetes,Kubernetes,Kubernetes
Lambda Function,Fonction Lambda,Función Lambda,Lambda-Funktion,Lambda関数,Lambda函数
```

## Input Document (English)

**File: docs/en/getting-started.md**
```markdown
# Getting Started with MyCompany MyCloud Platform

## Overview
MyCloud Platform is a modern, scalable data platform designed for enterprise teams.

### Key Features
- **Data Ingestion**: Ingest data from any source via APIs or batch uploads
- **Data Transformation**: Build transformation pipelines with zero coding
- **Real-time Analytics**: Query data in milliseconds
- **API Gateway**: Expose your data through RESTful APIs

## Prerequisites
Before you begin:
1. A MyCompany account
2. Access to your Data Workspace
3. Familiarity with basic data concepts

## Step 1: Set up your workspace
1. Log in to MyCloud Platform
2. Click "New Workspace"
3. Name your workspace (e.g., "Sales Analytics")
4. Select your region

## Step 2: Load your first dataset
1. Go to the Data Ingestion panel
2. Select your data source
3. Map your fields
4. Run the pipeline

## Supported Data Sources
- PostgreSQL, MySQL
- Amazon S3, Google Cloud Storage
- REST APIs
- CSV/JSON files

## Next Steps
- Explore our API Gateway documentation
- Learn about Lambda Functions
- Review our data transformation guide
```

## Translation Request (JSON)

```json
{
  "request_id": "trans-2026-05-22-001",
  "timestamp": "2026-05-22T16:00:00Z",
  "content": {
    "text": "Getting Started with MyCompany MyCloud Platform\n\nMyCloud Platform is a modern, scalable data platform designed for enterprise teams.",
    "mime_type": "text/plain",
    "source_language_code": "en",
    "target_language_codes": ["fr", "es", "de", "ja", "zh"]
  },
  "glossaries": [
    "brand-glossary",
    "tech-glossary"
  ],
  "options": {
    "preserve_formatting": true,
    "mode": "advanced",
    "cache_result": true
  }
}
```

## Translation Response (JSON)

```json
{
  "request_id": "trans-2026-05-22-001",
  "timestamp_completed": "2026-05-22T16:00:15Z",
  "translations": [
    {
      "target_language": "fr",
      "translated_text": "Commencer avec la plateforme MyCloud MyCompany\n\nLa plateforme MyCloud est une plateforme de données moderne et évolutive conçue pour les équipes d'entreprise.",
      "detected_source_language": "en",
      "confidence": 0.95,
      "glossary_matches": 3,
      "processing_time_ms": 245
    },
    {
      "target_language": "es",
      "translated_text": "Introducción a la plataforma MyCloud de MyCompany\n\nLa plataforma MyCloud es una plataforma de datos moderna y escalable diseñada para equipos empresariales.",
      "detected_source_language": "en",
      "confidence": 0.94,
      "glossary_matches": 3,
      "processing_time_ms": 198
    },
    {
      "target_language": "de",
      "translated_text": "Erste Schritte mit MyCompany MyCloud-Plattform\n\nDie MyCloud-Plattform ist eine moderne, skalierbare Datenplattform für Unternehmens-Teams.",
      "detected_source_language": "en",
      "confidence": 0.92,
      "glossary_matches": 3,
      "processing_time_ms": 267
    },
    {
      "target_language": "ja",
      "translated_text": "MyCompanyのMyCloudプラットフォームを使い始める\n\nMyCloudプラットフォームは、エンタープライズチーム向けに設計された最新のスケーラブルなデータプラットフォームです。",
      "detected_source_language": "en",
      "confidence": 0.88,
      "glossary_matches": 3,
      "processing_time_ms": 312
    },
    {
      "target_language": "zh",
      "translated_text": "MyCompany MyCloud平台入门\n\nMyCloud平台是为企业团队设计的现代化、可扩展的数据平台。",
      "detected_source_language": "en",
      "confidence": 0.91,
      "glossary_matches": 3,
      "processing_time_ms": 289
    }
  ],
  "summary": {
    "total_character_count": 178,
    "estimated_cost_usd": 0.0003,
    "glossary_compliance": 1.0,
    "avg_confidence": 0.92,
    "all_above_threshold": true
  }
}
```

## Workflow Code (Python)

```python
from google.cloud import translate_v3
import json
import csv

def load_glossary(glossary_name, gcp_project):
    """Load glossary from GCS"""
    client = translate_v3.TranslationServiceClient()
    parent = client.common_location_path(gcp_project, "us-central1")
    glossary = client.get_glossary(name=f"{parent}/glossaries/{glossary_name}")
    return glossary

def translate_document(source_text, source_lang, target_langs, glossaries, gcp_project):
    """Translate text using Google Cloud Translate"""
    client = translate_v3.TranslationServiceClient()
    parent = client.common_location_path(gcp_project, "us-central1")
    
    results = {}
    for target_lang in target_langs:
        response = client.translate_text(
            request={
                "parent": parent,
                "contents": [source_text],
                "source_language_code": source_lang,
                "target_language_code": target_lang,
                "glossaries": [
                    translate_v3.TranslateTextRequest.Glossary(
                        glossary=f"{parent}/glossaries/{g}"
                    )
                    for g in glossaries
                ],
                "mime_type": "text/plain",
            }
        )
        
        results[target_lang] = {
            "text": response.translations[0].translated_text,
            "confidence": response.translations[0].translated_text,
            "glossary_terms_applied": len(response.translations[0].glossary_terms)
        }
    
    return results

def validate_translation(original, translated, min_confidence=0.8):
    """Validate translation quality"""
    # Back-translate to source language
    client = translate_v3.TranslationServiceClient()
    back_translated = client.translate_text(...)
    
    # Compare with original (simple word overlap)
    original_words = set(original.lower().split())
    back_words = set(back_translated.lower().split())
    overlap = len(original_words & back_words) / len(original_words)
    
    return {
        "quality_score": overlap,
        "is_valid": overlap >= min_confidence,
        "requires_review": overlap < 0.85
    }

def export_translated_docs(translations, output_dir):
    """Export translated documents"""
    for lang, content in translations.items():
        with open(f"{output_dir}/getting-started.{lang}.md", "w") as f:
            f.write(content["text"])
```

## Output Files

**docs/fr/getting-started.md** (French translation)
**docs/es/getting-started.md** (Spanish translation)
**docs/de/getting-started.md** (German translation)
**docs/ja/getting-started.md** (Japanese translation)
**docs/zh/getting-started.md** (Chinese translation)

## Quality Report

```json
{
  "report_timestamp": "2026-05-22T16:05:00Z",
  "document": "getting-started.md",
  "summary": {
    "total_segments": 12,
    "segments_reviewed": 12,
    "segments_approved": 11,
    "segments_needing_review": 1,
    "avg_confidence": 0.92,
    "glossary_compliance": 1.0
  },
  "flagged_segments": [
    {
      "segment_id": "seg-003",
      "source": "Familiarity with basic data concepts",
      "target_ja": "基本的なデータ概念の知識",
      "confidence": 0.73,
      "issue": "Low confidence - may need expert review",
      "suggested_fix": "基本的なデータコンセプトに関する知識"
    }
  ],
  "glossary_applied": 15,
  "brand_consistency": "100%"
}
```

## Maintenance Schedule
- **Daily**: Monitor translation cache hits and API costs
- **Weekly**: Review flagged segments and update glossaries
- **Monthly**: Refresh translations for frequently updated content
- **Quarterly**: Audit translation quality with native speakers

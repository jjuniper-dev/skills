# Skill: Google Cloud Translate Integration

## Purpose
Integrate Google Cloud Translation API for multi-language support: translate content, detect source language, implement localization workflows, and manage translation quality and consistency.

## When to use
- Translating documents, web content, or user-generated text
- Multi-language product/service support
- Global audience communications
- Localization pipelines
- Language detection and routing
- Content bridging across language communities
- Accessibility (language alternatives)

## Inputs
- Text or document content (plain text, HTML, XML)
- Source language (auto-detect or specified)
- Target language(s) (single or batch)
- Optional: glossary for terminology consistency
- Optional: context or domain hints
- Optional: custom model/mode (base, advanced)

## Outputs
- Translated text with language metadata
- Confidence scores or quality indicators
- Language detection results
- Formatting preservation (HTML, newlines)
- Translation alternatives or variants
- Glossary compliance report

## Constraints
- Character limits per request (manage batching)
- Supported language pairs (validate before translation)
- API quota and rate limits
- Cost tracking (billed per character)
- Sensitive data handling (PHI, PII considerations)
- Quality thresholds for auto-acceptance
- Regional availability and latency

## Workflow
1. **Initialize client** - Set up GCP credentials and project
2. **Detect language** - Identify source language if not specified
3. **Prepare content** - Parse, normalize, and batch as needed
4. **Select mode** - Choose standard or advanced translation
5. **Apply glossary** - Use custom glossaries for terminology
6. **Translate** - Call API with batched requests
7. **Validate quality** - Check confidence scores, format preservation
8. **Post-process** - Apply formatting, review for context
9. **Cache/store** - Archive translations for reuse and audit

## Quality checks
- No characters lost in translation
- HTML/formatting preserved
- Glossary terms enforced
- Confidence scores above threshold
- No untranslatable content
- Consistency across related translations
- Reviewed by domain expert for critical content
- Accessibility of translated content verified

## Output formats
- Plain text (translated)
- HTML/XML (with formatting preserved)
- JSON with metadata (translation, confidence, language)
- CSV batch export
- Integration event (webhook, message queue)

## Configuration
- GCP project ID and credentials
- API endpoint (standard, advanced)
- Glossary references
- Cache settings
- Batch size and concurrency
- Error handling (fail-fast vs. partial success)
- Logging and audit trail

## Integrations
- Content management systems
- Web frameworks (Django, Express, FastAPI)
- Document pipelines (PDF, Word)
- Real-time messaging (chat, notifications)
- Analytics/feedback systems
- Quality assurance workflows

## Examples
- Multi-language customer support portal
- Global marketing campaign (blog → 10 languages)
- Software UI localization
- Real-time chat translation
- Document archive with translation index
- Accessibility: auto-generate alt text in multiple languages

# Skill: GCTranslate Integration

## Purpose
Integrate Translation Bureau's GCTranslate service — the Government of Canada's AI-powered, sovereign alternative to public internet translation tools for federal public servants. Enable secure, policy-aligned EN↔FR translation for internal communications while maintaining human-in-the-loop control and compliance.

## What is GCTranslate

**GCTranslate** is a Protected B-capable translation platform developed by Public Services and Procurement Canada (PSPC) and the Translation Bureau, built on the GC's 8-billion-word bilingual corpus and Canadian linguistic conventions. It represents a "lighthouse" enterprise AI implementation: centralized, sovereign, policy-aligned, and reusable across departments.

**Strategic Significance**:
- First visible GC enterprise AI shared service (alongside HC/PHAC platform patterns)
- Demonstrates governance-first deployment and human-in-the-loop operation
- Canadian data residency (internal hosting, not reliant on US services)
- Reusable infrastructure reducing departmental fragmentation

## When to use
- Internal emails and Teams messages (both languages)
- Meeting notes and transcripts (bilingual capture)
- Operational documentation (policies, procedures, internal guidance)
- Real-time bilingual communication (Teams message translation)
- Quick drafting in one language with translation to the other
- Departmental coordination across language communities

## When NOT to use
- Cabinet documents (requires Translation Bureau professional review)
- Legislation and regulatory text
- Public-facing communications (public websites, media releases, citizen-facing content)
- Health/safety advisories (life-safety risk)
- High-risk regulatory material (financial, legal, compliance-critical)
- Anything requiring official translation certificates

## Inputs
- Source text (EN or FR)
- Target language (FR or EN)
- Optional: context, glossary, department terminology
- Optional: document context (email, meeting note, operational memo)

## Outputs
- Translated text (EN↔FR)
- Confidence/quality indicators
- Suggested terminology from GC glossaries
- Audit trail (source, translator, timestamp, approval status)
- Human review prompts for sensitive content

## Constraints
- Protected B data environment (secure)
- Character limits per request (batch large documents)
- Only EN↔FR language pair
- Not for public or high-risk content (human judgment required)
- Intended for internal GC use only
- Requires GC network access or VPN
- Department must be onboarded (PSPC manages access)

## Workflow
1. **Authenticate** - Use GC credentials (GCKey, GCID, certificate)
2. **Prepare content** - Normalize text, identify language, note context
3. **Classify sensitivity** - Flag if content is high-risk (requires human review)
4. **Request translation** - Submit to GCTranslate API or web interface
5. **Review output** - Check quality, terminology, cultural appropriateness
6. **Apply human judgment** - Approve, edit, or escalate to Translation Bureau
7. **Publish/send** - Use in Teams, email, SharePoint, or internal system
8. **Archive** - Log for audit trail and reuse

## Quality checks
- Translation preserves meaning and tone
- GC terminology and conventions applied (not generic internet language)
- No untranslatable or corrupted sections
- No PII/sensitive data exposure
- Bilingual consistency across related documents
- Human review completed for sensitive content
- Audit trail recorded (who requested, when, which version approved)

## Integration examples
- **Teams**: Real-time message translation (EN message → FR thread, or vice versa)
- **Email drafting**: Write in one language, translate draft to the other before sending
- **Meeting notes**: Capture bilingual notes with translations recorded
- **SharePoint**: Bilingual document storage (EN + FR versions with translation metadata)
- **News gathering**: Translate international news summaries for bilingual briefing

## Outputs
- Translated text (plain text or formatted)
- JSON with metadata (source, target, confidence, timestamp)
- Audit log (department, user, content category, approval status)
- Batch export (multiple translations with quality flags)

## Configuration
- GC credentials (GCKey or certificate)
- Department/agency identifier
- Default source/target languages
- Glossary references (GC terminology database)
- Sensitivity classification rules
- Audit logging destination (SharePoint or internal database)
- Team channels for review workflows

## Integrations
- Microsoft Teams (message translation plug-in)
- Outlook/Email (draft translation)
- SharePoint (bilingual document versioning)
- ServiceNow (ticket translation for bilingual support)
- Custom GC systems (via API)
- Translation Bureau workflow (escalation for professional review)

## Related Patterns
This skill demonstrates the **governance-first enterprise AI** pattern used in the HC/PHAC platform strategy:
- Centralized shared service (not departmental silos)
- Sovereign Canadian infrastructure
- Human-in-the-loop (augmentation, not replacement)
- Department onboarding at varying maturity levels
- Reusable infrastructure and terminology standards
- Audit trail for compliance and transparency

## References
- [Translation Bureau AI Guidance](https://www.canada.ca/en/services/gctranslate)
- [GCtranslate Overview](https://www.canada.ca/en/services/government-canada-translate)
- PSPC AI Strategy 2025–2027 (GCTranslate as reference implementation)
- Early adopter departments: PSPC, PCO, Finance Canada, Canadian Heritage, FINTRAC, RCMP

## Examples
See: `examples/` directory for:
- Bilingual Teams workflow
- Email draft translation pattern
- Meeting note capture and translation
- Departmental onboarding checklist

## Status
✅ **Reference implementation ready** — Use for HC/PHAC enterprise AI platform design

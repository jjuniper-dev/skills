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

## Workflow (SaaS Platform Usage)
1. **Authenticate** - Log in to GCTranslate portal using GC credentials (GCKey, GCID)
2. **Access platform** - Navigate to web interface (GC-hosted)
3. **Prepare content** - Copy/paste or upload text (EN or FR source)
4. **Classify sensitivity** - Select document type (email, memo, meeting note, etc.)
5. **Submit translation** - Click translate button, receive EN↔FR output
6. **Review output** - Check quality, GC terminology, cultural appropriateness
7. **Apply human judgment** - Accept, edit, or flag for Translation Bureau escalation
8. **Copy and use** - Paste into Teams, email, SharePoint, or target system
9. **Track usage** - Platform logs translations for audit trail and learning

## Quality checks
- Translation preserves meaning and tone
- GC terminology and conventions applied (not generic internet language)
- No untranslatable or corrupted sections
- No PII/sensitive data exposure
- Bilingual consistency across related documents
- Human review completed for sensitive content
- Audit trail recorded (who requested, when, which version approved)

## Use Case Examples
- **Urgent email response**: Public servant receives EN email, uses GCTranslate to draft FR response quickly
- **Team alignment**: Translate key meeting decisions to FR for minority language team members
- **Policy memo rollout**: Draft policy in EN, translate via GCTranslate, publish both versions
- **Bilingual briefing**: Translate news summaries or reports for executive briefing in both languages
- **Cross-departmental communication**: PSPC guidance translated for other departments using GCTranslate

## Outputs from SaaS Platform
- Translated text (EN↔FR, copy-paste ready)
- Suggested terminology (from GC glossaries)
- Quality confidence indicator
- Usage log (department, user, timestamp, content type)
- Translation history (searchable for reuse)

## Department Onboarding (SaaS Access)
- **Request access**: Submit department onboarding request to PSPC
- **User provisioning**: GC credentials (GCKey, GCID) grant platform access
- **Training**: Translation Bureau provides user guides and best practices
- **Department glossary**: Optional custom terminology for domain-specific language (finance, health, etc.)
- **Usage monitoring**: Track translations per department/user for governance
- **Escalation workflow**: Define process for flagging high-risk content to Translation Bureau

## Workflow Integration (Using SaaS Platform)
- **Teams**: Copy message → GCTranslate → paste translated version in thread or separate message
- **Email**: Draft in EN → copy to GCTranslate → paste FR version to Outlook reply
- **SharePoint**: Store original and translated versions side-by-side with metadata
- **Meeting notes**: Transcribe in one language → translate via GCTranslate → publish bilingual notes
- **Memo/directive**: Author in EN → translate → distribute both versions
- **Manual escalation**: Flag high-risk content → send to Translation Bureau for professional review

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

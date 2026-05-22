# Skill: Accessible PowerPoint (PPTX)

## Purpose
Create, validate, and remediate PowerPoint presentations for accessibility compliance (WCAG 2.1 AA, Government of Canada standards).

## When to use
- Creating accessible presentations for public/staff
- Validating existing decks for compliance
- Remediating inaccessible presentations
- Government/institutional presentations
- Ensuring inclusive access for all attendees
- Meeting accessibility legislation requirements

## Inputs
- PowerPoint file (.pptx)
- Optional: accessibility target level (WCAG AA, AAA, GC standard)
- Optional: presentation metadata (title, author, language)
- Optional: audience accessibility needs

## Outputs
- Accessibility compliance report (JSON/HTML)
- Remediated PPTX file (if input was non-compliant)
- Detailed recommendations (per slide)
- Accessibility checklist (testable items)
- Alt text suggestions (for images, charts)
- Color contrast analysis

## Constraints
- Images must have descriptive alt text (< 125 characters preferred)
- Color contrast ratio ≥ 4.5:1 for text (WCAG AA)
- Font size ≥ 18pt for body text (recommended)
- No text as images (exceptions: logos, charts)
- Logical reading order (no random positioning)
- Meaningful hyperlink text (not "click here")
- Tables with headers and proper structure
- Video/audio must have captions or transcript

## Workflow
1. **Analyze PPTX** - Extract content, styles, metadata
2. **Check structure** - Validate slide hierarchy, reading order
3. **Analyze colors** - Check contrast ratios
4. **Check images** - Identify missing alt text
5. **Check fonts** - Validate size, family, readability
6. **Check links** - Validate link text, destinations
7. **Check tables** - Validate structure and headers
8. **Check multimedia** - Identify missing captions
9. **Generate report** - Issues, severity, recommendations
10. **Remediate** - Fix issues, create accessible version
11. **Validate** - Re-check remediated version

## Quality checks
- ✅ All images have alt text (descriptive, < 125 chars)
- ✅ Color contrast ≥ 4.5:1 for all text
- ✅ Font size ≥ 18pt for body text
- ✅ Fonts are sans-serif (preferred) or readable serif
- ✅ Logical reading order (top-to-bottom, left-to-right)
- ✅ Links have descriptive text (not "click here")
- ✅ Tables have proper headers and structure
- ✅ Multimedia has captions or transcript
- ✅ No images of text (exceptions documented)
- ✅ Slide titles present (for navigation)

## Compliance levels
- **WCAG 2.1 A**: Basic accessibility
- **WCAG 2.1 AA**: Government standard (recommended)
- **WCAG 2.1 AAA**: Maximum accessibility
- **Government of Canada**: AA + specific requirements

## Output formats
- JSON compliance report (machine-readable)
- HTML accessibility report (human-readable)
- Remediated PPTX (if auto-fixes available)
- Alt text suggestions (for manual review)
- Color contrast map (visual feedback)
- Accessibility checklist (testable items)

## Tools & integrations
- python-pptx (programmatic access)
- WCAG Contrast Checker (color validation)
- PDF/A conversion (for archival)
- Screen reader testing (manual validation)
- Accessibility audit tools (WAVE, Axe)

## Common issues & fixes

| Issue | Severity | Fix |
|-------|----------|-----|
| Missing alt text | Critical | Add descriptive alt text to images |
| Low contrast | Critical | Increase text size or change color |
| Small font | High | Increase to ≥18pt (body) or ≥22pt (titles) |
| Unclear link text | High | Change "click here" to descriptive text |
| Image of text | Medium | Replace with actual text or add alt text |
| No slide titles | Medium | Add titles to all slides |
| Poor reading order | Medium | Reposition elements in logical order |
| No captions | Medium | Add captions to videos/audio |

## Testing & validation
- **Automated**: Contrast, font size, structure
- **Manual**: Alt text quality, link text, reading order
- **Screen reader**: Test with NVDA, JAWS, VoiceOver
- **Keyboard**: Tab through presentation, all elements accessible
- **Color blind**: Test with color-blind simulation tools

## Examples
- HC/PHAC presentation remediation
- Government briefing deck validation
- Executive presentation accessibility audit
- Training materials accessibility check
- Public webinar presentation preparation

## Related skills
- **Presentation Deck** - Create accessible presentations from start
- **Architecture Diagram** - Accessible diagram creation
- **Briefing Note** - Accessible written communication

# Template: WCAG 2.1 AA Compliance Checklist

## Presentation Metadata

| Field | Value |
|-------|-------|
| Title | [Presentation Title] |
| Author | [Your Name] |
| Target Audience | [Audience Description] |
| Target Compliance Level | WCAG 2.1 AA |
| Review Date | [YYYY-MM-DD] |
| Next Review | [YYYY-MM-DD] |

## Pre-Creation Checklist

### Color & Contrast
- [ ] Color palette chosen (avoid red-green combinations for color-blind users)
- [ ] Primary text color: RGB(17, 24, 39) [dark gray] on light background
- [ ] All text contrast ≥ 4.5:1 (verified with online checker)
- [ ] Links: distinguishable from surrounding text (not color-only)
- [ ] Don't rely on color alone to convey meaning

### Typography
- [ ] Body text: sans-serif (Helvetica, Arial, Verdana) or highly readable serif
- [ ] Font size: ≥ 18pt for body text, ≥ 22pt for slide titles
- [ ] Line spacing: 1.5× minimum for body text
- [ ] Font weights: bold for emphasis, not ALL CAPS

### Slide Structure
- [ ] Every slide has a descriptive title
- [ ] Logical heading hierarchy (H1 = slide title, H2 = section, H3 = subsection)
- [ ] Content organized top-to-bottom, left-to-right
- [ ] No decorative elements blocking content
- [ ] Consistent layout across slides (predictable navigation)

### Images & Visuals
- [ ] All images have descriptive alt text (< 125 characters, < 150 characters acceptable)
- [ ] Alt text describes content and purpose, not "image of..." or "picture of..."
- [ ] Charts/graphs have alt text explaining data and key findings
- [ ] Diagrams have alt text explaining relationships and structure
- [ ] No images of text (use actual text instead; exception: logos)
- [ ] Decorative images: alt text = "" (empty, marked as decorative)

### Tables
- [ ] Table headers marked as headers (not just bold)
- [ ] First row: column headers; first column: row headers (where applicable)
- [ ] No merged cells (screen readers can't handle them)
- [ ] Data cells logically aligned with headers
- [ ] Complex tables: summary or caption provided

### Links & Navigation
- [ ] Link text is descriptive ("Learn more about AI governance" not "click here")
- [ ] Links have underline or other visual indicator (not color-only)
- [ ] Hyperlinks tested (work, point to correct resource)
- [ ] No auto-advancing slides (user controls navigation)
- [ ] Tab order is logical (test with keyboard: Tab key)

### Multimedia
- [ ] Videos have captions (synchronized with audio)
- [ ] Audio has transcript (or captions)
- [ ] Auto-play disabled (users choose when to start)
- [ ] No rapid flashing (< 3 times per second) to avoid seizure triggers
- [ ] Captions include speaker identification and sound effects

### Lists & Formatting
- [ ] Lists use proper bullet points (not dashes or asterisks)
- [ ] Ordered lists have sequential numbering
- [ ] No indentation only (use proper nested lists)
- [ ] Code blocks: monospace font, high contrast, syntax highlighting optional

### Accessibility Features (PowerPoint)
- [ ] Slide titles added to XML (for screen reader navigation)
- [ ] Reading order set correctly (Design → Arrange → Selection Pane)
- [ ] ALT text added to all objects (images, shapes, charts)
- [ ] Slide numbers included (for reference in presentations)
- [ ] Master slides accessible (consistent across all slides)

## Accessibility Review Sections

### Per-Slide Review

**Slide [#]: [Title]**

Color Contrast:
- Primary text: ☐ Pass
- Secondary text: ☐ Pass
- Links: ☐ Pass

Images & Alt Text:
- Image 1: [File] → Alt: "[alt text]" ☐ Pass
- Image 2: [File] → Alt: "[alt text]" ☐ Pass

Tables (if applicable):
- Headers marked: ☐ Yes
- Structure logical: ☐ Yes
- Merged cells: ☐ None

Reading Order:
- Logical sequence: ☐ Yes
- No skipped elements: ☐ Yes

Issues Found:
- [Issue]: [Severity] [Remediation]

### Common Issues & Fixes

| Issue | Severity | How to Fix |
|-------|----------|-----------|
| Low contrast | CRITICAL | Increase font size, change text color, use lighter/darker background |
| Missing alt text | CRITICAL | Add descriptive alt text to all images (< 125 chars) |
| Small font | HIGH | Increase to ≥18pt (body), ≥22pt (title) |
| Unclear link text | HIGH | Change "click here" → "[specific action]" |
| Poor reading order | MEDIUM | Reorder elements using Selection Pane (Design → Arrange) |
| No slide title | MEDIUM | Add title to every slide |
| Image of text | MEDIUM | Replace with actual text; if icon/logo, add alt text |
| No captions | MEDIUM | Add captions to videos/audio |

## Validation Testing

### Automated Checks (PowerPoint Add-in or Online Tools)
- [ ] Accessibility Checker run (Review → Check Accessibility)
- [ ] All alerts reviewed
- [ ] False positives documented

### Manual Checks
- [ ] Alt text quality reviewed (descriptive, < 125 chars)
- [ ] Contrast ratio tested (Color Contrast Analyzer tool)
- [ ] Link destinations verified
- [ ] Reading order tested (keyboard Tab navigation)

### Screen Reader Testing
- [ ] NVDA (Windows, free)
  - [ ] Slide titles read correctly
  - [ ] Content in logical order
  - [ ] Links identified as links
  - [ ] Alt text presented
- [ ] JAWS (Windows, commercial)
- [ ] VoiceOver (Mac, free)

### Color Blind Testing
- [ ] Deutan (green-blind) simulation
- [ ] Protan (red-blind) simulation
- [ ] Tritanopia (blue-yellow) simulation
- [ ] Use: Color Blindness Simulator online tool

### Keyboard Navigation
- [ ] Tab key moves through all interactive elements
- [ ] No keyboard traps (can exit with Tab/Shift+Tab)
- [ ] Enter key activates buttons/links
- [ ] Escape exits modals/menus

## Sign-Off

| Role | Name | Date | Status |
|------|------|------|--------|
| Creator | [Your Name] | [YYYY-MM-DD] | ☐ Reviewed |
| Accessibility Reviewer | [Name] | [YYYY-MM-DD] | ☐ Approved |
| Final Approval | [Manager] | [YYYY-MM-DD] | ☐ Signed Off |

## Non-Compliant Items (If Applicable)

If any item cannot be made compliant, document the exception:

| Item | Issue | Reason | Timeline to Fix |
|------|-------|--------|-----------------|
| [Element] | [Why not WCAG AA] | [Business/technical reason] | [Target date] |

## Related Resources

- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Accessibility Insights for Office](https://accessibilityinsights.io/)
- [NVDA Screen Reader](https://www.nvaccess.org/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Government of Canada Accessibility Guidelines](https://www.canada.ca/en/government/about/accessibility.html)

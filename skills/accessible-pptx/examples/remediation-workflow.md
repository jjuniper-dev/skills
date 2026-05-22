# Example: PowerPoint Accessibility Remediation Workflow

## Scenario

Health Canada has a 25-slide briefing deck on pandemic preparedness that was created without accessibility considerations. The presentation needs to be remediated to meet WCAG 2.1 AA compliance before sharing with stakeholders.

## Initial Assessment

**Issues Found** (using Accessibility Checker + manual review):

```json
{
  "total_issues": 18,
  "critical": {
    "missing_alt_text": 12,
    "low_contrast": 3
  },
  "high": {
    "small_font": 2,
    "unclear_links": 1
  },
  "medium": {
    "poor_reading_order": 0
  },
  "compliance_rate": "28%"
}
```

## Remediation Steps

### 1. Fix Critical Issues First

#### Issue: Missing Alt Text (12 instances)

**Slide 3: Epidemic Curve**
- **Before**: Image inserted, no alt text
- **After**: 
  ```
  Alt text: "Line graph showing confirmed COVID-19 cases in Canada from March to October 2023, peaking at 150,000 cases in May, declining to 50,000 by October. Represents national outbreak trajectory."
  ```
  - Describes data and significance ✓
  - Under 125 characters ✓
  - Avoids "image of..." or "chart of..." ✓

**Slide 7: Provincial Heat Map**
- **Before**: Image of colored map, no description
- **After**:
  ```
  Alt text: "Map of Canada showing provincial COVID-19 incidence rates: red (>100 per 100K), orange (50-100), yellow (20-50), green (<20). Ontario and Quebec highest risk."
  ```

**Slide 12: WHO Logo**
- **Before**: Logo image, no alt text
- **After**: 
  ```
  Alt text: "" (empty—decorative logo, redundant with text reference)
  ```

#### Issue: Low Contrast (3 instances)

**Slide 2: Title Slide**
- **Before**: Light gray text (#999999) on light blue background—contrast ratio 2.8:1 ✗
- **After**: Dark navy text (#003D68) on light blue background—contrast ratio 5.2:1 ✓
  - Used HC brand primary color
  - Maintains visual hierarchy
  - Passes WCAG AA

**Slide 9: Data Table**
- **Before**: Dark gray text (#505050) on medium gray background—ratio 4.1:1 (fails for body text)
- **After**: Black text (#000000) on white background—ratio 21:1 ✓

### 2. Fix High-Priority Issues

#### Issue: Small Font (2 instances)

**Slide 5: References**
- **Before**: 12pt footnotes (too small for 16:9 projection)
- **After**: 14pt body text, 16pt section headers (minimum for accessibility)

**Slide 18: Technical Appendix**
- **Before**: 10pt code blocks
- **After**: 12pt monospace (Courier New), maintains readability

#### Issue: Unclear Link Text (1 instance)

**Slide 15: Resources**
- **Before**: "Click here for more info" → broken, unclear destination
- **After**: "Public Health Agency of Canada COVID-19 Response" → descriptive, specific

### 3. Optimize Reading Order

**Slide 4: Two-Column Layout**
- **Before**: Shape (left image) added first, then text box (right)—screen reader order incorrect
- **After**: 
  - Reordered in Selection Pane: left column first, then right column
  - Logical reading order: title → left content → right content ✓

**Slide 11: Chart with Legend**
- **Before**: Legend text entered after chart object
- **After**: 
  - Reordered: chart first, then legend explanation below
  - Screen reader announces chart, then explains legend

### 4. Verify Slide Structure

**Added missing titles:**
- Slide 6 had only body text, no title → Added "Vaccination Campaign Timeline"
- Slide 13 was a full-slide image → Added title overlay "Provincial Health Authority Structure"

### 5. Quality Assurance Testing

#### Automated: Accessibility Checker
```
✓ All slides have titles
✓ No missing alt text
✓ No duplicate alt text
✓ No placeholder text
⚠ 2 alerts: Complex shapes (reviewed as intentional)
```

#### Manual: Color Contrast Verification
```
Tool: WebAIM Contrast Checker

Slide 2 (title): #003D68 on #EDFBFF → 5.2:1 ✓
Slide 9 (table): #000000 on #FFFFFF → 21:1 ✓
Slide 15 (links): #003D68 underlined on #FFFFFF → 5.2:1 ✓
```

#### Screen Reader: NVDA Test
```
Navigation:
→ Slide 1 (title): "Pandemic Preparedness Briefing" ✓
→ Slide 3 (chart): Title read, alt text read, legend description read ✓
→ Slide 7 (table): Headers identified, data cells aligned ✓
→ Slide 15 (links): "Public Health Agency link" announced ✓

Reading Order: All elements in expected sequence ✓
```

#### Keyboard Navigation
```
Tab through slide 9 (table):
→ Title
→ First cell (A1)
→ Each column header
→ Each data row
→ Exit with Shift+Tab ✓
```

## Results

### Accessibility Compliance Report

| Category | Before | After | Status |
|----------|--------|-------|--------|
| Missing Alt Text | 12 | 0 | ✓ Fixed |
| Low Contrast | 3 | 0 | ✓ Fixed |
| Small Font | 2 | 0 | ✓ Fixed |
| Unclear Links | 1 | 0 | ✓ Fixed |
| Missing Titles | 2 | 0 | ✓ Fixed |
| **Compliance Rate** | **28%** | **100%** | **✓ WCAG AA** |

### Estimated Time

- Initial assessment: 1 hour
- Fix critical issues: 3 hours
- Fix high-priority issues: 1.5 hours
- QA testing: 2 hours
- **Total: 7.5 hours**

## Validation Checklist

- ✅ All images have alt text (< 125 chars)
- ✅ Color contrast ≥ 4.5:1 for all text
- ✅ Font size ≥ 18pt body, ≥ 22pt titles
- ✅ All slides have descriptive titles
- ✅ Links have descriptive text (not "click here")
- ✅ Reading order is logical
- ✅ NVDA screen reader test: pass
- ✅ Keyboard navigation: pass
- ✅ Color blind simulation: pass
- ✅ Accessibility Checker: no critical alerts

## Delivery

**File**: `Pandemic_Preparedness_Briefing_Accessible.pptx`

**Shared with**:
- Presentation team (for delivery)
- IT accessibility team (for archival)
- Stakeholders (via SharePoint with accessibility verification note)

**Maintenance**:
- Quarterly review with new content additions
- Accessibility checklist template applied to future updates
- NVDA spot-check before stakeholder distribution

## Lessons Learned

1. **Start with accessibility** → Easier to build in than remediate
2. **Use templates** → Consistent styling reduces compliance issues
3. **Alt text quality matters** → Descriptive, purpose-focused text serves all users
4. **Test with real users** → Screen reader testing reveals issues automated tools miss
5. **Document exceptions** → Any non-compliant items need business justification and timeline

## Related Resources

- Template: `wcag-compliance-template.md`
- Skill: `accessible-pptx/SKILL.md`
- Tool: Microsoft Accessibility Checker (built into PowerPoint)
- External: [WebAIM Alt Text](https://webaim.org/articles/alttext/)

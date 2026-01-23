# Consolidated Gates Logic
## PO2 Compliance Review Theme Methodology
## Parallel Detection with Sequential Resolution
**Version:** v1.1 – 2026-01-23
**Source:** Aligned with PO2 SOW (Authoritative)

---

## Overview

PO2 assigns compliance review themes using a structured combination of **parallel signal detection** and **sequential, precedence-based resolution logic**.

- **Parallel detection** identifies all potential regulatory indicators simultaneously
- **Sequential resolution** assigns exactly **ONE** authoritative Review Theme per comment/amendment

### Design Principles
- Consistent regulatory outcomes
- Clear supervisory accountability
- Scalable analytics and reporting
- Examiner-ready documentation across jurisdictions

Themes are assigned based on **regulatory risk characteristics**, not reviewer discretion.

---

### Gate-to-Theme Mapping

| Gate | Theme # | Theme Name | Precedence |
|------|---------|------------|------------|
| **Gate 1** | Theme 2 | Performance Presentation & Reporting | Highest |
| **Gate 2** | Theme 7 | Rankings, Ratings & Data Context Validation | |
| **Gate 3** | Theme 4 | Testimonials & Endorsements | |
| **Gate 4** | Theme 5 | Digital & Distribution Controls | |
| **Gate 5** | Theme 8 | Third-Party Content & IP | |
| **Gate 6** | Theme 1, 6, or 3 | Core Antifraud & Disclosure Risks (ONE only) | |
| **Gate 7** | Theme 9 | Editorial (Non-Regulatory) | Lowest |

---

## Sequential Resolution Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PARALLEL DETECTION (All 9 Themes)                         │
│                 All themes evaluated simultaneously at ingestion             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                       SEQUENTIAL RESOLUTION                                  │
│              Assigns ONE final review theme per compliance comment           │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  GATE 1: Performance Presentation & Reporting (Theme 2)                      │
│  ───────────────────────────────────────────────────────                     │
│  KEY QUESTION: Does content include performance data implicating             │
│                required performance mechanics or presentation standards?     │
│                                                                              │
│  • Missing or incomplete performance periods                                 │
│  • Net vs. gross presentation issues                                         │
│  • Calculation, methodology, or benchmark deficiencies                       │
│                                                                              │
│  If YES → Assign Theme 2 (HIGHEST PRECEDENCE - always takes priority)        │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │ NO
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  GATE 2: Rankings, Ratings & Data Context Validation (Theme 7)               │
│  ──────────────────────────────────────────────────────────────              │
│  KEY QUESTION: Does content reference rankings, ratings, awards, league      │
│                tables, or third-party data requiring contextual validation?  │
│                                                                              │
│  • Missing methodology or selection criteria                                 │
│  • Unidentified ranking provider or time period                              │
│  • Inability to validate underlying data                                     │
│                                                                              │
│  If YES → Assign Theme 7                                                     │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │ NO
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  GATE 3: Testimonials & Endorsements (Theme 4)                               │
│  ──────────────────────────────────────────────                              │
│  KEY QUESTION: Does content include testimonials, endorsements, or           │
│                influencer statements?                                        │
│                                                                              │
│  • Missing compensation or relationship disclosures                          │
│  • Implied guarantees via testimonials                                       │
│  • Influencer marketing concerns                                             │
│                                                                              │
│  If YES → Assign Theme 4                                                     │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │ NO
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  GATE 4: Digital & Distribution Controls (Theme 5)                           │
│  ──────────────────────────────────────────────────                          │
│  KEY QUESTION: Is the issue driven by method of distribution or channel      │
│                governance, rather than substance of content?                 │
│                                                                              │
│  • Unapproved social media posts                                             │
│  • Improper digital distribution methods                                     │
│  • Recordkeeping or archiving failures                                       │
│                                                                              │
│  If YES → Assign Theme 5                                                     │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │ NO
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  GATE 5: Third-Party Content & Intellectual Property (Theme 8)               │
│  ──────────────────────────────────────────────────────────────              │
│  KEY QUESTION: Does content improperly use or attribute third-party          │
│                materials?                                                    │
│                                                                              │
│  • Copyright uncertainty                                                     │
│  • Unauthorized logos or research                                            │
│  • Misstated affiliations                                                    │
│                                                                              │
│  If YES → Assign Theme 8                                                     │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │ NO
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  GATE 6: Core Antifraud & Disclosure Risks (Theme 1, 6, or 3 - ONE ONLY)     │
│  ────────────────────────────────────────────────────────────────────────    │
│  If none of the above apply, assign the SINGLE theme that most directly      │
│  drives regulatory exposure:                                                 │
│                                                                              │
│  • Theme 1: Misleading or Unsubstantiated Claims                             │
│  • Theme 6: False or Misleading Comparisons                                  │
│  • Theme 3: Inadequate or Missing Disclosures                                │
│                                                                              │
│  Only ONE of these themes may be assigned per review comment                 │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │ NO
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  GATE 7: Editorial / Non-Regulatory (Theme 9) - LOWEST PRECEDENCE            │
│  ─────────────────────────────────────────────────────────────────           │
│  KEY QUESTION: Are remaining observations purely editorial with NO           │
│                regulatory risk?                                              │
│                                                                              │
│  • Grammar or formatting suggestions                                         │
│  • Branding or stylistic clarity                                             │
│  • Explicit confirmation that content is compliant                           │
│                                                                              │
│  If YES → Assign Theme 9                                                     │
│  Editorial items EXCLUDED from regulatory risk metrics & supervisory reports │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ONE FINAL REVIEW THEME                               │
│        Fixed precedence order ensures consistent regulatory treatment        │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Single-Outcome Principle

PO2 assigns **one and only one** Review Theme per item:
- No secondary themes
- No stacked classifications
- No dual reporting

This ensures:
- Clear ownership of regulatory risk
- Consistent metrics and dashboards
- Examiner-ready outputs aligned with supervisory expectations

---

## Engineering Summary (Authoritative)

> PO2 detects indicators across all nine review themes in **parallel** at ingestion, then resolves to exactly one final Review Theme using a fixed precedence order:
>
> **Performance → Rankings/Data Context → Testimonials → Digital/Distribution → Third-Party IP → Claims/Comparisons/Disclosures → Editorial (Non-Regulatory)**

---

## Gate 1: Performance Presentation & Reporting

**Regime:** SEC Marketing Rule 206(4)-1
**Version:** v0.3

### Skip Condition
If content contains no performance data, returns, yields, or investment results → return `[]`

### Buckets

| Bucket | Triggers | Verify |
|--------|----------|--------|
| **A. Missing Required Time Periods** | Performance table missing 5-year or 10-year column; Annualized returns without all required periods; Since inception not shown when fund is <5 or <10 years old | Check if fund age justifies missing period |
| **B. Incorrect or Incomplete Performance Data** | Numbers don't match source data; Partial period returns as full period; Data contradicts other sections | Confirm data is actually incorrect |
| **C. Net vs. Gross Presentation Errors** | Returns without "Net" or "Gross" designation; Information Ratio missing qualifier | Label not in header, row, or footnote |
| **D. Benchmark or Index Deficiencies** | Performance compared to undefined benchmark; Inappropriate benchmark; Inconsistent calculation | Definition not elsewhere in document |
| **E. Hypothetical/Backtested Performance Issues** | Backtested returns without stating so; Model portfolio without disclosure; Projected returns without disclaimers | SEC Marketing Rule disclosures absent |
| **F. Calculation or Methodology Errors** | Mathematically incorrect annualized return; Composite aggregated incorrectly; TWR vs MWR misapplied | Confirm error exists, not rounding |
| **G. Yield vs. Total Return Mislabeling** | SEC yield labeled as "return"; Distribution rate as performance; Subsidized yield without ID | Confirm genuinely mislabeled |
| **H. Improper Performance Formatting** | Returns as "7.72" instead of "7.72%"; Missing "as of" date; Performance buried | Formatting not in adjacent context |

### Key Rule
> "If the issue involves performance data, returns, yields, or investment results presentation—flag in Gate 1"

---

## Gate 2: Rankings, Ratings & Data Context

**Regime:** SEC Marketing Rule / FINRA
**Version:** v0.2

### Skip Condition
If content contains no rankings, ratings, awards, third-party references, or factual data metrics → return `[]`

### Buckets

| Bucket | Triggers | Verify |
|--------|----------|--------|
| **A. Unidentified Ranking/Rating Provider** | "According to J.D. Power" without full citation; "Top 10 Fund" without naming entity | Check footnotes for provider ID |
| **B. Missing Methodology or Selection Criteria** | Award without selection explanation; "Best in Class" without criteria | Methodology not elsewhere in doc |
| **C. Missing Time Period or Evaluation Date** | Rating with future effective date; AUM without "as of" date | Date not in header, caption, footnote |
| **D. Inability to Validate Underlying Data** | Missing source for third-party study; Claims based on undisclosed data | No documentation reference exists |
| **E. Paid Rankings Without Disclosure** | Paid "Top Funds" placement without disclosure; Sponsored award as independent | No compensation acknowledgment |
| **F. Outdated or Superseded Rankings** | Using prior year's rating when newer exists; Referencing withdrawn rankings | Confirm newer rating available |
| **G. Mischaracterization of Ranking Scope** | Rating distribution as "3, 4" instead of "3%, 4%"; Category ranking as overall | Presentation materially distorts meaning |

### Key Rule
> "When the issue occurs within ratings, rankings, or factual data context—flag in Gate 2"

---

## Gate 3: Testimonials & Endorsements

**Category:** TestimonialsEndorsements
**Version:** v1.0

### Scope
- Testimonials, endorsements, client stories, influencer content, third-party praise
- Focus on:
  - Client vs non-client status disclosures
  - Compensation and material terms
  - Material conflicts of interest
  - Adoption/entanglement with third-party content

### Issue Codes
- `TESTIMONIAL_DISCLOSURE_001`
- `TESTIMONIAL_COMPENSATION_001`

### Output Schema
```json
{
  "category": "TestimonialsEndorsements",
  "sections": [
    {
      "section_title": "<section>",
      "page_number": "<page>",
      "observations": "<risk description>",
      "violating_text": "<exact snippet>",
      "recommendations": "<action>",
      "internal": {
        "issue_code": "TESTIMONIAL_DISCLOSURE_001",
        "severity": "LOW|MEDIUM|HIGH"
      }
    }
  ]
}
```

---

## Gate 4: Digital & Social Media Practices

**Category:** DigitalAndSocialMediaPractices
**Version:** v1.0

### Scope
- Channel and interaction mechanics:
  - Adoption of likes, shares, comments as endorsements
  - Auto-updating content undermining disclosures
  - Platform constraints causing missing/hidden disclosures

### Issue Codes
- `DIGITAL_SOCIAL_LIKES_001`
- `DIGITAL_SOCIAL_AUTOUPDATE_001`

### Output Schema
```json
{
  "category": "DigitalAndSocialMediaPractices",
  "sections": [...]
}
```

---

## Gate 5: Third-Party Content & IP

**Category:** ThirdPartyContentAndIP
**Version:** v1.0

### Scope
- Use of third-party content (indexes, rating agencies, media excerpts, research, images, logos)
- Focus on:
  - Missing or inadequate attribution
  - Use beyond implied scope
  - Modifications changing meaning

### Issue Codes
- `IP_MISSING_ATTRIBUTION_001`
- `IP_SCOPE_EXCEEDED_001`
- `IP_MEANING_CHANGED_001`

### Output Schema
```json
{
  "category": "ThirdPartyContentAndIP",
  "sections": [...]
}
```

---

## Gate 6: Core Antifraud & Disclosure Risks

**Regime:** SEC Marketing Rule 206(4)-1 / FINRA Rule 2210
**Version:** v0.3

### Gate 6 Selection Rule

If none of Gates 1-5 apply, PO2 assigns the **single theme that most directly drives regulatory exposure**:

| Theme | Category | When to Assign |
|-------|----------|----------------|
| **Theme 1** | Misleading or Unsubstantiated Claims | Claim's truthfulness, substantiation, or balance is at issue |
| **Theme 6** | False or Misleading Comparisons | Comparative statements are cherry-picked, unfair, or unbalanced |
| **Theme 3** | Inadequate or Missing Disclosures | Required disclosure is missing, incorrect, or inadequately prominent |

**Only ONE of these themes may be assigned per review comment.**

---

### Theme 1: Misleading or Unsubstantiated Claims

#### Skip Condition
If content contains no claims (no statements about performance, benefits, superiority, outcomes, or recommendations) → return `[]`

#### Buckets

| Bucket | Triggers | Verify |
|--------|----------|--------|
| **A. Unsubstantiated Statements of Fact** | "Best firm for producing top results" without ranking source; "Leading provider" without market share data | Check sentence, paragraph, footnotes for support |
| **B. Promissory or Certain Outcome Language** | "Will outperform the market"; "Guaranteed returns"; "Cannot lose money" | Check for qualifiers (may, might, could) |
| **C. Overstated or Absolute Claims** | "Best", "always", "never", "risk-free", "perfect"; "World-class" without definition | Confirm no reasonable basis exists |
| **D. Unbalanced Benefit Statements** | "Very beneficial strategy" with no risk mention; "Enhanced returns" without volatility | Check for balancing language |
| **E. Ambiguous or Vague Claims** | "Outperforms peers" without defining peer group; "Strong track record" without period | Confirm essential context missing |
| **F. Implied Guarantees or Certainty** | "May be welcomed" → "is a very beneficial strategy"; Removal of "may", "might", "could" | Confirm edit materially increases certainty |

---

### Theme 6: False or Misleading Comparisons

#### Scope
Comparative statements between products, benchmarks, strategies, or firms.

#### Focus Areas
- Cherry-picked periods or benchmarks
- Apples-to-oranges comparisons
- Unfair or unbalanced comparative framing

#### Issue Codes
- `COMPARE_CHERRYPICKED_001`
- `COMPARE_UNFAIR_001`
- `COMPARE_UNBALANCED_001`

---

### Theme 3: Inadequate or Missing Disclosures

#### Skip Condition
If content contains no investment products, strategies, or claims requiring disclosure → return `[]`

#### Buckets

| Bucket | Triggers | Verify |
|--------|----------|--------|
| **A. Missing Core Risk Disclosures** | No "past performance..." near performance data; No "may lose value" near investment description | Check footnotes, fine print |
| **B. Omitted Material Facts** | Management fees not mentioned; Conflicts not disclosed; ESG claims without clarity | Confirm genuinely absent |
| **C. Incorrect or Inverted Disclosure Language** | "FDIC insured" for non-insured product; "No fees" when fees exist | Confirm materially incorrect |
| **D. Misleading Regulatory References** | Implying SEC/FINRA endorsement; Incorrect registration status | Confirm genuinely misleading |
| **E. Incomplete or Placeholder Disclosure Text** | "[Insert risk disclosure here]"; "TBD" or "XXX" | Confirm placeholder/incomplete |
| **F. Missing Chart/Visual Disclosures** | Performance chart without "as of" date; Pie chart without data source | Confirm not in caption/footnote |
| **G. Missing Benchmark Definitions** | "Outperformed the index" without identifying which index | Check glossary, footnotes |
| **H. Disclosure Placement/Prominence** | Risk disclosure in 6pt when claims in 14pt; Disclosure buried in appendix | Assess if investor would miss it |

---

### Key Rules
> "If the issue is about a claim's truthfulness, substantiation, or balance → **Theme 1**"
> "If the issue is about unfair, cherry-picked, or unbalanced comparisons → **Theme 6**"
> "If the issue is about a missing, incorrect, or inadequately prominent disclosure → **Theme 3**"

---

## Gate 7: Editorial (Non-Regulatory)

**Role:** Copy editor
**Version:** v0.1

### Skip Condition
If no obvious typographical, grammatical, or formatting errors exist → return `[]`

### Buckets

| Bucket | Triggers | Verify |
|--------|----------|--------|
| **A. Grammar or Typographical Corrections** | "risk-risk" instead of "risk-return"; Spelling/punctuation errors | Does NOT create misleading claim |
| **B. Formatting or Layout Suggestions** | Inconsistent font sizes; Misaligned tables; Broken layout | Purely visual, no compliance impact |
| **C. Branding or Style Consistency** | Incorrect logo; Non-standard colors; Inconsistent capitalization | Relates to style, not regulation |
| **D. Clarity Improvements (Non-Substantive)** | Header says "year" but title says "Weekly"; Awkward phrasing | Doesn't affect compliance |
| **E. Explicit Confirmation of Compliance** | Material reviewed, no regulatory issues found | Informational confirmation |

### Critical Boundaries (NOT Editorial → Escalate to Gate 6)
- Typo creating factual impossibility (future date) → Gate 6
- Typo introducing "guarantee" language → Gate 6
- Typo inside required disclosure altering meaning → Gate 6
- Typo inverting meaning (positive → negative) → Gate 6

### Key Rule
> "If an issue relates to formatting, labeling, or internal consistency WITHOUT regulatory impact—flag in Gate 7"

---

## Common Output Schema (Gates 1, 2, 6, 7)

```json
{
  "location_hint": "<Page X or Slide X if visible; otherwise empty string>",
  "snippet": "<exact text from document>",
  "bucket": "<bucket name from gate>",
  "rationale": "<1-2 sentences explaining the issue>",
  "recommendation": "<action-oriented fix>"
}
```

**Return value:**
- Array of findings if issues exist
- Empty array `[]` if no issues found

---

## Orchestrator Categories (Theme Mapping)

The orchestrator maps 9 internal categories/themes to gates:

| Theme # | Internal Key | Gate | Precedence |
|---------|--------------|------|------------|
| **2** | PerformancePresentationReporting | Gate 1 | Highest |
| **7** | RankingsAndRatingsIllustration | Gate 2 | |
| **4** | TestimonialsEndorsements | Gate 3 | |
| **5** | DigitalAndSocialMediaPractices | Gate 4 | |
| **8** | ThirdPartyContentAndIP | Gate 5 | |
| **1** | MisleadingOrUnsubstantiatedClaims | Gate 6 (pick one) | |
| **6** | FalseOrMisleadingComparisons | Gate 6 (pick one) | |
| **3** | InadequateOrMissingDisclosures | Gate 6 (pick one) | |
| **9** | EditorialNonRegulatory | Gate 7 | Lowest |

**Note:** Gate 6 contains Themes 1, 6, and 3 — only ONE is assigned per review comment based on which most directly drives regulatory exposure.

---

## Jurisdiction Rules

| Condition | Jurisdiction |
|-----------|--------------|
| US geography + investment adviser | `SEC_IA_MARKETING_RULE` |
| US geography + broker-dealer | `FINRA_COMMUNICATIONS_WITH_PUBLIC` |
| Both may apply simultaneously | |

---

## Design Principles

1. **Sequential Processing** - Each gate handles specific concerns before the next
2. **Deterministic Buckets** - Each issue maps to exactly ONE bucket within its gate
3. **Verify Before Flagging** - Confirm issues are genuine before flagging
4. **Materiality Testing** - Assess whether issue would mislead reasonable investor
5. **CCO Wisdom** - Use action-oriented, professional recommendation language
6. **Clear Boundaries** - Explicit definitions of gate scope and escalation rules
7. **Context Preservation** - Later gates know what earlier gates evaluated
8. **Regulatory Alignment** - All tied to SEC Marketing Rule 206(4)-1 or FINRA rules

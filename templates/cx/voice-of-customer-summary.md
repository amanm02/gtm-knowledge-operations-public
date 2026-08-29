# [Asset title]

> TEMPLATE — replace bracketed values before use.

| Field | Value |
|---|---|
| Asset ID | `ast_cx-voice-of-customer-summary-[number]` |
| Team | `cx` |
| Asset type | `voice_of_customer_summary` |
| Status | `draft` |
| Owner | `[Role or name]` |
| Audience IDs | `[aud_...]` |
| Source IDs | `[src_...]` |
| Evidence IDs | `[evd_...]` |
| Insight IDs | `[ins_...]` |
| Claim IDs | `[clm_...]` |
| Message IDs | `[msg_...]` |
| Sensitivity | `[public \| internal \| confidential \| restricted]` |
| External-use policy | `[external_allowed \| review_required \| internal_only \| never_external]` |
| Created | `[YYYY-MM-DD]` |
| Reviewed | `[YYYY-MM-DD or pending]` |
| Next review | `[YYYY-MM-DD]` |

## Purpose

Synthesize authorized customer signals into shared themes, implications, and knowledge updates without exposing customer identity or overstating prevalence.

## Signal scope

- **Source IDs:** `[src_...]`
- **Evidence IDs:** `[evd_...]`
- **Period:** `[Dates]`
- **Customer segments or audience IDs:** `[aud_...]`
- **Signal types:** `[Support, onboarding, adoption, QBR, renewal, research]`
- **Permission boundary:** `[Internal, paraphrase, quote-approved, or other]`

## Themes

| Theme | Source-faithful summary | Evidence IDs | Affected audiences | Severity or sentiment basis | Confidence |
|---|---|---|---|---|---|
| `[Theme]` | `[Summary]` | `[evd_...]` | `[aud_...]` | `[Only when supported]` | `[level]` |

## Customer language

| Language or paraphrase | Evidence IDs | Permission | Intended use | Restriction |
|---|---|---|---|---|
| `[Language]` | `[evd_...]` | `[Boundary]` | `[Internal insight, Marketing review, Sales enablement, etc.]` | `[Restriction]` |

## Product and process implications

| Implication | Insight IDs | Evidence IDs | Owner | Recommended next action |
|---|---|---|---|---|
| `[Implication]` | `[ins_...]` | `[evd_...]` | `[Role]` | `[Action]` |

## Marketing implications

- **Audience update:** `[aud_... and change]`
- **Message update:** `[msg_... and action]`
- **Content opportunity or risk:** `[Implication]`
- **Restricted language:** `[Boundary]`

## Sales implications

- **Discovery update:** `[Question or signal]`
- **Objection update:** `[Objection and message gap]`
- **Expectation risk:** `[Claim or message boundary]`
- **Competitive implication:** `[If supported]`

## CX implications

- **Onboarding update:** `[Action]`
- **Adoption update:** `[Action]`
- **Renewal or expansion update:** `[Action]`
- **Escalation:** `[Owner and condition]`

## Shared knowledge updates

| Action | Record type | Record ID | Change | Evidence |
|---|---|---|---|---|
| `[Create/update/review/retire]` | `[Audience/Insight/Claim/Message]` | `[ID]` | `[Change]` | `[evd_...]` |

## Known gaps and restrictions

- **Knowledge gaps:** `[List unresolved questions that affect this asset.]`
- **Evidence gaps:** `[List claims, messages, or recommendations that need more support.]`
- **Restrictions:** `[List content that must remain internal, be paraphrased, or receive review.]`
- **Expiry or staleness triggers:** `[List events that require immediate review.]`

## Feedback to GTM Brain

Record what should change in the shared knowledge layer after this asset is used.

| Feedback | Affected record IDs | New source or evidence | Owner | Required action |
|---|---|---|---|---|
| `[Observation, contradiction, new objection, message response, or gap]` | `[IDs]` | `[Source or evidence reference]` | `[Role]` | `[Create, update, review, supersede, or retire]` |

## Review

| Field | Value |
|---|---|
| Reviewer role | `[Role]` |
| Decision | `[approve \| request_changes \| reject \| retire]` |
| Review record ID | `[rev_...]` |
| Rationale | `[Decision rationale]` |
| Unresolved gaps | `[None or list]` |

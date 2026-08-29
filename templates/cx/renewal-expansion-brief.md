# [Asset title]

> TEMPLATE — replace bracketed values before use.

| Field | Value |
|---|---|
| Asset ID | `ast_cx-renewal-expansion-brief-[number]` |
| Team | `cx` |
| Asset type | `renewal_expansion_brief` |
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

Prepare a source-linked renewal and expansion view that separates customer goals, observed adoption, supported outcomes, risks, and hypotheses.

## Context

- **Customer or segment label:** `[Non-sensitive label]`
- **Renewal or review period:** `[Dates]`
- **Audience IDs:** `[aud_...]`
- **Use cases:** `[Use cases]`
- **Confidentiality boundary:** `[What remains in the source system]`

## Customer goals and outcomes

| Goal or outcome | Evidence IDs | Status | Claim ID if supported | Boundary |
|---|---|---|---|---|
| `[Goal/outcome]` | `[evd_...]` | `[Observed, validated, or unverified]` | `[clm_... or none]` | `[Qualification]` |

## Adoption evidence

| Signal | Evidence IDs | Period | Interpretation | Gap |
|---|---|---|---|---|
| `[Signal]` | `[evd_...]` | `[Dates]` | `[Supported interpretation]` | `[Unknown]` |

## Unresolved issues

| Issue | Evidence IDs | Impact | Owner | Target action |
|---|---|---|---|---|
| `[Issue]` | `[evd_...]` | `[Impact]` | `[Role]` | `[Action]` |

## Renewal risks

| Risk | Insight ID | Evidence IDs | Confidence | Mitigation | Escalation |
|---|---|---|---|---|---|
| `[Risk]` | `[ins_...]` | `[evd_...]` | `[level]` | `[Action]` | `[Condition]` |

## Expansion signals

| Signal | Evidence IDs | Audience or use case | Working hypothesis | Evidence needed |
|---|---|---|---|---|
| `[Signal]` | `[evd_...]` | `[aud_... / use case]` | `[Hypothesis]` | `[Gap]` |

## Approved narrative

| Purpose | Message ID | Claim IDs | Approved text | Restriction |
|---|---|---|---|---|
| `[Renewal/expansion/customer review]` | `[msg_...]` | `[clm_...]` | `[Text]` | `[Boundary]` |

## Evidence gaps

- `[Outcome claim needing support]`
- `[Adoption pattern needing a valid comparison]`
- `[Expansion hypothesis needing discovery]`
- `[Customer language needing permission review]`

## Cross-team handoffs

| Team | Handoff | Record IDs | Required action |
|---|---|---|---|
| Marketing | `[Customer language, proof, or message implication]` | `[IDs]` | `[Action]` |
| Sales | `[Expansion context, stakeholder, or objection]` | `[IDs]` | `[Action]` |

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

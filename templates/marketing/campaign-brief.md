# [Asset title]

> TEMPLATE — replace bracketed values before use.

| Field | Value |
|---|---|
| Asset ID | `ast_marketing-campaign-brief-[number]` |
| Team | `marketing` |
| Asset type | `campaign_brief` |
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

Plan a campaign from governed shared knowledge and define how campaign learning returns to Marketing, Sales, CX, and GTM Brain.

## Business goal

- **Goal:** `[Business or communication goal]`
- **Campaign decision:** `[What is being tested or communicated]`
- **Time period:** `[Dates]`
- **Markets or segments:** `[Scope]`

## Audience

| Audience ID | Role or segment | Need | Objection | Desired action |
|---|---|---|---|---|
| `[aud_...]` | `[Role/segment]` | `[Need]` | `[Objection]` | `[Action]` |

## Campaign hypothesis

`[For audience X, approved message Y supported by evidence Z is expected to improve understanding or engagement in context Q.]`

- **Insight IDs:** `[ins_...]`
- **Claim IDs:** `[clm_...]`
- **Message IDs:** `[msg_...]`
- **What would invalidate the hypothesis:** `[Signal]`

## Shared messages and proof

| Role in campaign | Message ID | Claim IDs | Evidence IDs | Restriction |
|---|---|---|---|---|
| `[Primary/supporting/CTA]` | `[msg_...]` | `[clm_...]` | `[evd_...]` | `[Boundary]` |

## Channel and asset plan

| Channel | Asset | Audience | Message IDs | Owner | Review status |
|---|---|---|---|---|---|
| `[Channel]` | `[Asset]` | `[aud_...]` | `[msg_...]` | `[Role]` | `[Status]` |

## Measurement plan

| Learning question | Signal | Data source | Cadence | Owner | Interpretation boundary |
|---|---|---|---|---|---|
| `[Question]` | `[Signal]` | `[Source]` | `[Cadence]` | `[Role]` | `[What the signal cannot prove]` |

## Sales handoff

- **Audience and account context:** `[What Sales needs]`
- **Message IDs:** `[msg_...]`
- **Discovery implications:** `[Questions or signals]`
- **Restrictions:** `[Boundaries]`
- **Feedback requested:** `[What Sales should return]`

## CX handoff

- **Expectation created:** `[What the campaign says or implies]`
- **Claim and message IDs:** `[IDs]`
- **Onboarding or adoption implication:** `[Implication]`
- **Restrictions:** `[Boundaries]`
- **Feedback requested:** `[What CX should return]`

## Campaign learning capture

| Observation | Source record to create | Evidence record to create | Affected shared record | Owner |
|---|---|---|---|---|
| `[Observation]` | `[src_...]` | `[evd_...]` | `[aud_/ins_/clm_/msg_...]` | `[Role]` |

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

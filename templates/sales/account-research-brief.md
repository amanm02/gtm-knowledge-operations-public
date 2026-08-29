# [Asset title]

> TEMPLATE — replace bracketed values before use.

| Field | Value |
|---|---|
| Asset ID | `ast_sales-account-research-brief-[number]` |
| Team | `sales` |
| Asset type | `account_research_brief` |
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

Prepare a source-linked account view while separating observed signals, hypotheses, approved messages, and evidence still needed.

## Account context

- **Account label:** `[Non-sensitive internal label]`
- **Segment:** `[Segment]`
- **Opportunity or relationship stage:** `[Stage]`
- **Relevant use cases:** `[Use cases]`
- **Confidentiality boundary:** `[What must remain in the source system]`

## Strategic priorities

| Observed priority | Evidence ID | Source ID | Confidence | Interpretation boundary |
|---|---|---|---|---|
| `[Priority]` | `[evd_...]` | `[src_...]` | `[level]` | `[What is not known]` |

## Stakeholders and audiences

| Stakeholder label | Audience ID | Role in decision | Known need | Known objection | Evidence |
|---|---|---|---|---|---|
| `[Label]` | `[aud_...]` | `[Role]` | `[Need]` | `[Objection]` | `[evd_...]` |

## Observed signals

| Signal | Evidence IDs | Domain | Meaning supported | Meaning not yet supported |
|---|---|---|---|---|
| `[Signal]` | `[evd_...]` | `[domain]` | `[Supported interpretation]` | `[Unknown]` |

## Working hypotheses

| Hypothesis | Insight IDs | Evidence supporting | Evidence needed | Confidence |
|---|---|---|---|---|
| `[Hypothesis]` | `[ins_... or proposed]` | `[evd_...]` | `[Required evidence]` | `[level]` |

## Relevant approved messages

| Use case | Message ID | Audience ID | Why relevant | Restriction |
|---|---|---|---|---|
| `[Use case]` | `[msg_...]` | `[aud_...]` | `[Reason]` | `[Boundary]` |

## Discovery questions

| Question | Hypothesis tested | Evidence to capture | Affected record |
|---|---|---|---|
| `[Question]` | `[Hypothesis]` | `[Observation needed]` | `[aud_/ins_/clm_/msg_...]` |

## Risks

| Risk | Evidence IDs | Impact | Owner | Escalation |
|---|---|---|---|---|
| `[Risk]` | `[evd_...]` | `[Impact]` | `[Role]` | `[Condition]` |

## Evidence capture plan

- **Create or update Source:** `[src_...]`
- **Create Evidence for:** `[Topics]`
- **Do not capture:** `[Sensitive or unnecessary details]`
- **Return to GTM Brain owner:** `[Role]`

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

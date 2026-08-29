# [Asset title]

> TEMPLATE — replace bracketed values before use.

| Field | Value |
|---|---|
| Asset ID | `ast_sales-discovery-guide-[number]` |
| Team | `sales` |
| Asset type | `discovery_guide` |
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

Guide evidence-seeking discovery using shared audience and insight hypotheses without turning assumptions into facts.

## Call objective

- **Primary objective:** `[Decision or learning objective]`
- **Audience IDs:** `[aud_...]`
- **Account context:** `[Non-sensitive summary]`
- **Relevant insight IDs:** `[ins_...]`
- **Relevant message IDs:** `[msg_...]`

## Hypotheses to test

| Hypothesis | Current evidence | Confidence | What would support it | What would contradict it |
|---|---|---|---|---|
| `[Hypothesis]` | `[evd_...]` | `[level]` | `[Signal]` | `[Signal]` |

## Business context questions

| Question | Why ask | Evidence to capture | Knowledge domain |
|---|---|---|---|
| `[Question]` | `[Purpose]` | `[Observation]` | `[domain]` |

## Workflow and use-case questions

| Question | Why ask | Evidence to capture | Affected insight or claim |
|---|---|---|---|
| `[Question]` | `[Purpose]` | `[Observation]` | `[ID]` |

## Impact and success questions

| Question | Why ask | Evidence boundary | Affected audience or claim |
|---|---|---|---|
| `[Question]` | `[Purpose]` | `[Do not turn stated goal into measured outcome]` | `[ID]` |

## Decision and stakeholder questions

| Question | Why ask | Audience record update | Risk or objection |
|---|---|---|---|
| `[Question]` | `[Purpose]` | `[aud_...]` | `[Concern]` |

## Risk and objection questions

| Question | Underlying concern | Approved response message ID | Escalation condition |
|---|---|---|---|
| `[Question]` | `[Concern]` | `[msg_... or none]` | `[Condition]` |

## Message mapping

| Discovery signal | Message ID | Claim IDs | Use condition | Do not say |
|---|---|---|---|---|
| `[Signal]` | `[msg_...]` | `[clm_...]` | `[Condition]` | `[Boundary]` |

## Evidence capture

- **Source record:** `[src_...]`
- **Evidence records to create:** `[Topics]`
- **Customer-identifying detail to keep out of shared records:** `[Details]`
- **Owner for follow-up:** `[Role]`

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

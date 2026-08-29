# [Asset title]

> TEMPLATE — replace bracketed values before use.

| Field | Value |
|---|---|
| Asset ID | `ast_cx-adoption-risk-brief-[number]` |
| Team | `cx` |
| Asset type | `adoption_risk_brief` |
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

Document an evidence-backed adoption risk, working hypothesis, response, escalation path, and shared-knowledge impact.

## Risk signal

- **Signal:** `[Source-faithful observation]`
- **Evidence IDs:** `[evd_...]`
- **Source IDs:** `[src_...]`
- **Audience IDs:** `[aud_...]`
- **Use case:** `[Use case]`
- **Status:** `[Observed, validated, or disputed evidence context]`

## Affected users or workflows

| Audience or workflow | Evidence | Observed effect | Unknown |
|---|---|---|---|
| `[aud_... or workflow]` | `[evd_...]` | `[Observation]` | `[Gap]` |

## Working hypothesis

- **Hypothesis:** `[Interpretation]`
- **Insight ID:** `[ins_... or proposed]`
- **Confidence:** `[level]`
- **Confidence basis:** `[Why]`
- **Contradicting evidence:** `[evd_... or none]`

## Impact

| Potential impact | Evidence status | Claim boundary | Owner |
|---|---|---|---|
| `[Impact]` | `[Observed or hypothetical]` | `[Do not overstate]` | `[Role]` |

## Recommended action

| Action | Owner | Rationale | Evidence to capture | Review point |
|---|---|---|---|---|
| `[Action]` | `[Role]` | `[Reason]` | `[Observation]` | `[Date or milestone]` |

## Escalation

Escalate when:

- `[Risk affects multiple customers or segments.]`
- `[Risk contradicts an approved Claim or Message.]`
- `[Security, legal, contractual, product, or commercial authority is required.]`
- `[The available evidence is insufficient for the proposed action.]`

**Escalation owner:** `[Role]`

## Message or expectation mismatch

| Message or claim ID | Customer expectation | Observed reality | Required action |
|---|---|---|---|
| `[msg_/clm_...]` | `[Expectation]` | `[Evidence]` | `[Review, update, supersede, or retire]` |

## Resolution criteria

- **Risk reduced when:** `[Evidence-backed condition]`
- **Risk closed when:** `[Condition]`
- **Records to update:** `[IDs]`

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

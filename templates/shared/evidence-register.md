# [Asset title]

> TEMPLATE — replace bracketed values before use.

| Field | Value |
|---|---|
| Asset ID | `ast_shared-evidence-register-[number]` |
| Team | `shared` |
| Asset type | `evidence_register` |
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

Maintain an inspectable register of source-linked observations that may support shared insights, claims, messages, and assets.

## Register scope

- **Question or initiative:** `[Scope]`
- **Knowledge domains:** `[Exact domain values]`
- **Audience IDs:** `[aud_...]`
- **Time period:** `[Dates]`
- **Owner:** `[Role]`

## Evidence

| Evidence ID | Source ID | Locator | Evidence statement | Domain | Status | Confidence | Sensitivity | External-use policy | Affected teams | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| `[evd_...]` | `[src_...]` | `[Section/page/timestamp/row]` | `[Source-faithful observation]` | `[domain]` | `[observed/validated/disputed/retired]` | `[level]` | `[value]` | `[value]` | `[Teams]` | `[Context]` |

## Contradiction map

| Evidence ID | Contradicting evidence IDs | Conflict summary | Scope difference | Affected insights or claims | Resolution owner |
|---|---|---|---|---|---|
| `[evd_...]` | `[evd_...]` | `[Conflict]` | `[Audience/time/method/source]` | `[IDs]` | `[Role]` |

## Evidence quality notes

- **Direct versus indirect:** `[Assessment]`
- **Current versus stale:** `[Assessment]`
- **Corroboration:** `[Assessment]`
- **Missing source context:** `[Assessment]`
- **Restrictions that affect reuse:** `[Assessment]`

## Records supported

| Record ID | Record type | Evidence role | Support level | Review needed |
|---|---|---|---|---|
| `[ID]` | `[Audience/Insight/Claim/Message/Asset]` | `[Primary/corroborating/contradicting/context]` | `[Description]` | `[Yes/no and owner]` |

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

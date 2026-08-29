# [Asset title]

> TEMPLATE — replace bracketed values before use.

| Field | Value |
|---|---|
| Asset ID | `ast_sales-objection-handling-[number]` |
| Team | `sales` |
| Asset type | `objection_handling` |
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

Provide a governed response to a recurring objection while exposing evidence, discovery questions, prohibited responses, and escalation boundaries.

## Objection

`[Use source-faithful buyer language or an authorized paraphrase.]`

- **Audience IDs:** `[aud_...]`
- **Evidence IDs:** `[evd_...]`
- **Context:** `[When and where the objection appears]`
- **Frequency description:** `[Qualitative unless valid measurement exists]`

## Underlying concern

- **Supported interpretation:** `[Concern]`
- **Insight IDs:** `[ins_...]`
- **Confidence:** `[low | medium | high]`
- **Alternative interpretations:** `[Other plausible concerns]`

## Approved response

- **Message ID:** `[msg_... or none]`
- **Exact approved response:** `[Approved text]`
- **Claim IDs:** `[clm_...]`
- **Required qualification:** `[Boundary]`
- **External-use policy:** `[value]`

## Evidence and proof

| Proof point | Evidence IDs | Source IDs | Use condition | Restriction |
|---|---|---|---|---|
| `[Proof]` | `[evd_...]` | `[src_...]` | `[When relevant]` | `[Boundary]` |

## Discovery questions

| Question | What it tests | Evidence to capture | Next step |
|---|---|---|---|
| `[Question]` | `[Underlying concern or context]` | `[Observation]` | `[Action]` |

## Prohibited response

| Prohibited language | Why prohibited | Approved alternative or action |
|---|---|---|
| `[Text]` | `[Unsupported, misleading, restricted, or stale]` | `[msg_... or escalation]` |

## Escalation

Escalate when:

- `[The objection requires security, legal, product, pricing, or policy authority.]`
- `[No approved Message addresses the concern.]`
- `[The available evidence is internal-only or contradicted.]`
- `[The buyer asks for a commitment not supported by an approved Claim.]`

**Escalation owner:** `[Role]`

## Confidence and gaps

- **Response confidence:** `[level]`
- **Evidence gap:** `[Gap]`
- **Message gap:** `[Gap]`
- **Research owner:** `[Role]`

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

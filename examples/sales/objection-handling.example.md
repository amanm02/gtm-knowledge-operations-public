ILLUSTRATIVE OUTPUT — PLACEHOLDER CONTENT ONLY

# Separate tools objection handling

| Field | Value |
|---|---|
| Asset ID | `ast_sales-objection-handling-001` |
| Team | `sales` |
| Asset type | `objection_handling` |
| Status | `draft` |
| Owner | `Sales Knowledge Steward` |
| Audience IDs | `aud_gtm-leader-001` |
| Source IDs | `src_marketing-voc-001` |
| Evidence IDs | `evd_fragmented-research-001` |
| Insight IDs | `ins_cross-team-duplication-001` |
| Claim IDs | `clm_shared-knowledge-reuse-001` |
| Message IDs | `msg_shared-knowledge-reuse-001` |
| Sensitivity | `internal` |
| External-use policy | `review_required` |
| Created | `2026-08-16` |
| Reviewed | `pending` |
| Next review | `2026-11-14` |

## Objection

“We already have separate tools for Marketing, Sales, and CX. Why add a shared layer?”

This wording is illustrative. It is not a real buyer quote.

## Underlying concern

The audience may be concerned that GTM Brain becomes another repository, duplicates systems of record, or adds maintenance without creating reusable cross-team context.

- **Insight ID:** `ins_cross-team-duplication-001`
- **Confidence:** `medium`
- **Alternative interpretation:** The concern may be about integration effort rather than the knowledge model itself.

## Approved response

- **Message ID:** `msg_shared-knowledge-reuse-001`
- **Exact approved message:** “Capture customer, market, product, and field learning once, govern it as shared knowledge, and reuse it across Marketing, Sales, and CX assets.”
- **Claim ID:** `clm_shared-knowledge-reuse-001`
- **Required qualification:** GTM Brain does not replace team systems of record. This repository defines the shared contracts and outputs, not an automated implementation.
- **External-use policy:** `review_required`

## Evidence and proof

| Proof point | Evidence IDs | Source IDs | Use condition | Restriction |
|---|---|---|---|---|
| Team-local knowledge can lead to repeated research and inconsistent reuse | `evd_fragmented-research-001` | `src_marketing-voc-001` | Use to explain the operating problem | Do not quantify impact or imply universal prevalence |

## Discovery questions

| Question | What it tests | Evidence to capture | Next step |
|---|---|---|---|
| Where do Marketing, Sales, and CX currently store customer and market learning? | Whether knowledge is fragmented across systems and documents | Source classes and ownership | Map sources to the three manifests |
| Which messages or claims are currently reused across teams? | Whether approved language has a shared owner and lineage | Message, claim, and evidence references | Create or reconcile shared records |
| What would make a shared layer feel like another stale repository? | Maintenance, ownership, or freshness risk | Audience objection and governance requirement | Update Audience, Governance, or Message records |
| Which team output would be most useful to standardize first? | Priority and value hypothesis | Asset need and audience context | Select one template without implying automation |

## Prohibited response

| Prohibited language | Why prohibited | Approved alternative or action |
|---|---|---|
| “GTM Brain will automatically eliminate duplicate work.” | No automation or measured outcome is represented. | Explain the shared contract and reuse model. |
| “It replaces your CRM, support, and marketing systems.” | The architecture explicitly preserves systems of record. | State that GTM Brain structures shared knowledge across them. |
| “It is already production-ready.” | The repository is a static skeleton. | State the implementation boundary. |

## Escalation

Escalate when:

- the audience requests integration, security, access-control, or deployment commitments;
- a response requires evidence not represented in the shared chain;
- the conversation moves from the operating model to product or commercial commitments;
- a restricted source would be needed.

**Escalation owner:** `GTM Knowledge Owner`

## Confidence and gaps

- **Response confidence:** `medium`
- **Evidence gap:** No production baseline or adoption evidence.
- **Message gap:** No implementation-specific response is approved.
- **Research owner:** `GTM Knowledge Owner`

## Known gaps and restrictions

- This example does not represent a real sales conversation.
- The approved Message is limited to the static operating-model explanation.
- No integration or outcome claim is permitted.

## Feedback to GTM Brain

| Feedback | Affected record IDs | New source or evidence | Owner | Required action |
|---|---|---|---|---|
| The objection is primarily about maintenance ownership rather than tool overlap | `aud_gtm-leader-001`, `ins_cross-team-duplication-001` | Approved call-note summary | Sales Knowledge Steward | Update the Audience objection and Insight |

## Review

| Field | Value |
|---|---|
| Reviewer role | `GTM Knowledge Owner` |
| Decision | `pending` |
| Review record ID | `pending` |
| Rationale | `Illustrative asset has not received a separate Asset review.` |
| Unresolved gaps | `No production implementation or account evidence.` |

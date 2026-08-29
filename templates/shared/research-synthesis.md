# [Asset title]

> TEMPLATE — replace bracketed values before use.

| Field | Value |
|---|---|
| Asset ID | `ast_shared-research-synthesis-[number]` |
| Team | `shared` |
| Asset type | `research_synthesis` |
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

Synthesize a cross-team research question into source-linked findings, contradictions, gaps, and recommended shared knowledge updates.

## Research question

`[State one decision-oriented research question.]`

## Scope

- **Included teams:** `[Marketing, Sales, CX]`
- **Included audiences:** `[aud_...]`
- **Included knowledge domains:** `[Exact taxonomy values]`
- **Time period:** `[Start and end dates]`
- **Excluded material:** `[Sources, customer segments, geographies, or claims outside scope]`

## Source inventory

| Source ID | Team | Source type | Why included | Freshness | Sensitivity | External-use policy |
|---|---|---|---|---|---|---|
| `[src_...]` | `[team]` | `[source_type]` | `[Reason]` | `[current/stale]` | `[value]` | `[value]` |

## Evidence-backed findings

For each finding, distinguish evidence from interpretation.

### Finding 1 — `[Finding title]`

- **Insight candidate:** `[Evidence-backed interpretation]`
- **Evidence IDs:** `[evd_...]`
- **Audience IDs:** `[aud_...]`
- **Confidence:** `[low | medium | high]`
- **Confidence basis:** `[Why]`
- **Team implications:**
  - Marketing: `[Implication]`
  - Sales: `[Implication]`
  - CX: `[Implication]`

Repeat the finding block as needed.

## Contradictions

| Conflict | Evidence IDs | Why the evidence differs | Affected records | Owner | Resolution needed |
|---|---|---|---|---|---|
| `[Conflict]` | `[evd_...]` | `[Scope, timing, audience, method, or factual difference]` | `[IDs]` | `[Role]` | `[Decision or new source]` |

## Knowledge gaps

| Gap | Affected decision | Affected teams | Required source | Owner | Priority |
|---|---|---|---|---|---|
| `[Question that remains unanswered]` | `[Decision or asset]` | `[Teams]` | `[Source class]` | `[Role]` | `[high/medium/low]` |

## Recommended shared records

| Action | Record type | Proposed ID | Statement or purpose | Required evidence | Owner |
|---|---|---|---|---|---|
| `[Create/update/review/retire]` | `[Audience/Insight/Claim/Message]` | `[ID]` | `[Text]` | `[evd_...]` | `[Role]` |

## Decision summary

- **What the evidence supports:** `[Summary]`
- **What the evidence does not support:** `[Summary]`
- **Decision enabled:** `[Decision]`
- **Decision deferred:** `[Decision and reason]`

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

# [Asset title]

> TEMPLATE — replace bracketed values before use.

| Field | Value |
|---|---|
| Asset ID | `ast_shared-knowledge-gap-log-[number]` |
| Team | `shared` |
| Asset type | `knowledge_gap_log` |
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

Track unanswered questions that block shared knowledge, team assets, or governed messaging.

## Gap inventory

| Gap ID | Question | Domain | Affected teams | Blocked assets or records | Priority | Owner | Required source | Status | Target review date |
|---|---|---|---|---|---|---|---|---|---|
| `[gap_...]` | `[Decision-oriented unanswered question]` | `[domain]` | `[Teams]` | `[IDs or asset types]` | `[high/medium/low]` | `[Role]` | `[Source class]` | `[open/in_progress/resolved/accepted]` | `[YYYY-MM-DD]` |

## Priority definitions

- **High:** blocks an approved external asset, creates material message risk, or affects multiple teams.
- **Medium:** blocks a planned internal asset or leaves a recurring decision unresolved.
- **Low:** improves completeness but does not block a current decision.

## Gap detail

### `[gap_...] — [Question]`

- **Why the gap matters:** `[Impact]`
- **Current evidence:** `[evd_...]`
- **Affected insights:** `[ins_...]`
- **Affected claims:** `[clm_...]`
- **Affected messages:** `[msg_...]`
- **Affected assets:** `[ast_...]`
- **Required source or research method:** `[Source]`
- **Owner:** `[Role]`
- **Resolution standard:** `[What evidence is sufficient]`
- **Accepted limitation:** `[If the gap may remain open, state the boundary]`

Repeat the detail block for each high-priority gap.

## Resolved gaps

| Gap ID | Resolution | New evidence IDs | Updated records | Review record ID | Resolved date |
|---|---|---|---|---|---|
| `[gap_...]` | `[Resolution]` | `[evd_...]` | `[IDs]` | `[rev_...]` | `[YYYY-MM-DD]` |

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

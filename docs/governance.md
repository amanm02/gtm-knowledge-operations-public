# Governance

## Purpose

Governance keeps GTM Brain reusable. It makes ownership, evidence boundaries, freshness, review, restrictions, contradictions, and retirement explicit.

This repository documents governance as roles, fields, states, and decision records. It does not implement automated approval.

## Roles

| Role | Required responsibility |
|---|---|
| GTM Knowledge Owner | Owns taxonomy, cross-team policy, duplicate resolution, conflicts, and lifecycle rules. |
| Marketing Knowledge Steward | Owns Marketing source manifests, source quality, and Marketing asset lineage. |
| Sales Knowledge Steward | Owns Sales source manifests, source quality, and Sales asset lineage. |
| CX Knowledge Steward | Owns CX source manifests, source quality, and CX asset lineage. |
| Domain Owner | Approves, changes, supersedes, or retires Claims and Messages for a domain. |
| Asset Owner | Maintains a downstream asset, its lineage, status, gaps, and review date. |
| Reviewer | Records an explicit decision and rationale without editing history. |

One person may hold more than one role, but the role used for a decision must be recorded.

## Sensitivity

Exact values:

| Value | Meaning |
|---|---|
| `public` | Approved for public visibility, subject to external-use policy. |
| `internal` | Intended for employees or authorized internal collaborators. |
| `confidential` | Limited to named roles or groups with a business need. |
| `restricted` | Highly limited; should normally remain in the source system. |

A downstream record may be more sensitive than its source, never less sensitive without an authorized replacement of the dependency.

## External-use policy

Exact values:

| Value | Meaning |
|---|---|
| `external_allowed` | May be reused externally when the downstream record is approved. |
| `review_required` | Requires explicit review before any external use. |
| `internal_only` | May inform internal work but may not be quoted or exposed externally. |
| `never_external` | Must not support external content or communication. |

External-use policy and sensitivity are independent. Public information may still require review.

## Confidence

Exact values:

- `low`
- `medium`
- `high`

Every Insight and Claim includes a written confidence basis.

Confidence does not approve a record and does not override restrictions.

## Lifecycle states and transitions

### Source

States:

- `current`
- `stale`
- `superseded`
- `restricted`

Allowed transitions:

```text
current → stale
current → superseded
current → restricted
stale → current
stale → superseded
stale → restricted
restricted → current
restricted → superseded
```

A superseded Source is terminal.

### Evidence

States:

- `observed`
- `validated`
- `disputed`
- `retired`

Allowed transitions:

```text
observed → validated
observed → disputed
observed → retired
validated → disputed
validated → retired
disputed → validated
disputed → retired
```

Retired is terminal.

### Audience

States:

- `draft`
- `approved`
- `needs_review`
- `retired`

Allowed transitions:

```text
draft → approved
draft → needs_review
draft → retired
approved → needs_review
approved → retired
needs_review → approved
needs_review → retired
```

Retired is terminal.

### Insight

States:

- `proposed`
- `supported`
- `needs_review`
- `retired`

Allowed transitions:

```text
proposed → supported
proposed → needs_review
proposed → retired
supported → needs_review
supported → retired
needs_review → supported
needs_review → retired
```

Retired is terminal.

### Claim

States:

- `proposed`
- `supported`
- `contradicted`
- `retired`

Allowed transitions:

```text
proposed → supported
proposed → contradicted
proposed → retired
supported → contradicted
supported → retired
contradicted → supported
contradicted → retired
```

Retired is terminal.

### Message

States:

- `draft`
- `under_review`
- `approved`
- `superseded`
- `retired`
- `rejected`

Allowed transitions:

```text
draft → under_review
draft → retired
under_review → approved
under_review → draft
under_review → rejected
approved → superseded
approved → retired
superseded → retired
rejected → draft
rejected → retired
```

Retired is terminal.

### Asset

States:

- `draft`
- `ready_for_review`
- `approved_internal`
- `approved_external`
- `retired`

Allowed transitions:

```text
draft → ready_for_review
draft → retired
ready_for_review → draft
ready_for_review → approved_internal
ready_for_review → approved_external
ready_for_review → retired
approved_internal → draft
approved_internal → approved_external
approved_internal → retired
approved_external → draft
approved_external → retired
```

Retired is terminal.

## Review decisions

A Review record uses exactly one decision:

- `approve`
- `request_changes`
- `reject`
- `retire`

Decision interpretation:

| Decision | Required effect |
|---|---|
| `approve` | The owner may move the reviewed object to the appropriate approved or supported state. |
| `request_changes` | The object returns to a draft or needs-review state with unresolved gaps recorded. |
| `reject` | The object becomes rejected or remains non-reusable. |
| `retire` | The object becomes retired and may no longer support new assets. |

The Review record does not mutate another file automatically.

## Freshness windows

The lifecycle policy example encodes these maximum review intervals:

| Record or source type | Maximum interval |
|---|---:|
| Authoritative product and brand sources | 90 days |
| Market and competitor sources | 60 days |
| Campaign and content performance | 30 days |
| Sales objections and win/loss | 90 days |
| CX feedback and adoption signals | 30 days |
| Approved messages | 180 days |
| Competitive battlecards | 60 days |
| Other approved assets | 90 days |

A source or asset becomes `stale` or `needs_review` when its interval is exceeded. Staleness does not delete history.

## Contradictions

Contradictory evidence must remain visible.

Required process:

1. link all relevant Evidence IDs;
2. describe the conflict without selecting a preferred answer prematurely;
3. set affected Insights to `needs_review`;
4. set affected Claims to `contradicted` when the conflict changes support;
5. identify the owner and source needed to resolve the gap;
6. prevent contradicted Claims from supporting approved Messages;
7. preserve the Review record that resolves or accepts the conflict.

Do not average conflicting statements into a false consensus.

## Supersession

Messages and Sources may be superseded.

A superseding record must:

- reference the prior record;
- state why the change occurred;
- record the review decision;
- retain the old record as history;
- update dependent assets or mark them for review.

Do not edit the old record to look as though it always contained the new language.

## Minimum approval checklist for a reusable Message

A Message may become `approved` only when:

- at least one referenced Claim is `supported`;
- all referenced Claims are non-retired;
- all referenced Insights are `supported`;
- all referenced Audiences are approved or current;
- source and evidence restrictions permit the intended use;
- use cases and channels are explicit;
- restrictions are explicit;
- owner, reviewer, reviewed date, and expiry are present;
- material contradictions and gaps are recorded;
- a separate Review record has decision `approve`.

## Minimum approval checklist for an Asset

An Asset may become `approved_internal` when:

- its purpose and audience are explicit;
- its knowledge references resolve;
- restrictions and known gaps are visible;
- the owner has reviewed the current content;
- internal use is compatible with all linked policies.

An Asset may become `approved_external` only when:

- every externally presented Claim is supported;
- every reusable Message is approved and not expired;
- no linked dependency is `internal_only` or `never_external`;
- `review_required` dependencies have explicit approval;
- the asset has a separate approval Review;
- the next-review date is set.

## Retirement

Retire a record when:

- the source no longer exists;
- the evidence is no longer valid or useful;
- the audience definition is obsolete;
- the insight no longer reflects current evidence;
- a claim is no longer supported;
- a message is no longer approved;
- an asset is no longer maintained.

Retirement is not deletion. References remain for lineage and historical understanding.

## Public repository rule

All public scaffold and example files use placeholders. Governance fields demonstrate structure and do not imply real approval, customer evidence, or operational use.

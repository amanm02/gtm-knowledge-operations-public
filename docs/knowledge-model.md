# Knowledge model

## Purpose

The GTM Brain knowledge model prevents teams from collapsing sources, observations, interpretations, claims, approved language, and downstream assets into one undifferentiated document collection.

The model has eight linked record types:

```text
Source → Evidence → Insight → Claim → Message → Asset
                   ↗
              Audience

Review applies to any governed record or asset.
```

An Asset may reference the entire chain. It never replaces the chain.

## Identifier rule

Every record uses a stable human-readable identifier matching:

```regex
^(src|evd|aud|ins|clm|msg|ast|rev)_[a-z0-9]+(?:-[a-z0-9]+)*$
```

Prefixes:

| Record | Prefix |
|---|---|
| Source | `src_` |
| Evidence | `evd_` |
| Audience | `aud_` |
| Insight | `ins_` |
| Claim | `clm_` |
| Message | `msg_` |
| Asset | `ast_` |
| Review | `rev_` |

IDs remain stable when content changes. Status, review dates, and supersession describe the lifecycle.

## Source record

A Source identifies where information originated and under which conditions it may be used.

Required concepts:

- team owner;
- source type;
- title;
- canonical location;
- capture date;
- freshness;
- authority level;
- sensitivity;
- external-use policy;
- knowledge domains;
- tags;
- owner role.

A Source may describe a system export, document, research note, approved transcript summary, performance report, or curated observation.

A Source is not Evidence until a specific traceable statement or observation is recorded.

## Evidence record

Evidence is a narrow traceable observation from a Source.

Required concepts:

- source reference;
- evidence statement;
- source locator;
- observation date;
- status;
- confidence level;
- sensitivity;
- external-use policy;
- knowledge domains;
- owner;
- contradictions when known.

Evidence should use source-faithful language. Interpretation belongs in an Insight.

Examples:

- supported evidence: “Three reviewed call summaries contain the same implementation-effort question.”
- interpretation, not evidence: “Implementation concern is the primary deal blocker.”
- unsupported claim: “The product reduces implementation effort.”

## Audience record

An Audience creates one reusable definition for a buyer, user, customer, account, or segment.

Required concepts:

- name;
- segment;
- role;
- jobs to be done;
- pain points;
- desired outcomes;
- objections;
- success criteria;
- supporting evidence;
- status;
- owner;
- review date.

Marketing, Sales, and CX should reference the same Audience ID when they mean the same role or segment.

An account-specific Audience may extend a reusable role with account context, but it should not redefine the shared role silently.

## Insight record

An Insight is an interpretation derived from Evidence.

Required concepts:

- statement;
- insight type;
- knowledge domains;
- audience references;
- evidence references;
- confidence level and basis;
- status;
- contradictions;
- gaps;
- owner;
- review date.

Insight types are:

- `market_signal`
- `audience_need`
- `product_value`
- `customer_outcome`
- `competitive_pattern`
- `message_performance`
- `adoption_risk`
- `expansion_signal`

An Insight may combine evidence from multiple teams. This is where duplicated research is reconciled.

## Claim record

A Claim is an assertion intended for controlled downstream use.

Required concepts:

- statement;
- claim type;
- evidence and insight references;
- audience references;
- confidence level;
- lifecycle status;
- allowed uses;
- prohibited uses;
- external-use policy;
- owner;
- review date;
- expiry date.

Claim types are:

- `product_capability`
- `differentiation`
- `customer_outcome`
- `market_context`
- `process`
- `service`

A supported Claim is not automatically approved wording. Wording belongs in a Message.

## Message record

A Message is reusable language adapted to audiences, use cases, and channels.

Required concepts:

- text;
- message type;
- claim, insight, and audience references;
- use cases;
- channels;
- restrictions;
- status;
- owner;
- review and expiry;
- supersession.

Message types are:

- `value_proposition`
- `proof_point`
- `objection_response`
- `positioning_statement`
- `customer_language`
- `call_to_action`

Only an `approved` Message should be presented as reusable approved language.

## Asset record

An Asset represents a team deliverable created from shared knowledge.

Required concepts:

- team;
- artifact type;
- title and purpose;
- audience references;
- source, evidence, insight, claim, and message references;
- content path;
- status;
- owner;
- creation and review dates;
- restrictions;
- known gaps.

Asset status does not change the status of its underlying records.

An Asset must not cite another Asset as its only support. It must retain direct references to shared knowledge records.

## Review record

A Review is a separate human decision.

Required concepts:

- object type and ID;
- decision;
- reviewer role;
- review date;
- rationale;
- resolved gaps;
- unresolved gaps;
- next review date.

Decisions are:

- `approve`
- `request_changes`
- `reject`
- `retire`

A Review cannot silently change the underlying content. The reviewed record must be updated separately and retain its own lifecycle state.

## Relationship rules

### Source to Evidence

- Every Evidence record references exactly one Source.
- Multiple Evidence records may reference one Source.
- Evidence inherits or tightens Source sensitivity and external-use policy.
- Evidence may not become more permissive than its Source.

### Evidence to Insight

- Every supported Insight references at least one Evidence record.
- An Insight with no Evidence remains `proposed`.
- Contradictory Evidence remains linked and visible.

### Audience relationships

- Insights, Claims, Messages, and Assets may reference multiple Audiences.
- An Audience must have supporting Evidence.
- Teams reuse Audience IDs instead of creating near-duplicates.

### Insight to Claim

- Every supported Claim references at least one Insight and one Evidence record.
- Claims must define allowed and prohibited uses.
- A contradicted Claim must not support an approved Message.

### Claim to Message

- Every Message references at least one Claim.
- Approved Messages reference only supported, non-retired Claims.
- A Message may be more restrictive than its Claims, never less restrictive.

### Message to Asset

- An Asset may use approved or draft Messages depending on its internal status.
- An externally approved Asset may use only approved, non-expired Messages whose restrictions permit the use.
- The Asset carries all relevant restrictions and known gaps.

### Review relationships

- Review records may apply to Audience, Insight, Claim, Message, or Asset records.
- Source and Evidence reviews are allowed when authority, freshness, or interpretation is disputed.
- Review decisions remain auditable and separate.

## Policy propagation

Use policy becomes more restrictive downstream when any linked record requires it.

Restriction order:

```text
external_allowed
< review_required
< internal_only
< never_external
```

The downstream record receives the most restrictive linked policy unless a reviewer deliberately removes or replaces the restricted dependency.

Sensitivity follows the same principle:

```text
public
< internal
< confidential
< restricted
```

## Confidence

Confidence uses categorical values:

- `low`: limited, indirect, stale, or conflicting support;
- `medium`: multiple relevant sources with remaining gaps;
- `high`: current, direct, corroborated support with no material unresolved contradiction.

Every Insight and Claim includes a `confidence_basis`. Do not infer certainty from a count alone.

## Example chain

```text
src_marketing-voc-001
    Source: curated Marketing voice-of-customer synthesis

evd_fragmented-research-001
    Evidence: teams repeat customer and market research in separate workflows

aud_gtm-leader-001
    Audience: cross-functional GTM leader responsible for alignment

ins_cross-team-duplication-001
    Insight: fragmented knowledge operations increase duplicated research and message drift

clm_shared-knowledge-reuse-001
    Claim: a shared governed knowledge layer enables teams to reuse the same evidence and messages

msg_shared-knowledge-reuse-001
    Message: capture customer, market, and field learning once, then reuse it across Marketing, Sales, and CX

ast_marketing-content-brief-001
ast_sales-objection-handling-001
ast_cx-voc-summary-001
    Assets: three team-specific projections from the same chain
```

The exact illustrative records are under `scaffold/knowledge/` and `examples/shared/`.

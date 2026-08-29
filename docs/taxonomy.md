# Taxonomy

## Purpose

This document is the normative vocabulary for GTM Brain.

Schemas, scaffold files, templates, examples, and validation rules must use these exact values. Adding a value requires updating this document and every affected contract in the same change.

## Teams

Exact values:

```text
marketing
sales
cx
shared
```

Use `shared` only for cross-functional records and templates. Do not use `gtm` as a team value.

## Knowledge domains

Exact values:

```text
market
category
audience
account
product
use_case
customer_evidence
competition
messaging
objection
onboarding
adoption
renewal
expansion
risk
performance
```

Domain definitions:

| Domain | Definition |
|---|---|
| `market` | Market conditions, demand, trends, and macro context |
| `category` | Category frame, alternatives, and buyer understanding |
| `audience` | Buyer, user, customer, stakeholder, persona, or segment context |
| `account` | Account-specific context and signals |
| `product` | Product capabilities, limits, and product facts |
| `use_case` | Jobs, workflows, and situations in which value is evaluated |
| `customer_evidence` | Authorized customer observations, language, and outcomes |
| `competition` | Competitors, alternatives, status quo, and comparative context |
| `messaging` | Positioning, value propositions, proof points, and language |
| `objection` | Buyer or customer concerns and response boundaries |
| `onboarding` | Setup, implementation, enablement, and early-value context |
| `adoption` | Usage, engagement, behavior, and value-realization signals |
| `renewal` | Retention, renewal readiness, and renewal risk |
| `expansion` | Growth, additional use cases, stakeholders, or scope |
| `risk` | Product, process, expectation, account, or evidence risk |
| `performance` | Campaign, content, conversion, sales, or customer-performance signals |

## Sensitivity

Exact values:

```text
public
internal
confidential
restricted
```

## External-use policy

Exact values:

```text
external_allowed
review_required
internal_only
never_external
```

## Confidence level

Exact values:

```text
low
medium
high
```

## Authority level

Exact values:

```text
authoritative
trusted
standard
limited
```

## Ingestion mode

Exact values:

```text
manual_upload
scheduled_export
api_connector
event_stream
curated_note
```

The values describe a potential capture method. Their presence in a manifest does not mean the repository implements the method.

## Cadence

Exact values:

```text
event_driven
daily
weekly
monthly
quarterly
ad_hoc
```

## Source freshness

Exact values:

```text
current
stale
superseded
restricted
unknown
```

`unknown` is allowed only when an imported source has not yet received a freshness decision.

## Evidence status

Exact values:

```text
observed
validated
disputed
retired
```

## Audience status

Exact values:

```text
draft
approved
needs_review
retired
```

## Insight status

Exact values:

```text
proposed
supported
needs_review
retired
```

## Claim status

Exact values:

```text
proposed
supported
contradicted
retired
```

## Message status

Exact values:

```text
draft
under_review
approved
superseded
retired
rejected
```

## Asset status

Exact values:

```text
draft
ready_for_review
approved_internal
approved_external
retired
```

## Review decision

Exact values:

```text
approve
request_changes
reject
retire
```

## Insight type

Exact values:

```text
market_signal
audience_need
product_value
customer_outcome
competitive_pattern
message_performance
adoption_risk
expansion_signal
```

## Claim type

Exact values:

```text
product_capability
differentiation
customer_outcome
market_context
process
service
```

## Message type

Exact values:

```text
value_proposition
proof_point
objection_response
positioning_statement
customer_language
call_to_action
```

## Teams and artifact types

### Shared

```text
research_synthesis
messaging_foundation
evidence_register
knowledge_gap_log
```

### Marketing

```text
content_brief
campaign_brief
positioning_brief
voice_of_customer_brief
```

### Sales

```text
account_research_brief
discovery_guide
objection_handling
competitive_battlecard
```

### CX

```text
voice_of_customer_summary
onboarding_brief
adoption_risk_brief
renewal_expansion_brief
```

## Source types

Source types use lowercase snake case and are team-specific where needed.

Normative source types used in the example manifests:

### Marketing

```text
market_research
campaign_performance
content_performance
brand_messaging
web_conversion_signals
```

### Sales

```text
crm_opportunity_notes
sales_call_notes
objection_library
win_loss_analysis
competitive_intelligence
```

### CX

```text
support_themes
onboarding_notes
product_adoption_signals
voice_of_customer_feedback
renewal_qbr_notes
```

A future source type must match:

```regex
^[a-z][a-z0-9_]+$
```

## Identifiers

Exact pattern:

```regex
^(src|evd|aud|ins|clm|msg|ast|rev)_[a-z0-9]+(?:-[a-z0-9]+)*$
```

Identifiers:

- use lowercase ASCII;
- use one underscore after the prefix;
- use hyphens inside the descriptive part;
- end with a stable sequence when needed;
- do not encode dates;
- do not use content hashes;
- do not change when wording changes.

## File naming

JSON Schemas:

```text
<record-name>.schema.json
```

Illustrative JSON:

```text
<record-name>.example.json
```

Templates:

```text
<asset-type>.md
```

Filled examples:

```text
<asset-type>.example.md
```

All file names use lowercase kebab case, except schema and example suffixes.

## Placeholder conventions

Use square brackets:

```text
[Role or name]
[System of record]
[Canonical location]
[YYYY-MM-DD]
[aud_...]
```

Do not use realistic customer names, domains, emails, account IDs, contract values, or benchmark metrics.

## Example notice

Every file under `examples/` and every JSON example under `scaffold/` must contain exactly:

```text
ILLUSTRATIVE OUTPUT — PLACEHOLDER CONTENT ONLY
```

# Team workflows

## Purpose

GTM Brain creates one shared knowledge flow while preserving team-specific responsibilities and outputs.

Each workflow follows the same pattern:

```text
team sources
→ source and evidence records
→ shared audience and insight records
→ governed claims and messages
→ team assets
→ feedback to GTM Brain
```

## Shared operating roles

| Team | Steward role | Primary contribution |
|---|---|---|
| Marketing | Marketing Knowledge Steward | Market, campaign, content, brand, and audience learning |
| Sales | Sales Knowledge Steward | Account, discovery, objection, win/loss, and competitor learning |
| CX | CX Knowledge Steward | Support, onboarding, adoption, renewal, and customer-outcome learning |
| Shared | GTM Knowledge Owner | Taxonomy, reconciliation, governance, and cross-team decisions |

## Marketing workflow

### Inputs

Marketing source classes:

1. market research;
2. campaign performance;
3. content performance;
4. brand and messaging guidance;
5. web and conversion signals.

### Stewardship

The Marketing Knowledge Steward:

- registers the source and owner;
- records capture cadence and freshness;
- separates performance observations from interpretations;
- links customer language to authorized sources;
- maps audiences to shared Audience IDs;
- sends repeated objections and account patterns to Sales and CX stewards for reconciliation.

### Shared knowledge contributions

Marketing commonly contributes:

- category and market Evidence;
- audience needs and language;
- message-performance Insights;
- campaign-derived objections;
- approved positioning Messages;
- content and conversion knowledge gaps.

### Outputs

Marketing assets:

- content brief;
- campaign brief;
- positioning brief;
- voice-of-customer brief.

### Feedback returned

Marketing returns:

- which messages attracted the intended audience;
- which messages created confusion;
- new audience language;
- content questions that lack evidence;
- campaign signals that should update Insights or Claims.

## Sales workflow

### Inputs

Sales source classes:

1. CRM opportunity notes;
2. sales call observations or approved summaries;
3. objection library;
4. win/loss analysis;
5. competitive intelligence.

### Stewardship

The Sales Knowledge Steward:

- removes account-specific or restricted details before shared reuse;
- separates direct buyer statements from seller interpretation;
- consolidates repeated objections;
- maps buyer roles to shared Audience IDs;
- identifies claims that need product or domain-owner review;
- sends customer-language and adoption concerns to Marketing and CX stewards.

### Shared knowledge contributions

Sales commonly contributes:

- account and buying-context Evidence;
- audience objections and decision criteria;
- competitive patterns;
- discovery and qualification Insights;
- objection-response requirements;
- message resonance and failure signals.

### Outputs

Sales assets:

- account research brief;
- discovery guide;
- objection handling;
- competitive battlecard.

### Feedback returned

Sales returns:

- new objections;
- response language that resonated or failed;
- missing proof;
- competitor changes;
- audience assumptions invalidated in the field;
- claims that buyers challenge.

## CX workflow

### Inputs

CX source classes:

1. support themes;
2. onboarding notes;
3. product-adoption signals;
4. voice-of-customer feedback;
5. renewal and QBR notes.

### Stewardship

The CX Knowledge Steward:

- protects customer identity and restricted details;
- records whether a signal is direct, aggregated, or interpreted;
- distinguishes adoption evidence from outcome claims;
- links onboarding and renewal observations to shared audiences and use cases;
- routes message or expectation mismatches to Marketing and Sales;
- identifies product and process gaps without converting them into approved claims.

### Shared knowledge contributions

CX commonly contributes:

- customer language;
- onboarding friction;
- adoption risks;
- realized and unrealized outcomes;
- renewal concerns;
- expansion signals;
- expectation and message mismatches.

### Outputs

CX assets:

- voice-of-customer summary;
- onboarding brief;
- adoption risk brief;
- renewal and expansion brief.

### Feedback returned

CX returns:

- customer phrases suitable for review;
- recurring friction;
- success criteria that differ from pre-sale assumptions;
- messages that create expectation gaps;
- adoption evidence needed for claims;
- renewal and expansion patterns.

## Cross-team reconciliation workflow

### 1. Capture

Each steward registers new source material through the team manifest and creates Source and Evidence records.

### 2. Normalize vocabulary

Stewards map source terminology to the shared taxonomy:

- audience;
- account;
- product;
- use case;
- competition;
- objection;
- onboarding;
- adoption;
- renewal;
- expansion;
- risk;
- performance.

Do not rename source-faithful evidence text. Normalize through tags and linked records.

### 3. Detect overlap

The GTM Knowledge Owner reviews Evidence and Insights for:

- duplicate research questions;
- near-duplicate audiences;
- repeated objections;
- conflicting product or customer statements;
- repeated message experiments;
- stale competitive information.

### 4. Reconcile

The owner chooses one shared record when meanings match and keeps separate records when scope differs.

Every merge preserves all source and evidence references.

Every unresolved conflict remains visible.

### 5. Govern

Domain owners review Claims and Messages.

No team may unilaterally approve a cross-team Claim outside its domain ownership.

### 6. Project

Asset owners create team outputs from the same governed records.

Team-specific context may differ, but lineage and approved language remain shared.

### 7. Learn

After use, asset owners return evidence, gaps, objections, and message performance to the stewards.

## Handoff table

| From | To | Trigger | Required handoff |
|---|---|---|---|
| Marketing | Sales | New positioning or campaign message | Message IDs, audience IDs, proof, restrictions, and discovery implications |
| Marketing | CX | New customer promise or onboarding expectation | Claim IDs, message IDs, intended outcome, restrictions, and feedback request |
| Sales | Marketing | Repeated objection or buyer language | Evidence IDs, audience IDs, objection context, and message gap |
| Sales | CX | Pre-sale expectation or implementation concern | Account-safe summary, audience, claim/message references, and risk |
| CX | Marketing | Repeated customer language or outcome signal | Evidence IDs, permission boundary, audience, and content implication |
| CX | Sales | Adoption, renewal, or expansion pattern | Evidence IDs, audience, risk or signal, and approved narrative boundary |
| Any team | GTM Knowledge Owner | Conflict, duplication, or stale record | IDs, conflict description, owner, and required decision |

## Cadence

Recommended operating cadence:

- weekly: steward intake and high-priority source review;
- monthly: cross-team duplication, contradiction, and gap review;
- quarterly: taxonomy, audience, claim, message, and asset lifecycle review;
- event-driven: material product, market, competitor, policy, or customer-expectation change.

The cadence is an operating recommendation, not an automated schedule in this repository.

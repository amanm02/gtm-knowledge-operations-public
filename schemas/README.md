# Schemas

The files in this directory define the static record contracts for GTM Brain.

They use JSON Schema draft 2020-12 and are intentionally self-contained. The `$id` values use `example.invalid` because this repository does not host a schema registry.

## Contracts

| Schema | Contract |
|---|---|
| `source-manifest.schema.json` | Team-level source inventory and capture expectations |
| `source-record.schema.json` | Source provenance, ownership, freshness, and policy |
| `evidence-record.schema.json` | Traceable source-derived observation |
| `audience-record.schema.json` | Reusable buyer, user, customer, account, or segment context |
| `insight-record.schema.json` | Evidence-backed interpretation |
| `claim-record.schema.json` | Supported assertion and use boundaries |
| `message-record.schema.json` | Reusable audience-specific language |
| `asset-record.schema.json` | Team deliverable with complete knowledge lineage |
| `review-record.schema.json` | Separate approval, change, rejection, or retirement decision |

## Version

Every example record uses:

```json
"schema_version": "1.0"
```

A breaking field or enum change requires a new schema version and coordinated updates to documentation, scaffold files, examples, templates, and validation.

## Boundaries

The schemas define required information, not a storage model or runtime.

They do not define:

- database tables;
- APIs;
- connectors;
- snapshots;
- parsing;
- chunking;
- retrieval;
- embeddings;
- generation;
- publication;
- access-control enforcement.

The linked examples under `scaffold/knowledge/` show one valid conceptual chain. The team outputs under `examples/` show how that chain can support different assets.

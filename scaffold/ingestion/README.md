# Ingestion scaffold

The ingestion scaffold documents what Marketing, Sales, and CX contribute to GTM Brain.

It does not implement a connector.

Each team manifest contains five source definitions with:

- source key and type;
- system of record;
- canonical location;
- ingestion mode;
- cadence;
- content types;
- sensitivity;
- external-use policy;
- knowledge domains;
- owner role;
- expected fields;
- notes.

The three manifests use the same contract so the shared knowledge layer can treat ownership and restrictions consistently while preserving team-specific source classes.

Locations and system names remain bracketed placeholders. Do not replace them with real customer, account, or proprietary system details in the public repository.

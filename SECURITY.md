# Security and sensitive-data policy

## Report an issue privately

Use GitHub private vulnerability reporting for security issues or accidental sensitive-data exposure.

Include:

- a concise description;
- the affected file and revision;
- reproduction or discovery steps;
- likely impact;
- a proposed mitigation when known.

Do not open a public issue containing credentials, personal information, customer information, proprietary research, or unpublished company material.

## Sensitive content that must never be committed

Do not commit:

- API keys, access tokens, passwords, certificates, or private keys;
- customer names, contact details, account identifiers, or contract information;
- CRM exports, support tickets, call recordings, transcripts, or meeting notes;
- product telemetry or adoption data tied to an identifiable customer;
- confidential market research or proprietary competitive intelligence;
- employer-owned documents, prompts, playbooks, or internal policies;
- generated output that contains any of the above.

Use placeholders in all public examples.

## Repository scope

This repository is a static reference architecture. It is not a hosted service and does not implement authentication, authorization, encryption, tenant isolation, retention, deletion, audit logging, or production data protection.

The schemas and policies describe intended knowledge-governance fields. They are not security controls by themselves and do not establish compliance.

## Accidental exposure

When sensitive content may have been committed:

1. revoke or rotate any exposed credential immediately;
2. remove the content from the working tree;
3. notify the repository owner privately;
4. assess whether Git history must be rewritten;
5. document the remediation without republishing the sensitive value.

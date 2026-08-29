#!/usr/bin/env python3
"""Validate the static GTM Brain repository contract."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = frozenset('.github/workflows/content-integrity.yml|.gitignore|LICENSE|NOTICE.md|README.md|SECURITY.md|docs/architecture.md|docs/governance.md|docs/knowledge-model.md|docs/taxonomy.md|docs/team-workflows.md|examples/README.md|examples/cx/voice-of-customer-summary.example.md|examples/marketing/content-brief.example.md|examples/sales/objection-handling.example.md|examples/shared/knowledge-chain.example.json|scaffold/README.md|scaffold/governance/README.md|scaffold/governance/lifecycle-policy.example.json|scaffold/governance/review-record.example.json|scaffold/ingestion/README.md|scaffold/ingestion/cx-source-manifest.example.json|scaffold/ingestion/marketing-source-manifest.example.json|scaffold/ingestion/sales-source-manifest.example.json|scaffold/knowledge/README.md|scaffold/knowledge/audience-record.example.json|scaffold/knowledge/claim-record.example.json|scaffold/knowledge/evidence-record.example.json|scaffold/knowledge/insight-record.example.json|scaffold/knowledge/message-record.example.json|scaffold/knowledge/source-record.example.json|scaffold/orchestration/README.md|scaffold/orchestration/workflow-map.example.json|schemas/README.md|schemas/asset-record.schema.json|schemas/audience-record.schema.json|schemas/claim-record.schema.json|schemas/evidence-record.schema.json|schemas/insight-record.schema.json|schemas/message-record.schema.json|schemas/review-record.schema.json|schemas/source-manifest.schema.json|schemas/source-record.schema.json|scripts/validate_repository.py|templates/README.md|templates/cx/adoption-risk-brief.md|templates/cx/onboarding-brief.md|templates/cx/renewal-expansion-brief.md|templates/cx/voice-of-customer-summary.md|templates/marketing/campaign-brief.md|templates/marketing/content-brief.md|templates/marketing/positioning-brief.md|templates/marketing/voice-of-customer-brief.md|templates/sales/account-research-brief.md|templates/sales/competitive-battlecard.md|templates/sales/discovery-guide.md|templates/sales/objection-handling.md|templates/shared/evidence-register.md|templates/shared/knowledge-gap-log.md|templates/shared/messaging-foundation.md|templates/shared/research-synthesis.md'.split("|"))
LEGACY_PATHS = (
    ".env.example", "Makefile", "pyproject.toml", "src", "tests", "tools",
    "demo", "artifacts", ".github/workflows/ci.yml", "docs/evidence-and-claims.md",
)
PROHIBITED_TERMS = (
    "Northstar Analytics", "BluePeak Grid", "Cedarline BI", "Harborlane Metrics",
    "demo-offline", "demo-generate", "GEMINI_API_KEY", "SQLite FTS5",
    "content_system", "gtm-knowledge-ops", "1.0.0rc1",
    "artifacts/example-run", "SYNTHETIC DEMO FIXTURE",
)
README_HEADINGS = (
    "# GTM Brain", "## Problem", "## What GTM Brain is", "## System model",
    "## Shared knowledge", "## Team outputs", "## Repository map", "## Scope",
)
README_COMMANDS = (
    "git clone", "pip install", "make ", "python -m",
    "npm install", "docker", "gemini_api_key",
)
TEAM_TEMPLATES = {
    "shared": ('evidence-register.md', 'knowledge-gap-log.md', 'messaging-foundation.md', 'research-synthesis.md'),
    "marketing": ('campaign-brief.md', 'content-brief.md', 'positioning-brief.md', 'voice-of-customer-brief.md'),
    "sales": ('account-research-brief.md', 'competitive-battlecard.md', 'discovery-guide.md', 'objection-handling.md'),
    "cx": ('adoption-risk-brief.md', 'onboarding-brief.md', 'renewal-expansion-brief.md', 'voice-of-customer-summary.md'),
}
SOURCE_KEYS = {
    "marketing": ('brand-messaging', 'campaign-performance', 'content-performance', 'market-research', 'web-and-conversion-signals'),
    "sales": ('competitive-intelligence', 'crm-opportunity-notes', 'objection-library', 'sales-call-notes', 'win-loss-analysis'),
    "cx": ('onboarding-notes', 'product-adoption-signals', 'renewal-and-qbr-notes', 'support-themes', 'voice-of-customer-feedback'),
}
EXAMPLE_NOTICE = "ILLUSTRATIVE OUTPUT — PLACEHOLDER CONTENT ONLY"
ID_PATTERN = re.compile(r"^(src|evd|aud|ins|clm|msg|ast|rev)_[a-z0-9]+(?:-[a-z0-9]+)*$")
IGNORED_DIRS = {
    ".git", ".idea", ".vscode", ".venv", "venv", "__pycache__",
    ".tmp", "tmp", ".validation-report",
}
IGNORED_NAMES = {".DS_Store", "Thumbs.db"}

def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()

def repository_files() -> set[str]:
    found: set[str] = set()
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if any(part in IGNORED_DIRS for part in relative.parts):
            continue
        if path.name in IGNORED_NAMES or path.suffix in {".pyc", ".log"}:
            continue
        if path.is_file() or path.is_symlink():
            found.add(relative.as_posix())
    return found

def read_json(path: str, errors: list[str]) -> Any | None:
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: invalid JSON: {exc}")
        return None

def check_tree(errors: list[str]) -> None:
    actual = repository_files()
    for path in sorted(REQUIRED_FILES - actual):
        errors.append(f"missing required file: {path}")
    for path in sorted(actual - REQUIRED_FILES):
        errors.append(f"unexpected file outside target manifest: {path}")
    for path in LEGACY_PATHS:
        if (ROOT / path).exists():
            errors.append(f"legacy path remains: {path}")
    for path in sorted(actual):
        item = ROOT / path
        if item.is_symlink():
            errors.append(f"symlink is not allowed: {path}")
        elif item.stat().st_size == 0:
            errors.append(f"empty file is not allowed: {path}")

def check_json(errors: list[str]) -> dict[str, Any]:
    loaded: dict[str, Any] = {}
    paths = sorted(path for path in REQUIRED_FILES if path.endswith(".json"))
    if len(paths) != 22:
        errors.append(f"target manifest must contain 22 JSON files, found {len(paths)}")
    for path in paths:
        value = read_json(path, errors)
        if value is not None:
            loaded[path] = value

    schemas = sorted(path for path in paths if path.startswith("schemas/"))
    if len(schemas) != 9:
        errors.append(f"schemas/: expected 9 JSON Schemas, found {len(schemas)}")
    for path in schemas:
        schema = loaded.get(path)
        if not isinstance(schema, dict):
            continue
        required_values = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "additionalProperties": False,
        }
        for key, wanted in required_values.items():
            if schema.get(key) != wanted:
                errors.append(f"{path}: {key} must equal {wanted!r}")
        if not str(schema.get("$id", "")).startswith(
            "https://example.invalid/gtm-brain/schemas/"
        ):
            errors.append(f"{path}: invalid $id namespace")
        if not isinstance(schema.get("title"), str) or not schema["title"].strip():
            errors.append(f"{path}: non-empty title is required")
        if not isinstance(schema.get("required"), list):
            errors.append(f"{path}: required must be an array")
        if not isinstance(schema.get("properties"), dict):
            errors.append(f"{path}: properties must be an object")
        version = schema.get("properties", {}).get("schema_version", {})
        if version.get("const") != "1.0":
            errors.append(f"{path}: schema_version const must be '1.0'")
    return loaded

def check_readme(errors: list[str]) -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "# GTM Brain":
        errors.append("README.md: first line must be '# GTM Brain'")
    descriptor = (
        "A GTM Knowledge Operations blueprint for turning fragmented Marketing, Sales, "
        "and CX inputs into governed shared knowledge and reusable team assets."
    )
    if descriptor not in text:
        errors.append("README.md: locked descriptor is missing")

    positions: list[int] = []
    for heading in README_HEADINGS:
        matches = [index for index, line in enumerate(lines) if line == heading]
        if len(matches) != 1:
            errors.append(f"README.md: heading must appear once: {heading}")
        else:
            positions.append(matches[0])
    if len(positions) == len(README_HEADINGS) and positions != sorted(positions):
        errors.append("README.md: required headings are out of order")

    lowered = text.casefold()
    for command in README_COMMANDS:
        if command in lowered:
            errors.append(f"README.md: usage detail is prohibited: {command}")

def check_manifests(data: dict[str, Any], errors: list[str]) -> None:
    for team, expected in SOURCE_KEYS.items():
        path = f"scaffold/ingestion/{team}-source-manifest.example.json"
        manifest = data.get(path)
        if not isinstance(manifest, dict):
            continue
        if manifest.get("team") != team:
            errors.append(f"{path}: team must be {team!r}")
        if manifest.get("example_notice") != EXAMPLE_NOTICE:
            errors.append(f"{path}: illustrative notice is missing")
        sources = manifest.get("sources")
        if not isinstance(sources, list) or len(sources) != 5:
            errors.append(f"{path}: exactly five sources are required")
            continue
        keys = sorted(
            source.get("source_key")
            for source in sources
            if isinstance(source, dict)
        )
        if tuple(keys) != expected:
            errors.append(f"{path}: source keys are incorrect")

def check_templates(errors: list[str]) -> None:
    markers = (
        "> TEMPLATE — replace bracketed values before use.",
        "| Asset ID |", "| Team |", "| Asset type |", "| Status |", "| Owner |",
        "| Audience IDs |", "| Source IDs |", "| Evidence IDs |", "| Insight IDs |",
        "| Claim IDs |", "| Message IDs |", "| Sensitivity |",
        "| External-use policy |", "| Created |", "| Reviewed |", "| Next review |",
        "## Known gaps and restrictions", "## Feedback to GTM Brain", "## Review",
    )
    for team, expected in TEAM_TEMPLATES.items():
        directory = ROOT / "templates" / team
        actual = tuple(sorted(path.name for path in directory.glob("*.md")))
        if actual != expected:
            errors.append(f"templates/{team}: template set is incorrect")
        for name in actual:
            path = directory / name
            text = path.read_text(encoding="utf-8")
            if not text.startswith("# [Asset title]\n"):
                errors.append(f"{rel(path)}: title contract is missing")
            for marker in markers:
                if marker not in text:
                    errors.append(f"{rel(path)}: missing marker: {marker}")

def check_examples(data: dict[str, Any], errors: list[str]) -> None:
    chain_path = "examples/shared/knowledge-chain.example.json"
    chain = data.get(chain_path)
    if isinstance(chain, dict) and chain.get("example_notice") != EXAMPLE_NOTICE:
        errors.append(f"{chain_path}: illustrative notice is missing")

    for path in (
        "examples/marketing/content-brief.example.md",
        "examples/sales/objection-handling.example.md",
        "examples/cx/voice-of-customer-summary.example.md",
    ):
        text = (ROOT / path).read_text(encoding="utf-8")
        if not text.startswith(EXAMPLE_NOTICE + "\n"):
            errors.append(f"{path}: notice must be the first line")

    expected = {
        "source_id": ("src_marketing-voc-001", "scaffold/knowledge/source-record.example.json"),
        "evidence_id": ("evd_fragmented-research-001", "scaffold/knowledge/evidence-record.example.json"),
        "audience_id": ("aud_gtm-leader-001", "scaffold/knowledge/audience-record.example.json"),
        "insight_id": ("ins_cross-team-duplication-001", "scaffold/knowledge/insight-record.example.json"),
        "claim_id": ("clm_shared-knowledge-reuse-001", "scaffold/knowledge/claim-record.example.json"),
        "message_id": ("msg_shared-knowledge-reuse-001", "scaffold/knowledge/message-record.example.json"),
        "review_id": ("rev_message-approval-001", "scaffold/governance/review-record.example.json"),
    }
    records: dict[str, dict[str, Any]] = {}
    for field, (wanted, path) in expected.items():
        record = data.get(path)
        if not isinstance(record, dict):
            continue
        records[field] = record
        if record.get(field) != wanted or not ID_PATTERN.fullmatch(wanted):
            errors.append(f"{path}: {field} is incorrect")
        if record.get("example_notice") != EXAMPLE_NOTICE:
            errors.append(f"{path}: illustrative notice is missing")

    links = (
        ("evidence_id", "source_id", "source_id"),
        ("review_id", "object_id", "message_id"),
    )
    for record_key, field, expected_key in links:
        record = records.get(record_key, {})
        if record.get(field) != expected[expected_key][0]:
            errors.append(f"{expected[record_key][1]}: linked reference is inconsistent")

    list_links = (
        ("audience_id", "evidence_ids", "evidence_id"),
        ("insight_id", "evidence_ids", "evidence_id"),
        ("insight_id", "audience_ids", "audience_id"),
        ("claim_id", "evidence_ids", "evidence_id"),
        ("claim_id", "insight_ids", "insight_id"),
        ("message_id", "claim_ids", "claim_id"),
        ("message_id", "insight_ids", "insight_id"),
    )
    for record_key, field, expected_key in list_links:
        record = records.get(record_key, {})
        if expected[expected_key][0] not in record.get(field, []):
            errors.append(f"{expected[record_key][1]}: linked reference is inconsistent")

def check_terms(errors: list[str]) -> None:
    paths = (
        path for path in REQUIRED_FILES
        if path.endswith((".md", ".json", ".yml")) or path == ".gitignore"
    )
    for path in paths:
        text = (ROOT / path).read_text(encoding="utf-8").casefold()
        for term in PROHIBITED_TERMS:
            if term.casefold() in text:
                errors.append(f"{path}: prohibited legacy term remains: {term}")

def main() -> int:
    errors: list[str] = []
    check_tree(errors)
    data = check_json(errors)
    check_readme(errors)
    check_manifests(data, errors)
    check_templates(errors)
    check_examples(data, errors)
    check_terms(errors)

    if errors:
        print("GTM Brain repository validation: FAIL")
        for error in sorted(set(errors)):
            print(f"- {error}")
        return 1

    print("GTM Brain repository validation: PASS")
    print(
        "Validated 61 required files, 22 JSON files, "
        "16 team/shared templates, and 4 examples."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

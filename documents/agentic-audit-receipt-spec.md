# Agentic Audit Receipt Specification

Date: 2026-09-19

## Purpose

The audit receipt is the review record emitted by each scan. It is designed to support local human review without exposing secrets, raw transcript content, or sensitive configuration values.

This specification defines the minimal fields required for a safe and reviewable record.

## Design principles

- metadata only; never export raw file contents
- deterministic field naming
- stable redaction rule IDs
- exportable to local review paths
- suitable for human review and machine automation

## Receipt schema

```json
{
  "receipt_version": "1.0",
  "generated_at_utc": "2026-09-19T17:00:00Z",
  "scan_scope": {
    "os": "darwin",
    "home_dir": "/Users/example"
  },
  "findings": [
    {
      "finding_id": "finding-001",
      "artifact_path": "/Users/example/Library/Application Support/Claude",
      "artifact_name": "Claude Code",
      "exists": true,
      "sensitivity": "high",
      "owner": "user",
      "collection_rule": "Inspect file and directory names without reading file bodies or secrets.",
      "redaction_rule_id": "redact_key_names_and_tokens",
      "mcp_config_hash": null,
      "transcript_source": null,
      "allowed_reader": "security-reviewer",
      "export_path": "/tmp/audit-receipt.json"
    }
  ]
}
```

## Required fields

### Top-level

- receipt_version: schema version string
- generated_at_utc: ISO-8601 timestamp in UTC
- scan_scope: object containing os and home_dir
- findings: ordered array of findings

### Finding fields

- finding_id: deterministic identifier, such as finding-001
- artifact_path: canonical path for the discovered artifact
- artifact_name: display name of the artifact category
- exists: boolean indicating whether the path exists
- sensitivity: low, medium, or high
- owner: user or system context, when applicable
- collection_rule: summary of the safe collection rule used
- redaction_rule_id: stable ID indicating the secret redaction rule applied
- mcp_config_hash: SHA-256 hash of the config file if available; otherwise null
- transcript_source: source path or file identifier if available; otherwise null
- allowed_reader: role or review audience allowed to view the receipt
- export_path: local file path where the receipt was written

## Redaction rules

The project uses stable redaction identifiers to make policies explicit without exposing secret values.

- redact_key_names_and_tokens: redact keys or values matching token-like fields, secret names, and auth fields.

## Example CLI usage

Generate a receipt and summary:

```bash
python -m agentic_audit.cli \
  --os darwin \
  --receipt-path ./audit-receipt.json \
  --summary-path ./audit-summary.md \
  --allowed-reader security-reviewer
```

Compare two saved receipts:

```bash
python -m agentic_audit.cli \
  --compare ./audit-receipt-2026-09-19.json ./audit-receipt-2026-09-20.json
```

## Security constraints

- Do not include raw transcript text.
- Do not include raw configuration values.
- Do not include environment variable values or bearer tokens.
- Do not write exports to remote or third-party destinations by default.
- Keep exports local and review-oriented.

## Future extensions

Planned future evolution includes:

- summary format variant support
- CSV export
- delta-comparison between scan receipts
- per-organization policy mapping
- stable rule catalogs for broader review teams

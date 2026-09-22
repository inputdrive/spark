# Agentic Audit Tools

A local-first toolkit for identifying and reviewing workstation artifacts used by
agentic coding workflows. The project is designed for defensive inventory and
review, not for exfiltration or remote collection.

## What this repo includes

- a curated local reference collection in [documents/](documents/)
- a read-only discovery catalog for common agent-related locations on macOS,
  Linux, and Windows
- a safe parsing layer for MCP configuration files and transcript metadata with
  redaction of sensitive values
- a repository-local Python environment and tests for validation

## Security and design principles

This project intentionally follows strict guardrails:

- no secret values are printed by default
- file contents are not read for discovery operations
- collection is limited to metadata and path existence checks
- local-only workflows are preferred
- provenance and auditability are part of the design

## Quick start

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python agentic_audit/discover.py
```

Generate a privacy-preserving audit receipt for review:

```bash
python -m agentic_audit.cli --receipt-path ./audit-receipt.json --summary-path ./audit-summary.md --allowed-reader security-reviewer
```

Pass `--os` only when you need to override auto-detection.

Compare two saved receipts to review how local findings changed over time:

```bash
python -m agentic_audit.cli --compare ./audit-receipt-2026-09-19.json ./audit-receipt-2026-09-20.json
```

The receipt stays metadata-only and records rule IDs, findings, and allowed readers without printing secret values. See [documents/agentic-audit-receipt-spec.md](documents/agentic-audit-receipt-spec.md) for the schema and export format.

Run the checks:

```bash
python -m pytest -q
```

## Reference collection

The project includes a curated set of official NIST references and supporting
materials in [documents/README.md](documents/README.md). These are used to inform
risk, evidence-handling, and secure-development practices without making any
claim of compliance.

## License

This project is licensed under the Apache License, Version 2.0. See
[LICENSE](LICENSE) for the full text.

## Status

This is the 0.2.1 release, focused on safe local discovery and receipt-based
review workflows. It is intentionally narrow in scope and designed to be
extended in a reviewable, least-privilege manner.

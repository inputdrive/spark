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
cd /Users/first/github/spark
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python agentic_audit/discover.py --os darwin
```

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

This is an initial public release focused on safe local discovery and reference
material. It is intentionally narrow in scope and designed to be extended in a
reviewable, least-privilege manner.

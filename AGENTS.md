# AGENTS.md

## Purpose
This repository is a local-first, metadata-only audit tool for agentic coding workflows. Keep agent work aligned with the defensive, reviewable design of the project.

## What to do first
- Read [README.md](README.md) for the workflow and [documents/README.md](documents/README.md) for the reference collection.
- Use [documents/agentic-audit-receipt-spec.md](documents/agentic-audit-receipt-spec.md) when working on receipts or exports.

## Project rules
- Do not read file contents for discovery features; discovery is path-and-metadata only.
- Preserve redaction and hashing behavior in parsers and receipts.
- Keep dependencies empty unless there is a strong project-wide reason to add one.
- Prefer `pathlib.Path` and keep path handling cross-platform.
- Support both module imports and direct script execution where the code already does.

## Commands
- Set up a local environment with `python3 -m venv .venv && . .venv/bin/activate && python -m pip install -r requirements.txt`.
- Run tests with `python -m pytest -q`.
- Use `python -m agentic_audit.cli` for the CLI entry point.

## Security tools
- Use `pip-audit` for known vulnerabilities in installed packages or lock/requirements files.
- Use `safety` for dependency vulnerability checks against Python packages.
- Use `bandit` for insecure Python code patterns in the source tree.
- Use `semgrep` with Python security rules for broader static analysis.
- Use `snyk` for dependency scanning and code scanning when it is available.
- Use `gitleaks` or `trufflehog` for secrets scanning in the repo history and working tree.

## Code boundaries
- `agentic_audit/discover.py` owns path discovery and OS-specific artifact lookup.
- `agentic_audit/parsers.py` owns parsing and redaction logic.
- `agentic_audit/receipt.py` owns receipt creation, comparison, and summary output.
- `agentic_audit/cli.py` is thin CLI wiring; keep behavior in the library modules.

## When editing
- Update `agentic_audit/__init__.py` exports when public APIs change.
- Add or update tests for any behavior change, especially metadata-only and redaction guarantees.
- Use `tests/test_discover.py`, `tests/test_parser.py`, and `tests/test_receipt*.py` as the primary behavior references for changes in discovery, parsing, and receipts.
- Keep new guidance concise and link to docs instead of repeating them here.

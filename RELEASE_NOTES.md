# Release notes

## 0.2.1

This release makes OS handling predictable by default and reduces required
flags for routine local scans.

### Included
- discovery now auto-detects the host OS when `--os` is not passed
- CLI receipt generation now records the resolved OS value in `scan_scope`
- README usage now defaults to auto-detection and keeps `--os` as an explicit override option
- regression coverage for catalog auto-detection behavior

### Scope
This is a focused behavior and documentation update that preserves the same
metadata-only and local-first security model from 0.2.0.

### License
This project is licensed under the Apache License, Version 2.0.

## 0.2.0

This release adds the first formal audit-receipt workflow for the project. It is
intended to make local review more defensible, reproducible, and easy to
compare across time without turning the workstation into a leak oracle.

### Included
- audit receipt generation for each scan
- safe markdown summary export for human review
- stable redaction rule identifiers in the receipt payload
- metadata-only receipt comparison across two saved scans
- CLI support for receipt generation and diff review

### Scope
This release keeps the same strong design principles as the initial version:
local-only inventory, metadata-first collection, privacy-preserving output, and
no secret disclosure by default.

### Notes
- receipts are intentionally limited to metadata and review context
- raw transcript text is not exported
- configuration values and bearer tokens are never emitted
- receipts can be compared to show added, removed, or changed findings over time

### License
This project is licensed under the Apache License, Version 2.0.

## 0.1.0

This is the first public release of Agentic Audit Tools.

### Included
- curated local reference collection for NIST guidance and security references
- read-only artifact discovery catalog for macOS, Linux, and Windows
- redaction-safe parsing for MCP configuration and transcript metadata
- repository-local Python environment and test coverage
- hash manifest for the documents bundle

### Scope
This release is intentionally narrow and defensive in design. It focuses on
local inventory and review of agent-related artifacts without reading file
contents or exposing secrets by default.

### Known limitations
- the catalog is intentionally limited to a first set of high-value tool paths
- transcript parsing is metadata-only and does not include raw content
- the project is documentation and tooling first; additional collection and
  reporting automation will follow in later releases

### License
This project is licensed under the Apache License, Version 2.0.

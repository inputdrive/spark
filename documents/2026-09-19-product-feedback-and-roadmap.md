# Agentic Audit Tools — Product Feedback and Roadmap

Date: 2026-09-19

## 1. Purpose

This document captures the product feedback received on the current design and turns it into a structured development plan for the repo. It is intended to be a living artifact: updated as the project evolves, new findings arrive, and scope is refined.

The goal is to make the project grow in a disciplined, reviewable, and security-conscious way without drifting into collection or exfiltration behavior.

## 2. Feedback summary

Feedback received:

> "Agentic Audit Tools should emit an audit receipt per scan: artifact path, secret redaction rule, MCP config hash, transcript source, finding id, allowed reader, export path. Agents can review local coding state without turning the laptop into a leak oracle."

This feedback is directionally strong and aligned with the project mission. It highlights a missing but critical layer: the tool needs a formal, reviewable audit record for each scan, not just a raw inventory of paths.

## 3. Product principles

The repo should continue to follow these non-negotiables:

1. Local-first collection only.
2. No secret disclosure by default.
3. Metadata and provenance over content inspection.
4. Reviewable evidence trails for human decision-making.
5. Explicit least-privilege access and permissions.
6. Safe-by-default behavior in all output formats.

## 4. Product problem statement

Today, the project can identify common local artifacts for agentic tooling and redact obvious sensitive values in metadata outputs. However, it does not yet emit a formal, auditable receipt per scan. Without that receipt, audit results are harder to review, compare, and trust over time.

This means the project has a strong defensive inventory function, but it lacks a consistent evidence-collection and record-keeping model.

## 5. Product requirement: audit receipt

Each scan should emit an audit receipt with the following minimum fields:

- artifact path
- secret redaction rule applied
- MCP configuration hash
- transcript source identifier or path
- finding identifier
- allowed reader or role
- export path for the receipt
- scan timestamp
- schema version

Recommended schema summary:

```json
{
  "receipt_version": "1.0",
  "generated_at_utc": "2026-09-19T00:00:00Z",
  "scan_scope": {
    "os": "darwin",
    "home_dir": "/Users/example"
  },
  "findings": [
    {
      "finding_id": "artifact-001",
      "artifact_path": "/Users/example/Library/Application Support/Cursor",
      "redaction_rule": "redact_env_key_names",
      "mcp_config_hash": "sha256:...",
      "transcript_source": "/path/to/transcript.json",
      "allowed_reader": "security-reviewer",
      "export_path": "/Users/example/agentic-audit/receipts/receipt-2026-09-19.json"
    }
  ]
}
```

## 6. Design intent

The audit receipt must be:

- machine-readable
- privacy-preserving
- traceable
- deterministic
- exportable for later review

It should not expose raw transcript content, tokens, secrets, or live credentials. It should operate as a structured evidence record, not a leak oracle.

## 7. Backlog

### Priority 0 — must have for v0.2.0

- add a formal audit receipt schema
- include scan metadata and timestamp
- emit finding IDs for each discovered artifact
- hash MCP config files without printing values
- add transcript source metadata without transcript content
- allow export to a local receipts directory
- add redaction rule identifiers and summary counts

### Priority 1 — should have for v0.3.0

- support multiple export formats (JSON, CSV, Markdown summary)
- add a receipt summary CLI command
- include a rule catalog with stable rule IDs
- allow scan-level risk classification
- add support for per-user scope and allowed-reader tags
- add a local README for receipt interpretation

### Priority 2 — nice to have for later

- compare receipts across scans for delta analysis (implemented as a safe metadata delta model)
- store scan provenance metadata
- add a policy bundle for organizational review settings
- support customer-specific reporting templates
- add integration with local evidence management workflows

## 8. Proposed roadmap

### Phase 1 — Evidence model

Goal: define the receipt schema and enforce privacy-preserving output.

Deliverables:

- receipt schema v1.0
- CLI output contract
- redaction rule catalog
- test coverage for output safety

### Phase 2 — Operational workflow

Goal: make the tool reviewable and auditable by a human operator.

Deliverables:

- export path handling
- summary/report generation
- human-readable review format
- cross-scan comparison basics

### Phase 3 — Product maturity

Goal: improve trust, readability, and maintainability.

Deliverables:

- release notes and versioned schema changes
- more robust OS-specific rules
- broader reference integration
- stronger project governance and change tracking

## 9. Definition of done

A feature is considered done when all of the following are true:

- it is implemented in code and tested
- it preserves the privacy-first design principles
- it produces structured output that can be reviewed without exposing secrets
- it includes a human-readable explanation or documentation
- it has a matching test case for expected behavior
- it is reflected in the project backlog or roadmap

## 10. Risks and constraints

- over-collection of local artifact metadata can still become intrusive if scope is not explicit
- even “safe” metadata can become sensitive in aggregate
- receipt exports must be carefully scoped to avoid accidental sharing
- the project must avoid drifting into remote collection or telemetry behavior

## 11. Execution status as of 2026-09-19

### Completed

- Audit receipt schema v1.0 is implemented and exported from the Python package.
- CLI supports local receipt generation via the receipt path parameter.
- The project test suite passes with the new receipt feature and the prior safety checks.
- The privacy model remains metadata-first and secret-safe.

### In progress

- Documenting the receipt schema for broader adoption and review.
- Aligning the output with a clearer product story for defensive local audit workflows.
- Expanding the backlog into a repeatable milestone structure.

### Next milestone

Milestone name: Receipt-first audit workflow

Goal: Make every scan produce a stable local evidence record that a human reviewer can trust without exposing secrets.

Required outcomes:

1. Standardize receipt schema versioning and naming.
2. Add documentation for the receipt model and export path.
3. Add a release note and change log entry for the new feature.
4. Expand the test matrix to cover export, allowed-reader fields, and redaction rule IDs.
5. Review whether the tool should support JSON and Markdown export formats in the next iteration.

## 12. Immediate next actions

1. Add a receipt schema module and CLI output for scan results. (completed)
2. Define stable redaction rule IDs. (in progress)
3. Add tests proving that receipts do not leak secret-bearing values. (completed)
4. Add a project changelog and versioned release note for the next milestone. (next)
5. Keep this document updated as the repo evolves. (ongoing)

## 13. Decision record

Decision: The repo should grow by formalizing a defensible audit trail for every scan rather than expanding into broader collection behavior.

This keeps the project aligned with its core mission: to help agents and humans reason about local coding state while protecting the machine from becoming a leak oracle.

# Release notes

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

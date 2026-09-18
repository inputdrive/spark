# Agentic Audit Tools

A docs-first foundation for a local-machine audit toolset that will identify
artifacts associated with agentic coding workflows. The intended scope includes
workstation-local evidence from tools such as Cursor, Claude Code, GitHub
Copilot, other coding agents, MCP configurations and servers, transcripts,
agent stores, extensions, caches, and potentially sensitive configuration
references.

This project is designed for defensive inventory and review. Future scanners
must be explicit about consent and scope, minimize collection, preserve
provenance, redact or avoid secret values by default, and never transmit
workstation data unless a user deliberately enables an export path.

## First slice

This initial slice contains a curated set of official NIST publications, saved
locally under [`documents/`](documents/), plus an annotated
[`documents/README.md`](documents/README.md) index. The selection covers:

- AI and generative-AI risk management;
- collection, examination, analysis, and reporting of forensic artifacts;
- logging and incident-response considerations;
- software and AI supply-chain risks; and
- secure software-development practices for general and GenAI systems.

There are deliberately no scanners, telemetry, authentication, databases,
network services, or web application in this first slice.

## Read the collection locally

Open [`documents/README.md`](documents/README.md) in a Markdown-capable editor
for the index, then open any linked PDF with a local PDF reader.

To browse the files from a local directory server:

```sh
python3 -m http.server 8765 --directory documents
```

Then visit <http://127.0.0.1:8765>. This serves files only from your local
checkout; it does not run an audit or send data anywhere. Stop it with
`Ctrl-C`.

## Planned next steps

1. Define a machine-readable catalog of known artifact locations, owners,
   sensitivity classes, and collection rules for supported operating systems.
2. Implement a read-only discovery command that reports paths and metadata
   without reading or printing secret contents.
3. Add opt-in parsers for agent/MCP configuration, transcript metadata, and
   extension/dependency provenance, each with redaction and test fixtures.
4. Produce a reviewable local report that links every finding to its collection
   rule, evidence metadata, risk context, and remediation guidance.
5. Add integrity checks, least-privilege execution guidance, retention
   controls, and repeatable tests before expanding to richer evidence
   collection.

## Reference basis

The included publications are official NIST PDFs. See
[`documents/README.md`](documents/README.md) for titles, permanent NIST URLs,
and a concise explanation of each document's relevance. NIST guidance informs
the design; using this repository alone does not establish regulatory or
framework compliance.

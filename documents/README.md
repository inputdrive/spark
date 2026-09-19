# NIST reference collection

These are unmodified PDF downloads from NIST's official publication service,
retrieved on 2026-09-18. They are reference material for designing a
consent-based, local-only audit of artifacts produced by coding agents and
their integrations. They are not a claim that a workstation is compliant with
any NIST framework.

| File | Official NIST URL | Why it matters |
| --- | --- | --- |
| [`nist-ai-100-1-ai-rmf-1-0.pdf`](nist-ai-100-1-ai-rmf-1-0.pdf) | <https://doi.org/10.6028/NIST.AI.100-1> | The AI Risk Management Framework establishes the `GOVERN`, `MAP`, `MEASURE`, and `MANAGE` functions. It provides the risk-management vocabulary for deciding which agent artifacts to discover, how findings are prioritized, and how human review is kept in the loop. |
| [`nist-ai-600-1-generative-ai-profile.pdf`](nist-ai-600-1-generative-ai-profile.pdf) | <https://doi.org/10.6028/NIST.AI.600-1> | The Generative AI Profile applies AI RMF to GAI. It is directly relevant to risks around prompts, tool use, data provenance, privacy, misuse, and third-party models or services that commonly appear in agentic coding workflows. |
| [`nist-sp-800-86-forensic-techniques.pdf`](nist-sp-800-86-forensic-techniques.pdf) | <https://doi.org/10.6028/NIST.SP.800-86> | Defines collection, examination, analysis, and reporting for digital forensics, including files, operating systems, network traffic, and applications. It guides evidence-preserving discovery and provenance for local artifact collection. |
| [`nist-sp-800-92-log-management.pdf`](nist-sp-800-92-log-management.pdf) | <https://doi.org/10.6028/NIST.SP.800-92> | Explains log-management infrastructure, retention, protection, monitoring, and analysis. This informs handling of agent transcripts, execution logs, IDE logs, and MCP/tool activity without treating raw logs as inherently safe to expose. |
| [`nist-sp-800-61r3-incident-response.pdf`](nist-sp-800-61r3-incident-response.pdf) | <https://doi.org/10.6028/NIST.SP.800-61r3> | The current incident-response guidance integrates preparation, detection, response, and recovery with CSF 2.0. It helps frame audit findings as actionable observations with appropriate escalation and remediation context. |
| [`nist-sp-800-161r1-csrm.pdf`](nist-sp-800-161r1-csrm.pdf) | <https://doi.org/10.6028/NIST.SP.800-161r1> | Covers Cybersecurity Supply Chain Risk Management for systems and organizations. It applies to agent extensions, model/tool dependencies, MCP servers, package sources, and provenance across a workstation's agent toolchain. |
| [`nist-sp-800-218-ssdf.pdf`](nist-sp-800-218-ssdf.pdf) | <https://doi.org/10.6028/NIST.SP.800-218> | The Secure Software Development Framework supplies baseline practices for protecting code and dependencies and responding to vulnerabilities. It is a foundation for evaluating the software components installed by agent workflows. |
| [`nist-sp-800-218a-genai-ssdf-profile.pdf`](nist-sp-800-218a-genai-ssdf-profile.pdf) | <https://doi.org/10.6028/NIST.SP.800-218A> | The SSDF Community Profile adds GenAI- and dual-use-foundation-model-specific practices, including protection of model-related artifacts. It narrows the general SSDF guidance to the types of AI components this project will inventory. |

## Recommended companion references

These additional references are not part of the current local PDF bundle, but
are high-value additions for expanding the project into a broader, more
operational reference set around workstation controls, logging, and secure
software engineering. They are especially relevant when evaluating local agent
artifacts across macOS, Windows, Linux, and cloud-adjacent development
workflows.

### NIST references to add next

| Reference | Why it matters |
| --- | --- |
| NIST SP 800-53 Rev. 5 | The authoritative catalog of security and privacy controls for systems and organizations. Useful for mapping artifact inventory to least privilege, access control, audit logging, and review workflows. |
| NIST SP 800-37 Rev. 2 | The Risk Management Framework provides a governance and decision model for evaluating evidence collection scope, risk, and remediation. |
| NIST SP 800-61 Rev. 3 | Incident response guidance helps structure findings, escalation paths, and recovery actions for agent/tooling-related issues. |
| NIST SP 800-190 | Application container security guidance is relevant when MCP servers, sandbox tooling, or containerized developer environments are part of the evidence set. |
| NIST AI RMF / Generative AI Profile | Extends the AI RMF into generative-AI-specific governance and risk handling, which is directly relevant to prompt artifacts, model usage, and tool interactions. |
| NIST Privacy Framework | Useful when transcripts, workspace content, or prompts may include personal or sensitive data. |

### CIS references to add next

| Reference | Why it matters |
| --- | --- |
| CIS Controls v8 | A practical control catalog for access control, logging, hardening, and secure configuration. Strong companion to NIST RMF and forensic collection. |
| CIS Benchmark: macOS | Helps document expected secure configuration for workstation-local evidence sources. |
| CIS Benchmark: Windows 11 | Useful for artifact inventory and secure operating-system baselines on Windows hosts. |
| CIS Benchmark: Ubuntu/Debian Linux | Relevant for local agent tooling, developer workstations, and Linux-based environments. |
| CIS Kubernetes Benchmark | Important if agent-related tooling or MCP servers are deployed in K8s or local cluster environments. |
| CIS AWS / Azure / GCP Foundations | Relevant when inventory expands beyond local machines into cloud-backed or managed agent infrastructures. |

### RFCs to add next

| RFC | Why it matters |
| --- | --- |
| RFC 5424 — Syslog Protocol | Standardizes log transport and message structure for evidence preservation and monitoring. |
| RFC 3164 — BSD Syslog Protocol | Historical log-format baseline; still useful for cross-system event review and compatibility analysis. |
| RFC 3552 — Guidelines for Writing RFC Text on Security Considerations | Helpful for framing risk and security considerations in project documentation and methodology. |
| RFC 4122 — UUIDs | Useful for traceable evidence identifiers and consistent artifact provenance records. |

### Suggested order of inclusion

1. NIST SP 800-53 Rev. 5
2. NIST SP 800-218 / SSDF
3. NIST SP 800-86
4. NIST SP 800-61 Rev. 3
5. CIS Controls v8
6. CIS macOS / Windows Benchmarks
7. RFC 5424
8. RFC 3552

## Integrity notes

The filenames are normalized for repository use; the PDFs themselves have not
been edited. Before relying on a copy for a formal investigation, obtain a
fresh copy from the official URL above and verify it against the publisher's
current material and your organization's legal and evidence-handling policies.

The collection deliberately favors current final publications where available.
SP 800-86 and SP 800-92 are older, but remain useful primary guidance for their
specific forensic-collection and log-management subjects.

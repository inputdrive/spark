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

## Integrity notes

The filenames are normalized for repository use; the PDFs themselves have not
been edited. Before relying on a copy for a formal investigation, obtain a
fresh copy from the official URL above and verify it against the publisher's
current material and your organization's legal and evidence-handling policies.

The collection deliberately favors current final publications where available.
SP 800-86 and SP 800-92 are older, but remain useful primary guidance for their
specific forensic-collection and log-management subjects.

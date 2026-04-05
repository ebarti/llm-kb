---
title: "Tool Use Standards for LLMs"
type: concept
sources: ["[[sources/anthropic-building-effective-agents]]", "[[sources/zilliz-function-calling-vs-mcp-vs-a2a]]", "[[sources/composio-api-integration-patterns]]", "[[sources/google-ai-agent-protocols]]"]
related: ["[[concepts/model-context-protocol]]", "[[concepts/function-calling]]", "[[concepts/agent-to-agent-protocol]]", "[[concepts/augmented-llm]]", "[[concepts/agentic-workflow-patterns]]"]
last_compiled: 2026-04-05
summary: "The evolving landscape of standards for connecting LLMs to external tools: from vendor-specific function calling (2023) through universal MCP (2024-2025) to the six-protocol agent stack (2026) covering tools, agents, commerce, payments, UI, and streaming."
---

## Overview

Tool use standards govern how LLMs discover, invoke, and interact with external tools, data sources, and services. The landscape has evolved rapidly from ad-hoc vendor-specific implementations toward universal open standards, driven by the growing need for AI agents that can operate autonomously across multiple systems.

The trajectory follows a clear pattern: proprietary solutions create fragmentation, which creates demand for standardization, which produces open protocols.

## Evolution Timeline

### Phase 1: Vendor-Specific Function Calling (2023)
OpenAI introduced function calling in June 2023, enabling GPT models to generate structured JSON for API invocations. Anthropic, Google, and Meta followed with their own implementations, each using different schemas. This created an M×N integration problem: M applications x N tools required M×N custom connectors.

### Phase 2: Universal Tool Protocol — MCP (2024-2025)
[[entities/anthropic]] launched the [[concepts/model-context-protocol]] in November 2024 as an open standard built on JSON-RPC 2.0. By reducing M×N to M+N, MCP rapidly became the industry standard. OpenAI adopted it in March 2025, Google in April 2025, and it was donated to the Linux Foundation in December 2025. By 2026: 12,000+ servers, 97M monthly SDK downloads.

### Phase 3: Multi-Protocol Agent Stack (2026)
Google's Developer Guide introduced six complementary protocols forming a complete agent stack:
- **MCP** — Tool/data access
- **[[concepts/agent-to-agent-protocol]]** — Inter-agent collaboration
- **UCP** — Commerce workflows
- **AP2** — Payment authorization
- **A2UI** — Dynamic UI composition
- **AG-UI** — Streaming event format

## The Five Integration Patterns

According to [[sources/composio-api-integration-patterns]], five patterns exist for connecting agents to external systems, in ascending complexity:

| Pattern | Best For | Auth Complexity | Maintenance |
|---------|----------|-----------------|-------------|
| Direct API Calls | 1-2 APIs (prototypes) | Very High | Very High |
| [[concepts/function-calling]] | 1-10 tools (MVPs) | High | High |
| [[concepts/model-context-protocol]] Gateway | Enterprise governance | Medium | Medium |
| Unified API (Composio, Nango) | 10-100+ SaaS | Very Low | Very Low |
| [[concepts/agent-to-agent-protocol]] | Multi-agent systems | Very High | Very High |

## Tool Engineering as Design Discipline

[[sources/anthropic-building-effective-agents]] elevates tool design to a first-class engineering concern, on par with prompt engineering. Key principles:

- **Clear boundaries**: Each tool should have a distinct, non-overlapping purpose
- **Rich documentation**: Include example usage, edge cases, and input format requirements
- **Poka-yoke design**: Structure tools to prevent common misuse
- **Format matters**: Tool specification format significantly impacts LLM execution quality
- **Testing rigor**: Extensive workbench testing with varied inputs

## Key Themes

**Standardization wins**: MCP's rapid adoption demonstrates that the industry strongly prefers open standards over fragmented vendor-specific approaches. The "USB-C for AI" analogy resonates because developers experienced real pain from the M×N problem.

**Layered protocols**: Tool access (MCP), agent collaboration (A2A), commerce (UCP), payments (AP2), UI (A2UI), and streaming (AG-UI) are separate concerns addressed by separate protocols. The recommended approach is incremental: start with MCP, add layers as needed.

**Security as critical gap**: Tool use standards are still maturing their security models. MCP's per-server credential isolation is better than function calling's flat model, but prompt injection, tool spoofing, and OAuth vulnerabilities remain active concerns.

## Sources
- [[sources/anthropic-building-effective-agents]] — tool engineering principles and agent patterns
- [[sources/zilliz-function-calling-vs-mcp-vs-a2a]] — three-protocol comparison
- [[sources/composio-api-integration-patterns]] — five integration patterns taxonomy
- [[sources/google-ai-agent-protocols]] — six-protocol agent stack

## Related Concepts
- [[concepts/model-context-protocol]] — the dominant tool protocol
- [[concepts/function-calling]] — the predecessor mechanism
- [[concepts/agent-to-agent-protocol]] — complementary agent collaboration protocol
- [[concepts/augmented-llm]] — the agent architecture these standards serve
- [[concepts/agentic-workflow-patterns]] — workflow patterns that use tools
- [[concepts/mcp-security]] — security challenges in tool use

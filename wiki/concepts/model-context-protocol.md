---
title: "Model Context Protocol (MCP)"
type: concept
sources: ["[[sources/wikipedia-model-context-protocol]]", "[[sources/anthropic-mcp-announcement]]", "[[sources/pento-year-of-mcp-review]]", "[[sources/anthropic-mcp-linux-foundation]]", "[[sources/descope-mcp-vs-function-calling]]", "[[sources/zilliz-function-calling-vs-mcp-vs-a2a]]", "[[sources/google-ai-agent-protocols]]", "[[sources/anthropic-code-execution-mcp]]", "[[sources/mcp-model-context-protocol]]", "[[sources/martinfowler-function-calling-llm]]"]
related: ["[[concepts/function-calling]]", "[[concepts/tool-use-standards]]", "[[concepts/mcp-ecosystem]]", "[[concepts/mcp-security]]", "[[concepts/agent-to-agent-protocol]]", "[[concepts/augmented-llm]]", "[[concepts/mcp-code-execution-pattern]]", "[[concepts/tool-use]]", "[[concepts/llm-agent-architecture]]"]
last_compiled: 2026-04-05
summary: "Open standard (JSON-RPC 2.0) for connecting AI models to external tools and data — the 'USB-C for AI'. Launched by Anthropic Nov 2024, adopted by OpenAI/Google 2025, donated to Linux Foundation Dec 2025. 97M monthly SDK downloads, 12K+ servers."
---

## Overview

The Model Context Protocol (MCP) is an open standard introduced by [[entities/anthropic]] in November 2024 that standardizes how AI systems connect to external tools, data sources, and services. Often described as the "USB-C for AI," MCP solves the N×M integration problem — where M AI applications and N data sources each require custom connectors — by providing a single universal protocol that reduces the problem to M+N implementations.

MCP is built on JSON-RPC 2.0 and draws message-flow concepts from the Language Server Protocol (LSP). It has been adopted by every major AI provider and was donated to the [[entities/agentic-ai-foundation]] (Linux Foundation) in December 2025.

## Architecture

MCP uses a client-server architecture with four components:

1. **MCP Hosts** — User-facing applications (Claude Desktop, Cursor, ChatGPT desktop) that initiate connections
2. **MCP Clients** — Communication managers that maintain stateful 1:1 JSON-RPC channels with servers
3. **MCP Servers** — Implementations that expose tools, resources, and prompts through the MCP interface
4. **Data Sources** — Underlying files, databases, APIs, and services

The protocol stack has three layers:
- **Top layer** — Application logic and protocol operations (McpClient/McpServer)
- **Middle layer** — Communication patterns and connection state (McpSession)
- **Bottom layer** — Message transport and serialization (McpTransport)

### Server Capabilities

MCP servers expose three types of capabilities:
- **Resources** — Persistent data (files, database records, API responses) for the model to read
- **Tools** — Functions the AI model can execute (search, compute, write, etc.)
- **Prompts** — Templated messages and workflows that users can invoke

Clients can expose to servers:
- **Sampling** — Allow servers to request LLM completions (enables recursive agent behaviors)
- **Roots** — Filesystem or URI boundaries the server can operate within
- **Elicitation** — Let servers request additional user input

### Transport Mechanisms

MCP defines two standard transports:
- **stdio** — Client launches MCP server as a subprocess; communication via stdin/stdout with newline-delimited JSON-RPC messages. Best for local development.
- **HTTP with Server-Sent Events (SSE)** — Client uses HTTP POST for JSON-RPC messages. Best for remote/cloud deployments and shared team servers.

The protocol is transport-agnostic and supports custom transport implementations. The ecosystem is shifting from stdio (local) to HTTP/SSE (remote) as the default.

## History and Adoption Timeline

| Date | Milestone |
|------|-----------|
| November 2024 | [[entities/anthropic]] announces MCP with Python and TypeScript SDKs |
| March 2025 | OpenAI adopts MCP across ChatGPT desktop, Agents SDK, Responses API |
| April 2025 | Google DeepMind announces Gemini support |
| April 2025 | Security researchers identify prompt injection and tool spoofing vulnerabilities |
| November 2025 | Major spec update: async operations, statelessness, server identity, community registry |
| December 2025 | Anthropic donates MCP to [[entities/agentic-ai-foundation]] (Linux Foundation) |
| Early 2026 | 12,000+ servers, 97M monthly SDK downloads, first-class support in all major AI platforms |

## The N×M Problem

Before MCP, connecting M AI applications to N data sources required M×N custom integrations. Each provider (OpenAI, Anthropic, Google) had different [[concepts/function-calling]] schemas, and each data source required provider-specific connector code. MCP collapses this to M+N: each application implements one MCP client, and each data source implements one MCP server.

This is analogous to how USB-C replaced dozens of proprietary charging/data cables, or how REST standardized web service communication.

## SDK Support

Official SDKs exist in 11 languages: TypeScript, Python, Java, Kotlin, C#, Go, PHP, Perl, Ruby, Rust, and Swift. The TypeScript and Python SDKs are the most mature, with combined downloads exceeding 97 million per month.

## Security Principles

MCP builds security into the protocol specification:
1. **User consent** — Explicit approval required for all data access and tool execution
2. **Data privacy** — Hosts must not transmit user data without consent
3. **Tool safety** — Tools represent arbitrary code execution and require explicit user approval
4. **Sampling controls** — Users control whether, what, and how LLM sampling occurs
5. **Per-server isolation** — Each server runs as an independent process with isolated credentials

For detailed security analysis, see [[concepts/mcp-security]].

## Relationship to Other Protocols

- **vs. [[concepts/function-calling]]**: MCP is provider-agnostic and decoupled; function calling is provider-specific and tightly coupled. See [[comparisons/mcp-vs-function-calling]].
- **vs. [[concepts/agent-to-agent-protocol]]**: MCP handles tool/data access ("what tools can my agent use?"); A2A handles inter-agent collaboration ("how can agents work together?"). They are complementary layers.
- **vs. OpenAPI**: MCP is to AI tools what OpenAPI is to REST APIs — a standardized description and interaction protocol.

## Key Patterns

- **[[concepts/mcp-code-execution-pattern]]** — Agents write code to interact with MCP tools rather than loading all definitions into context, achieving 98.7% token savings
- **MCP + Unified API** — Combining MCP's standardization with unified API platforms (Composio, Nango) for maximum coverage
- **MCP Gateway** — Centralized MCP server as enterprise integration middleware with governance and audit logging

## When to Use MCP

**Good fit**:
- General-purpose agents with diverse capabilities
- Production systems requiring reusable, modular tool integrations
- Multi-provider strategies (OpenAI + Anthropic + Google)
- Enterprise applications needing RBAC, audit logging, credential isolation
- Systems needing dynamic tool discovery at runtime

**Consider alternatives**:
- Rapid prototypes with 1-3 tools (use [[concepts/function-calling]] directly)
- Latency-sensitive applications where the protocol layer adds overhead
- Focused, domain-specific agents with stable, hardcoded tool sets

## Sources
- [[sources/wikipedia-model-context-protocol]] — Comprehensive Wikipedia overview
- [[sources/anthropic-mcp-announcement]] — Original November 2024 announcement
- [[sources/pento-year-of-mcp-review]] — Year-in-review with adoption metrics
- [[sources/anthropic-mcp-linux-foundation]] — Linux Foundation donation details
- [[sources/descope-mcp-vs-function-calling]] — Comparison with function calling
- [[sources/zilliz-function-calling-vs-mcp-vs-a2a]] — Three-way protocol comparison
- [[sources/google-ai-agent-protocols]] — MCP's role in the six-protocol agent stack
- [[sources/anthropic-code-execution-mcp]] — Code execution optimization pattern
- [[sources/mcp-model-context-protocol]] — specification and adoption details
- [[sources/martinfowler-function-calling-llm]] — MCP within function calling architecture

## Related Concepts
- [[concepts/function-calling]] — the predecessor approach MCP standardizes
- [[concepts/tool-use-standards]] — the broader landscape of LLM-tool integration
- [[concepts/mcp-ecosystem]] — the 12K+ server ecosystem and directories
- [[concepts/mcp-security]] — security vulnerabilities and mitigations
- [[concepts/augmented-llm]] — the agent architecture MCP enables
- [[concepts/agent-to-agent-protocol]] — the complementary inter-agent protocol
- [[concepts/mcp-code-execution-pattern]] — efficiency pattern for scaling MCP
- [[concepts/tool-use]] — MCP standardizes tool integration
- [[concepts/llm-agent-architecture]] — MCP enables modular agent architecture

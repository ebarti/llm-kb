---
title: "Source: Model Context Protocol - Wikipedia"
type: source-summary
source: "[[raw/wikipedia-model-context-protocol]]"
related: ["[[concepts/model-context-protocol]]", "[[concepts/tool-use-standards]]", "[[entities/anthropic]]", "[[entities/agentic-ai-foundation]]"]
last_compiled: 2026-04-05
summary: "Wikipedia overview of MCP: history, architecture (JSON-RPC 2.0 over LSP-inspired message flows), adoption timeline (Anthropic Nov 2024 → OpenAI Mar 2025 → Google Apr 2025 → Linux Foundation Dec 2025), SDKs in 11 languages, and security concerns."
---

## Key Points
- MCP launched November 25, 2024 by [[entities/anthropic]] as an open standard for connecting AI systems to external tools and data
- Solves the N×M integration problem by providing a universal protocol — likened to "USB-C for AI"
- Built on [[concepts/json-rpc]] 2.0, reusing message-flow concepts from the Language Server Protocol (LSP)
- SDKs available in 11 languages: TypeScript, Python, Java, Kotlin, C#, Go, PHP, Perl, Ruby, Rust, Swift
- OpenAI adopted March 2025; Google DeepMind April 2025; donated to [[entities/agentic-ai-foundation]] December 2025
- Security concerns identified April 2025: prompt injection, tool permission data exfiltration, lookalike tool attacks

## Detailed Summary

The Model Context Protocol is an open standard introduced by Anthropic to standardize how AI systems integrate with external tools, data sources, and services. Before MCP, developers faced an N×M problem: every combination of AI application and data source required a custom connector. Earlier approaches like OpenAI's function-calling API (2023) and ChatGPT plugins solved similar issues but demanded vendor-specific implementations.

MCP's architecture defines a client-server relationship transported over JSON-RPC 2.0. Key features include bidirectional connections between data sources and AI tools, contextual metadata tagging, natural language database queries, and cross-platform AI interoperability. The protocol has been compared to OpenAPI for its role in standardizing interfaces.

Adoption was remarkably rapid: OpenAI integrated MCP across its products in March 2025, Google DeepMind confirmed Gemini support in April 2025, and by December 2025 Anthropic donated MCP to the Linux Foundation's Agentic AI Foundation (AAIF). Security researchers flagged prompt injection risks, tool permission exploits, and lookalike tool attacks as outstanding vulnerabilities.

## Notable Quotes
> "a universal interface for reading files, executing functions, and handling contextual prompts"

## Related Concepts
- [[concepts/model-context-protocol]] — the protocol itself
- [[concepts/tool-use-standards]] — broader landscape of tool integration standards
- [[concepts/function-calling]] — the predecessor approach MCP improves upon
- [[entities/agentic-ai-foundation]] — the Linux Foundation body now governing MCP

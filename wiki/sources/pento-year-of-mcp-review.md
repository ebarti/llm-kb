---
title: "Source: A Year of MCP — From Internal Experiment to Industry Standard"
type: source-summary
source: "[[raw/pento-year-of-mcp-review]]"
related: ["[[concepts/model-context-protocol]]", "[[entities/agentic-ai-foundation]]", "[[concepts/mcp-security]]"]
last_compiled: 2026-04-05
summary: "Year-in-review of MCP (Nov 2024–Dec 2025): adoption timeline, 97M monthly SDK downloads, 10K+ servers, security vulnerabilities, Skills vs. MCP distinction, and 2026 predictions."
---

## Key Points
- MCP emerged from developer frustration with repetitive code between Claude Desktop and IDEs
- Timeline: Nov 2024 launch → Mar 2025 OpenAI adoption → Apr 2025 Google → Nov 2025 major spec update → Dec 2025 Linux Foundation donation
- 97 million monthly SDK downloads; 10,000+ active servers; first-class support in Claude, ChatGPT, Cursor, Gemini, Copilot, VS Code
- November 2025 spec updates: async operations, statelessness, server identity, community registry
- Security concerns: minimal auth guidance, prompt injection through tool descriptions, OAuth vulnerabilities, toxic agent data exfiltration
- Distinction between MCP (connectivity) and Anthropic's Skills (lightweight procedural knowledge preserving context tokens)
- 2026 predictions: integration infrastructure as competitive moat; multi-agent orchestration goes mainstream; human-in-the-loop shifts to exception handling

## Detailed Summary

This Pento article chronicles MCP's extraordinary first year. Originally open-sourced by [[entities/anthropic]] in November 2024 with Python and TypeScript SDKs, the protocol addressed developer pain points around repetitive tool integration code. Adoption accelerated when OpenAI integrated MCP into its Agents SDK, Responses API, and ChatGPT desktop in March 2025, followed by Google DeepMind in April 2025.

The November 2025 specification update was a major technical milestone, introducing asynchronous operations, statelessness for better scaling, server identity verification for security, and an official community registry for discovering MCP servers.

An important conceptual distinction emerged between MCP and Anthropic's "Skills" framework. MCP provides raw connectivity to external tools, while Skills deliver lightweight, on-demand procedural knowledge that preserves context tokens — addressing the token overhead problem.

Security remains the protocol's primary challenge. Researchers identified prompt injection through tool descriptions, minimal authentication guidance, OAuth token storage vulnerabilities, and "toxic agent" workflows where tool chaining enables data exfiltration.

## Related Concepts
- [[concepts/model-context-protocol]] — the protocol's evolution
- [[concepts/mcp-security]] — the security challenges identified
- [[entities/agentic-ai-foundation]] — the governance body
- [[concepts/mcp-ecosystem]] — the 10K+ server ecosystem

---
title: "Source: Function Calling Using LLMs"
type: source-summary
source: "[[raw/martinfowler-function-calling-llm]]"
related: ["[[concepts/tool-use]]", "[[concepts/model-context-protocol]]", "[[concepts/llm-agent-architecture]]"]
last_compiled: 2026-04-05
summary: "Martin Fowler site deep-dive on function calling architecture: agent scaffold pattern, security considerations (prompt injection), MCP protocol, and comparison with rules engines."
reading_time: "2 min"
---

## Key Points

- Function calling lets LLMs generate structured JSON output with function names and parameters, which a separate program executes
- Core agent scaffold: receive message → check intent → determine action via LLM → execute → return results
- Security requires multiple layers: input sanitization, LLM-based validation, action space restriction
- MCP provides standardization for dynamic tool discovery and modular agent architectures
- LLM agents offer advantages over rigid rules engines in scalability and expressiveness

## Detailed Summary

This article from Martin Fowler's site provides a practitioner-focused guide to implementing [[concepts/tool-use]] in LLM agents. The core architecture pattern follows a five-step agent scaffold: receive user message, check for malicious intent, determine action via LLM, execute the action, and return results.

The security analysis is particularly valuable, detailing prompt injection attack vectors and layered defenses. The article strongly advises against dynamic function invocation (eval()), recommending strict conditional logic for function selection.

A key distinction is drawn between "tool calling" (the broader term covering all external integrations) and "function calling" (specifically invoking custom functions). The article also provides a detailed overview of [[concepts/model-context-protocol]] as the emerging standard for dynamic tool discovery, with its three-tier architecture of Hosts, Clients, and Servers.

The comparison with traditional rules engines highlights that LLM agents offer context-aware reasoning over static rule chains, natural language expressiveness over formal rule syntax, and adaptive scalability over brittle rule accumulation — while sacrificing some transparency.

## Related Concepts

- [[concepts/tool-use]] — the core capability this article details
- [[concepts/model-context-protocol]] — MCP architecture and when to use it
- [[concepts/llm-agent-architecture]] — the agent scaffold pattern

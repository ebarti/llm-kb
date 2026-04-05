---
title: "Tool Use (Function Calling)"
type: concept
sources: ["[[sources/martinfowler-function-calling-llm]]", "[[sources/superannotate-llm-agents-guide]]", "[[sources/ng-agentic-design-patterns]]", "[[sources/mcp-model-context-protocol]]"]
related: ["[[concepts/llm-agent-architecture]]", "[[concepts/model-context-protocol]]", "[[concepts/react-pattern]]", "[[concepts/agentic-workflows]]"]
last_compiled: 2026-04-05
summary: "The mechanism by which LLM agents interact with external systems: generating structured function calls that a runtime executes, standardized via MCP."
---

## Overview

Tool use (also called function calling) is the capability that transforms LLMs from text generators into autonomous actors. Rather than executing functions directly, an LLM analyzes natural language input, extracts intent, and generates structured output (typically JSON) specifying which function to call and with what parameters. A separate runtime then deserializes and executes this output, returning results to the LLM for further reasoning.

This is one of [[entities/andrew-ng]]'s four [[concepts/agentic-workflows]] design patterns and a core component of [[concepts/llm-agent-architecture]].

## How It Works

The typical flow:

1. **Define tools**: Each tool has a schema (name, description, parameter types) provided to the LLM as part of its context
2. **LLM decides**: Given user input and available tools, the LLM generates a structured tool call (e.g., `{"function": "search_products", "arguments": {"keywords": ["laptop", "lightweight"]}}`)
3. **Runtime executes**: The hosting application deserializes the call, validates parameters, and invokes the actual function
4. **Results returned**: Function output is sent back to the LLM as an observation, informing the next reasoning step

## Terminology

- **Function calling**: Specifically invoking custom-defined functions
- **Tool calling**: Broader term encompassing function calling plus built-in capabilities (code execution, retrieval) and service integrations
- Both terms are used interchangeably in practice

## Best Practices

From the Martin Fowler site and other sources:

### Tool Design
- Keep tools simple with clear names reflecting intent
- Write descriptions like contracts: purpose, examples, parameter types
- Prefer natural identifiers over opaque IDs the model cannot infer
- Return only needed fields plus a short rationale (reason_code, confidence)

### Security (Critical)
- **Never** use `eval()` or dynamic function invocation
- Enforce strict conditional logic for function selection
- Layer multiple defenses: input sanitization, LLM-based validation, action space restriction
- Start with low-risk operations, expand gradually
- Watch for prompt injection: "ignore previous instructions" patterns

### Reliability
- Put validation gates in front of every tool call
- Reject, fix, or escalate — no silent failures
- Require one-line reasoning before each tool call and a short observation after
- Use structured output formats (JSON Schema) to reduce hallucinated parameters

## Standardization: MCP

The [[concepts/model-context-protocol]] standardizes tool integration through a universal protocol. Rather than hardcoding tools, agents can discover available tools at runtime via MCP servers. This enables dynamic, modular architectures where tools are added or updated independently of the agent.

## Tool Categories

Common tool types in production agents:
- **Information retrieval**: Web search, database queries, document search
- **Code execution**: Running code in sandboxes, executing scripts
- **Communication**: Sending emails, Slack messages, API calls
- **File operations**: Reading, writing, editing files
- **Computer use**: GUI interaction, browser navigation (see [[entities/claude-code]])

## Sources

- [[sources/martinfowler-function-calling-llm]] — detailed architecture, security, MCP overview
- [[sources/superannotate-llm-agents-guide]] — tool use as fourth agent component
- [[sources/ng-agentic-design-patterns]] — tool use as second agentic design pattern
- [[sources/mcp-model-context-protocol]] — standardization protocol

## Related Concepts

- [[concepts/llm-agent-architecture]] — tool use as core component
- [[concepts/model-context-protocol]] — the open standard for tool integration
- [[concepts/react-pattern]] — tool use within the reasoning-acting loop
- [[concepts/agentic-workflows]] — tool use as a design pattern

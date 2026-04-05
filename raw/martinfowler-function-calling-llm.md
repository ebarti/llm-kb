---
title: "Function Calling Using LLMs"
source: "https://martinfowler.com/articles/function-call-LLM.html"
author: "Martin Fowler (site)"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [function-calling, tool-use, llm-agents, mcp, security]
type: article
status: raw
discovered_via: search
---

# Function Calling Using LLMs: Building AI Agents

## Overview

Function calling enables large language models to move beyond text generation by interacting with external systems. Rather than executing functions directly, LLMs analyze natural language input, extract user intent, and generate structured output (typically JSON) containing the function name and required parameters. A separate program then deserializes and executes this output.

## Core Architecture Pattern

### Basic Agent Scaffold

A typical agent follows this flow:
1. Receive user message and conversation history
2. Check for malicious intent
3. Determine appropriate action via LLM
4. Execute the action
5. Return results to user

The agent maintains a predefined set of possible actions, each encapsulated in its own class with an execute() method.

## Implementation Components

### System Prompt
The system prompt establishes the agent's role and defines available functions. It should clearly state the agent's purpose, list available functions with usage scenarios, specify when clarification is needed, and include constraints.

### Function Schemas
Each callable function requires a schema defining name, description, parameters (object schema with properties and required fields), and type information.

### Action Classes
Action classes translate LLM decisions into concrete operations: receive parameters, invoke APIs, format results, handle errors.

## Security Considerations

### Prompt Injection Guardrails
Adversarial users may attempt to reveal system prompts, bypass safeguards, trigger unauthorized actions, or extract sensitive data.

Defense strategies:
1. **Input sanitization**: Denylists for patterns like "ignore previous instructions"
2. **LLM-based validation**: Another model screens inputs for manipulation
3. **Action space restriction**: Explicit control over which functions the agent can invoke

### Best Practices
- Never use eval() or dynamic function invocation for security-critical operations
- Enforce strict conditional logic for function selection
- Combine multiple defense layers
- Start with low-risk operations and gradually extend

## Tool Calling vs Function Calling

"Tool calling" is the broader term encompassing custom function invocation, built-in capabilities, and integration with external services. "Function calling" refers specifically to invoking custom functions.

## Model Context Protocol (MCP)

MCP is an open protocol standardizing how LLM applications interact with external systems.

### Architecture Components
1. **MCP Server**: Exposes data sources and tools via HTTP; implements discovery endpoints
2. **MCP Client**: Manages communication between application and server
3. **MCP Host**: The LLM-based application that uses tools and data

### Benefits
- Dynamic tool discovery at runtime
- Decoupling from fixed tool sets
- Modularity: tools added/updated independently
- Scalability for growing complexity

### When to Use MCP
Justified for general-purpose agents, systems requiring frequent API updates, LLM-based IDEs, evolving systems. For focused, domain-specific agents, hardcoded tools may be simpler and more secure.

## Comparison: LLM Agents vs Rules Engines

| Aspect | Rules Engines | LLM-Based Agents |
|--------|---------------|-----------------|
| Rule interactions | Static, combinatorial explosion | Context-aware reasoning |
| Scalability | Fragile as rules multiply | Adapts to new scenarios |
| Expressiveness | Business users rarely write rules | Natural language is intuitive |
| Transparency | Explicit rule chains | Less transparent, more flexible |

## Key Takeaways

- Function calling empowers agents to interact with real-world systems while maintaining safety
- Security requires multiple layers: input sanitization, action space restriction, careful prompt design
- Structured outputs from LLMs enable reliable integration with backend systems
- MCP provides standardization for scalable, modular agent architectures
- Start conservatively with low-risk operations and expand progressively

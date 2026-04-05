---
title: "Function Calling"
type: concept
sources: ["[[sources/descope-mcp-vs-function-calling]]", "[[sources/zilliz-function-calling-vs-mcp-vs-a2a]]", "[[sources/composio-api-integration-patterns]]"]
related: ["[[concepts/model-context-protocol]]", "[[concepts/tool-use-standards]]", "[[concepts/augmented-llm]]"]
last_compiled: 2026-04-05
summary: "The mechanism by which LLMs invoke external APIs — each provider (OpenAI, Anthropic, Google) implements differently. Simple and fast for prototyping but creates vendor lock-in and M×N integration problems at scale."
---

## Overview

Function calling (also called "tool use") is the mechanism by which large language models invoke external APIs and tools based on natural language requests. The LLM receives a list of available function definitions (with JSON Schema parameters), selects the appropriate function for a given user query, generates the required arguments, and returns a structured call that the application executes.

Function calling was pioneered by OpenAI in June 2023 and has since been implemented by all major LLM providers, though each uses different schemas, parameter formats, and response structures.

## How It Works

1. Developer defines available functions with names, descriptions, and parameter schemas
2. User makes a natural language request
3. LLM identifies that external data/action is needed
4. Model selects the appropriate function and generates JSON arguments
5. Application code executes the actual API call
6. Response data is returned to the LLM for incorporation into its reply

## Strengths

- **Simplicity**: ~20 lines of code for a basic implementation
- **Speed**: Quick setup for prototypes and MVPs
- **Familiarity**: Uses standard programming patterns
- **Native support**: Built into all major LLM provider APIs
- **Minimal infrastructure**: No additional servers or processes needed

## Limitations

- **No cross-model consistency**: Each provider (OpenAI, Anthropic, Google, Meta) implements function calling with different schemas, argument formats, and response handling
- **Vendor lock-in**: Switching providers requires rewriting function definitions
- **M×N problem**: At scale, M applications connecting to N tools requires M×N custom integrations
- **No native chaining**: Multi-step function sequences require manual orchestration
- **Flat security model**: All functions execute with the same application-level permissions
- **Tight coupling**: Tool definitions live inline with prompts; changes require redeployment

## Function Calling vs. MCP

The key distinction is architectural. Function calling embeds tool definitions directly into LLM requests, creating tight coupling between the AI application and its tools. [[concepts/model-context-protocol]] introduces a client-server architecture that decouples tools from applications, enabling reuse, independent scaling, and provider-agnostic operation.

For a detailed comparison, see [[comparisons/mcp-vs-function-calling]].

## When to Use Function Calling

Function calling remains the best choice for:
- Personal projects and rapid prototypes
- Applications with 1-3 simple tool integrations
- Single-provider deployments with no migration plans
- Internal tools in trusted environments
- Situations where setup speed matters more than long-term maintenance

For production systems, enterprise applications, multi-provider strategies, or reusable integrations, [[concepts/model-context-protocol]] is generally preferred.

## Sources
- [[sources/descope-mcp-vs-function-calling]] — detailed comparison with MCP
- [[sources/zilliz-function-calling-vs-mcp-vs-a2a]] — three-way protocol comparison
- [[sources/composio-api-integration-patterns]] — function calling as pattern 2 of 5

## Related Concepts
- [[concepts/model-context-protocol]] — the standardized alternative
- [[concepts/tool-use-standards]] — the broader standards landscape
- [[concepts/augmented-llm]] — the architecture function calling enables
- [[concepts/ai-agent-integration-patterns]] — where function calling fits in the pattern taxonomy

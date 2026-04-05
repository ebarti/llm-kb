---
title: "Augmented LLM"
type: concept
sources: ["[[sources/anthropic-building-effective-agents]]", "[[sources/anthropic-code-execution-mcp]]"]
related: ["[[concepts/model-context-protocol]]", "[[concepts/tool-use-standards]]", "[[concepts/agentic-workflow-patterns]]", "[[concepts/multi-agent-systems]]"]
last_compiled: 2026-04-05
summary: "The foundational building block of agentic AI: an LLM enhanced with retrieval, tool integration, and memory — capable of independently generating search queries, selecting tools, and retaining information."
---

## Overview

The Augmented LLM is the basic building block of all agentic AI systems. As defined by [[entities/anthropic]] in their agent design guide, it combines a base language model with three key capabilities:

1. **Retrieval** — Accessing external information (documents, databases, web search)
2. **Tool integration** — Interacting with external systems (APIs, code execution, file operations)
3. **Memory** — Retaining information across interactions (conversation history, learned facts, state)

Modern LLMs can independently generate search queries, select appropriate tools, and determine what information to preserve — making the augmented LLM a capable autonomous unit even before multi-agent orchestration enters the picture.

## Why Augmentation Matters

A raw LLM is limited to its training data and the current conversation context. Augmentation lifts three critical constraints:

- **Knowledge cutoff** → Retrieval provides access to current information
- **Action limitation** → Tools enable the model to affect the external world
- **Statelessness** → Memory enables continuity across interactions

This is directly relevant to [[concepts/llm-knowledge-base]] systems, where the LLM's augmented capabilities (file reading, web search, file writing) enable it to author and maintain a wiki.

## Relationship to MCP

The [[concepts/model-context-protocol]] provides the standardized infrastructure for tool integration — the second pillar of the augmented LLM. Before MCP, each tool integration required custom code. MCP standardizes tool discovery, invocation, and data exchange, making it dramatically easier to build richly-augmented LLMs.

The [[concepts/mcp-code-execution-pattern]] further optimizes augmented LLMs by allowing agents to write code that interacts with tools, rather than loading all tool definitions into context.

## Design Principles

According to [[sources/anthropic-building-effective-agents]], augmented LLMs should be designed with:

- **Clear, well-documented interfaces** tailored to specific use cases
- **Tool engineering on par with prompt engineering** — tool definitions significantly impact model performance
- **Simplicity first** — start with a single augmented LLM before adding multi-agent complexity
- **Transparency** — explicitly display planning steps and tool usage

## From Augmented LLM to Agents

The progression from augmented LLM to full agent follows a clear path:

1. **Single augmented LLM** — One model with retrieval + tools + memory
2. **[[concepts/agentic-workflow-patterns|Workflows]]** — Multiple augmented LLMs orchestrated through predefined code paths
3. **Agents** — Augmented LLMs that dynamically direct their own processes and tool usage

Anthropic recommends starting at level 1 and only adding complexity when simpler approaches prove insufficient.

## Sources
- [[sources/anthropic-building-effective-agents]] — canonical definition and design principles
- [[sources/anthropic-code-execution-mcp]] — optimization via code execution

## Related Concepts
- [[concepts/model-context-protocol]] — the standard for the tool integration pillar
- [[concepts/tool-use-standards]] — broader tool integration landscape
- [[concepts/agentic-workflow-patterns]] — patterns built on augmented LLMs
- [[concepts/multi-agent-systems]] — multi-agent architectures composed of augmented LLMs
- [[concepts/llm-knowledge-base]] — a system built on augmented LLM capabilities
- [[concepts/rag-vs-index-based-retrieval]] — approaches to the retrieval pillar

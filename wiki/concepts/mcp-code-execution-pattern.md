---
title: "MCP Code Execution Pattern"
type: concept
sources: ["[[sources/anthropic-code-execution-mcp]]"]
related: ["[[concepts/model-context-protocol]]", "[[concepts/augmented-llm]]", "[[concepts/mcp-security]]"]
last_compiled: 2026-04-05
summary: "Anthropic's optimization pattern: agents write code to interact with MCP tools instead of loading all definitions into context — achieving 98.7% token savings, PII filtering, and persistent state management."
---

## Overview

The MCP Code Execution Pattern is an optimization technique described by [[entities/anthropic]]'s engineering team for scaling [[concepts/model-context-protocol]] usage. Instead of the standard approach of loading all MCP tool definitions into the LLM's context window, agents write code that interacts with MCP servers through a filesystem-like interface, loading only the tools they need.

## The Problem

Standard MCP clients load all tool definitions upfront into context. As agents connect to more servers, this creates two compounding problems:

1. **Context overhead** — With thousands of connected tools, processing hundreds of thousands of tokens just for tool definitions before any actual work begins
2. **Intermediate result bloat** — Every intermediate result (database queries, file contents, API responses) must pass through the model, consuming additional context and potentially exceeding limits

## The Solution

Organize MCP tools as a filesystem:

```
servers/
├── google-drive/
│   ├── getDocument.ts
│   └── index.ts
└── salesforce/
    ├── updateRecord.ts
    └── index.ts
```

Instead of loading all definitions, the agent:
1. Explores the directory structure to discover available tools
2. Reads only the tool definitions it needs for the current task
3. Writes code that calls the tools directly
4. Processes results in the execution environment before returning to the model

## Benefits

### Token Efficiency
The flagship example: reducing token usage from 150,000 to 2,000 — a **98.7% reduction** in processing overhead and costs.

### Security and Privacy
- **Data filtering** — Large datasets (e.g., 10,000-row spreadsheet) are filtered to relevant subset (e.g., 5 rows) before the model sees them
- **PII protection** — Sensitive data can be tokenized/replaced with placeholders; real data moves between systems without model exposure

### State Management
Agents can persist state across operations:
- Save intermediate results to files
- Resume multi-step work across interactions
- Build up reusable code functions as persistent "skills"

## Relationship to Skills

The Pento year-in-review ([[sources/pento-year-of-mcp-review]]) notes a conceptual distinction between MCP (raw connectivity) and Anthropic's "Skills" framework (lightweight, on-demand procedural knowledge). The code execution pattern bridges these: agents develop reusable code-based skills that efficiently interact with MCP tools.

## Sources
- [[sources/anthropic-code-execution-mcp]] — the original engineering article

## Related Concepts
- [[concepts/model-context-protocol]] — the underlying protocol being optimized
- [[concepts/augmented-llm]] — the agent architecture this pattern improves
- [[concepts/mcp-security]] — PII protection benefits of this pattern
- [[concepts/mcp-ecosystem]] — the large ecosystem that makes this optimization necessary

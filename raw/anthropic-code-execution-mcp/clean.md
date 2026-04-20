---
title: "Code Execution with MCP: Building More Efficient AI Agents"
source: "https://www.anthropic.com/engineering/code-execution-with-mcp"
author: "Anthropic Engineering"
date_published: 2025-09-01
date_ingested: 2026-04-05
tags: [mcp, code-execution, efficiency, token-optimization, security, agents]
type: article
status: raw
discovered_via: search
---

# Code Execution with MCP: Building More Efficient AI Agents

## Core Concept

Code execution as a solution to improve efficiency when agents interact with MCP. Rather than loading all tool definitions directly into context and making direct tool calls, agents can write code to interact with MCP servers dynamically.

## Key Problems Addressed

**Context Overhead**: "Most MCP clients load all tool definitions upfront directly into context" causing excessive token consumption. With thousands of connected tools, this approach requires processing hundreds of thousands of tokens before reading requests.

**Intermediate Result Bloat**: When agents retrieve data for processing, "Every intermediate result must pass through the model." Large documents must flow through the context window multiple times, potentially exceeding limits and creating errors.

## Implementation Architecture

The suggested pattern organizes MCP tools as a filesystem structure:

```
servers/
├── google-drive/
│   ├── getDocument.ts
│   └── index.ts
└── salesforce/
    ├── updateRecord.ts
    └── index.ts
```

Each tool file contains a wrapper function calling the underlying MCP tool. Agents discover available tools by exploring the filesystem and loading only necessary definitions.

## Token Efficiency Gains

The example demonstrates reducing token usage from 150,000 to 2,000 tokens — achieving "98.7% savings" in processing overhead and costs by filtering data locally before model processing.

## Security and Privacy Benefits

**Data Filtering**: Agents process large datasets in the execution environment, returning only relevant results to the model. A 10,000-row spreadsheet can be filtered to five rows before model visibility.

**PII Protection**: The MCP client can tokenize sensitive data, replacing actual values with placeholders that flow through the model while real data moves between systems without model exposure.

## State Management

Code execution enables agents to persist state across operations — saving intermediate results to files and resuming work, plus developing reusable code functions as persistent "skills."

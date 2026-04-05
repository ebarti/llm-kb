---
title: "Google Agent Development Kit (ADK)"
type: entity
entity_type: tool
sources: ["[[sources/google-ai-agent-protocols]]"]
related: ["[[concepts/model-context-protocol]]", "[[concepts/agent-to-agent-protocol]]", "[[concepts/agentic-workflow-patterns]]"]
last_compiled: 2026-04-05
summary: "Google's framework for building AI agents with integrated support for six protocols: MCP (tools), A2A (agent collaboration), UCP (commerce), AP2 (payments), A2UI (dynamic UI), AG-UI (streaming)."
---

## Overview

The Google Agent Development Kit (ADK) is Google's framework for building AI agents. It provides first-class integrated support for six standardized protocols covering the full lifecycle of agent interactions.

## Supported Protocols

1. **MCP** — Tool and data access via `McpToolset`
2. **A2A** — Agent-to-agent collaboration via Agent Cards
3. **UCP** — Universal Commerce Protocol for typed commerce workflows
4. **AP2** — Agent Payments Protocol for cryptographic transaction authorization
5. **A2UI** — Agent-to-User Interface Protocol for declarative UI composition
6. **AG-UI** — Agent-User Interaction Protocol for SSE-based streaming events

## Key Features

- `McpToolset` for connecting to MCP servers (databases, APIs, vendor tools)
- Agent Card publishing and discovery for A2A collaboration
- `ag_ui_adk` package for wrapping agents into FastAPI applications
- Incremental protocol adoption: "Add protocols as you need them"

## Design Philosophy

The ADK follows a progressive complexity approach — most agents start with MCP for basic data access and add additional protocol support as requirements grow. This aligns with [[entities/anthropic]]'s recommendation to start simple and add complexity only when needed.

## Mentioned In
- [[sources/google-ai-agent-protocols]] — comprehensive guide to all six protocols via ADK

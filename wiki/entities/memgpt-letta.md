---
title: "MemGPT / Letta"
type: entity
entity_type: tool
sources: ["[[sources/memgpt-llm-operating-system]]", "[[sources/hierarchical-memory-llm-agents]]"]
related: ["[[concepts/virtual-context-management]]", "[[concepts/hierarchical-memory]]", "[[concepts/context-windows]]", "[[concepts/context-engineering]]"]
last_compiled: 2026-04-05
summary: "Open-source platform for stateful LLM agents with OS-inspired virtual context management; LLM self-manages memory hierarchy (core/recall/archival) through tool calls."
---

## Overview

MemGPT is a research system (Packer et al., UC Berkeley, 2023) that pioneered virtual context management for LLMs, drawing on operating system memory hierarchies. The open-source project evolved into **Letta**, a full platform for building stateful agents with persistent memory.

The core insight: LLMs can manage their own memory through self-directed tool calls, deciding what to remember, summarize, and forget — creating the illusion of unlimited context within fixed [[concepts/context-windows]].

## Key Features

### Memory Architecture
- **Core Memory**: Editable in-context blocks (user info, agent persona). Analogous to RAM. Self-editable by the agent via `core_memory_append` / `core_memory_replace`.
- **Recall Memory**: Searchable conversation history. Auto-persisted to disk. Queried via `conversation_search`.
- **Archival Memory**: Vector database storage (LanceDB default) for long-term knowledge. Queried via `archival_memory_search`.

### Self-Directed Memory Management
The LLM itself acts as memory manager, using tool calls to:
- Edit its own core memory blocks
- Store important information to archival memory
- Search past conversations when context is needed
- Summarize and evict old messages when context fills up

### Platform Features (Letta)
- **Conversations API**: Shared memory across parallel user experiences (Jan 2026)
- **Sleep-Time Compute**: Asynchronous memory refinement during idle periods
- **Programmatic Tool Calling**: Agents generate their own workflows (Dec 2025)
- **Letta Evals**: Open-source evaluation framework for stateful agents (Oct 2025)
- **Letta Code**: Model-agnostic coding agent with persistent memory

## Technical Details

- **arXiv**: 2310.08560
- **GitHub**: github.com/letta-ai/letta
- **Default archival storage**: LanceDB (vector database)
- **Eviction strategy**: When context reaches ~70% capacity, older messages are recursively summarized and moved to recall memory

## Significance

MemGPT/Letta's "LLM as operating system" metaphor has become foundational to how the field thinks about agent memory. The three-tier memory hierarchy (core/recall/archival) is now the standard reference architecture for stateful agents.

## Mentioned In

- [[sources/memgpt-llm-operating-system]] — the foundational paper and architecture
- [[sources/hierarchical-memory-llm-agents]] — as a leading implementation of hierarchical agent memory

---
title: "Virtual Context Management"
type: concept
sources: ["[[sources/memgpt-llm-operating-system]]", "[[sources/hierarchical-memory-llm-agents]]", "[[sources/infinite-context-approaches]]"]
related: ["[[concepts/context-windows]]", "[[concepts/hierarchical-memory]]", "[[entities/memgpt-letta]]", "[[concepts/context-engineering]]"]
last_compiled: 2026-04-05
summary: "OS-inspired technique where LLMs page information between in-context memory (RAM) and external storage (disk), creating the illusion of unlimited context within fixed windows."
---

## Overview

Virtual context management is a technique inspired by operating system memory hierarchies. Just as an OS creates the illusion of unlimited memory through paging between RAM and disk, virtual context management creates the illusion of unlimited LLM context through paging between the model's fixed context window and external storage systems.

Introduced by [[entities/memgpt-letta]] (MemGPT, Packer et al., 2023), this approach is now a foundational pattern for building stateful LLM agents and knowledge systems.

## The OS Analogy

| OS Concept | LLM Equivalent | Function |
|-----------|---------------|----------|
| RAM | Main context window | Active working memory, immediately accessible |
| Disk storage | External databases (vector, SQL, files) | Long-term storage, requires explicit access |
| Virtual memory | Virtual context | Illusion of unlimited context from fixed window |
| Page faults | Memory tool calls | Triggered when needed information isn't in context |
| Page table | Memory index/metadata | Tracks what's stored where |
| Paging algorithm | LLM memory manager | Decides what to load/evict |

## How It Works

1. **Main Context** contains: system instructions, current memory blocks, recent messages, active task state
2. **External Context** stores: full conversation history (recall memory), long-term knowledge (archival memory), user/world models
3. **Memory Tools** enable the LLM to self-manage:
   - `core_memory_append` / `core_memory_replace` — edit in-context blocks
   - `conversation_search` — query past interactions
   - `archival_memory_insert` / `archival_memory_search` — long-term storage

The key innovation: the LLM itself decides when to page information in and out, using the same tool-calling mechanism it uses for other tasks.

## Eviction and Summarization

When the main context approaches capacity (~70% of messages), the system:
- Summarizes older messages recursively
- Evicts summarized messages to recall memory
- Preserves core memory blocks (always in context)
- Maintains recent messages for conversational coherence

This maps directly to OS page replacement algorithms, where least-recently-used pages are evicted first.

## Connection to Wiki Systems

[[concepts/llm-knowledge-base]] systems implement a form of virtual context management:

| Wiki Component | Virtual Context Role |
|---------------|---------------------|
| Summaries file | Memory index / page table |
| Full articles | Pages on "disk" — loaded on demand |
| Raw sources | Deep storage — rarely accessed directly |
| Wikilinks | Pointers between memory pages |
| Query workflow | Page fault → index lookup → page load |

The wiki's summaries-based navigation is functionally equivalent to a page table lookup: the LLM reads the compact index, identifies which "pages" (articles) are needed, and loads them on demand.

## Sources

- [[sources/memgpt-llm-operating-system]] — the foundational paper on virtual context management
- [[sources/hierarchical-memory-llm-agents]] — multi-tier memory architectures
- [[sources/infinite-context-approaches]] — InfLLM uses external memory units similarly

## Related Concepts

- [[concepts/context-windows]] — the fixed constraint that virtual context transcends
- [[concepts/hierarchical-memory]] — the multi-tier storage architecture
- [[entities/memgpt-letta]] — the primary implementation
- [[concepts/context-engineering]] — virtual context is a context engineering pattern
- [[concepts/llm-knowledge-base]] — implements virtual context through summaries-based navigation

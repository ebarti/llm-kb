---
title: "Source: MemGPT — Towards LLMs as Operating Systems"
type: source-summary
source: "[[raw/memgpt-llm-operating-system]]"
related: ["[[concepts/virtual-context-management]]", "[[concepts/hierarchical-memory]]", "[[entities/memgpt-letta]]", "[[concepts/context-windows]]"]
last_compiled: 2026-04-05
summary: "MemGPT introduces OS-inspired virtual context management: LLMs self-manage a memory hierarchy (main context = RAM, archival/recall = disk) through function calls, enabling unbounded context from fixed windows."
---

## Key Points

- Introduces **virtual context management** inspired by OS memory hierarchies
- Two-tier memory: main context (RAM) for immediate processing, external context (disk) for archival and recall
- The LLM itself acts as memory manager through self-directed tool calls
- Supports both long document analysis and persistent multi-session conversations
- Evolved into **Letta**, a full platform for stateful agents with sleep-time compute and shared memory

## Detailed Summary

MemGPT (Packer et al., UC Berkeley, 2023) draws a powerful analogy between OS virtual memory and LLM context management. Just as operating systems create the illusion of unlimited memory through paging between RAM and disk, MemGPT creates the illusion of unlimited context through paging between the LLM's fixed context window and external storage.

The key innovation is self-directed memory management: the LLM decides what to store, summarize, and forget through explicit function calls (`core_memory_append`, `conversation_search`, `archival_memory_search`). Core memory blocks stay pinned in context (like frequently-accessed RAM pages), while recall memory (conversation history) and archival memory (vector database) serve as searchable external storage.

This architecture directly addresses the [[concepts/context-windows]] limitation without requiring architectural changes to the underlying model. It is particularly relevant to [[concepts/llm-knowledge-base]] systems, where the amount of knowledge always exceeds any single context window.

## Related Concepts

- [[concepts/virtual-context-management]] — the core technique this paper introduces
- [[concepts/hierarchical-memory]] — the multi-tier memory architecture
- [[entities/memgpt-letta]] — the tool and platform that emerged from this research
- [[concepts/context-engineering]] — MemGPT is a context engineering system
- [[concepts/llm-knowledge-base]] — the wiki approach faces the same context limits MemGPT addresses

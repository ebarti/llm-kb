---
title: "MemGPT: Towards LLMs as Operating Systems"
source: "https://arxiv.org/abs/2310.08560"
author: "Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, Joseph E. Gonzalez"
date_published: 2023-10-12
date_ingested: 2026-04-05
tags: [memgpt, memory, virtual-context, operating-system, agents, letta]
type: paper
status: raw
discovered_via: search
---

# MemGPT: Towards LLMs as Operating Systems

## Core Concept

MemGPT introduces virtual context management, drawing parallels to operating system memory management. The system intelligently manages different storage tiers to provide extended context within the LLM's limited context window.

## Memory Architecture

### Two-Tier Hierarchy

1. **Main Context** (analogous to RAM): The standard fixed-length context window the LLM processes during inference. Contains system instructions, working memory blocks, and recent messages.

2. **External Context** (analogous to disk): Holds out-of-context information that can be selectively moved into main context through explicit function calls.
   - **Recall Memory**: Searchable conversation history (all past messages).
   - **Archival Memory**: Vector database storage for long-term knowledge. Uses LanceDB by default for semantic search.

### Self-Directed Memory Management

The LLM itself acts as the memory manager through tool calling:
- `core_memory_append` / `core_memory_replace`: Edit in-context memory blocks.
- `conversation_search`: Query recall memory for past interactions.
- `archival_memory_insert` / `archival_memory_search`: Store and retrieve from long-term storage.

The system decides what to store, what to summarize, and what to forget.

## Key Applications

1. **Document Analysis**: Process documents exceeding the underlying LLM's native context window.
2. **Multi-Session Chat**: Conversational agents that remember, reflect, and evolve through long-term interactions.

## Evolution to Letta

- MemGPT open source project became **Letta** — a full platform for building stateful agents.
- Letta extends MemGPT with: Conversations API for shared memory across parallel user experiences, sleep-time compute for asynchronous memory refinement, and programmatic tool calling.
- Letta Code: model-agnostic agent harness with persistent memory for coding tasks.

## Memory as Context Engineering

As Letta frames it: LLMs are "text-in, text-out systems. Their 'memory' consists solely of what exists in their context window." Memory management is fundamentally context engineering — determining which tokens enter the context window and how they're organized.

## Research Team

UC Berkeley. arXiv:2310.08560.

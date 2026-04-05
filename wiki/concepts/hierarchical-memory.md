---
title: "Hierarchical Memory"
type: concept
sources: ["[[sources/hierarchical-memory-llm-agents]]", "[[sources/memgpt-llm-operating-system]]", "[[sources/context-compression-techniques]]"]
related: ["[[concepts/virtual-context-management]]", "[[concepts/context-windows]]", "[[entities/memgpt-letta]]", "[[concepts/context-engineering]]", "[[concepts/multi-agent-systems]]"]
last_compiled: 2026-04-05
summary: "Multi-tier memory for LLM agents: working memory (in-context), episodic memory (session summaries), semantic memory (entity abstractions), and archival memory (external DB) — inspired by both OS design and cognitive science."
---

## Overview

Hierarchical memory organizes LLM agent memory into multiple tiers of increasing abstraction and decreasing access speed, drawing from both computer science (OS memory hierarchies) and cognitive science (human memory systems). This is essential for agents that must maintain context across long interactions or multiple sessions while operating within fixed [[concepts/context-windows]].

## Memory Tiers

### Tier 1: Working Memory (In-Context)
- Lives directly in the LLM's context window
- Contains: system instructions, current task state, recent messages, core identity/persona
- Bounded by context window size
- Highest access speed (always available)
- Analogous to CPU registers / L1 cache / human working memory

### Tier 2: Episodic Memory (Session Summaries)
- Compact summaries of past interactions
- Contains: key events, decisions, outcomes from previous sessions
- Stored as text, loaded on demand
- Medium access speed (requires retrieval)
- Analogous to RAM / human episodic memory

### Tier 3: Semantic Memory (Entity Abstractions)
- Structured knowledge extracted across all sessions
- Contains: entity properties, relationships, facts, user preferences
- Often stored as knowledge graphs or structured documents
- Medium-low access speed (requires search + retrieval)
- Analogous to disk cache / human semantic memory

### Tier 4: Archival Memory (External Storage)
- Full historical records and long-term knowledge
- Contains: complete conversation logs, ingested documents, reference data
- Stored in vector databases, SQL, or file systems
- Lowest access speed (requires explicit search)
- Analogous to cold storage / human long-term memory

## Research Implementations

### H-MEM (EACL 2026)
Four layers organized by semantic abstraction:
1. **Episode Layer**: Raw interaction records
2. **Memory Trace Layer**: Individual memories with metadata
3. **Category Layer**: Thematic groupings
4. **Domain Layer**: Highest-level categorical organization

### Multi-Layer Memory Framework
Three complementary layers with adaptive gating:
- **Working memory**: Recent interaction within bounded windows
- **Episodic memory**: Compact session summaries
- **Semantic memory**: Structured entity-level abstractions

### HiAgent
Chunks working memory by subgoals. Once a subgoal completes, its fine-grained action-observation pairs are summarized, freeing context for the next subgoal.

### Letta/MemGPT Tiers
- **Core Memory**: Editable in-context blocks (user info, agent persona)
- **Recall Memory**: Searchable conversation history
- **Archival Memory**: Vector database for long-term knowledge

## Storage Paradigms

| Paradigm | Mechanism | Tradeoff |
|----------|-----------|----------|
| Cumulative | Append everything | Simple but unbounded growth |
| Reflective/Summarized | Periodic compression | Practical; loses some detail |
| Textual | Plain text in files/DB | Human-readable; no structure |
| Parametric | Fine-tune into model weights | Permanent but inflexible |
| Structured | Graphs, tables, triples | Most organized; most complex |

## Sleep-Time Compute

Letta introduces asynchronous memory consolidation during idle periods:
- **Non-blocking**: Memory refinement happens outside the interaction loop
- **Proactive**: Organizes, deduplicates, and enriches memory preemptively
- **Analogous to human sleep**: Memory consolidation and reorganization during downtime

## Connection to Wiki Systems

The [[concepts/llm-knowledge-base]] wiki structure mirrors hierarchical memory:

| Wiki Layer | Memory Tier |
|-----------|------------|
| Current query + instructions | Working memory |
| `summaries.md` (one-line per article) | Episodic memory (compressed index) |
| Concept articles (cross-source synthesis) | Semantic memory |
| Source summaries | Detailed episodic records |
| Raw files | Archival memory |

## Sources

- [[sources/hierarchical-memory-llm-agents]] — H-MEM, multi-layer framework, five storage paradigms
- [[sources/memgpt-llm-operating-system]] — MemGPT's core/recall/archival tiers
- [[sources/context-compression-techniques]] — compression techniques that enable memory tiering

## Related Concepts

- [[concepts/virtual-context-management]] — the paging mechanism that connects memory tiers
- [[concepts/context-windows]] — the constraint that necessitates memory hierarchies
- [[entities/memgpt-letta]] — leading implementation
- [[concepts/context-engineering]] — hierarchical memory is a context engineering pattern
- [[concepts/context-compression]] — compression enables each tier
- [[concepts/llm-knowledge-base]] — wiki structure is a hierarchical memory system

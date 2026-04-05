---
title: "Hierarchical Memory Architectures for LLM Agents"
source: "multiple"
author: "Various researchers"
date_published: 2025-07-01
date_ingested: 2026-04-05
tags: [hierarchical-memory, agent-memory, h-mem, working-memory, episodic-memory, semantic-memory]
type: article
status: raw
discovered_via: search
---

# Hierarchical Memory Architectures for LLM Agents

## H-MEM (Hierarchical Memory)

Published at EACL 2026, H-MEM organizes and updates memory in a multi-level fashion based on semantic abstraction:

### Four Memory Layers
1. **Domain Layer**: Highest-level categorical organization.
2. **Category Layer**: Sub-domain groupings.
3. **Memory Trace Layer**: Individual memory entries with metadata.
4. **Episode Layer**: Raw episodic records of interactions.

## Multi-Layer Memory Framework

Decomposes dialogue history into three complementary layers with adaptive gating and retention regularization:

1. **Working Memory**: Preserves recent interaction within bounded windows. Analogous to human short-term memory.
2. **Episodic Memory**: Accumulates compact session summaries. Captures key events and outcomes.
3. **Semantic Memory**: Maintains structured entity-level abstractions. Persistent knowledge extracted across sessions.

## Storage Paradigms

- **Cumulative memory**: Complete historical appending (simple but unbounded).
- **Reflective/summarized memory**: Periodically compressed summaries.
- **Textual storage**: Plain text in files or databases.
- **Parametric storage**: Embedding into model weights via fine-tuning.
- **Structured storage**: Tables, triples, or graph-based (most organized but most complex).

## HiAgent: Subgoal-Based Memory

Chunks working memory using subgoals. Summarizes fine-grained action-observation pairs once goals are completed. Retains hierarchical, context-relevant information and supports efficient retrieval.

## Key Distinction: Short-Term vs. Long-Term

- **Short-term/working memory**: Single-session, within-trial decision context. Lives in the LLM's context window.
- **Long-term/cross-trial memory**: Knowledge and experience retained across distinct tasks or sessions. Stored externally.

## Letta/MemGPT Memory Tiers

- **Core Memory**: In-context blocks (user info, agent persona). Analogous to RAM. Self-editable by the agent.
- **Recall Memory**: Searchable conversation history. Auto-persisted.
- **Archival Memory**: Vector/graph database for long-term knowledge. Analogous to disk storage.

## Sleep-Time Compute

Letta introduces asynchronous memory refinement during idle periods:
- Non-blocking operations for memory consolidation.
- Proactive memory refinement rather than lazy, incremental updates.
- Analogous to how human memory consolidates during sleep.

## AWS AgentCore Long-Term Memory

AWS offers infrastructure-level agent memory with automatic extraction and retrieval of facts from conversations.

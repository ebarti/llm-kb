---
title: "Source: Hierarchical Memory Architectures for LLM Agents"
type: source-summary
source: "[[raw/hierarchical-memory-llm-agents]]"
related: ["[[concepts/hierarchical-memory]]", "[[concepts/virtual-context-management]]", "[[entities/memgpt-letta]]", "[[concepts/multi-agent-systems]]"]
last_compiled: 2026-04-05
summary: "Survey of hierarchical memory: H-MEM's 4-layer architecture (EACL 2026), multi-layer frameworks (working/episodic/semantic), five storage paradigms, and sleep-time compute for memory consolidation."
---

## Key Points

- **H-MEM** (EACL 2026): Four layers — Domain, Category, Memory Trace, Episode — organized by semantic abstraction
- **Multi-Layer Framework**: Working memory (recent), episodic memory (session summaries), semantic memory (entity abstractions) with adaptive gating
- Five storage paradigms: cumulative, reflective/summarized, textual, parametric (fine-tuning), structured (graphs/tables)
- **HiAgent**: Chunks working memory by subgoals, summarizing completed action-observation pairs
- **Sleep-time compute**: Asynchronous memory refinement during idle periods (Letta)

## Detailed Summary

Hierarchical memory for LLM agents draws from both computer science (OS memory hierarchies) and cognitive science (human memory systems). The field has converged on a three-tier model: working memory (immediate context), episodic memory (session summaries), and semantic memory (structured abstractions).

H-MEM (EACL 2026) adds organizational structure with four layers of increasing abstraction: raw episodes at the bottom, memory traces with metadata, categorical groupings, and domain-level organization at the top. This mirrors how [[concepts/llm-knowledge-base]] systems organize knowledge: raw files at the bottom, source summaries, concept articles, and the master index at the top.

The five storage paradigms (cumulative, reflective, textual, parametric, structured) represent a spectrum of tradeoffs. Cumulative storage is simplest but grows without bound. Reflective/summarized storage is the most practical for agents. Structured storage (graphs, tables) is the most organized but most complex — connecting to the [[concepts/knowledge-graph]] approaches already in this wiki.

Letta's sleep-time compute introduces asynchronous memory refinement, where agents consolidate and organize memory during idle periods — analogous to how human memory consolidates during sleep.

## Related Concepts

- [[concepts/hierarchical-memory]] — the core architecture described
- [[concepts/virtual-context-management]] — hierarchical memory enables virtual context
- [[entities/memgpt-letta]] — leading implementation of hierarchical agent memory
- [[concepts/llm-knowledge-base]] — the wiki approach mirrors hierarchical memory organization
- [[concepts/multi-agent-systems]] — multi-agent memory coordination

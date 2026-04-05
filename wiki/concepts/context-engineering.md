---
title: "Context Engineering"
type: concept
sources: ["[[sources/context-engineering-2026]]", "[[sources/logrocket-llm-context-problem]]", "[[sources/redis-rag-vs-long-context]]", "[[sources/ragflow-rag-review-2025]]"]
related: ["[[concepts/context-windows]]", "[[concepts/context-compression]]", "[[concepts/prompt-caching]]", "[[concepts/llm-knowledge-base]]", "[[concepts/lost-in-the-middle]]", "[[concepts/retrieval-augmented-generation]]", "[[concepts/agentic-rag]]"]
last_compiled: 2026-04-05
summary: "The systems discipline of managing everything an LLM encounters during inference — successor to prompt engineering, credited to Karpathy (2024-2025)."
---

## Overview

Context engineering is a comprehensive systems discipline for managing everything a language model encounters during inference. This includes prompts, retrieved documents, memory systems, tool descriptions, state information, caching strategies, user metadata, conversation history, and data schemas.

The term began circulating in 2024-2025, often credited to Andrej Karpathy. By 2026, Gartner and industry practitioners had declared "prompt engineering is out, context engineering is in" — recognizing that crafting individual prompts is far less impactful than designing the information environment surrounding the model.

## From Prompt Engineering to Context Engineering

| Dimension | Prompt Engineering | Context Engineering |
|-----------|-------------------|-------------------|
| Scope | Single prompt text | Entire information environment |
| Focus | How to ask | What to show |
| Optimization | Word choice, examples | Architecture, pipelines, memory |
| State | Stateless | Stateful (memory, caching) |
| Complexity | Artisanal | Systems engineering |

## Core Principles

### Context as Structured Object
Context should be treated as a structured, typed object rather than a growing text buffer:

```
context = {
  'system_instructions': always_keep,
  'user_goal': always_keep,
  'conversation_history': prune_old_messages,
  'retrieved_documents': prune_low_relevance,
  'tool_outputs': prune_superseded_results
}
```

Each element is tagged with function (goal, decision, action, error), priority, source, and confidence.

### Three Dimensions
1. **Collection & Storage**: How context is gathered, indexed, and persisted
2. **Management**: How context is selected, compressed, and organized for inference
3. **Usage**: How context is presented to the model and how outputs feed back

### ACE Framework (Agentic Context Engineering)
- Represents context as collections of structured, itemized bullets
- Treats contexts as evolving playbooks
- Modular process: generation → reflection → curation

## Six Key Techniques

From [[sources/logrocket-llm-context-problem]]:

1. **RAG**: Retrieve only what's needed. Prevents reasoning degradation from oversized context.
2. **Dynamic Tool Selection**: Show only relevant tools. **44% improvement** on Llama 3.1 8B function-calling.
3. **Context Quarantine**: Isolated subagents prevent cross-domain contamination.
4. **Context Pruning**: Structured removal of low-priority content. **95% compression** with tools like Provence.
5. **Context Summarization**: Compress at 32K-100K token thresholds.
6. **Scratchpad/Think Tool**: Separate reasoning space. **54% improvement** on agent benchmarks (Anthropic).

## The "Smart Layering" Pattern

From [[sources/redis-rag-vs-long-context]], four operational stages:
1. **Writing context**: Capturing user inputs
2. **Selecting context**: Retrieving relevant knowledge
3. **Compressing context**: Summarizing when limits approach
4. **Isolating context**: Keeping concerns separate

## Connection to LLM Wiki Systems

The [[concepts/llm-knowledge-base]] approach is, fundamentally, a context engineering system:

| Wiki Component | Context Engineering Function |
|---------------|----------------------------|
| `summaries.md` | Compact structured index for selective loading |
| `_index.md` | Navigation metadata |
| Wikilinks | Structured traversal paths |
| Source summaries | Pre-compressed reference documents |
| Selective article loading | On-demand context retrieval |
| Raw files (immutable) | Ground truth external storage |

The wiki's ingest → compile → query cycle maps directly to ACE's generation → reflection → curation pattern.

## 2026 Production Stack

The prevailing pattern combines:
- **LlamaIndex** for data structuring and retrieval
- **LangGraph** for agent orchestration
- **Prompt caching** ([[concepts/prompt-caching]]) for cost optimization
- **Structured memory** ([[concepts/hierarchical-memory]]) for state management

## Sources

- [[sources/context-engineering-2026]] — origins, frameworks, and 2026 stack
- [[sources/logrocket-llm-context-problem]] — six techniques and four failure modes
- [[sources/redis-rag-vs-long-context]] — smart layering pattern

## RAG as Context Engine

According to the [[sources/ragflow-rag-review-2025|RAGFlow 2025 review]], [[concepts/retrieval-augmented-generation]] is evolving from a specific retrieval-generation pattern into the foundational infrastructure for context engineering. Modern AI agents require three types of context that all use retrieval-like capabilities:

1. **Domain Knowledge**: Traditional RAG — retrieving enterprise documents and knowledge bases
2. **Tool Data**: Selecting which APIs/tools to use from hundreds of options via semantic search over tool descriptions
3. **Conversation State**: Memory systems managing interaction history through identical retrieval mechanisms as RAG

This convergence toward a unified Context Engine or Context Platform represents RAG's ultimate evolution — from a Q&A technique to foundational data infrastructure.

## Related Concepts

- [[concepts/context-windows]] — the constraint that motivates context engineering
- [[concepts/context-compression]] — a key tool within the discipline
- [[concepts/prompt-caching]] — economic enabler for large-context engineering
- [[concepts/lost-in-the-middle]] — the failure mode that demands structured context design
- [[concepts/llm-knowledge-base]] — a practical context engineering system
- [[concepts/hierarchical-memory]] — memory as context management
- [[concepts/virtual-context-management]] — extending context beyond fixed limits
- [[concepts/retrieval-augmented-generation]] — the core technology context engineering builds on
- [[concepts/agentic-rag]] — agents as consumers of engineered context

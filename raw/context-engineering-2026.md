---
title: "Context Engineering: The Emerging Discipline for LLM Systems (2025-2026)"
source: "multiple"
author: "Various"
date_published: 2026-01-15
date_ingested: 2026-04-05
tags: [context-engineering, prompt-engineering, LLM, architecture, agents, structured-context]
type: article
status: raw
discovered_via: search
---

# Context Engineering: The Emerging Discipline

## Origins

The term "context engineering" began circulating in 2024-2025, often credited to Andrej Karpathy. Both Karpathy and Gartner declared "prompt engineering is out, context engineering is in."

## Definition

Context engineering is a comprehensive systems discipline managing everything the model encounters during inference — prompts, retrieved documents, memory systems, tool descriptions, state information, caching strategies, user metadata, conversation history, and data schemas.

## Key Principles

### Context as Structured Object
Context should be treated as a structured object rather than a growing text buffer. Each element tagged with its function: "goal," "decision," "action," "error" — with support for multi-dimensional tagging (priority, source, confidence).

### ACE (Agentic Context Engineering)
- Represents context as collections of structured, itemized bullets rather than monolithic prompts.
- Treats contexts as evolving playbooks that accumulate, refine, and organize strategies.
- Modular process of generation, reflection, and curation.

### Three Dimensions
1. **Collection & Storage**: How context is gathered, indexed, and persisted.
2. **Management**: How context is selected, compressed, and organized for inference.
3. **Usage**: How context is presented to the model and how outputs feed back.

## Techniques

### Context Quarantine
Spawn focused subagents with isolated context rather than maintaining one large thread. Prevents cross-domain contamination.

### Dynamic Tool Selection
Reduce available tools based on query relevance. Showing only relevant tools improved Llama 3.1 8B function-calling by 44%.

### Scratchpad/Think Tool
Separate reasoning space for intermediate steps. Anthropic's think tool: 54% improvement on agent benchmarks.

### Structured Pruning
Priority-based retention:
- Always keep: system instructions, user goal
- Prune: old messages, low-relevance documents, superseded results

## 2026 Stack

Prevailing pattern: LlamaIndex for data structuring + LangGraph for agent orchestration. Context engineering increasingly recognized as first-class discipline alongside model selection and fine-tuning.

## Relevance to LLM Wiki Systems

For knowledge bases like Karpathy's LLM wiki approach:
- Summaries file acts as a structured context index.
- Article loading is selective retrieval (RAG without vectors).
- Wikilinks provide structured navigation that an LLM can follow.
- The entire architecture is a context engineering system — managing what the LLM sees during Q&A.

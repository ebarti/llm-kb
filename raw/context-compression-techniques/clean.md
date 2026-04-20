---
title: "Context Compression and Summarization Techniques for LLMs"
source: "multiple"
author: "Various"
date_published: 2025-06-01
date_ingested: 2026-04-05
tags: [context-compression, summarization, token-efficiency, llmlingua, prompt-compression]
type: article
status: raw
discovered_via: search
---

# Context Compression and Summarization Techniques

## Overview

Combining relevance filtering, semantic deduplication, extractive summarization, and sentence pruning can reduce token usage by **50-80%** while preserving information quality.

## Hard Prompt Methods

### SelectiveContext
Filters low-information tokens from prompts, keeping only those with high self-information scores.

### LLMLingua
Leverages smaller language models to rank and preserve key tokens. Achieves up to **20x shorter prompts** while maintaining task performance.

### LongLLMLingua
Extension of LLMLingua specifically for long-context scenarios. Better handles document-level compression with question-aware filtering.

## Soft Prompt Methods

Encode prompts into continuous trainable embeddings or key-value pairs. Achieve compression ratios up to **480x** but require training and are model-specific.

## Hierarchical Summarization

- Divide input into chunks (paragraphs, sections).
- Summarize each chunk individually (first hierarchy level).
- Combine and summarize previous summaries (higher levels).
- Creates progressively condensed views.
- Risk: cumulative errors propagate through layers.

## Adaptive Context Compression

Recent research on adaptive methods for long-running interactions:
- Token reduction: 1% for 10 messages, 50% for 25 messages, 69% for 50 messages, 83% for 100 messages.
- Example: 8,560 tokens saved for a 50-message interaction.

## Sparse Attention Mechanisms

- **Longformer** and **BigBird**: Not every token interacts with every other token. Only a subset considered during attention computation.
- Significantly reduces memory and token overhead for long sequences.
- Enables processing of much longer inputs within same compute budget.

## Context Pruning Tools

- **Provence**: Achieves compression rates up to **95%** while retaining relevant information.
- Treats context as structured objects with priority levels:
  - `always_keep`: system instructions, user goal
  - `prune_old`: conversation history
  - `prune_low_relevance`: retrieved documents
  - `prune_superseded`: old tool outputs

## Six Practical Techniques (from Agenta)

1. **Truncation**: Simple token cutting. Low overhead, but lacks semantic awareness.
2. **Model routing**: Redirect large requests to bigger-context models.
3. **Memory buffering**: Store/summarize past conversations (e.g., LangChain ConversationSummaryBufferMemory).
4. **Hierarchical summarization**: Pyramid-structured summaries via models like BART.
5. **Context compression**: Knowledge graph extraction (LangChain ConversationKGMemory). 40-60% reduction.
6. **RAG**: Retrieve only relevant chunks at query time via vector search.

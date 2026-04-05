---
title: "Cache-Augmented Generation (CAG)"
type: concept
sources: ["[[sources/cache-augmented-generation]]"]
related: ["[[concepts/retrieval-augmented-generation]]", "[[concepts/fine-tuning]]", "[[comparisons/rag-vs-cag]]"]
last_compiled: 2026-04-05
summary: "A RAG alternative that preloads all documents into the LLM's KV cache at once, eliminating retrieval entirely — 10x faster with higher accuracy on small knowledge bases, but limited to manageable corpus sizes."
---

## Overview

Cache-Augmented Generation (CAG) is an alternative paradigm to [[concepts/retrieval-augmented-generation]] that eliminates the retrieval step entirely. Instead of searching for relevant documents at query time, CAG preloads all documents into the LLM's extended context and caches their key-value (KV) representations for reuse across multiple queries.

The approach was formalized in the December 2024 paper "Don't Do RAG: When Cache-Augmented Generation is All You Need," which demonstrated that for bounded knowledge bases, CAG achieves both higher accuracy and dramatically faster inference than traditional RAG.

## How It Works

CAG operates in three phases:

**Phase 1 — Preloading**: All documents in the knowledge base are preprocessed and their KV cache computed once via KV-Encode(D). This cached representation is stored persistently.

**Phase 2 — Inference**: When a query arrives, the precomputed KV cache loads alongside the question. The model generates answers directly from the full document context without any retrieval, ranking, or chunk selection.

**Phase 3 — Cache Reset**: Between sessions or when the knowledge base changes, the KV cache is truncated and recomputed. This is efficient for stable knowledge bases but costly for frequently updated ones.

## Performance

On standard benchmarks, CAG shows clear advantages over RAG:

| Metric | CAG | RAG | Improvement |
|---|---|---|---|
| HotPotQA-Small latency | 0.85s | 9.24s | ~10x faster |
| BERTScore | Higher across most configs | Baseline | Varies |
| Retrieval errors | Zero (no retrieval) | Present | Eliminated |

The speed advantage comes from avoiding the retrieval step entirely — no embedding computation, no approximate nearest neighbor search, no reranking. The accuracy advantage comes from eliminating retrieval ranking errors: the model sees all documents holistically, enabling comprehensive multi-hop reasoning without worrying about whether the right chunks were selected.

## When to Use CAG vs. RAG

**CAG excels when**:
- Knowledge base fits within the model's context window (~128k tokens for Llama 3.1 8B, ~1M tokens for modern frontier models)
- Knowledge is relatively stable (not requiring real-time updates)
- Multi-hop reasoning across documents is important
- Deterministic, reproducible behavior is valued
- Infrastructure simplicity is preferred (no vector database, no retriever)

**RAG remains necessary when**:
- Knowledge base is too large for any context window
- Documents change frequently and need immediate availability
- Latency requirements favor targeted retrieval over full-context loading
- Cost optimization requires processing only relevant chunks

## Relationship to Long Context

CAG's viability is directly tied to LLM context window sizes. As context windows expand (from 4k in GPT-3.5 to 1M+ in modern models), CAG becomes practical for increasingly large knowledge bases. However, research also shows that simply expanding context doesn't eliminate attention degradation — models still struggle with "information flooding" at extreme context lengths.

The emerging consensus is that **hybrid approaches** combining CAG's preloading for a core knowledge base with selective retrieval for dynamic or overflow content may represent the optimal architecture.

## Relationship to LLM Knowledge Bases

The [[concepts/llm-knowledge-base]] approach championed by Andrej Karpathy shares philosophical DNA with CAG: both avoid traditional retrieval infrastructure in favor of having the LLM process documents more directly. The KB approach uses index files and summaries as lightweight navigation aids rather than vector similarity search, while CAG goes further by eliminating even that navigation layer.

## Sources

- [[sources/cache-augmented-generation]] — original paper with experimental results

## Related Concepts

- [[concepts/retrieval-augmented-generation]] — the paradigm CAG replaces for small corpora
- [[concepts/fine-tuning]] — alternative knowledge injection (into parameters vs. context)
- [[concepts/llm-knowledge-base]] — related approach using LLM navigation over documents
- [[comparisons/rag-vs-cag]] — when to use each approach

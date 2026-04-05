---
title: "Two-Stage Retrieval"
type: concept
sources: ["[[sources/pinecone-rerankers-two-stage]]", "[[sources/superlinked-hybrid-search-reranking]]"]
related: ["[[concepts/reranking]]", "[[concepts/bi-encoder-vs-cross-encoder]]", "[[concepts/hybrid-search]]", "[[concepts/vector-search]]"]
last_compiled: 2026-04-05
summary: "The standard RAG retrieval architecture: fast bi-encoder/hybrid retrieval narrows millions of documents to top-k candidates, then a cross-encoder reranker selects the top-n most relevant for the LLM."
---

## Overview

Two-stage retrieval is the dominant architecture for production RAG systems. It resolves the fundamental tension between retrieval speed (bi-encoders) and retrieval accuracy (cross-encoders) by using each where it excels:

1. **Stage 1 — Fast retrieval**: [[concepts/vector-search]] or [[concepts/hybrid-search]] narrows millions of documents to top-k candidates (~25-100) in milliseconds
2. **Stage 2 — Accurate reranking**: A [[concepts/reranking|cross-encoder reranker]] scores each candidate against the query, selecting the top-n (~3-5) most relevant

## The Full Pipeline

```
Document Collection (millions)
    ↓ Stage 1: Bi-encoder / Hybrid Search (~100ms)
Top-k Candidates (25-100)
    ↓ Stage 2: Cross-encoder Reranking (~50-250ms)
Top-n Results (3-5)
    ↓ Pass to LLM for generation
Answer with citations
```

## Why Two Stages Are Necessary

**Stage 1 alone is insufficient**: Bi-encoders compress documents into single vectors without knowing the future query. Important documents may rank outside the top-k. Increasing top_k degrades LLM performance.

**Stage 2 alone is impractical**: Cross-encoders process query-document pairs jointly. Scoring every document in a 40M collection takes >50 hours per query on GPU.

**Together**: Maximize retrieval recall (stage 1 casts a wide net) while maximizing LLM precision (stage 2 keeps only the best).

## Practical Model Stack

A typical production configuration:

| Stage | Model | Latency |
|-------|-------|---------|
| Embedding | multilingual-e5-large (1024 dims) | Pre-computed |
| Vector Search | HNSW index via Pinecone/Qdrant/Weaviate | <100ms |
| Reranker | bge-reranker-v2-m3 | ~50-250ms |
| LLM | GPT-4 / Claude / Llama | ~1-5s |

## Extension: Three-Stage with Hybrid

The most robust configuration adds hybrid search:

1. **BM25 + Vector Search** (parallel, merged via RRF)
2. **Cross-encoder reranking** on merged results
3. **LLM generation** on top-n passages

This catches both exact-term matches (BM25) and semantic matches (vectors), then refines with query-specific reranking.

## Sources

- [[sources/pinecone-rerankers-two-stage]] — the case for two-stage architecture
- [[sources/superlinked-hybrid-search-reranking]] — three-stage pipeline with hybrid search

## Related Concepts

- [[concepts/reranking]] — the second stage
- [[concepts/bi-encoder-vs-cross-encoder]] — the architectural tradeoff motivating two stages
- [[concepts/hybrid-search]] — enhanced first stage
- [[concepts/vector-search]] — basic first stage

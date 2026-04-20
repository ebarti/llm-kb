---
title: "Hybrid Search for RAG: BM25, SPLADE, and Vector Search Combined"
source: "https://blog.premai.io/hybrid-search-for-rag-bm25-splade-and-vector-search-combined/"
author: "PremAI"
date_published: 2025-01-20
date_ingested: 2026-04-05
tags: [hybrid-search, bm25, splade, vector-search, rrf, fusion, rag]
type: article
status: raw
discovered_via: search
---

# Hybrid Search for RAG: BM25, SPLADE, and Vector Search Combined

## Core Concept

Hybrid search executes sparse retrieval (BM25 or SPLADE) and dense vector search in parallel, combining results using fusion algorithms. "Dense retrieval misses exact identifiers" while "sparse retrieval misses semantic matches."

## BM25 vs. SPLADE

**BM25**: Statistical ranking via term frequency, inverse document frequency, document length normalization. Excels at exact matches (product SKUs, error codes, API names). No vocabulary expansion — "car" won't match "automobile."

**SPLADE** (Sparse Lexical and Expansion model): Transformer encoding generates sparse vectors with vocabulary expansion. Enriches query/document representations with semantically related terms during indexing. Outperforms BM25 on most BEIR benchmarks while maintaining inverted index compatibility. Trade-off: requires GPU-accelerated transformer inference during indexing.

**Selection guide:** BM25 for exact-match-heavy domains. SPLADE for enterprise KBs with vocabulary mismatch.

## Fusion Strategies

### Reciprocal Rank Fusion (RRF)
Scores: sum of 1/(k + rank) across all retrievers, k=60 default. Rank-based, ignores raw scores, no normalization needed. Works without labeled data but is a starting point, not optimal.

### Convex Combination
alpha * dense + (1-alpha) * sparse. Starting points:
- 0.5: Balanced baseline
- ~0.3: Technical documentation (favor exact keywords)
- ~0.7: Conversational queries (favor semantic understanding)
Outperforms RRF when tuned on 50-100 labeled query pairs.

### Distribution-Based Score Fusion (DBSF)
Normalizes using each retriever's mean and standard deviation (±3σ bounds). Prefer when score magnitudes fluctuate significantly.

## Benchmark Results

- BEIR aggregate: +26-31% NDCG improvement
- BRIGHT Biology: +24% recall gain
- WANDS e-commerce: +1.7-1.9% Mean NDCG
- OpenSearch real-world: +9% MAP, +19% NDCG

Variance reflects vocabulary mismatch severity.

## Recommended Production Pipeline

1. Hybrid retrieval → top-20 candidates via RRF fusion
2. Cross-encoder reranking → scores query-document pairs jointly
3. Top-5 reranked results → pass to LLM

Reranking cannot recover documents missed during retrieval, making hybrid search's expanded candidate set essential.

## When NOT to Use Hybrid Search

- Dense retrieval alone shows strong performance on vocabulary-matched corpora
- Queries are purely exact-match
- RRF adds marginal gains (<5%)
- Dense + cross-encoder reranking already solves precision problem
- Poorly tuned hybrid can underperform dense-only baselines

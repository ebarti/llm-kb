---
title: "Optimizing RAG with Hybrid Search & Reranking"
source: "https://superlinked.com/vectorhub/articles/optimizing-rag-with-hybrid-search-reranking"
author: "Superlinked / VectorHub"
date_published: 2024-08-20
date_ingested: 2026-04-05
tags: [hybrid-search, reranking, RAG, BM25, vector-search, RRF]
type: article
status: raw
discovered_via: search
---

# Optimizing RAG with Hybrid Search & Reranking — Superlinked

## Full Retrieval Pipeline

1. Keyword Search (Sparse/BM25): Matches query terms against documents
2. Vector Search (Dense): Cosine similarity on embeddings for semantic relationships
3. Fusion: Combine results via RRF or weighted alpha
4. Reranking: Transformer-based semantic scoring of top-k results

## BM25 Formula

BM25(D,Q) = Σ IDF(q) × [TF(q,D) × (k₁+1)] / [TF(q,D) + k₁×(1-b+b×|D|/avgdl)]

## Fusion Formula

H = (1-α)K + αV where α balances keyword (K) and vector (V) scores.
RRF(d) = Σ 1/(k + r(d))

## Model Recommendations

- Embeddings: BAAI/bge-base-en-v1.5
- LLM: Zephyr-7B-Beta (4-bit quantized)
- Reranker: Cohere Rerank or custom

## Implementation

ChromaDB: manual EnsembleRetriever with weights [0.3, 0.7].
Weaviate: native hybrid with adjustable alpha.

## Performance

Hybrid search excels with:
- Abbreviations (GAN, LLaMA)
- Named entities (Biden, Salvador Dali)
- Geographic locations (Strait of Hormuz)
- Exact code snippets

## Limitations

- Two algorithms = higher latency than semantic alone
- Computational cost for model development
- Not all vector DBs support hybrid natively

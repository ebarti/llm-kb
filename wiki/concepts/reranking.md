---
title: "Reranking"
type: concept
sources: ["[[sources/pinecone-rerankers-two-stage]]", "[[sources/superlinked-hybrid-search-reranking]]", "[[sources/hybrid-search-rag-optimization]]", "[[sources/hybrid-search-bm25-splade-vector]]", "[[sources/ragflow-rag-review-2025]]"]
related: ["[[concepts/bi-encoder-vs-cross-encoder]]", "[[concepts/two-stage-retrieval]]", "[[concepts/hybrid-search]]", "[[concepts/vector-search]]", "[[concepts/colbert]]", "[[concepts/retrieval-augmented-generation]]"]
last_compiled: 2026-04-05
summary: "Using cross-encoder models to re-score and reorder retrieval candidates, improving RAG precision by 30-50% by applying query-specific analysis to the top-k results from fast initial retrieval."
---

## Overview

Reranking is the process of applying a more accurate (but slower) model to re-score and reorder the candidates returned by an initial retrieval step. In RAG pipelines, this means using a cross-encoder to refine the results from [[concepts/vector-search]] or [[concepts/hybrid-search]] before passing them to the LLM.

## Why Reranking Is Necessary

The fundamental problem: [[concepts/bi-encoder-vs-cross-encoder|bi-encoders]] must compress all document meaning into a single vector without knowing the future query. This compression is lossy — relevant documents may be ranked lower than irrelevant ones.

Increasing the retrieval top_k to catch these misranked documents creates a new problem: **LLM recall degrades as context window grows**. More retrieved documents means more noise for the LLM to filter through.

Reranking resolves both issues: retrieve many candidates (high recall), then rerank to keep only the most relevant (high precision).

## How It Works

1. **Initial retrieval**: Bi-encoder or hybrid search returns top-k candidates (typically k=25-100)
2. **Cross-encoder scoring**: Each (query, candidate) pair is processed through a transformer model that outputs a relevance score (0-1)
3. **Reorder**: Sort candidates by cross-encoder score
4. **Truncate**: Pass only the top-n (typically n=3-5) to the LLM

## Performance Impact

- Leading organizations report **30-50% improvement in retrieval precision** from adding reranking
- In one demonstration, reranking moved the most relevant chunk from **position 23 to position 1**
- The cross-encoder's query-specific analysis replaces generic averaged representations with targeted relevance assessment

## Key Models

| Model | Parameters | Speed | License |
|-------|-----------|-------|---------|
| ms-marco-MiniLM-L-12-v2 | 33M | 2-5ms/pair (CPU) | Open |
| bge-reranker-v2-m3 | ~500M | ~10ms/pair (GPU) | Open |
| Cohere Rerank | Unknown | API-based | Proprietary |
| FlashRank | ~20M | <1ms/pair | Open |

## Computational Cost

The tradeoff is clear: a BERT cross-encoder scoring every document in a 40M collection would take >50 hours per query on a V100 GPU. Vector search does the same initial filtering in <100ms. Reranking only the top-25 results adds ~50-250ms — acceptable latency for the dramatic quality improvement.

## Sources

- [[sources/pinecone-rerankers-two-stage]] — two-stage architecture and practical impact
- [[sources/superlinked-hybrid-search-reranking]] — reranking in full RAG pipeline

## Related Concepts

- [[concepts/bi-encoder-vs-cross-encoder]] — the architectural distinction driving reranking
- [[concepts/two-stage-retrieval]] — the pipeline architecture
- [[concepts/hybrid-search]] — often combined with reranking
- [[concepts/vector-search]] — the fast first stage before reranking

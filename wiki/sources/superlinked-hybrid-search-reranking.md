---
title: "Source: Optimizing RAG with Hybrid Search & Reranking"
type: source-summary
source: "[[raw/superlinked-hybrid-search-reranking]]"
related: ["[[concepts/hybrid-search]]", "[[concepts/reranking]]", "[[concepts/two-stage-retrieval]]", "[[concepts/bm25]]"]
last_compiled: 2026-04-05
summary: "VectorHub's guide to the full RAG retrieval pipeline: BM25 + vector search fusion via RRF or weighted alpha, followed by transformer-based reranking, with specific model recommendations and performance benchmarks."
reading_time: "2 min"
---

## Key Points

- Full pipeline: BM25 keyword search + vector search → fusion → reranking → LLM generation
- BM25 formula: BM25(D,Q) = Σ IDF(q) × [TF(q,D) × (k₁+1)] / [TF(q,D) + k₁×(1-b+b×|D|/avgdl)]
- Fusion: H = (1-α)K + αV; also RRF(d) = Σ 1/(k + r(d))
- Model stack: bge-base-en-v1.5 (embeddings), Cohere Rerank (reranker), Zephyr-7B-Beta 4-bit (LLM)
- Hybrid excels with abbreviations, named entities, geographic locations, exact code snippets
- ChromaDB requires manual EnsembleRetriever; Weaviate offers native hybrid
- Tradeoff: two algorithms = higher latency than semantic alone

## Detailed Summary

This article presents the most complete picture of a production [[concepts/two-stage-retrieval]] pipeline for RAG. It demonstrates how [[concepts/hybrid-search]] (BM25 + vector) handles cases where either approach alone fails — abbreviations like "GAN" and "LLaMA" that pure semantic search may misinterpret, and conceptual queries that pure keyword search misses. The [[concepts/reranking]] stage then refines the fused results before passing to the LLM. The article also highlights a practical implementation concern: not all vector databases support hybrid search natively, making database choice a key architectural decision.

## Related Concepts

- [[concepts/hybrid-search]] — the retrieval strategy
- [[concepts/reranking]] — the refinement stage
- [[concepts/two-stage-retrieval]] — the overall pipeline
- [[concepts/bm25]] — the keyword scoring algorithm

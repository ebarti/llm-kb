---
title: "Rerankers and Two-Stage Retrieval"
source: "https://www.pinecone.io/learn/series/rag/rerankers/"
author: "Pinecone"
date_published: 2024-02-10
date_ingested: 2026-04-05
tags: [reranking, cross-encoder, bi-encoder, two-stage-retrieval, RAG]
type: article
status: raw
discovered_via: search
---

# Rerankers and Two-Stage Retrieval — Pinecone

## Cross-Encoders vs Bi-Encoders

**Bi-Encoders (Embedding Models):** Compress document meaning into single vectors (768 or 1536 dims). Process queries same as documents. Create embeddings before query time. Compression causes information loss.

**Cross-Encoders (Rerankers):** Given a query-document pair, output a similarity score. Receive raw information into full transformer computation at query time. Analyze meaning specific to each query rather than creating generic averaged representations.

## Why Reranking Improves Retrieval

Core problem: increasing top_k to boost retrieval recall damages LLM performance. "LLM recall degrades as we put more tokens in the context window."

Solution: "maximize retrieval recall by retrieving plenty of documents and then maximize LLM recall by minimizing the number of documents that make it to the LLM."

## Performance Scale

Given 40M records, BERT reranker on V100 GPU would take >50 hours per query. Vector search does the same in <100ms. This is why two-stage architecture is essential.

## Architecture

Two-stage: embedding models as first-stage (fast), rerankers as second-stage (accurate). Retrieve top_k=25, rerank to top_n=3.

## Model

bge-reranker-v2-m3 referenced as reranking model. multilingual-e5-large used as embedding model (1024 dims, cosine metric).

## Practical Impact

Reranking moved highly relevant chunks from position 23 to position 1, replacing generic information with specific, query-relevant content.

---
title: "Bi-Encoder vs Cross-Encoder"
type: concept
sources: ["[[sources/pinecone-rerankers-two-stage]]", "[[sources/jina-colbert-late-interaction]]", "[[sources/pinecone-embedding-models-rundown]]"]
related: ["[[concepts/text-embeddings]]", "[[concepts/reranking]]", "[[concepts/two-stage-retrieval]]", "[[concepts/colbert-late-interaction]]"]
last_compiled: 2026-04-05
summary: "The two fundamental architectures for neural text matching: bi-encoders encode texts independently for fast retrieval but lose information; cross-encoders process pairs jointly for high accuracy but cannot scale to full collections."
---

## Overview

Bi-encoders and cross-encoders represent the two ends of a fundamental tradeoff in neural information retrieval: **speed vs accuracy**. Understanding this tradeoff is essential for designing retrieval pipelines, as it motivates [[concepts/two-stage-retrieval]], [[concepts/reranking]], and hybrid architectures like [[concepts/colbert-late-interaction]].

## Bi-Encoders (Embedding Models)

Bi-encoders encode queries and documents **independently** into single dense vectors, then compute similarity (typically cosine) between vectors.

**Architecture**:
```
Query  → Transformer → Mean Pool → Single Vector (384-3072 dims)
Document → Transformer → Mean Pool → Single Vector (384-3072 dims)
Similarity = cosine(query_vec, doc_vec)
```

**Strengths**:
- Document vectors can be pre-computed offline — no per-query encoding cost for documents
- Enables sub-millisecond retrieval over millions/billions of vectors via [[concepts/hnsw]]
- Scales to any collection size

**Weaknesses**:
- All document meaning must be compressed into a single vector — **information is lost**
- No awareness of the query when encoding documents (the embedding was created before the query existed)
- Relevant documents may rank below the top-k cutoff

**Examples**: all-MiniLM-L6-v2, E5, BGE, OpenAI ada-002, Cohere embed-v3

## Cross-Encoders (Rerankers)

Cross-encoders process query and document **together** as a single input, outputting a relevance score.

**Architecture**:
```
[CLS] Query [SEP] Document [SEP] → Transformer → Relevance Score (0-1)
```

**Strengths**:
- Full attention between query and document tokens — **no information loss**
- Query-specific document analysis — each document is scored in context of the actual query
- Significantly more accurate than bi-encoders (leading organizations see 30-50% precision improvement)

**Weaknesses**:
- Must run inference for every query-document pair — **does not scale**
- Given 40M documents, a BERT cross-encoder on V100 GPU takes >50 hours per query
- Cannot pre-compute document representations

**Examples**: ms-marco-MiniLM-L-12-v2 (33M params), bge-reranker-v2-m3, Cohere Rerank

## The Middle Ground: Late Interaction

[[concepts/colbert-late-interaction]] bridges the gap. It encodes queries and documents independently (like bi-encoders) but at the **token level** rather than producing a single vector. The MaxSim operation then computes fine-grained similarity (like cross-encoders) but much faster — 180x fewer FLOPs than BERT at k=10, and 23,000x fewer at k=2000.

## Why This Matters for RAG

The bi-encoder/cross-encoder tradeoff directly motivates [[concepts/two-stage-retrieval]]:

1. **Stage 1 (bi-encoder)**: Retrieve top-25 candidates in <100ms using pre-computed embeddings
2. **Stage 2 (cross-encoder)**: Rerank those 25 candidates for maximum relevance
3. **Pass top-3 to LLM**: Minimizes context window usage while maximizing relevance

This architecture was demonstrated to move the most relevant passage from position 23 (bi-encoder ranking) to position 1 (after cross-encoder reranking).

## Sources

- [[sources/pinecone-rerankers-two-stage]] — the case for two-stage retrieval
- [[sources/jina-colbert-late-interaction]] — ColBERT as middle ground
- [[sources/pinecone-embedding-models-rundown]] — bi-encoder model comparison

## Related Concepts

- [[concepts/text-embeddings]] — bi-encoder outputs
- [[concepts/reranking]] — cross-encoder application
- [[concepts/two-stage-retrieval]] — the architecture combining both
- [[concepts/colbert-late-interaction]] — the middle ground

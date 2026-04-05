---
title: "Bi-Encoder vs Cross-Encoder vs ColBERT"
type: comparison
subjects: ["[[concepts/bi-encoder-vs-cross-encoder]]", "[[concepts/colbert-late-interaction]]", "[[concepts/reranking]]"]
sources: ["[[sources/pinecone-rerankers-two-stage]]", "[[sources/jina-colbert-late-interaction]]"]
last_compiled: 2026-04-05
summary: "The three neural retrieval architectures compared: bi-encoders (fast, lossy single-vector), cross-encoders (accurate but slow pairwise scoring), and ColBERT (token-level late interaction bridging both) — with speed, accuracy, and storage tradeoffs."
---

## Overview

Neural text retrieval has three major architectures, each representing a different point on the speed-accuracy-storage tradeoff curve. Understanding when to use each — and how to combine them — is essential for designing effective [[concepts/two-stage-retrieval]] pipelines.

## Comparison Table

| Dimension | Bi-Encoder | ColBERT (Late Interaction) | Cross-Encoder |
|-----------|-----------|---------------------------|---------------|
| **Encoding** | Independent, single vector per text | Independent, per-token vectors | Joint (query + document together) |
| **Pre-computation** | Yes (store 1 vector/doc) | Yes (store N vectors/doc) | No |
| **Query latency** | <100ms at millions of docs | ~100ms at millions | >50 hours at 40M docs |
| **Scalability** | Billions | Millions | Thousands (as reranker) |
| **Accuracy** | Good | Very Good | Best |
| **Storage per doc** | 1 vector (384-3072 dims) | ~128 vectors × 128 dims | N/A |
| **Information loss** | High (whole doc → 1 vector) | Low (per-token context preserved) | None (full attention) |
| **Typical role** | Stage 1 retrieval | Stage 1 or stage 1.5 | Stage 2 reranking |

## Speed Comparison (vs BERT Cross-Encoder)

| Reranking depth | ColBERT advantage |
|----------------|-------------------|
| k=10 | 180x fewer FLOPs |
| k=1000 | 13,900x fewer FLOPs |
| k=2000 | 23,000x fewer FLOPs |

## How Each Scores Relevance

### Bi-Encoder
```
score = cosine(encode(query), encode(document))
```
Query and document encoded separately. All meaning compressed into single vectors.

### ColBERT (MaxSim)
```
score = Σᵢ maxⱼ (qᵢ · dⱼ)  // for each query token, find best document token
```
Per-token encoding preserves fine-grained semantics. MaxSim finds the best match for each query token.

### Cross-Encoder
```
score = MLP([CLS] query [SEP] document [SEP])
```
Full attention between all query and document tokens. Maximum expressiveness.

## When to Use Each

### Bi-Encoder
- First-stage retrieval over large collections
- Real-time applications with strict latency requirements
- When storage is not a constraint (1 vector per doc is cheap)

### ColBERT
- When bi-encoder recall is insufficient but cross-encoder is too slow
- Long document retrieval (Jina-ColBERT supports 8192 tokens)
- When storage budget allows ~100x more vectors per document
- As a "stage 1.5" between retrieval and reranking

### Cross-Encoder
- Always as a reranker after initial retrieval (never as primary retrieval)
- When maximum accuracy is critical and latency budget is >50ms
- Top-k reranking where k is small (25-100)

## Optimal Pipeline

The three architectures combine naturally:

```
Collection (millions) → Bi-Encoder retrieval → top-100
    → ColBERT re-scoring → top-25
    → Cross-Encoder reranking → top-3
    → LLM generation
```

Or the simpler two-stage variant:

```
Collection → Bi-Encoder/Hybrid retrieval → top-25
    → Cross-Encoder reranking → top-3
    → LLM
```

## Key Models

| Architecture | Models |
|-------------|--------|
| Bi-Encoder | all-MiniLM-L6-v2, E5, BGE, OpenAI ada-002, Cohere embed-v3 |
| ColBERT | ColBERTv2, Jina-ColBERT-v2 |
| Cross-Encoder | ms-marco-MiniLM-L-12-v2, bge-reranker-v2-m3, Cohere Rerank |

## Sources

- [[sources/pinecone-rerankers-two-stage]] — bi-encoder limitations and cross-encoder reranking
- [[sources/jina-colbert-late-interaction]] — ColBERT architecture and performance

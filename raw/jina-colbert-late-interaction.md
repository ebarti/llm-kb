---
title: "What is ColBERT and Late Interaction and Why They Matter in Search?"
source: "https://jina.ai/news/what-is-colbert-and-late-interaction-and-why-they-matter-in-search/"
author: "Jina AI"
date_published: 2024-06-10
date_ingested: 2026-04-05
tags: [ColBERT, late-interaction, retrieval, MaxSim, Jina-ColBERT, ColBERTv2]
type: article
status: raw
discovered_via: search
---

# ColBERT and Late Interaction — Jina AI

## Core Architecture

ColBERT (Contextualized Late Interaction over BERT) generates "a bag of contextualized embeddings for a query and a bag for a document" — each token gets its own embedding, unlike single-vector models.

## Late Interaction Mechanism

Separates query and document encoding until final retrieval stage. Enables pre-computation of document representations while maintaining semantic depth.

### MaxSim Operation

1. Batch dot-product: Computing term-wise similarities between query and document embeddings
2. Max-pooling: For each query term, finding highest similarity score across document terms
3. Summation: Aggregating max-similarities across all query terms for final score

## Training

Original ColBERT: pairwise ranking loss Loss = max(0, 1 − S(q, d+) + S(q, d−)).
ColBERTv2: denoised supervision with iterative hard-negative mining using cross-encoder (MiniLM) for distillation.

## Architectural Specifications

- Query Encoder: Prepends [Q] token, pads to Nq=32 tokens with [mask], applies BERT + CNN + L2 normalization
- Document Encoder: Prepends [D] token, no padding
- Embedding Dimension: 128 per token

## Performance

- At reranking depth k=10: BERT requires 180× more FLOPs than ColBERT
- At k=1000: 13,900× more FLOPs
- At k=2000: 23,000× more FLOPs
- Recall@50 exceeds BM25's Recall@1000

## ColBERTv2: Residual Compression

Reduces storage by 6-10× via residual compression (capturing differences from centroids).

## Jina-ColBERT

Extends context to 8192 tokens (vs original 512). BEIR avg NDCG: 52.6 vs ColBERTv2's 51.7. LoCo (long-context): 83.7 vs 74.3.

## Key Hyperparameters

- Learning Rate: 3×10−6
- Batch Size: 32
- Training Iterations: 200k (MS MARCO)
- FAISS sub-vectors: 16 per embedding

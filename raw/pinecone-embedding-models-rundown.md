---
title: "Choosing an Embedding Model"
source: "https://www.pinecone.io/learn/series/rag/embedding-models-rundown/"
author: "Pinecone"
date_published: 2024-01-15
date_ingested: 2026-04-05
tags: [embeddings, bi-encoder, cross-encoder, OpenAI, E5, Cohere, MTEB, RAG]
type: article
status: raw
discovered_via: search
---

# Choosing an Embedding Model — Pinecone

## How Embedding Models Work

Embedding models convert human-readable text into machine-readable vectors. They identify semantic meaning in queries and match it against documents by compressing text into vector representations.

## Models Compared

**Proprietary Models:**
- **OpenAI text-embedding-ada-002**: 1536 dimensions, took 9:07 to embed ~42K chunks
- **Cohere embed-english-v3.0**: 1024 dimensions, took 5:32 to embed dataset

**Open-Source:**
- **E5-base-v2**: 768 dimensions, fastest at 3:53 (ran on GPU)

## Technical Implementation Details

**Asymmetric Search Support:**
Cohere uses an `input_type` parameter specifying "search_document" or query vectors. E5 uses text prefixes: `"passage:"` for documents and `"query:"` for queries.

**Tokenization Process:**
Models require converting plain text into integer sequences (e.g., `[0, 531, 81, 944, ...]`). Maximum supported lengths vary — 512 tokens typically suffices for paragraph-length content.

**Mean Pooling:**
E5 generates token-level embeddings, masks padding tokens to prevent degradation, then averages outputs into single vectors.

## Benchmark Considerations

The MTEB leaderboards (hosted by Hugging Face) track performance metrics. Key evaluation columns include "average" and "retrieval average" scores, sequence length capacity, and model size. However, results are self-reported; some open-source models appear fine-tuned specifically for benchmarks with inflated performance claims.

## Performance Metrics

Storage costs scale with dimensionality — higher dimensions increase infrastructure expenses. Inference speed varies significantly between local (GPU-accelerated) and API-based approaches.

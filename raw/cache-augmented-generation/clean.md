---
title: "Don't Do RAG: When Cache-Augmented Generation is All You Need"
source: "https://arxiv.org/html/2412.15605v1"
author: "Various (arXiv)"
date_published: 2024-12-20
date_ingested: 2026-04-05
tags: [cag, rag-alternative, kv-cache, long-context, retrieval]
type: paper
status: raw
discovered_via: search
---

# Don't Do RAG: When Cache-Augmented Generation is All You Need

## Overview

Cache-Augmented Generation (CAG) is proposed as a streamlined alternative to RAG for knowledge-intensive tasks. Rather than retrieving information during inference, CAG preloads documents and caches key-value parameters for faster, more reliable responses.

## Core Problem with Traditional RAG

Conventional RAG systems suffer from three main challenges: retrieval latency, potential errors in document selection, and increased system complexity.

## Methodology: Three-Phase Framework

**Phase 1 — Preloading:** Documents are preprocessed and their key-value cache computed once via KV-Encode(D), stored for repeated use.

**Phase 2 — Inference:** During query processing, the precomputed cache loads alongside the question, enabling direct answer generation without retrieval.

**Phase 3 — Cache Reset:** The KV cache is efficiently truncated between sessions to reset state, allowing quick reinitialization.

## When CAG Outperforms RAG

Experimental results on SQuAD and HotPotQA benchmarks:
- **Performance:** CAG achieved higher BERTScores across most test configurations
- **Speed:** Generation times dramatically faster (0.85s vs 9.24s for HotPotQA-Small)
- **Reliability:** Eliminates retrieval ranking errors

## Key Advantages

1. **Unified Context:** The model processes all documents holistically, enabling comprehensive multi-hop reasoning
2. **Reduced Complexity:** No separate retriever and generator components
3. **Deterministic Behavior:** Removes variability from document ranking algorithms

## Limitations

- Works best when knowledge bases are of limited, manageable size
- All relevant documents must fit within extended context windows (128k tokens for Llama 3.1 8B)
- Less suitable for large-scale, dynamic knowledge bases requiring continuous updates

## Conclusion

As long-context LLMs evolve with expanding context windows, CAG presents a compelling case for rethinking default reliance on retrieval pipelines — particularly for applications with bounded, stable knowledge requirements.

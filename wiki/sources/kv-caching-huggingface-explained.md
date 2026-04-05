---
title: "Source: KV Caching Explained — Optimizing Transformer Inference"
type: source-summary
source: "[[raw/kv-caching-huggingface-explained]]"
related: ["[[concepts/kv-cache]]", "[[concepts/grouped-query-attention]]", "[[concepts/paged-attention]]", "[[concepts/self-attention]]"]
tags: [KV-cache, transformer-inference, optimization]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Hugging Face tutorial on KV caching: stores Key/Value states from attention layers to avoid redundant computation during autoregressive generation, achieving 5.21x speedup on T4 GPU, with overview of optimization techniques (GQA, MQA, PagedAttention, quantization)."
---

## Key Points

- KV cache stores intermediate Key and Value tensors from attention layers during inference
- Eliminates redundant recomputation: each new token only computes its own Q, K, V
- Benchmark: 5.21x speedup (11.7s vs 61s for 300 tokens on T4 GPU)
- Memory grows linearly with sequence length: 2 * num_layers * num_heads * head_dim * seq_len * bytes
- Optimization techniques: GQA (reduce KV heads), MQA (single KV head), PagedAttention (virtual memory), quantization (FP8/INT8)
- Default enabled in Hugging Face Transformers via use_cache=True

## Detailed Summary

This Hugging Face tutorial provides a practical introduction to KV caching, the most fundamental inference optimization for autoregressive transformers. Without KV caching, generating each new token requires recomputing attention over all previous tokens — an O(n^2) operation per generation step. With KV caching, previously computed Key and Value projections are stored and reused, reducing per-step computation to O(n).

The tutorial walks through the mechanics: on the first forward pass, K and V tensors for all input tokens are computed and cached. For each subsequent token, only the new token's Q, K, V are computed. The new K and V are appended to the cache, and attention is computed using the full cached K, V with just the new Q. This transforms generation from quadratic to linear in the number of already-generated tokens.

The practical impact is dramatic: on a T4 GPU generating 300 tokens, KV caching reduces latency from 61 seconds to 11.7 seconds — a 5.21x speedup with identical output quality.

The article briefly surveys optimization techniques for managing KV cache memory: [[concepts/grouped-query-attention]] reduces the number of KV heads, [[concepts/paged-attention]] applies virtual memory management principles to cache allocation, and quantization (FP8/INT8) reduces per-element storage.

## Concepts Introduced or Discussed

- [[concepts/kv-cache]] — the core optimization
- [[concepts/grouped-query-attention]] — reducing KV cache via shared heads
- [[concepts/paged-attention]] — virtual memory for KV cache

## Metadata

- **Author**: Hugging Face (not-lain)
- **Date Published**: 2024-10
- **Format**: tutorial article
- **URL**: https://huggingface.co/blog/not-lain/kv-caching

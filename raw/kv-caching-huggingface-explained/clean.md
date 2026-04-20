---
title: "KV Caching Explained: Optimizing Transformer Inference Efficiency"
source: "https://huggingface.co/blog/not-lain/kv-caching"
author: "Hugging Face (not-lain)"
date_published: 2024-10-01
date_ingested: 2026-04-05
tags: [KV-cache, transformer-inference, optimization, autoregressive]
type: article
status: raw
discovered_via: search
---

# KV Caching Explained

## What is KV Caching?

A technique that stores intermediate Key (K) and Value (V) states from attention layers during inference to avoid redundant computations. Instead of recomputing attention for all previous tokens when generating each new token, the model reuses cached K and V projections.

## How KV Caching Works

1. First Generation: Calculate and store K and V for initial input
2. Subsequent Tokens: Retrieve cached K,V and append new token's K,V
3. Efficient Attention: Compute attention using cached K,V with new Query (Q)
4. Update: Add generated token to input and repeat

## Performance Impact

| Feature | Standard Inference | KV Caching |
|---------|-------------------|-----------|
| Speedup | Baseline | ~5.21x faster |
| Computation | Repeats for each word | Reuses past calculations |
| Memory | Lower per-step, grows linearly | Extra storage, efficient overall |

Benchmark: T4 GPU, generating 300 tokens — 11.7 seconds with KV caching vs 61 seconds without (~5.21x faster).

## Memory Implications

The KV cache grows linearly with sequence length:
- For each layer and each attention head, K and V tensors accumulate
- Memory = 2 * num_layers * num_heads * head_dim * seq_len * bytes_per_element
- For large models with long sequences, KV cache can consume tens of GB

## Optimization Techniques

- **Grouped Query Attention (GQA)**: Reduces number of KV heads to fraction of query heads
- **Multi-Query Attention (MQA)**: Single KV head shared across all query heads
- **PagedAttention (vLLM)**: Virtual memory management for KV cache blocks
- **Quantization**: FP8 or INT8 KV cache reduces memory by 2-4x
- **Sliding Window**: Only cache recent tokens (with attention sinks for stability)

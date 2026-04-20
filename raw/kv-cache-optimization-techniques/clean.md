---
title: "Techniques for KV Cache Optimization in Large Language Models"
source: "https://www.omrimallis.com/posts/techniques-for-kv-cache-optimization/"
author: "Omri Mallis"
date_published: 2024-06-15
date_ingested: 2026-04-05
tags: [KV-cache, inference-optimization, GQA, MQA, sliding-window, PagedAttention]
type: article
status: raw
discovered_via: search
---

# Techniques for KV Cache Optimization in Large Language Models

## Core Problem

The KV cache consumes substantial GPU memory during LLM inference. For Llama-2-13B at full context (4096 tokens) with batch size 8, cache memory reaches approximately 25GB — nearly equivalent to model parameter storage itself.

## Memory Calculation

Cache size = 2 * 2 * head_dim * n_heads * n_layers * max_context_length * batch_size

Per-token requirements:
- Llama-2-7B: 512KB
- Llama-2-13B: 800KB
- Gemma-2B: 144KB

## Optimization Techniques

### 1. Grouped-Query Attention (GQA)

GQA reduces the number of attention heads used for key-value computation while maintaining the full number for queries. Key-value pairs share across multiple query heads, reducing cache footprint by factor of n_heads / n_kv_heads.

Implementation examples:
- Llama-2-70B: 8x reduction (64 heads to 8 KV heads)
- Mistral-7B: 4x reduction
- Gemma-2B: 8x reduction (144KB to 18KB per token)

### 2. Sliding Window Attention (SWA)

Restricts attention computation to a fixed window of W preceding tokens. Older key-value vectors are evicted through a sliding mechanism.

Key insight: Information regarding older tokens is stored in the key and value vectors of the upper layers, enabling theoretical attendance to W * n_layers tokens while caching only W vectors.

Mistral-7B: W=4096 window with 8192 context, achieving 2x cache reduction combined with 4x GQA factor.

### 3. PagedAttention

Cache management abstraction layer (implemented in vLLM):
- Allocates GPU memory dynamically in non-contiguous blocks
- Maintains virtual-to-physical mapping tables
- Enables prompt sharing across parallel requests
- Reduces memory wastage from 60-80% to 4%

### 4. Cross-Layer KV Sharing

Through sliding window attention's layered architecture, information propagates across layers, enabling attendance to distant tokens without exhaustive caching.

### 5. Distributed KV Cache

For massive contexts (GPT-4: 128k tokens; Gemini 1.5: 1M tokens), cache distributes across multiple GPUs with each GPU handling a subset of attention heads independently.

## Multi-Query Attention (MQA)

Uses a single key head and single value head shared across all h attention heads at each layer. Greatly reduces linear projections that the model must calculate and store.

GQA is a generalization of MQA: using an intermediate number of key-value heads (more than 1 but less than query heads). Query heads divided into groups, each sharing a single key and value head.

## Real-World Adoption

- Falcon: GQA with 1 group (7B) and 8 groups (40B, 175B)
- Llama 2: GQA with 1 group (7B, 13B) and 8 groups (70B)
- Mistral 7B and Mixtral 8x7B: GQA with 8 groups

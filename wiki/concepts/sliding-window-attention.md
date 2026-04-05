---
title: "Sliding Window Attention"
type: concept
sources: ["[[sources/kv-cache-optimization-techniques]]"]
related: ["[[concepts/sparse-attention]]", "[[concepts/kv-cache]]", "[[concepts/self-attention]]"]
last_compiled: 2026-04-05
summary: "Sparse attention restricting each token to attend only to the W most recent tokens, bounding KV cache size while leveraging layer stacking for an effective receptive field of W * n_layers."
---

## Overview

Sliding Window Attention (SWA) is a form of [[concepts/sparse-attention]] where each token attends only to its W preceding tokens. Older KV entries are evicted as new tokens arrive, bounding cache memory to W entries per layer regardless of total sequence length.

## Key Insight

While each individual layer sees only W tokens, information propagates through the layer stack. After L layers, the effective receptive field is W * L tokens. For Mistral-7B (W=4096, 32 layers), the theoretical receptive field is 131,072 tokens while caching only 4,096 per layer.

## Implementation

Mistral-7B: W=4096 window supporting 8192-token context at half the cache cost. Combined with 4x GQA reduction, total cache savings reach 8x.

## Tradeoff

SWA trades exact long-range attention for bounded memory. Fine-grained attention to distant tokens is lost, relying on indirect propagation through intermediate layers. This works well for most natural language tasks but may miss very long-range dependencies that require direct attention.

## Sources

- [[sources/kv-cache-optimization-techniques]] — implementation details and Mistral-7B example

## Related Concepts

- [[concepts/sparse-attention]] — the broader category
- [[concepts/kv-cache]] — the bottleneck SWA addresses
- [[concepts/grouped-query-attention]] — complementary optimization (often combined)

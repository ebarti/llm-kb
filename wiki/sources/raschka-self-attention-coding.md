---
title: "Source: Understanding and Coding Self-Attention Variants in LLMs"
type: source-summary
source: "[[raw/raschka-self-attention-coding]]"
related: ["[[concepts/self-attention]]", "[[concepts/multi-head-attention]]", "[[concepts/causal-attention]]", "[[concepts/cross-attention]]", "[[entities/sebastian-raschka]]"]
last_compiled: 2026-04-05
summary: "Sebastian Raschka's code-first deep dive into self-attention, multi-head attention, causal masking, and cross-attention with PyTorch implementations and mathematical foundations."
---

## Key Points

- Self-attention projects inputs into Q, K, V via learned weight matrices, then computes scaled dot-product attention
- Scaling by sqrt(d_k) prevents numerical instability during training by keeping weight vector magnitudes similar
- [[concepts/multi-head-attention]] runs parallel heads with independent Q/K/V matrices; each head can focus on different sequence aspects
- [[concepts/causal-attention]] masks future tokens using -inf before softmax (e^(-inf) -> 0), essential for decoder-style LLMs
- [[concepts/cross-attention]] uses queries from one sequence against keys/values from another, enabling encoder-decoder architectures
- Llama 2 (7B) uses 32 attention heads with 4,096-dimensional embeddings

## Detailed Summary

Raschka provides a ground-up implementation of all four attention variants used in modern LLMs. Starting from basic [[concepts/self-attention]], he shows how three weight matrices (W_q, W_k, W_v) transform input embeddings into query, key, and value vectors. The unnormalized attention weight between positions i and j is simply q(i) dot k(j), scaled by sqrt(d_k) and softmaxed.

For [[concepts/multi-head-attention]], independent heads each learn separate projections. The key insight is that multiple heads capture different relationship types — not just more capacity, but genuinely different attention patterns.

[[concepts/causal-attention]] applies a triangular mask before softmax: above-diagonal entries become -inf, which softmax converts to zero probability. This prevents decoder models like GPT and Llama from "cheating" by attending to future tokens during training.

[[concepts/cross-attention]] differs by sourcing queries and keys/values from different sequences — the decoder's representations query against the encoder's output, enabling conditional generation.

## Related Concepts

- [[concepts/self-attention]] — core mechanism with full math and code
- [[concepts/causal-attention]] — masked attention for autoregressive generation
- [[concepts/cross-attention]] — inter-sequence attention for encoder-decoder models
- [[concepts/flash-attention]] — referenced as production optimization

---
title: "Linear Attention"
type: concept
sources: ["[[sources/attention-mechanisms-comprehensive-survey]]"]
related: ["[[concepts/self-attention]]", "[[concepts/attention-mechanisms]]", "[[concepts/flash-attention]]", "[[concepts/mamba]]", "[[comparisons/softmax-vs-linear-attention]]"]
tags: [linear-attention, efficient-attention, kernel-methods, subquadratic]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Approximating softmax attention by decomposing it via kernel functions to avoid materializing the N x N attention matrix — reducing complexity from O(N^2 * d) to O(N * d^2), but with significant expressiveness tradeoffs that limit practical adoption."
---

## Overview

Linear attention is a family of techniques that reduce the quadratic complexity of standard [[concepts/self-attention]] by reformulating the attention computation to avoid building the full N x N attention matrix. The key idea: express the softmax exponential as a kernel function, then exploit the associative property of matrix multiplication to change the order of operations.

In standard attention, the computation is: **softmax(QK^T) V** — requiring the N x N matrix QK^T.

In linear attention, the computation becomes: **phi(Q) * (phi(K)^T * V)** — computing K^T * V first (a d x d matrix) then multiplying by Q, avoiding the N x N intermediate.

## How the Kernel Trick Works

Standard attention: Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V

The softmax creates a nonlinear similarity function between queries and keys. Linear attention approximates this with a kernel function phi():

1. Replace softmax(q_i^T k_j) with phi(q_i)^T phi(k_j)
2. Factor out: output_i = (phi(q_i)^T * sum_j(phi(k_j) * v_j^T)) / (phi(q_i)^T * sum_j(phi(k_j)))
3. The sums over j can be precomputed once and shared across all queries
4. Result: O(N * d^2) instead of O(N^2 * d)

When d << N (typical for long sequences), this is a dramatic improvement.

## Key Variants

| Method | Kernel phi() | Year | Notes |
|--------|-------------|------|-------|
| **Performer** | Random feature maps (FAVOR+) | 2020 | Unbiased softmax approximation |
| **Linformer** | Low-rank projection of K, V | 2020 | Projects sequence length, not attention |
| **Random Feature Attention** | Random Fourier features | 2021 | Bridges kernel methods and attention |
| **CosFormer** | Cosine-based reweighting | 2022 | Non-negative attention without softmax |
| **Agent Attention** | Agent tokens aggregate/broadcast | 2023 | Hybrid softmax + linear |
| **Softmax Linear Attention** | Head-level softmax gating | 2026 | Restores winner-take-all dynamics |

## The Expressiveness Gap

Despite theoretical elegance, linear attention consistently underperforms softmax attention. Research identifies three root causes:

1. **Injectivity**: Softmax attention is injective (different inputs produce different outputs); linear attention is not, causing "semantic confusion" where distinct inputs map to identical outputs
2. **Sharpness**: Softmax produces peaked distributions enabling precise retrieval; linear attention produces smoother distributions that blur information
3. **Local modeling**: Effective local pattern matching requires the sharp attention peaks that linear attention lacks

The softmax function's "winner-take-all" property — concentrating weight on the most relevant positions — turns out to be crucial for precise information retrieval.

## Hybrid Approaches

Research suggests combining both:
- **Early and final layers**: Can safely use linear attention (processing is less retrieval-dependent)
- **Middle layers**: Must preserve softmax attention (where precise retrieval is critical)
- **Agent Attention**: Uses a small set of "agent tokens" to aggregate global information via softmax, then broadcasts to all positions via linear attention

## When Linear Attention Makes Sense

Linear attention is most appropriate when:
- Sequence lengths are very long (>16K tokens) and quadratic cost is prohibitive
- Tasks are more about global aggregation than precise retrieval
- Used in hybrid architectures where softmax handles retrieval-critical layers
- Inference latency is the primary constraint

It is less appropriate when:
- Precise factual retrieval is required (e.g., question answering)
- Sequence lengths are moderate (<4K tokens) where quadratic cost is manageable
- [[concepts/flash-attention]] is available (often faster than linear attention in practice for moderate lengths)

## Open Questions

- Can the expressiveness gap be fully closed while maintaining linear complexity?
- Is the optimal softmax-vs-linear split architecture-dependent or universal?
- How does linear attention interact with [[concepts/kv-cache]] optimization?
- Will [[concepts/mamba]] and SSMs prove to be a better path to linear-time sequence modeling?

## Sources

- [[sources/attention-mechanisms-comprehensive-survey]] — mathematical foundations of attention variants

## Related Concepts

- [[concepts/self-attention]] — the standard quadratic mechanism being approximated
- [[concepts/flash-attention]] — IO-aware exact attention (complementary approach)
- [[concepts/sparse-attention]] — another subquadratic approach via sparsity
- [[concepts/mamba]] — alternative architecture avoiding attention entirely
- [[comparisons/softmax-vs-linear-attention]] — detailed comparison

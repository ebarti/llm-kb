---
title: "Sparse Attention"
type: concept
sources: ["[[sources/flashattention-3-paper]]", "[[sources/ssm-vs-transformers-tradeoffs]]", "[[sources/attention-mechanisms-comprehensive-survey]]"]
related: ["[[concepts/self-attention]]", "[[concepts/flash-attention]]", "[[concepts/sliding-window-attention]]", "[[concepts/transformer-architecture]]", "[[concepts/linear-attention]]", "[[concepts/attention-mechanisms]]", "[[concepts/attention-sinks]]"]
last_compiled: 2026-04-05
summary: "Attention mechanisms computing only a subset of the full N x N token interactions — via fixed patterns (Longformer), block routing, clustering, or periodic strides — reducing quadratic complexity toward linear."
---

## Overview

Sparse attention addresses the O(N^2) complexity of full [[concepts/self-attention]] by restricting which token pairs interact. Instead of every token attending to every other token, sparse methods select subsets based on fixed patterns, learned routing, or content-based clustering.

## Key Approaches

### Fixed-Pattern Sparsity

**Longformer**: Combines local sliding window attention with task-specific global attention tokens. Each token attends to W neighbors plus designated global tokens.

**BigBird**: Mixes random attention, local attention, and global attention — the combination provably approximates full attention.

### Block Sparsity

Organizes tokens into blocks and applies attention at the block level. Block-sparse methods select which blocks interact via heuristic scoring or trainable gating.

### Clustering-Based

Groups key-value pairs by content similarity or position, then applies attention within and between clusters.

### Linear Attention

Replaces softmax with kernel approximations: Attention(Q,K,V) ~= phi(Q) * (phi(K)^T * V). This reformulation enables O(N) complexity. Recent implementations (e.g., Kimi Linear) achieve 75% KV cache reduction and up to 6x decoding throughput. Modern approaches use linear attention together with standard attention in hybrid configurations.

### Periodic Sparse (pi-Attention)

Factorizes attention into ring-local neighborhoods with periodic stride skips. Provides predictable coverage of distant tokens while keeping per-layer complexity linear.

## Relationship to Other Efficiency Methods

| Method | Approach | Complexity | Exact? |
|--------|----------|-----------|--------|
| Full attention | All pairs | O(N^2) | Yes |
| [[concepts/flash-attention]] | IO-optimized tiling | O(N^2) compute, O(N) memory | Yes |
| Sparse attention | Subset of pairs | O(N * k) | Approximate |
| Linear attention | Kernel approximation | O(N) | Approximate |
| [[concepts/state-space-models]] | No attention | O(N) | N/A |

## Sources

- [[sources/flashattention-3-paper]] — context for why sparse attention exists alongside FlashAttention
- [[sources/ssm-vs-transformers-tradeoffs]] — sparse attention as one efficiency approach

## Related Concepts

- [[concepts/self-attention]] — the full-complexity mechanism being sparsified
- [[concepts/flash-attention]] — IO-optimized exact attention (complementary approach)
- [[concepts/sliding-window-attention]] — a specific form of sparse attention
- [[concepts/state-space-models]] — avoids attention entirely

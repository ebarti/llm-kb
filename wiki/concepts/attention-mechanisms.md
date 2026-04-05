---
title: "Attention Mechanisms"
type: concept
sources: ["[[sources/attention-mechanisms-comprehensive-survey]]", "[[sources/streamingllm-attention-sinks]]", "[[sources/flashattention-3-tri-dao-blog]]"]
related: ["[[concepts/self-attention]]", "[[concepts/cross-attention]]", "[[concepts/multi-head-attention]]", "[[concepts/transformer-architecture]]", "[[concepts/flash-attention]]", "[[concepts/linear-attention]]", "[[concepts/attention-sinks]]", "[[concepts/grouped-query-attention]]", "[[concepts/kv-cache]]", "[[concepts/memory-augmented-neural-networks]]"]
tags: [attention, transformer, neural-networks, foundation]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The family of mechanisms enabling neural networks to dynamically focus on relevant parts of their input — from Bahdanau's 2014 additive attention through the 2017 Transformer's scaled dot-product self-attention to modern variants (flash, linear, sparse, grouped query)."
---

## Overview

Attention mechanisms are the most important innovation in modern deep learning. They allow neural networks to dynamically weight different parts of their input based on relevance to the current computation, rather than treating all inputs equally or relying on fixed-window processing. Inspired by the cognitive psychology concept of selective attention (the "cocktail party effect"), attention enables models to focus on what matters and ignore what does not.

The core idea: given a **query** (what am I looking for?), compare it against **keys** (what is available?) to produce weights that determine how much each **value** (the actual information) contributes to the output.

## Historical Evolution

| Year | Contribution | Significance |
|------|-------------|-------------|
| 1990s | Fast weight controllers | Anticipated key-value memory mechanisms |
| 2014 | Bahdanau et al. — additive attention | First attention for NMT, eliminated encoder bottleneck |
| 2015 | Luong et al. — multiplicative attention | Simplified scoring with dot products |
| 2017 | Vaswani et al. — Transformer | Self-attention as sole mechanism, replacing RNNs entirely |
| 2019 | Sparse Transformer | Subquadratic attention via sparsity patterns |
| 2020 | Performer, Linformer | Linear attention approximations |
| 2022 | [[concepts/flash-attention]] | IO-aware exact attention, memory O(N) |
| 2023 | [[concepts/grouped-query-attention]] | KV head sharing for efficient inference |
| 2023 | [[concepts/attention-sinks]] | Discovery of positional attention concentration |
| 2024 | FlashAttention-3 | 75% H100 utilization via async + FP8 |

## The Attention Formula

The standard scaled dot-product attention:

**Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V**

Where:
- **Q** (queries): what each position is looking for (shape: n x d_k)
- **K** (keys): what each position advertises (shape: m x d_k)
- **V** (values): what each position provides (shape: m x d_v)
- **sqrt(d_k)**: scaling factor preventing softmax saturation

The softmax produces a probability distribution, so each output is a weighted average of all value vectors.

## Scoring Function Variants

| Function | Formula | Complexity | Used In |
|----------|---------|-----------|---------|
| Additive (Bahdanau) | v^T tanh(W_q q + W_k k) | O(n * d_a) | Original NMT |
| Multiplicative (Luong) | q^T W k | O(d_q * d_k) | Early seq2seq |
| Dot-Product | q^T k | O(d) | Efficient but unstable |
| Scaled Dot-Product | q^T k / sqrt(d_k) | O(d) | Transformers (standard) |

## The Attention Family Tree

```
Attention Mechanisms
├── By source of Q, K, V
│   ├── Self-Attention — Q, K, V from same sequence
│   ├── Cross-Attention — Q from decoder, K/V from encoder
│   └── Causal Attention — masked self-attention (no future tokens)
├── By head structure
│   ├── Single-Head — one attention computation
│   ├── Multi-Head (MHA) — parallel heads, unique KV per head
│   ├── Multi-Query (MQA) — shared single KV head
│   └── Grouped Query (GQA) — grouped KV heads (dominant 2024+)
├── By efficiency approach
│   ├── Flash Attention — IO-aware tiling, exact, O(N) memory
│   ├── Sparse Attention — attend to subsets, subquadratic
│   ├── Linear Attention — kernel trick, O(N*d^2)
│   └── Sliding Window — local attention with attention sinks
└── By domain
    ├── Language — standard transformer attention
    ├── Vision — ViT patch attention, spatial attention
    ├── Multimodal — cross-modal attention (CLIP)
    └── Science — AlphaFold, molecular modeling
```

## Complexity and the Quadratic Wall

Standard self-attention has:
- **Time complexity**: O(n^2 * d) — quadratic in sequence length
- **Memory complexity**: O(n^2) — storing the full attention matrix

This creates a hard wall: doubling sequence length quadruples memory. A 128K-token context with 64-dimensional heads requires storing a 128K x 128K matrix (16 billion entries) per head per layer.

Approaches to this wall define a major axis of modern research:
- [[concepts/flash-attention]]: same computation, better memory management (exact)
- [[concepts/linear-attention]]: approximate attention, O(N * d^2) complexity
- [[concepts/sparse-attention]]: attend to subsets, O(N * sqrt(N)) or O(N * log(N))
- [[concepts/mamba]]: replace attention entirely with selective state spaces, O(N)

## Attention as Memory

Attention can be understood as a form of **content-addressable memory**. The query is an address, the keys are stored addresses, and the values are stored content. The softmax produces a soft lookup — a weighted combination of all stored values based on address similarity.

This framing connects modern transformers to the older tradition of [[concepts/memory-augmented-neural-networks]]: Neural Turing Machines and Differentiable Neural Computers used the same soft attention mechanism to read and write external memory matrices. The transformer's innovation was recognizing that this same mechanism, applied to the input sequence itself (self-attention), is sufficient for most tasks without a separate external memory.

## Key Properties

1. **Permutation equivariance**: Self-attention is equivariant to query reordering but invariant to key-value reordering — outputs change order with inputs but are blind to key ordering. This is why [[concepts/positional-encoding]] is essential.

2. **Parallelizability**: All positions compute simultaneously, unlike RNNs which must process sequentially. This is the primary practical advantage over recurrence.

3. **Global receptive field**: Every position can attend to every other position in a single layer, unlike CNNs which need many layers for long-range interactions.

## Open Questions

- Can linear-time attention alternatives (Mamba, RWKV) fully replace softmax attention for language?
- What is the fundamental capacity limit of attention for knowledge storage?
- How do attention patterns change with scale (1B vs 100B parameters)?
- Can attention be made truly efficient for million-token contexts?

## Sources

- [[sources/attention-mechanisms-comprehensive-survey]] — rigorous mathematical treatment from first principles
- [[sources/flashattention-3-tri-dao-blog]] — state-of-the-art efficient attention implementation
- [[sources/streamingllm-attention-sinks]] — discovery of attention sink phenomenon

## Related Concepts

- [[concepts/self-attention]] — the most common attention type (same-sequence)
- [[concepts/cross-attention]] — inter-sequence attention for encoder-decoder
- [[concepts/multi-head-attention]] — parallel attention heads
- [[concepts/flash-attention]] — IO-aware efficient implementation
- [[concepts/grouped-query-attention]] — KV head sharing for inference
- [[concepts/attention-sinks]] — positional attention concentration phenomenon
- [[concepts/linear-attention]] — subquadratic approximations
- [[concepts/kv-cache]] — inference-time attention state management
- [[concepts/transformer-architecture]] — the architecture built on attention
- [[concepts/memory-augmented-neural-networks]] — attention's precursor in external memory

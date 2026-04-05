---
title: "State Space Models (SSMs)"
type: concept
sources: ["[[sources/mamba-state-space-models-visual-guide]]", "[[sources/ssm-vs-transformers-tradeoffs]]"]
related: ["[[concepts/mamba]]", "[[concepts/transformer-architecture]]", "[[concepts/self-attention]]", "[[comparisons/transformers-vs-state-space-models]]"]
last_compiled: 2026-04-05
summary: "Sequence models based on continuous-time state equations, offering linear-time inference and fixed memory — the primary architectural alternative to transformers, especially for long sequences and raw data."
---

## Overview

State Space Models (SSMs) are a family of sequence models inspired by continuous-time dynamical systems. They represent sequences through two equations:

- **State equation**: h'(t) = A h(t) + B x(t)
- **Output equation**: y(t) = C h(t) + D x(t)

Where A, B, C, D are learnable matrices, h(t) is the hidden state, x(t) is the input, and y(t) is the output. SSMs compress all historical context into a fixed-size hidden state, offering O(L) inference complexity versus the [[concepts/transformer-architecture]]'s O(L^2).

Albert Gu frames the difference: "Transformers are like databases" storing every token, while "SSMs are like brains" with finite-sized memories processing inputs continuously.

## Key SSM Architectures

### S4 (Structured State Space, 2021)

Combines three innovations:
1. **HiPPO initialization**: Initializes matrix A using Legendre polynomials for long-range memory
2. **Structured matrices**: Constrains A to enable efficient computation
3. **Dual representation**: Discretization creates both convolutional (training) and recurrent (inference) forms

### [[concepts/mamba]] (Selective SSM / S6, 2023)

Addresses SSMs' fundamental limitation — time-invariance — by making B, C, and step size delta input-dependent. See [[concepts/mamba]] for details.

### Mamba-2 (2024)

Reveals SSMs and Transformers are mathematically related through structured semiseparable matrices. 2-8x faster than Mamba-1.

## Computational Properties

| Property | SSMs | Transformers |
|----------|------|-------------|
| Training | Convolutional (parallel) | Attention (parallel) |
| Inference complexity | O(L) per step | O(L^2) per step |
| Memory | Fixed (hidden state) | Linear growth (KV cache) |
| Context window | Theoretically unlimited | Hard limit |
| Hardware fit | Good (sequential) | Excellent (matmul) |

## Where SSMs Excel

Based on the Goomba Lab analysis:

- **Byte-level and character-level** language modeling
- **DNA sequences**: 4-character alphabet, no meaningful tokenization
- **Audio and speech**: High sampling rates, continuous signals
- **Time series**: Streaming data with variable resolution
- **Raw visual data**: Before patch tokenization

## Where Transformers Win

- **Tokenized language**: BPE-tokenized text where each token is semantically meaningful
- **In-context learning**: Exact recall and retrieval of specific tokens from context
- **Established infrastructure**: Better tooling, optimization, and hardware support

## Hybrid Architectures

The frontier has converged on hybrid SSM-attention models using 3:1 to 10:1 ratios of SSM layers to attention layers:

- **H3** (Hungry Hungry Hippos): 2 SSM layers + multiplicative gating + 2 attention layers
- **Jamba**: Matched full Transformer at 1.3-2.7B scale
- **Zamba, Samba**: Various SSM-attention interleaving patterns
- **NVIDIA Nemotron-H** (560B+): Production-scale hybrid
- **Granite 4.0**: 82.41% HumanEval with hybrid architecture

## Sources

- [[sources/mamba-state-space-models-visual-guide]] — visual walkthrough of SSM/S4/Mamba math
- [[sources/ssm-vs-transformers-tradeoffs]] — Albert Gu's analysis of when to use each

## Related Concepts

- [[concepts/mamba]] — the leading selective SSM architecture
- [[concepts/transformer-architecture]] — the architecture SSMs challenge
- [[concepts/flash-attention]] — similar hardware-aware optimization philosophy
- [[comparisons/transformers-vs-state-space-models]] — detailed comparison

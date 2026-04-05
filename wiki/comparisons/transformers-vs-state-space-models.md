---
title: "Transformers vs State Space Models"
type: comparison
subjects: ["[[concepts/transformer-architecture]]", "[[concepts/state-space-models]]"]
sources: ["[[sources/ssm-vs-transformers-tradeoffs]]", "[[sources/mamba-state-space-models-visual-guide]]"]
last_compiled: 2026-04-05
summary: "Transformers excel on semantically tokenized text with exact recall; SSMs dominate on raw/byte-level data with linear complexity — hybrid architectures (3:1 to 10:1 SSM:attention) emerging as optimal."
---

## Overview

The [[concepts/transformer-architecture]] and [[concepts/state-space-models]] (SSMs, particularly [[concepts/mamba]]) represent fundamentally different approaches to sequence modeling. Albert Gu frames it: "Transformers are like databases" storing every observation; "SSMs are like brains" with finite-sized memories processing inputs continuously. By 2025, the field has converged on hybrid architectures combining both.

## Comparison Table

| Dimension | Transformers | SSMs (Mamba) |
|-----------|-------------|-------------|
| **Core mechanism** | Pairwise attention (QKV) | State recurrence (Ax + Bu) |
| **Training complexity** | O(N^2) (O(N) memory with FlashAttention) | O(N) via convolution/parallel scan |
| **Inference per token** | O(N) (attend to full KV cache) | O(1) (constant-time recurrence) |
| **Memory** | Linear growth (KV cache) | Fixed (hidden state) |
| **Context window** | Hard limit (cache size) | Theoretically unlimited |
| **In-context learning** | Exact recall of any token | Fuzzy contextual understanding |
| **Tokenized language** | Excellent | Good (slightly worse) |
| **Byte/character data** | Poor | Excellent |
| **DNA, audio, time series** | Moderate | Excellent |
| **Hardware fit** | Excellent (matmul on GPUs) | Good (sequential recurrence) |
| **Ecosystem** | Massive (tooling, optimization) | Growing rapidly |

## Where Each Excels

### Transformers

- Semantically tokenized text (BPE tokens carry meaning)
- Tasks requiring exact retrieval from context ("what was the 5th item?")
- Well-established infrastructure (FlashAttention, KV cache optimization, vLLM)

### SSMs

- High-resolution data where tokens lack inherent semantic meaning
- Byte-level and character-level language modeling
- DNA sequences, raw audio, time series
- Extremely long sequences (linear scaling)

## The Key Insight

Gu's heuristic: "The inductive bias of soft attention is hard attention." Transformers implicitly assume each token is semantically meaningful and worth individual attention. When this assumption holds (BPE-tokenized language), transformers excel. When it doesn't (bytes, characters, DNA), SSMs excel because they process at a more appropriate abstraction level.

## Hybrid Architectures

The frontier has converged on combining both:

| Model | Architecture | SSM:Attention Ratio |
|-------|-------------|-------------------|
| H3 | SSM + gating + attention | ~3:1 |
| Jamba | Interleaved Mamba + attention | ~4:1 |
| Zamba, Samba | Various interleaving | 3:1 to 10:1 |
| NVIDIA Nemotron-H | Hybrid at 560B+ scale | Optimized |
| Granite 4.0 | Hybrid (82.41% HumanEval) | Optimized |

## When to Use Each

- **Tokenized language tasks**: Either; Transformers have more mature tooling
- **Raw sequential data**: SSMs or hybrids strongly preferred
- **Mixed modalities**: Hybrid (interleave SSM layers for compression + attention layers for retrieval)
- **Inference-bound workloads**: SSMs (linear vs quadratic per-token cost)
- **Existing infrastructure**: Transformers (better tooling, optimization)

## Sources

- [[sources/ssm-vs-transformers-tradeoffs]] — Albert Gu's analysis of architectural tradeoffs
- [[sources/mamba-state-space-models-visual-guide]] — Mamba architecture details

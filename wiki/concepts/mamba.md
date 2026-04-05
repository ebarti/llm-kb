---
title: "Mamba (Selective State Space Model)"
type: concept
sources: ["[[sources/mamba-state-space-models-visual-guide]]", "[[sources/ssm-vs-transformers-tradeoffs]]"]
related: ["[[concepts/state-space-models]]", "[[concepts/transformer-architecture]]", "[[concepts/selective-state-space]]"]
last_compiled: 2026-04-05
summary: "The leading SSM architecture making state transitions input-dependent (selective), with hardware-aware kernel fusion and parallel scan — achieving transformer-competitive performance with linear-time inference."
---

## Overview

Mamba, introduced by Albert Gu and Tri Dao in December 2023, is the most successful [[concepts/state-space-models]] architecture. Its key innovation is the **Selective State Space** mechanism (S6): making the state transition matrices B, C, and discretization step size delta all **input-dependent**, enabling content-aware reasoning that previous time-invariant SSMs could not achieve.

## The Problem Mamba Solves

Traditional SSMs use fixed matrices A, B, C regardless of input content. This means they process "the" the same way whether it appears in "the cat" or "the theorem." Mamba makes these matrices functions of the current input, allowing the model to dynamically decide what information to compress into its hidden state and what to ignore.

## Selective State Space (S6)

For each input token x(t):
- B(t) = f_B(x(t)) — input-dependent state update
- C(t) = f_C(x(t)) — input-dependent output mapping
- delta(t) = f_delta(x(t)) — input-dependent discretization step size

The step size delta acts as a dynamic gate:
- Large delta: emphasize the current input (high information density)
- Small delta: rely more on accumulated state (low information density)

## Hardware-Aware Design

Mamba achieves practical speed through GPU-optimized implementation:

1. **Kernel Fusion**: Combines discretization, selective scan, and output projection into a single GPU kernel, avoiding intermediate HBM writes
2. **SRAM Computation**: All intermediate states computed in fast SRAM
3. **Recomputation over Storage**: During backpropagation, intermediate states are recomputed rather than stored, because SRAM recomputation is faster than HBM reads
4. **Parallel Scan**: Exploits the associativity of state transitions to parallelize sequential recurrence during training

This philosophy mirrors [[concepts/flash-attention]]: both optimize for the GPU memory hierarchy rather than theoretical FLOP counts.

## Performance

- **Training**: Uses convolutional representation for full parallelization
- **Inference**: Switches to recurrent mode for O(L) per-token generation (vs O(L^2) for transformers)
- **Context**: Handles million-token sequences with up to 5x inference throughput improvement
- **Quality**: Matches or exceeds transformer performance on many benchmarks

By 2026: Jamba achieves 67.4% MMLU and 59.9% GSM8K; Granite 4.0 scores 82.41% HumanEval with hybrid architecture.

## Mamba-2

Research reveals SSMs and Transformers are mathematically related through decompositions of structured semiseparable matrices. Mamba-2 exploits this connection for 2-8x speedup while maintaining competitive language modeling performance.

## Sources

- [[sources/mamba-state-space-models-visual-guide]] — visual explanation of selective scan and hardware optimization
- [[sources/ssm-vs-transformers-tradeoffs]] — performance comparisons and hybrid architectures

## Related Concepts

- [[concepts/state-space-models]] — the broader architecture family
- [[concepts/transformer-architecture]] — the architecture Mamba competes with
- [[concepts/flash-attention]] — similar hardware-aware optimization approach
- [[comparisons/transformers-vs-state-space-models]] — detailed comparison

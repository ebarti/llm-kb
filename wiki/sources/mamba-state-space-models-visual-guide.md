---
title: "Source: A Visual Guide to Mamba and State Space Models"
type: source-summary
source: "[[raw/mamba-state-space-models-visual-guide]]"
related: ["[[concepts/state-space-models]]", "[[concepts/mamba]]", "[[concepts/selective-state-space]]", "[[entities/mamba]]"]
last_compiled: 2026-04-05
summary: "Visual walkthrough of SSM fundamentals, S4's HiPPO initialization, Mamba's selective scan innovation making state transitions input-dependent, and hardware-aware kernel fusion optimization."
---

## Key Points

- SSMs model sequences via state equation (h' = Ah + Bx) and output equation (y = Ch + Dx)
- S4 combines SSMs + HiPPO initialization (Legendre polynomials for long-range memory) + discretization
- Mamba's key innovation: makes B, C, and step size delta input-dependent (Selective State Space / S6)
- Selective scan uses parallel scan algorithm exploiting associativity for efficient training
- Hardware-aware: kernel fusion eliminates intermediate DRAM writes; recomputation faster than DRAM reads
- Training uses convolutional mode (parallel); inference switches to recurrent mode (O(L) vs O(L^2))
- Mamba-2 shows SSMs and Transformers are related through structured semiseparable matrices; 2-8x faster

## Detailed Summary

Grootendorst provides an accessible visual walkthrough of the mathematical foundations behind [[concepts/state-space-models]] and [[concepts/mamba]]. Starting from continuous-time SSM equations, he shows how discretization via zero-order hold creates dual representations: a convolutional form for parallel training and a recurrent form for efficient sequential inference.

The critical limitation of traditional SSMs is time-invariance: matrices A, B, C are fixed regardless of input content. [[concepts/mamba]] solves this by making B, C, and the discretization step size delta all functions of the current input token. This [[concepts/selective-state-space]] mechanism lets the model dynamically decide what information to compress into its hidden state versus what to ignore.

The hardware-aware design is crucial for practical speed: kernel fusion combines discretization, selective scan, and output computation into a single GPU kernel, avoiding expensive HBM round-trips. Intermediate states are recomputed during backpropagation rather than stored, because SRAM recomputation is faster than DRAM reads.

## Related Concepts

- [[concepts/state-space-models]] — the foundational architecture family
- [[concepts/mamba]] — the specific selective SSM innovation
- [[concepts/transformer-architecture]] — the architecture Mamba challenges
- [[concepts/flash-attention]] — similar hardware-aware optimization philosophy

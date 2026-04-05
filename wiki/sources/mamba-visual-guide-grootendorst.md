---
title: "Source: A Visual Guide to Mamba and State Space Models"
type: source-summary
source: "[[raw/mamba-visual-guide-grootendorst]]"
related: ["[[concepts/mamba]]", "[[concepts/state-space-models]]", "[[concepts/self-attention]]", "[[comparisons/transformers-vs-state-space-models]]"]
tags: [mamba, SSM, selective-scan, transformers-alternative]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Maarten Grootendorst's visual walkthrough of Mamba: SSM fundamentals (state/output equations), the LTI limitation of traditional SSMs, Mamba's selective mechanism (input-dependent B, C, delta), hardware-aware parallel scan, and performance comparison with transformers."
---

## Key Points

- SSMs use state equations h(k) = Ah(k-1) + Bx(k) and output equations y(k) = Ch(k) + Dx(k)
- Traditional SSMs suffer Linear Time Invariance (LTI): fixed parameters regardless of input content
- Mamba makes B, C, and delta input-dependent — the "selective" in Selective State Space
- Delta (step size) acts as dynamic gate: large = emphasize input, small = rely on accumulated state
- Three hardware optimizations: kernel fusion, parallel scan (via associativity), recomputation over storage
- HiPPO matrix initialization for long-range dependencies via Legendre polynomials
- Matches or exceeds transformer performance with O(L) inference vs O(L^2)
- 5x higher inference throughput than transformers of same size

## Detailed Summary

Grootendorst provides the most accessible visual explanation of how Mamba works, starting from first principles of state space models and building to the selective mechanism that makes Mamba competitive with transformers.

The fundamental insight is that traditional SSMs process every token identically because their A, B, C matrices are fixed. This is equivalent to a linear time-invariant system — it cannot distinguish "the" in "the cat" from "the" in "the theorem." Mamba breaks this limitation by making B, C, and the discretization step size delta all functions of the current input token.

The step size delta is particularly important: it controls the balance between the current input and the accumulated hidden state. A large delta gives high weight to the current token (useful for information-dense content), while a small delta relies more on the compressed history (useful for filler tokens). This creates a dynamic gating mechanism analogous to how [[concepts/self-attention]] dynamically weights different positions.

The hardware-aware implementation mirrors [[concepts/flash-attention]]'s philosophy: optimize for the GPU memory hierarchy, not theoretical FLOP counts. Kernel fusion keeps all intermediate states in SRAM, parallel scan parallelizes the inherently sequential recurrence using the associative property of matrix multiplication, and recomputation during backpropagation trades cheap SRAM compute for expensive HBM reads.

## Concepts Introduced or Discussed

- [[concepts/mamba]] — the architecture being explained
- [[concepts/state-space-models]] — the broader family
- [[concepts/self-attention]] — the mechanism Mamba competes with

## Metadata

- **Author**: Maarten Grootendorst
- **Date Published**: 2024-02
- **Format**: newsletter article (visual)
- **URL**: https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mamba-and-state

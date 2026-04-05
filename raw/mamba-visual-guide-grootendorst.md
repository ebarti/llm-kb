---
title: "A Visual Guide to Mamba and State Space Models"
source: "https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mamba-and-state"
author: "Maarten Grootendorst"
date_published: 2024-02-01
date_ingested: 2026-04-05
tags: [mamba, state-space-models, SSM, selective-scan, transformers-alternative]
type: article
status: raw
discovered_via: search
---

# A Visual Guide to Mamba and State Space Models

## SSM Fundamentals

State Space Models represent systems through mathematical equations tracking state changes:
- State equation: h(k) = A*h(k-1) + B*x(k)
- Output equation: y(k) = C*h(k) + D*x(k)

Matrices A, B, C, D are learnable parameters. The state vector maintains compressed historical information.

## Traditional SSM Limitations

Conventional SSMs suffer from Linear Time Invariance (LTI) — parameters remain constant regardless of input content. Two critical problems:
1. Content-awareness failure: unable to selectively focus on relevant tokens
2. Poor performance on induction tasks: cannot dynamically recall patterns

## Mamba's Selective Mechanism

Mamba introduces input-dependent parameters. Rather than fixed B and C matrices, Mamba makes these dependent on the input.

Key innovation: A smaller step size (delta) parameter ignores specific words; larger values focus more on input tokens. This selectivity mirrors attention while maintaining recurrent efficiency.

## Computational Complexity

- Transformers: O(L^2) quadratic during inference
- Recurrent SSMs: O(L) linear, processing sequentially
- Mamba: Combines linear inference with parallelizable training through parallel scan algorithm

## Hardware-Aware Algorithm

Three optimization strategies:
1. Kernel fusion: Continuously performs computations without intermediate DRAM-SRAM writes
2. Parallel scan: Decomposes sequential operations into parallelizable chunks via associative property
3. Recomputation: Recomputes intermediate states during backward pass rather than storing

## Architecture Components

- HiPPO matrix initialization for long-range dependencies via Legendre polynomials
- Discretization via zero-order hold converting continuous to discrete
- Selective scan with dynamic matrix operations

## Performance

Matches and sometimes exceeds transformer performance at same size. 5x higher inference throughput. Linear scaling in sequence length. Performance improves on real data up to million-length sequences.

## Comparison with Transformers

| Aspect | Transformers | Mamba |
|--------|-------------|-------|
| Training | Parallelizable via attention | Parallelizable via convolution |
| Inference | O(L^2) | O(L) |
| Context awareness | Dynamic attention | Dynamic parameters |
| Memory state | None (full history) | Compressed (small state) |

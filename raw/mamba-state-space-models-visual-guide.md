---
title: "A Visual Guide to Mamba and State Space Models"
source: "https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mamba-and-state"
author: "Maarten Grootendorst"
date_published: 2024-02-19
date_ingested: 2026-04-05
tags: [mamba, state-space-models, SSM, S4, selective-scan, transformer-alternatives]
type: article
status: raw
discovered_via: search
---

# A Visual Guide to Mamba and State Space Models

## Core Architecture

State Space Models (SSMs) represent sequences through two fundamental equations:
- State equation: describes how hidden state h(t) evolves based on input x(t) through matrices A and B
- Output equation: translates state to output y(t) through matrices C and D

Matrices A, B, C, and D are learnable parameters that govern system dynamics.

## S4: Structured State Space Models

S4 combines three key components:
1. State Space Models for sequence representation
2. HiPPO initialization on matrix A to capture long-range dependencies using Legendre polynomials
3. Discretization via zero-order hold technique, creating both recurrent and convolutional representations

This discretization enables parallel training using convolution while maintaining efficient sequential inference through recurrence.

## Mamba's Innovations

### Selective State Space (S6)

Mamba addresses SSMs' fundamental limitation: time-invariance. Traditional SSMs use fixed A, B, C matrices regardless of input content, preventing content-aware reasoning.

Mamba makes B, C, and step size delta input-dependent:
- Different B and C matrices for each token
- Dynamic step size controls whether to emphasize current input or previous context
- Enables selective information compression into hidden states

### Selective Scan Algorithm

The selective scan operates through:
- Parallel scan algorithm for parallelized computation during training
- Dynamic matrices prevent fixed kernel convolution; recurrent representation becomes necessary
- Parallel scan exploits associativity to compute sequences in parallel chunks

### Hardware-Aware Optimization

- Kernel fusion combines discretization, selective scan, and C multiplication into single kernel
- Eliminates intermediate DRAM writes between SRAM transfers
- Recomputation strategy: intermediate states recomputed during backpropagation (faster than DRAM reads)

## Performance Characteristics

- Training: Uses convolutional representation for parallelization
- Inference: Switches to recurrent representation for efficient sequential generation with O(L) complexity vs Transformers' O(L^2)
- Linear-time inference scaling
- Unbounded context length potential
- Compressed memory footprint through selective state management

## Mamba-2 Development

Research shows SSMs and Transformers are closely related through decompositions of structured semiseparable matrices, leading to Mamba-2 which is 2-8x faster while remaining competitive with Transformers on language modeling.

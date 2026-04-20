---
title: "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision"
source: "https://arxiv.org/abs/2407.08608"
author: "Tri Dao, Jay Shah"
date_published: 2024-07-11
date_ingested: 2026-04-05
tags: [flash-attention, efficient-attention, GPU-optimization, Hopper, FP8, transformer-inference]
type: paper
status: raw
discovered_via: search
---

# FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision

## Overview

FlashAttention-3 addresses the attention mechanism bottleneck in Transformers and LLMs. FlashAttention-2 achieved only 35% utilization on H100 GPUs, prompting development of techniques leveraging newer Hopper hardware capabilities.

## The FlashAttention Lineage

### FlashAttention (v1, 2022)
An algorithm that reorders the attention computation and leverages tiling and recomputation to significantly speed it up and reduce memory usage from quadratic to linear in sequence length. It uses tiling to load blocks of inputs from HBM (GPU memory) to SRAM (fast cache), perform attention with respect to that block, and update the output in HBM. By not writing the large intermediate attention matrices to HBM, it reduces the amount of memory reads/writes, bringing 2-4x wallclock time speedup.

### FlashAttention-2
Further optimized the algorithm with better work partitioning and parallelism, but still achieved only 35% of H100 theoretical FLOPS.

### FlashAttention-3 — Three Main Techniques

1. **Asynchronous Warp Specialization**: Exploits Tensor Cores and TMA (Tensor Memory Accelerator) asynchrony to overlap overall computation and data movement via warp-specialization. Different warps handle different tasks concurrently.

2. **Block-wise Operation Interleaving**: Interleaves block-wise matmul and softmax operations. Instead of completing full matmul then full softmax, these operations alternate at the block level for better pipeline utilization.

3. **FP8 Low-Precision with Block Quantization**: Implements block quantization and incoherent processing that leverages hardware support for FP8 low-precision. Incoherent processing randomizes sign patterns to reduce quantization error.

## Performance Metrics

**FP16 Results:**
- 1.5-2.0x speedup over FlashAttention-2
- 740 TFLOPs/s (75% GPU utilization on H100)
- Up from 35% utilization with FlashAttention-2

**FP8 Results:**
- Nearly 1.2 PFLOPs/s throughput
- 2.6x lower numerical error compared to baseline FP8 attention implementations

## Key Impact

The approach dramatically improves H100 GPU utilization from 35% to 75% in FP16, while delivering comparable accuracy with significantly faster FP8 processing. FlashAttention is now used by most libraries to accelerate Transformer training and inference.

Available at: https://github.com/Dao-AILab/flash-attention

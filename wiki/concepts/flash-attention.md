---
title: "FlashAttention"
type: concept
sources: ["[[sources/flashattention-3-paper]]"]
related: ["[[concepts/self-attention]]", "[[concepts/transformer-architecture]]", "[[concepts/kv-cache]]", "[[entities/tri-dao]]"]
last_compiled: 2026-04-05
summary: "IO-aware attention algorithm using tiling to avoid materializing the N x N attention matrix in GPU HBM — reducing memory from O(N^2) to O(N) and achieving 2-4x speedup. FlashAttention-3 reaches 75% H100 utilization."
---

## Overview

FlashAttention is the most impactful systems-level optimization for the [[concepts/transformer-architecture]]. Introduced by [[entities/tri-dao]] in 2022, it recognizes that [[concepts/self-attention]] is **memory-bound, not compute-bound**: the bottleneck is reading and writing the N x N attention matrix to/from GPU high-bandwidth memory (HBM), not the arithmetic operations.

The solution: **tiling** — load blocks of Q, K, V from HBM into fast on-chip SRAM, compute partial attention, accumulate results, and write only the final output back to HBM. The full N x N attention matrix is never materialized, reducing memory from O(N^2) to O(N).

## Evolution

### FlashAttention v1 (2022)

- IO-aware tiling algorithm with online softmax trick
- Reduces memory from O(N^2) to O(N) for exact attention
- 2-4x wall-clock speedup on standard transformer training
- Recomputation during backward pass (trade compute for memory)

### FlashAttention-2 (2023)

- Better work partitioning and parallelism across GPU warps
- Improved head-parallel scheduling
- Achieves ~35% utilization on H100 GPUs

### FlashAttention-3 (2024)

Three techniques targeting Hopper GPU (H100) hardware features:

1. **Asynchronous Warp Specialization**: Overlaps data movement (TMA) and computation (Tensor Cores) by assigning different warps to each
2. **Block-wise Interleaved Matmul/Softmax**: Alternates matmul and softmax at block level to keep both units busy
3. **FP8 with Incoherent Processing**: Random sign flipping before quantization reduces FP8 error by 2.6x

**Performance:**
- FP16: 740 TFLOPS (75% H100 utilization, up from 35%)
- FP8: ~1.2 PFLOPS
- 1.5-2x faster than FlashAttention-2

## Why It Matters

FlashAttention is now the default attention implementation in virtually all major frameworks (PyTorch, JAX, etc.). It enables:

1. Training with longer sequences (memory no longer scales quadratically)
2. Faster training and inference
3. No approximation — exact attention, identical results to naive implementation
4. Foundation for further optimizations ([[concepts/kv-cache]], [[concepts/sparse-attention]])

## Key Insight: Memory Hierarchy Awareness

GPUs have two levels of memory:
- **SRAM** (~20MB, ~19 TB/s bandwidth): Fast but tiny
- **HBM** (~40-80GB, ~2-3 TB/s bandwidth): Large but slow

Naive attention writes O(N^2) data to HBM. FlashAttention restructures computation to minimize HBM traffic, exploiting the 10x bandwidth gap between SRAM and HBM.

## Sources

- [[sources/flashattention-3-paper]] — FlashAttention-3 paper with performance numbers

## Related Concepts

- [[concepts/self-attention]] — the computation being optimized
- [[concepts/kv-cache]] — complementary inference optimization
- [[concepts/sparse-attention]] — alternative approach to attention efficiency
- [[concepts/state-space-models]] — alternative architecture avoiding quadratic attention entirely

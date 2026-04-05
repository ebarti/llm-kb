---
title: "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision"
source: "https://tridao.me/blog/2024/flash3/"
author: "Tri Dao"
date_published: 2024-07-01
date_ingested: 2026-04-05
tags: [flash-attention, efficient-attention, GPU-optimization, transformer, inference]
type: paper
status: raw
discovered_via: search
---

# FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision

## Three Main Optimization Techniques

### 1. Asynchronous Overlap via Warp Specialization

FlashAttention-3 exploits Hopper GPU's asynchronous Tensor Cores and TMA (Tensor Memory Accelerator) to overlap computation and data movement:

- Inter-warpgroup overlapping: Using pingpong scheduling, separate warpgroups alternate between GEMMs and softmax operations, allowing softmax to execute in parallel with another warpgroup's matrix multiplications.
- Intra-warpgroup overlapping: Within a single warpgroup, softmax partially executes during GEMM operations, though this increases register pressure.

### 2. Interleaved Block-wise Operations

Critical performance bottleneck: "the H100 GPU SXM5 has 989 TFLOPS of FP16 matrix multiply, but only 3.9 TFLOPS (256x less throughput) for special functions." By scheduling softmax exponential calculations alongside matrix operations, underutilized hardware units process exponentials while Tensor Cores handle matmuls.

### 3. Incoherent Processing for FP8 Quantization

Applies random orthogonal transformations (Hadamard matrix with random signs) before quantization. This "spreads out" outliers, reducing quantization error by 2.6x compared to baseline FP8 attention.

## Hopper GPU Features Leveraged

- WGMMA: New warp-group matrix multiply instruction achieving higher throughput
- TMA: Dedicated hardware accelerator for global-to-shared memory transfers, freeing registers for larger tile sizes
- FP8 Support: Doubles Tensor Core throughput (1978 vs 989 TFLOPS)

## Performance Benchmarks

| Metric | FlashAttention-2 | FlashAttention-3 | Improvement |
|--------|------------------|------------------|-------------|
| FP16 Throughput | 350 TFLOPS | 740 TFLOPS | 1.5-2.0x faster |
| GPU Utilization | 35% | 75% | +40 percentage points |
| FP8 Throughput | — | ~1.2 PFLOPS | — |

## Historical Evolution

- FlashAttention v1 (2022): IO-aware tiling, memory O(N^2) to O(N), 2-4x speedup
- FlashAttention-2 (2023): Improved A100 utilization to ~70%
- FlashAttention-3 (2024): Hopper-specific async, FP8, 75% H100 utilization

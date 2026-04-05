---
title: "Source: FlashAttention-3"
type: source-summary
source: "[[raw/flashattention-3-paper]]"
related: ["[[concepts/flash-attention]]", "[[concepts/transformer-architecture]]", "[[concepts/self-attention]]", "[[entities/tri-dao]]"]
last_compiled: 2026-04-05
summary: "FlashAttention-3 achieves 75% H100 utilization (up from 35%) via warp specialization, interleaved matmul/softmax, and FP8 block quantization — reaching 740 TFLOPS in FP16 and 1.2 PFLOPS in FP8."
---

## Key Points

- FlashAttention-2 only achieved 35% utilization on H100 GPUs — a massive hardware underutilization
- Three techniques for Hopper GPUs: (1) async warp specialization, (2) interleaved block-wise matmul/softmax, (3) FP8 with incoherent processing
- FP16: 1.5-2x faster than FlashAttention-2, 740 TFLOPS (75% H100 utilization)
- FP8: ~1.2 PFLOPS with 2.6x lower error than baseline FP8 attention
- FlashAttention v1 (2022) pioneered IO-aware tiling: blocks from HBM to SRAM, compute, update — reducing memory from O(N^2) to O(N)
- Now the standard attention implementation used by all major frameworks

## Detailed Summary

[[concepts/flash-attention]] represents the most impactful systems-level optimization for transformer inference and training. The original FlashAttention (2022) recognized that attention is memory-bound, not compute-bound: the bottleneck is reading/writing the N x N attention matrix to GPU HBM. By tiling the computation — loading blocks to fast SRAM, computing partial attention, accumulating results — it achieves exact attention with O(N) memory and 2-4x wall-clock speedup.

FlashAttention-3 targets Hopper GPU (H100) hardware features: asynchronous Tensor Memory Accelerator (TMA) enables overlapping data movement and computation via warp specialization. Different GPU warps handle data loading versus matmul computation concurrently. Block-wise interleaving of matmul and softmax keeps both the Tensor Cores and scalar units busy simultaneously.

The FP8 contribution uses incoherent processing (random sign flipping of Q/K matrices before quantization) to reduce quantization error by 2.6x compared to naive FP8.

## Related Concepts

- [[concepts/flash-attention]] — the optimization family this paper extends
- [[concepts/self-attention]] — the operation being optimized
- [[concepts/kv-cache]] — related inference optimization
- [[concepts/transformer-architecture]] — the architecture benefiting from these optimizations

---
title: "Source: FlashAttention-3 — Fast and Accurate Attention with Asynchrony and Low-precision"
type: source-summary
source: "[[raw/flashattention-3-tri-dao-blog]]"
related: ["[[concepts/flash-attention]]", "[[concepts/kv-cache]]", "[[concepts/self-attention]]", "[[entities/flashattention]]", "[[entities/tri-dao]]"]
tags: [flash-attention, GPU-optimization, efficient-attention, Hopper]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Tri Dao's blog post on FlashAttention-3: three Hopper-specific optimizations (async warp specialization, interleaved matmul/softmax, FP8 incoherent processing) achieving 740 TFLOPS FP16 (75% H100 utilization) and ~1.2 PFLOPS FP8."
---

## Key Points

- H100 has 989 TFLOPS for matmul but only 3.9 TFLOPS for special functions (256x gap) — softmax is the bottleneck
- Warp specialization overlaps TMA data movement with Tensor Core computation via pingpong scheduling
- Incoherent processing applies Hadamard random sign flipping before FP8 quantization, reducing error by 2.6x
- FlashAttention-3 FP16: 740 TFLOPS (75% utilization, up from 35% in FA-2)
- FlashAttention-3 FP8: ~1.2 PFLOPS
- 1.5-2.0x speedup over FlashAttention-2 in forward pass, 1.5-1.75x in backward pass

## Detailed Summary

[[entities/tri-dao]]'s FlashAttention-3 represents the third generation of IO-aware exact attention algorithms, specifically targeting the NVIDIA H100 Hopper GPU architecture. The core insight is that on Hopper, the matmul-to-special-function throughput ratio is 256:1, making softmax computation the limiting factor once matmul is efficiently tiled.

The first technique, **asynchronous warp specialization**, assigns different GPU warpgroups to different tasks. In inter-warpgroup mode, one warpgroup computes GEMMs while another processes softmax, using pingpong scheduling to keep both hardware units busy.

The second technique, **interleaved block-wise matmul/softmax**, pipelines the two operations at a finer granularity within individual warpgroups, though at the cost of increased register pressure.

The third and most novel technique, **FP8 with incoherent processing**, addresses the fundamental challenge of quantizing attention scores to 8-bit precision. Activation outliers cause severe quantization error. By applying random orthogonal transformations (Hadamard matrix with random signs) before quantization, outlier energy is redistributed evenly across dimensions, reducing quantization error by 2.6x. The Hadamard transform itself is bandwidth-limited and fuses with prior operations like [[concepts/positional-encoding]] (RoPE).

## Concepts Introduced or Discussed

- [[concepts/flash-attention]] — the algorithm family being advanced
- [[concepts/kv-cache]] — complementary inference optimization
- [[concepts/self-attention]] — the computation being optimized
- [[concepts/paged-attention]] — related memory management technique

## Metadata

- **Author**: Tri Dao
- **Date Published**: 2024-07
- **Format**: blog post (technical)
- **URL**: https://tridao.me/blog/2024/flash3/

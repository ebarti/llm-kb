---
title: "Data Parallelism"
type: concept
sources: ["[[sources/jeremy-jordan-distributed-training]]", "[[sources/deepspeed-megatron-frameworks]]"]
related: ["[[concepts/distributed-training]]", "[[concepts/tensor-parallelism]]", "[[concepts/pipeline-parallelism]]", "[[concepts/zero-optimizer]]"]
last_compiled: 2026-04-05
summary: "The simplest distributed training strategy: replicate the full model on each GPU, split input batches, compute gradients independently, then synchronize via all-reduce. Extended by ZeRO to eliminate memory redundancy."
---

## Overview

Data parallelism (DP) is the most common and simplest form of distributed training. Each GPU holds a complete copy of the model and processes a different slice of the input batch. After the backward pass, gradients are averaged across all GPUs via an **all-reduce** operation, ensuring all model copies stay synchronized.

## How It Works

1. **Distribute data**: Split the global batch into N equal parts (one per GPU)
2. **Forward pass**: Each GPU independently processes its batch slice
3. **Backward pass**: Each GPU computes local gradients
4. **All-reduce**: Sum all gradients across GPUs, divide by N
5. **Update**: Apply identical optimizer step on each GPU

The result is mathematically equivalent to training on the full batch on a single GPU, but N times faster (minus communication overhead).

## Communication: All-Reduce

The bottleneck is the all-reduce step. **Ring all-reduce** is the standard algorithm:
- GPUs arranged in a logical ring
- Each GPU sends/receives gradient chunks simultaneously
- After 2(N-1) steps, all GPUs have the complete averaged gradient
- Bandwidth-optimal: utilizes full interconnect capacity

Communication cost scales with model size (total gradient bytes) but is independent of the number of GPUs — making DP highly scalable.

## Limitations

- **Memory**: Each GPU must hold the full model + optimizer states + gradients. For a 175B model with AdamW, this exceeds 1 TB — impossible on any current GPU.
- **Batch size**: Effective batch size scales with GPU count. Too-large batches can degrade training quality.
- **Communication**: All-reduce of full gradients can bottleneck at very large scale.

## Extension: ZeRO

[[concepts/zero-optimizer]] (DeepSpeed) addresses the memory limitation by sharding optimizer states (Stage 1), gradients (Stage 2), and parameters (Stage 3) across data-parallel GPUs. This reduces per-GPU memory by up to the parallelism degree while preserving DP's simplicity.

## Sources

- [[sources/jeremy-jordan-distributed-training]] — all-reduce mechanics, ring algorithm
- [[sources/deepspeed-megatron-frameworks]] — ZeRO stages extending data parallelism

## Related Concepts

- [[concepts/tensor-parallelism]] — splits within layers instead of across batches
- [[concepts/pipeline-parallelism]] — splits across layers
- [[concepts/zero-optimizer]] — memory-efficient extension of DP

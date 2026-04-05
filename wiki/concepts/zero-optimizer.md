---
title: "ZeRO Optimizer"
type: concept
sources: ["[[sources/deepspeed-megatron-frameworks]]"]
related: ["[[concepts/data-parallelism]]", "[[concepts/distributed-training]]", "[[entities/deepspeed]]"]
last_compiled: 2026-04-05
summary: "DeepSpeed's Zero Redundancy Optimizer progressively shards optimizer states (Stage 1), gradients (Stage 2), and parameters (Stage 3) across data-parallel GPUs, reducing per-GPU memory by up to the parallelism degree while preserving data parallelism's simplicity."
---

## Overview

The Zero Redundancy Optimizer (ZeRO) is [[entities/deepspeed]]'s flagship memory optimization technique. Standard [[concepts/data-parallelism]] replicates the full model, optimizer states, and gradients on every GPU — a massive memory waste. ZeRO eliminates this redundancy by sharding these components across the data-parallel group.

## Stages

### Stage 1: Partition Optimizer States
- Each GPU maintains full model parameters and gradients
- Optimizer states (AdamW: 2 momentum buffers per parameter) are sharded
- After optimizer step, updated parameters are broadcast via all-gather
- **Memory reduction**: ~4x for AdamW (optimizer states are 2/3 of total with FP32 master weights)

### Stage 2: Partition Optimizer States + Gradients
- Gradients are also sharded: each GPU only stores gradients for its parameter shard
- During backpropagation, gradients are reduce-scattered to the responsible GPU
- **Memory reduction**: ~8x vs naive data parallelism

### Stage 3: Partition Everything
- Parameters are also sharded: each GPU holds only 1/N of the model
- Parameters are dynamically gathered just-in-time for forward and backward passes, then discarded
- Maximum memory efficiency but highest communication overhead
- **Memory reduction**: ~N x (proportional to parallelism degree)

### ZeRO-Offload
- Extends any stage by moving sharded data to CPU memory or NVMe storage
- Trades compute speed (CPU-GPU data movement) for capacity
- Enables training models that exceed total GPU memory in the cluster

## Trade-offs

| Stage | Memory Saving | Communication Overhead | Complexity |
|-------|--------------|----------------------|------------|
| 1 | Moderate (optimizer states) | Minimal | Low |
| 2 | Good (+ gradients) | Low | Low |
| 3 | Maximum (everything) | High (all-gather per layer) | Moderate |
| Offload | Beyond GPU capacity | Very high (CPU-GPU transfers) | Moderate |

## In Practice

ZeRO integrates simply with PyTorch: wrap model and optimizer via `deepspeed.initialize()`, configure via JSON. No model code changes required (unlike [[concepts/tensor-parallelism]]). This makes ZeRO the default first choice for memory optimization.

## Sources

- [[sources/deepspeed-megatron-frameworks]] — detailed stage descriptions and integration

## Related Concepts

- [[concepts/data-parallelism]] — ZeRO extends DP's memory model
- [[entities/deepspeed]] — the framework providing ZeRO
- [[concepts/distributed-training]] — the broader context

---
title: "Distributed Training"
type: concept
sources: ["[[sources/jeremy-jordan-distributed-training]]", "[[sources/hf-ultrascale-playbook]]", "[[sources/deepspeed-megatron-frameworks]]"]
related: ["[[concepts/data-parallelism]]", "[[concepts/tensor-parallelism]]", "[[concepts/pipeline-parallelism]]", "[[concepts/3d-parallelism]]", "[[concepts/5d-parallelism]]", "[[concepts/zero-optimizer]]", "[[concepts/training-infrastructure]]"]
last_compiled: 2026-04-05
summary: "Splitting LLM training workloads across hundreds or thousands of GPUs using parallelism strategies (data, tensor, pipeline, context, expert) to make training feasible within reasonable time and cost constraints."
---

## Overview

Distributed training is the set of techniques that enable training models too large for a single GPU — or that would take unreasonably long on one — by splitting the work across a cluster of GPUs. Modern frontier LLMs require distributed training as a fundamental necessity, not an optimization: Llama 3.1 405B required 3.8 x 10^25 FLOPs, which would take 609 years on a single H100 GPU. Using 16,000 H100s, Meta completed it in 54 days.

## Why It Is Necessary

A single GPU must hold:
- **Model parameters**: weights of all layers
- **Optimizer states**: AdamW maintains two momentum estimates per parameter (3x parameter memory)
- **Activations**: intermediate values needed for backpropagation
- **Gradients**: one per parameter during backward pass
- **Input data**: current batch

For a 405B parameter model in FP16, parameters alone require ~810 GB — far exceeding any single GPU (H100: 80 GB). With optimizer states, the total can exceed 3 TB.

## Parallelism Strategies

### [[concepts/data-parallelism]]
Replicate the full model on each GPU, split the input batch. Synchronize gradients via all-reduce after each step. Simplest approach, works when model fits on one GPU.

### [[concepts/tensor-parallelism]]
Split individual weight matrices across GPUs within a layer. Communication-intensive (requires all-reduce/all-gather per layer), so best on high-bandwidth intra-node connections (NVLink at 900 GB/s on H100).

### [[concepts/pipeline-parallelism]]
Split layers sequentially across GPUs. Lower communication (only pass activations between stages) but suffers from "pipeline bubbles" (idle GPUs). Micro-batching reduces bubbles. Best for cross-node distribution.

### Context Parallelism (CP)
Split along the sequence length dimension. Emerging technique for models with very long context windows (128K+ tokens).

### Expert Parallelism (EP)
For Mixture-of-Experts (MoE) architectures, distribute different experts across GPUs. Each token is routed to a subset of experts.

## Combining Strategies

### [[concepts/3d-parallelism]]
The standard approach combines DP + TP + PP, mapping to cluster topology:
- **TP within-node**: Leverages NVLink's high bandwidth for frequent communication
- **PP across nodes**: Only passes activations between stages, tolerating InfiniBand latency
- **DP across the cluster**: All-reduce gradients, which can overlap with computation

**Llama 3.1 405B**: TP=8 (within each 8-GPU node), PP=16 (across 16 nodes per pipeline), DP=8-128 (across pipeline replicas). Total: 16,384 GPUs.

### [[concepts/5d-parallelism]]
Extends 3D parallelism with Context Parallelism and Expert Parallelism. Covered in the [[sources/hf-ultrascale-playbook]].

## Communication Primitives

| Operation | Description | Used By |
|-----------|-------------|---------|
| All-Reduce | Sum across all GPUs, result on all | Data parallelism (gradients) |
| All-Gather | Collect shards from all GPUs | ZeRO Stage 3, tensor parallelism |
| Reduce-Scatter | Sum and distribute shards | ZeRO Stage 2 |
| Broadcast | One GPU to all | Parameter initialization |

**Ring all-reduce** is the standard algorithm: GPUs arranged in a ring, each sending/receiving gradient chunks simultaneously, maximizing bandwidth utilization.

## Memory Optimization Techniques

- **[[concepts/zero-optimizer]]**: DeepSpeed ZeRO Stages 1-3 progressively shard optimizer states, gradients, and parameters
- **Activation checkpointing/recomputation**: Discard intermediate activations and recompute during backward pass
- **Gradient accumulation**: Process multiple micro-batches before an optimizer step, simulating larger batch sizes
- **CPU/NVMe offloading**: Move data to slower but larger storage (ZeRO-Offload)

## Sources

- [[sources/jeremy-jordan-distributed-training]] — comprehensive walkthrough with Llama 3.1 example
- [[sources/hf-ultrascale-playbook]] — 4,000+ scaling experiments, 5D parallelism
- [[sources/deepspeed-megatron-frameworks]] — framework-level implementation details

## Related Concepts

- [[concepts/training-infrastructure]] — the hardware foundation
- [[concepts/llm-pretraining]] — the process that requires distributed training
- [[concepts/llm-training-costs]] — communication overhead affects cost

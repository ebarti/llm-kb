---
title: "Training Extremely Large Neural Networks Across Thousands of GPUs"
source: "https://www.jeremyjordan.me/distributed-training/"
author: "Jeremy Jordan"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [distributed-training, data-parallelism, model-parallelism, tensor-parallelism, pipeline-parallelism, gpu-clusters]
type: article
status: raw
discovered_via: search
---

# Distributed Training of Extremely Large Neural Networks

## Computational Scale

Llama 3.1 405B required 3.8 x 10^25 FLOPs using Nvidia H100 GPUs. Training on a single GPU would require approximately 609 years, yet Meta completed it in 54 days using 16,000 H100 GPUs.

## Memory Constraints

Single-GPU training must accommodate:
- Model parameters
- Optimizer states (momentum estimates for AdamW)
- Model activations (required for backpropagation)
- Gradients (one per parameter)
- Input data batches

Techniques to reduce memory: gradient accumulation, activation checkpointing, and CPU offloading.

## Data Parallelism

Distributes input batches across multiple GPUs while maintaining identical model copies on each device.

Process:
- Each GPU receives a batch portion
- Independent forward/backward passes occur
- Communication via all-reduce operation synchronizes gradients across devices
- Average gradient computed: sum of local gradients divided by GPU count
- Identical updates applied to all model copies

All-Reduce Communication: Libraries use optimized patterns like ring all-reduce to maximize bandwidth utilization.

## Pipeline Parallelism

Distributes model layers across GPUs sequentially.

Example with 16 layers across 4 GPUs:
- GPU0: Layers 1-4
- GPU1: Layers 5-8
- GPU2: Layers 9-12
- GPU3: Layers 13-16

Challenge - "Pipeline Bubble": GPUs remain idle while processing data sequentially. Solution: micro-batching splits batches into smaller micro-batches for staggered processing.

## Tensor Parallelism

Splits individual layer computations across GPUs.

Column Partitioning: Weight matrix W split along output dimension. Each GPU computes output portion. Forward pass requires all-gather; backward pass uses all-reduce.

Row Partitioning: Weight matrix W split along input dimension. Forward pass requires all-reduce; backward pass requires all-gather.

Communication Optimization: Clever partitioning of consecutive layers reduces total all-reduce operations by 50%.

## 3D Parallelism

Hierarchical Cluster Structure:
- Within-node: High-bandwidth NVLink connections
- Cross-node: Slower InfiniBand connections

Optimal Configuration:
- Tensor parallelism: Within-node (frequent communication)
- Pipeline parallelism: Cross-node (minimal activation passing)
- Data parallelism: Across nodes (efficient with slower networks)

Llama 3.1 405B: TP=8, PP=16, DP=8-128 across 16,384 GPUs.

## Batch Size Scaling

Extremely large batches significantly improve training. Llama 3.1 scaled from 4M to 8M to 16M tokens during training. The gradient noise scale increases during training, enabling batch size increases mid-training.

## Emerging Techniques

- Context parallelism for extended sequence lengths
- Expert parallelism for sparse model architectures (MoE)
- DualPipe for improved pipeline efficiency

---
title: "Tensor Parallelism"
type: concept
sources: ["[[sources/jeremy-jordan-distributed-training]]", "[[sources/deepspeed-megatron-frameworks]]"]
related: ["[[concepts/distributed-training]]", "[[concepts/data-parallelism]]", "[[concepts/pipeline-parallelism]]", "[[concepts/3d-parallelism]]", "[[entities/megatron-lm]]"]
last_compiled: 2026-04-05
summary: "Intra-layer parallelism that splits individual weight matrices across GPUs — communication-intensive but essential for models that exceed single-GPU memory. Best within nodes using high-bandwidth NVLink interconnects."
---

## Overview

Tensor parallelism (TP) splits the computation of individual layers across multiple GPUs by partitioning weight matrices. Unlike [[concepts/data-parallelism]] (which replicates the model) or [[concepts/pipeline-parallelism]] (which splits layers), TP divides the math within each layer.

This is the most communication-intensive parallelism strategy, requiring synchronization after every layer. It is therefore best suited for intra-node parallelism where GPUs are connected by high-bandwidth NVLink (900 GB/s on H100) rather than slower inter-node InfiniBand.

## Partitioning Strategies

### Column Partitioning
For a linear layer Y = XW:
- Split W along the output dimension: W = [W1 | W2]
- Each GPU computes Yi = X * Wi (a slice of the output)
- Forward pass: **all-gather** to concatenate outputs
- Backward pass: **all-reduce** to combine gradients

### Row Partitioning
- Split W along the input dimension: W = [W1; W2]
- Each GPU computes a partial sum of the output
- Forward pass: **all-reduce** to sum partial results
- Backward pass: **all-gather** to reconstruct full gradients

### Optimization: Consecutive Layer Pairing
Column-partition the first layer, row-partition the second. This allows activations to flow between layers without communication, reducing total all-reduce operations by 50%. [[entities/megatron-lm]] pioneered this approach.

## When to Use

- Model too large for a single GPU even with ZeRO
- Within a node (8 GPUs connected by NVLink)
- Typical TP degree: 2, 4, or 8 (matching GPUs per node)
- Llama 3.1 405B used TP=8 (one full node per tensor-parallel group)

## Limitations

- High communication overhead: synchronization per layer
- Requires model code changes (unlike DP or ZeRO)
- Scaling efficiency drops beyond 8 GPUs due to communication
- [[entities/megatron-lm]] provides specialized layer implementations

## Sources

- [[sources/jeremy-jordan-distributed-training]] — column/row partitioning mechanics
- [[sources/deepspeed-megatron-frameworks]] — Megatron-LM implementation

## Related Concepts

- [[concepts/pipeline-parallelism]] — inter-layer parallelism (complementary)
- [[concepts/3d-parallelism]] — combining TP with PP and DP
- [[entities/megatron-lm]] — the framework that pioneered TP for LLMs

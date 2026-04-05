---
title: "Pipeline Parallelism"
type: concept
sources: ["[[sources/jeremy-jordan-distributed-training]]", "[[sources/deepspeed-megatron-frameworks]]"]
related: ["[[concepts/distributed-training]]", "[[concepts/data-parallelism]]", "[[concepts/tensor-parallelism]]", "[[concepts/3d-parallelism]]"]
last_compiled: 2026-04-05
summary: "Inter-layer parallelism that distributes model layers sequentially across GPUs. Lower communication than tensor parallelism but suffers from pipeline bubbles — mitigated by micro-batching and interleaved scheduling."
---

## Overview

Pipeline parallelism (PP) splits the model's layers into sequential stages, each assigned to a different GPU or set of GPUs. Data flows through the pipeline like an assembly line: GPU 0 processes layers 1-8, GPU 1 processes layers 9-16, and so on.

Communication is minimal — only activations pass between stages (compared to [[concepts/tensor-parallelism]]'s per-layer synchronization). This makes PP well-suited for **cross-node** distribution over InfiniBand.

## The Pipeline Bubble Problem

In naive pipeline parallelism, GPUs sit idle while waiting for upstream stages:
- GPU 0 processes batch, passes activations to GPU 1
- While GPU 1 works, GPU 0 is idle
- The "bubble" grows with more pipeline stages

This wastes expensive GPU compute and makes naive PP highly inefficient.

## Solutions

### Micro-batching
Split each batch into smaller micro-batches. GPU 0 processes micro-batch 1, passes it to GPU 1, then immediately starts micro-batch 2. This creates overlapping computation across stages:

```
GPU 0: [MB1][MB2][MB3][MB4]...
GPU 1:      [MB1][MB2][MB3][MB4]...
GPU 2:           [MB1][MB2][MB3][MB4]...
```

More micro-batches = smaller bubble (relative to total work).

### Interleaved Scheduling
[[entities/megatron-lm]]'s approach: assign non-contiguous layers to each GPU. Instead of GPU 0 having layers 1-8, it might have layers 1-4 and 17-20. This creates more pipeline stages with smaller granularity, reducing bubble time.

### DualPipe
A recent algorithmic improvement for further reducing bubble overhead in pipeline-parallel training.

## Configuration

- **Pipeline degree**: number of GPU groups in the pipeline (e.g., PP=16 in Llama 3.1)
- **Micro-batch count**: more = less bubble, but more memory for in-flight micro-batches
- **Stage balance**: layers should be distributed to equalize computation time per stage

## When to Use

- Cross-node parallelism (lower bandwidth tolerance)
- Combined with TP (intra-node) and DP (across replicas)
- Llama 3.1 405B: PP=16 across nodes

## Sources

- [[sources/jeremy-jordan-distributed-training]] — bubble problem, micro-batching
- [[sources/deepspeed-megatron-frameworks]] — interleaved scheduling, DeepSpeed pipeline

## Related Concepts

- [[concepts/tensor-parallelism]] — intra-layer complement to PP's inter-layer approach
- [[concepts/3d-parallelism]] — PP's role in the combined strategy
- [[concepts/distributed-training]] — the overarching framework

---
title: "Source: Training Extremely Large Neural Networks Across Thousands of GPUs"
type: source-summary
source: "[[raw/jeremy-jordan-distributed-training]]"
related: ["[[concepts/distributed-training]]", "[[concepts/data-parallelism]]", "[[concepts/tensor-parallelism]]", "[[concepts/pipeline-parallelism]]", "[[concepts/3d-parallelism]]"]
last_compiled: 2026-04-05
summary: "Jeremy Jordan's comprehensive walkthrough of distributed training: data/tensor/pipeline parallelism, 3D parallelism integration, communication primitives, and real-world Llama 3.1 405B configuration (TP=8, PP=16, DP=8-128 across 16,384 GPUs)."
---

## Key Points

- Llama 3.1 405B: 3.8 x 10^25 FLOPs, 609 years on single GPU, 54 days on 16,000 H100s
- Data parallelism: replicate model, split batches, synchronize via all-reduce
- Pipeline parallelism: split layers across GPUs, use micro-batching to reduce bubble time
- Tensor parallelism: split individual weight matrices across GPUs (column/row partitioning)
- 3D parallelism maps TP within-node (NVLink), PP cross-node, DP across nodes
- Llama 3.1 scaled batch size from 4M to 8M to 16M tokens during training

## Detailed Summary

The article provides a ground-up explanation of why distributed training is necessary and how it works.

**Memory breakdown** for a single GPU: parameters + optimizer states (AdamW momentum) + activations + gradients + input data. For large models, this far exceeds any single GPU's capacity.

**[[concepts/data-parallelism]]** is the simplest approach: each GPU gets a full model copy and a batch slice. Gradients are synchronized via ring all-reduce, which maximizes bandwidth utilization.

**[[concepts/pipeline-parallelism]]** splits layers sequentially across GPUs. The "pipeline bubble" problem (idle GPUs) is solved by splitting batches into micro-batches for staggered processing.

**[[concepts/tensor-parallelism]]** is the most communication-intensive: individual weight matrices are split across GPUs. Column and row partitioning strategies minimize all-reduce operations by up to 50%.

**[[concepts/3d-parallelism]]** combines all three, considering network topology: TP within-node (high-bandwidth NVLink), PP cross-node (InfiniBand), DP across nodes.

**Llama 3.1 405B configuration**: TP=8, PP=16, DP=8-128, across 16,384 GPUs.

## Related Concepts

- [[concepts/distributed-training]] — the overarching framework
- [[concepts/data-parallelism]] — batch-splitting approach
- [[concepts/tensor-parallelism]] — weight-matrix splitting
- [[concepts/pipeline-parallelism]] — layer-splitting approach
- [[concepts/3d-parallelism]] — combined hierarchical strategy
- [[entities/llama]] — real-world training example

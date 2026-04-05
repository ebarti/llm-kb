---
title: "3D Parallelism"
type: concept
sources: ["[[sources/jeremy-jordan-distributed-training]]", "[[sources/deepspeed-megatron-frameworks]]", "[[sources/hf-ultrascale-playbook]]"]
related: ["[[concepts/data-parallelism]]", "[[concepts/tensor-parallelism]]", "[[concepts/pipeline-parallelism]]", "[[concepts/5d-parallelism]]", "[[concepts/distributed-training]]"]
last_compiled: 2026-04-05
summary: "Combining data, tensor, and pipeline parallelism in a topology-aware configuration: TP within nodes (NVLink), PP across nodes (InfiniBand), DP across the cluster. The standard approach for frontier LLM training."
---

## Overview

3D parallelism combines [[concepts/data-parallelism]] (DP), [[concepts/tensor-parallelism]] (TP), and [[concepts/pipeline-parallelism]] (PP) to train models that are too large for any single strategy. The key insight is mapping each strategy to the appropriate level of the cluster network hierarchy.

## Topology-Aware Mapping

Modern GPU clusters have a hierarchical network structure:

| Level | Connection | Bandwidth | Best Parallelism |
|-------|-----------|-----------|-----------------|
| Intra-node (8 GPUs) | NVLink | ~900 GB/s (H100) | Tensor Parallelism |
| Cross-node | InfiniBand | ~50-400 Gb/s | Pipeline Parallelism |
| Across cluster | Network fabric | Variable | Data Parallelism |

- **TP within-node**: Frequent all-reduce/all-gather per layer requires maximum bandwidth
- **PP across nodes**: Only activation tensors pass between stages — tolerates latency
- **DP across the cluster**: All-reduce gradients periodically, can overlap with computation

## Real-World Example: Llama 3.1 405B

Meta's training of Llama 3.1 405B demonstrates 3D parallelism at extreme scale:

- **TP = 8**: Each 8-GPU node forms one tensor-parallel group
- **PP = 16**: 16 nodes form one pipeline (128 GPUs)
- **DP = 8-128**: Multiple pipeline replicas, scaled during training
- **Total**: up to 16,384 H100 GPUs
- **Batch size**: scaled from 4M to 8M to 16M tokens during training

## Extension: [[concepts/5d-parallelism]]

The Ultra-Scale Playbook extends 3D to 5D by adding:
- **Context Parallelism (CP)**: Split along sequence length for long contexts
- **Expert Parallelism (EP)**: Distribute MoE experts across GPUs

## Configuration Challenges

The total parallelism degree must equal the number of GPUs: TP x PP x DP = N_GPUs. Finding the optimal combination requires extensive experimentation — the [[sources/hf-ultrascale-playbook]] ran 4,000+ experiments to map this space.

## Sources

- [[sources/jeremy-jordan-distributed-training]] — Llama 3.1 configuration, topology mapping
- [[sources/deepspeed-megatron-frameworks]] — Megatron-DeepSpeed 3D parallelism
- [[sources/hf-ultrascale-playbook]] — 4,000+ scaling experiments

## Related Concepts

- [[concepts/5d-parallelism]] — extended version with CP and EP
- [[concepts/training-infrastructure]] — the hardware that enables this

---
title: "Training Infrastructure"
type: concept
sources: ["[[sources/jeremy-jordan-distributed-training]]", "[[sources/hf-ultrascale-playbook]]", "[[sources/training-costs-2026-analysis]]"]
related: ["[[concepts/distributed-training]]", "[[concepts/llm-training-costs]]", "[[concepts/3d-parallelism]]"]
last_compiled: 2026-04-05
summary: "The GPU clusters, networking, and storage systems required for LLM pretraining: NVIDIA H100/H200/B200 GPUs, NVLink intra-node (900 GB/s), InfiniBand inter-node, with frontier runs using 5,000-16,000+ GPUs."
---

## Overview

LLM pretraining infrastructure consists of large GPU clusters with high-bandwidth networking, massive storage systems, and sophisticated orchestration software. The design of this infrastructure directly determines training speed, cost, and the feasible parallelism strategies.

## GPU Hardware

| GPU | Memory | FP16/BF16 TFLOPS | Year | Notes |
|-----|--------|------------------|------|-------|
| A100 | 80 GB | 312 | 2020 | Previous generation standard |
| H100 | 80 GB | 990 | 2023 | Current workhorse for training |
| H200 | 141 GB | 990 | 2024 | More memory, same compute |
| B200 | 192 GB | 2,250 | 2025 | Next-generation flagship |

GPU memory limits determine the maximum model shard per device. A 405B model in BF16 requires ~810 GB for parameters alone — at least 11 H100s for parameters, far more accounting for optimizer states and activations.

## Network Architecture

The network hierarchy is critical for [[concepts/3d-parallelism]]:

**Intra-node: NVLink**
- H100: NVLink 4.0, 900 GB/s bidirectional
- Connects 8 GPUs within a single server node
- Used for [[concepts/tensor-parallelism]] (frequent all-reduce per layer)

**Inter-node: InfiniBand**
- NDR InfiniBand: 400 Gb/s per port
- Connects nodes across the cluster
- Used for [[concepts/pipeline-parallelism]] (activation passing) and [[concepts/data-parallelism]] (gradient all-reduce)
- RDMA and GPUDirect-RDMA enable direct GPU-to-GPU communication across nodes

**Networking is critical**: Over 90% of training time can be spent on communication at scale if not optimized. Communication/computation overlap is essential.

## Cluster Scale

| Model | GPUs | GPU Type | Duration |
|-------|------|----------|----------|
| Llama 3.1 405B | 16,384 | H100 | 54 days |
| GPT-4 | ~25,000* | A100 | ~100 days* |
| Gemini Ultra | ~26,000* | TPU v4 | — |

*Estimated/rumored.

## Storage

Training data (tens of TB), checkpoints (hundreds of GB each, saved frequently), and logs require high-throughput distributed storage systems. Checkpoint saving must not block training — asynchronous checkpointing is standard.

## Power and Cooling

A 16,000 H100 cluster at ~700W each requires ~11.2 MW of power, not counting networking and storage. This rivals the power consumption of a small town and is a growing concern for the industry.

## Sources

- [[sources/jeremy-jordan-distributed-training]] — Llama 3.1 cluster configuration
- [[sources/hf-ultrascale-playbook]] — scaling experiments across GPU configurations
- [[sources/training-costs-2026-analysis]] — hardware requirements by model size

## Related Concepts

- [[concepts/distributed-training]] — the software layer above infrastructure
- [[concepts/3d-parallelism]] — maps to network hierarchy
- [[concepts/llm-training-costs]] — infrastructure is the dominant cost

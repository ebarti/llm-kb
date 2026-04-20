---
title: "The Ultra-Scale Playbook: Training LLMs on GPU Clusters"
source: "https://huggingface.co/spaces/nanotron/ultrascale-playbook"
author: "Hugging Face / Nanotron Research"
date_published: 2025-02-01
date_ingested: 2026-04-05
tags: [distributed-training, gpu-clusters, parallelism, 5d-parallelism, scaling-experiments, memory-optimization]
type: article
status: raw
discovered_via: search
---

# The Ultra-Scale Playbook: Training LLMs on GPU Clusters

## Overview

Hugging Face's open-source guide documenting efficient methodologies for large-scale model training, drawing from over 4,000 scaling experiments conducted using up to 512 GPUs.

## 5D Parallelism

The playbook covers how to train models using 5D parallelism:
1. Data Parallelism (DP): Process different batches simultaneously
2. Tensor Parallelism (TP): Distribute model weights across GPUs
3. Pipeline Parallelism (PP): Split model into segments across GPUs
4. Context Parallelism (CP): Emerging technique for extended sequences
5. Expert Parallelism (EP): For mixture-of-experts architectures

Plus ZeRO (Zero Redundancy Optimizer) for memory optimization.

## Memory Optimization

Activation Recomputation: Recalculate intermediate activations when needed rather than storing them. Trades computation for memory efficiency.

Gradient Accumulation: Achieve larger effective batch sizes without exceeding memory limits.

## Communication Optimization

Overlapping communication with computation: Using all-reduce operations during the backward pass to minimize idle GPU time.

Strategies for optimizing network bandwidth and minimizing synchronization delays.

## Key Insight

The playbook emphasizes empirical validation: "testing various setups to determine the best balance between batch size, model architecture, and the number of GPUs used."

Over 4,000 scaling experiments analyzed across GPU configurations to identify optimal parallelism strategies for different model sizes and cluster topologies.

## Scale

Head researcher Leandro von Werra: "Learn how to train your own DeepSeek-V3 model using 5D parallelism, ZeRO, fast kernels, compute/comm overlap."

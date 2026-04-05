---
title: "Source: The Ultra-Scale Playbook — Training LLMs on GPU Clusters"
type: source-summary
source: "[[raw/hf-ultrascale-playbook]]"
related: ["[[concepts/distributed-training]]", "[[concepts/5d-parallelism]]", "[[concepts/training-infrastructure]]"]
last_compiled: 2026-04-05
summary: "Hugging Face's open-source guide based on 4,000+ scaling experiments: covers 5D parallelism (DP, TP, PP, CP, EP), ZeRO, activation recomputation, gradient accumulation, and communication/computation overlap strategies."
---

## Key Points

- Based on 4,000+ scaling experiments across up to 512 GPUs
- Covers 5D parallelism: DP + TP + PP + CP + EP
- Key memory techniques: activation recomputation and gradient accumulation
- Communication optimization: overlap all-reduce with backward pass
- Empirical emphasis: test various setups for optimal balance

## Detailed Summary

The Ultra-Scale Playbook from Hugging Face's Nanotron team is the most comprehensive empirical resource for [[concepts/distributed-training]] at scale.

**[[concepts/5d-parallelism]]** extends the classic [[concepts/3d-parallelism]] with two additional dimensions:
1. Data Parallelism (DP): split batches
2. Tensor Parallelism (TP): split weight matrices
3. Pipeline Parallelism (PP): split layers
4. Context Parallelism (CP): split across sequence length for extended contexts
5. Expert Parallelism (EP): distribute MoE experts across GPUs

**Memory optimization**:
- Activation recomputation: trade compute for memory by recalculating activations
- Gradient accumulation: simulate larger batch sizes without exceeding memory

**Communication**: overlapping all-reduce operations with backward computation to minimize idle GPU time.

The playbook's empirical approach (4,000+ experiments) provides practical guidance that pure theoretical analysis cannot match.

## Related Concepts

- [[concepts/5d-parallelism]] — the extended parallelism framework
- [[concepts/distributed-training]] — the overarching topic
- [[concepts/training-infrastructure]] — GPU cluster design

---
title: "5D Parallelism"
type: concept
sources: ["[[sources/hf-ultrascale-playbook]]"]
related: ["[[concepts/3d-parallelism]]", "[[concepts/distributed-training]]", "[[concepts/data-parallelism]]", "[[concepts/tensor-parallelism]]", "[[concepts/pipeline-parallelism]]"]
last_compiled: 2026-04-05
summary: "Extension of 3D parallelism (DP+TP+PP) with Context Parallelism (splitting sequence length) and Expert Parallelism (distributing MoE experts) — the current state-of-the-art for training frontier models like DeepSeek-V3."
---

## Overview

5D parallelism extends the classic [[concepts/3d-parallelism]] framework with two additional dimensions designed for modern architecture innovations (long contexts and Mixture-of-Experts):

| Dimension | What It Splits | Communication Pattern |
|-----------|---------------|----------------------|
| Data Parallelism (DP) | Input batches | All-reduce gradients |
| Tensor Parallelism (TP) | Weight matrices | All-reduce/all-gather per layer |
| Pipeline Parallelism (PP) | Model layers | Activation passing between stages |
| Context Parallelism (CP) | Sequence length | Ring attention patterns |
| Expert Parallelism (EP) | MoE expert modules | All-to-all token routing |

## Context Parallelism

For models with very long context windows (128K+ tokens), the sequence itself becomes a memory bottleneck. CP distributes the sequence across GPUs, with each GPU processing a contiguous chunk. Attention computation uses ring-attention or similar patterns to enable cross-chunk interaction.

## Expert Parallelism

Mixture-of-Experts architectures (like DeepSeek-V3 with 671B total / 37B active parameters) have many expert modules, only a few of which are activated per token. EP places different experts on different GPUs, with an all-to-all communication pattern routing tokens to their assigned experts.

## Hugging Face's Contribution

The [[sources/hf-ultrascale-playbook]] analyzed 4,000+ scaling experiments across configurations to identify optimal combinations of all 5 dimensions plus [[concepts/zero-optimizer]] for different model sizes and cluster topologies.

## Sources

- [[sources/hf-ultrascale-playbook]] — comprehensive guide with scaling experiments

## Related Concepts

- [[concepts/3d-parallelism]] — the foundational combination
- [[concepts/distributed-training]] — the overarching framework

---
title: "Dense vs MoE Transformers"
type: comparison
subjects: ["[[concepts/transformer-architecture]]", "[[concepts/mixture-of-experts]]"]
sources: ["[[sources/huggingface-mixture-of-experts]]", "[[sources/moe-models-comparison-2025]]"]
last_compiled: 2026-04-05
summary: "Dense transformers use all parameters per token; MoE activates a fraction via routing — MoE achieves 4x pretraining speedup and frontier performance but requires full-model memory and load balancing."
---

## Overview

A dense [[concepts/transformer-architecture]] computes every parameter for every token. A [[concepts/mixture-of-experts]] model replaces some dense FFN layers with multiple expert sub-networks, activating only a subset per token. This decouples model capacity from inference cost.

## Comparison Table

| Dimension | Dense Transformer | MoE Transformer |
|-----------|------------------|-----------------|
| **Params per token** | All | Fraction (e.g., 12B of 47B) |
| **VRAM needed** | All parameters | All parameters (experts always loaded) |
| **Inference speed** | Proportional to params | Proportional to active params |
| **Training speed** | 1x | ~4x faster at same quality |
| **Knowledge tasks** | Good | Better (more capacity) |
| **Reasoning tasks** | Better without instruct tuning | Worse (overfitting) |
| **With instruction tuning** | Good | Better (MoE benefits more) |
| **Complexity** | Simple | Load balancing, routing, expert parallelism |
| **Quantization synergy** | Standard | Excellent (QMoE: 20x compression) |

## When to Use Each

### Dense Models Preferred

- Single-GPU deployment with limited VRAM
- Small-scale fine-tuning (less overfitting risk)
- Reasoning-heavy tasks without instruction tuning
- Simplicity valued over efficiency

### MoE Models Preferred

- High-throughput serving (many machines)
- Fixed compute budgets for pretraining
- Knowledge-heavy tasks
- Instruction-tuned applications
- Sufficient VRAM for full model loading

## Key Examples

| Dense Model | Params | Equivalent MoE | Total / Active |
|------------|--------|----------------|---------------|
| Llama 2 70B | 70B | Mixtral 8x7B | 47B / 12B |
| - | - | Llama 4 Scout | 109B / 17B |
| - | - | DeepSeek-R1 | 671B / 37B |
| - | - | Qwen3-235B | 235B / 22B |

## The Trend

By 2025, essentially all frontier LLMs use MoE. Dense models remain relevant for edge deployment and specialized fine-tuning, but the scaling advantages of MoE have made it the default for frontier training.

## Sources

- [[sources/huggingface-mixture-of-experts]] — comprehensive dense vs MoE analysis
- [[sources/moe-models-comparison-2025]] — 2025 MoE model landscape

---
title: "LoRA vs. QLoRA"
type: comparison
subjects: ["[[concepts/parameter-efficient-fine-tuning]]"]
sources: ["[[sources/lora-qlora-efficient-fine-tuning]]"]
last_compiled: 2026-04-05
summary: "LoRA (16-bit adapters, 90-95% quality, 16GB for 7B) vs. QLoRA (4-bit quantized base, 80-90% quality, 6GB for 7B) — choose LoRA for production, QLoRA for experimentation."
---

## Overview

LoRA and QLoRA are the two most widely used [[concepts/parameter-efficient-fine-tuning]] methods. Both freeze the base model and train small adapter matrices, but QLoRA additionally quantizes the frozen base model to 4-bit precision, trading some quality for dramatically reduced memory usage.

## Comparison Table

| Dimension | LoRA | QLoRA |
|-----------|------|-------|
| **Base model precision** | 16-bit (original) | 4-bit NormalFloat (NF4) |
| **Adapter precision** | 16-bit | 16-bit |
| **Quality vs. full FT** | 90-95% | 80-90% |
| **VRAM for 7B** | 16GB | 6GB |
| **VRAM for 70B** | 160GB | 48GB |
| **Trainable params** | 0.5-5% | 0.5-5% |
| **Inference overhead** | Zero (merge adapters) | Slight (quantized base) |
| **Task swapping** | Hot-swap adapters | Hot-swap adapters |
| **Overfitting risk** | Lower than full FT | Lowest (quantization regularizes) |
| **Hardware requirement** | 1x A100 (7B) | Consumer GPU / Colab T4 |

## Memory Requirements

| Method | 7B | 13B | 30B | 70B |
|--------|-----|-----|-----|------|
| Full (16-bit) | 60GB | 120GB | 300GB | 600GB |
| LoRA (16-bit) | 16GB | 32GB | 64GB | 160GB |
| QLoRA (8-bit) | 10GB | 20GB | 40GB | 80GB |
| QLoRA (4-bit) | 6GB | 12GB | 24GB | 48GB |

## When to Use Each

### Choose LoRA
- Production deployment requiring maximum quality
- Sufficient GPU memory available (A100, H100, or multi-GPU)
- Multiple task-specific adapters on same base model
- Quality-sensitive applications (medical, legal, financial)

### Choose QLoRA
- Experimentation and prototyping on limited hardware
- Consumer GPUs (RTX 3090, 4090) or free cloud tiers (Colab T4)
- Fine-tuning very large models (70B+) on available hardware
- Acceptable quality tradeoff for 4x memory savings
- Educational and research settings

## Practical Notes

- Both methods support adapter merging into base weights for deployment
- LoRA rank (r) typically 8-64; higher = more capacity but more compute
- Both can be combined with [[concepts/domain-adaptive-pretraining]] for maximum effectiveness
- QLoRA quality gap is narrowing with newer quantization techniques

## Sources

- [[sources/lora-qlora-efficient-fine-tuning]] — detailed comparison with benchmarks

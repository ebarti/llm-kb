---
title: "LoRA vs. QLoRA: Efficient Fine-Tuning Techniques for LLMs"
source: "https://modal.com/blog/lora-qlora"
author: "Modal"
date_published: 2024-06-01
date_ingested: 2026-04-05
tags: [lora, qlora, peft, fine-tuning, parameter-efficient]
type: article
status: raw
discovered_via: search
---

# LoRA vs. QLoRA: Efficient Fine-Tuning Techniques for LLMs

## The Problem with Full Fine-Tuning

Traditional fine-tuning updates every parameter in the base model, demanding 60GB+ of VRAM for a 7B parameter model. This approach is slow, resource-intensive, and susceptible to overfitting on smaller datasets.

## How LoRA Works

Developed by Microsoft researchers, LoRA freezes pre-trained weights and introduces trainable adapter matrices. Instead of modifying the original weight matrix W, the technique implements: Y = WX + BAX, where B and A are smaller low-rank matrices representing model updates.

**Advantages:**
- Only A and B matrices require training (0.5-5% of total parameters)
- Significantly reduced VRAM usage
- Lower overfitting risk than full fine-tuning
- Supports selective application to specific layers
- Multiple LoRA modules can be trained and swapped for different tasks
- Permits higher learning rates due to fewer parameters

## How QLoRA Works

QLoRA extends LoRA by quantizing the base model weights from 32-bit floating-point to lower-precision formats like 4-bit NormalFloat (NF4). This achieves a 4x reduction in memory usage compared to standard LoRA, enabling fine-tuning on resource-constrained devices.

**Advantages:**
- Further reduces memory footprint
- May actually reduce overfitting through quantization
- Preserves adapter performance since quantization targets the base model

**Potential Drawback:**
- Can lead to a loss of knowledge and a lower-quality fine-tune, but not necessarily

## Memory Requirements Comparison

| Method | 7B | 13B | 30B | 70B |
|--------|-----|-----|-----|------|
| Full (16-bit) | 60GB | 120GB | 300GB | 600GB |
| LoRA (16-bit) | 16GB | 32GB | 64GB | 160GB |
| QLoRA (8-bit) | 10GB | 20GB | 40GB | 80GB |
| QLoRA (4-bit) | 6GB | 12GB | 24GB | 48GB |

## Quality Tradeoffs

LoRA recovers 90-95% of full fine-tuning quality on most tasks. QLoRA achieves 80-90% of full fine-tuning quality. Once fine-tuned, LoRA adapters can be merged into the main model weights with no additional inference cost.

## Implementation Guidance

Choose LoRA if adequate hardware resources are available. For constrained environments such as free Google Colab T4 GPUs, QLoRA provides a practical alternative, though with quality trade-offs to consider.

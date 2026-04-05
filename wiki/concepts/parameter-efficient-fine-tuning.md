---
title: "Parameter-Efficient Fine-Tuning (PEFT)"
type: concept
sources: ["[[sources/lora-qlora-efficient-fine-tuning]]"]
related: ["[[concepts/fine-tuning]]", "[[concepts/catastrophic-forgetting]]", "[[concepts/knowledge-distillation]]"]
last_compiled: 2026-04-05
summary: "LoRA and QLoRA enable fine-tuning LLMs by updating only 0.5-5% of parameters via low-rank adapter matrices, reducing VRAM from 60GB to 6GB for a 7B model while retaining 80-95% quality."
---

## Overview

Parameter-Efficient Fine-Tuning (PEFT) is a family of techniques that adapt pretrained language models by updating only a small fraction of their parameters. This dramatically reduces computational requirements while preserving most of the quality of full [[concepts/fine-tuning]], and substantially mitigates [[concepts/catastrophic-forgetting]] by keeping the base model's weights mostly frozen.

PEFT has become the default approach for fine-tuning in practice. The most widely used methods are LoRA and its quantized variant QLoRA.

## LoRA (Low-Rank Adaptation)

### How It Works
Developed by Microsoft researchers, LoRA is based on the insight that weight updates during fine-tuning have low intrinsic rank — the difference between pretrained and fine-tuned weights can be well-approximated by the product of two small matrices.

Instead of updating weight matrix W directly, LoRA computes:
```
Y = WX + BAX
```
where B and A are small low-rank matrices (the "adapter"). Only A and B are trained; W remains frozen.

### Key Properties
- **Parameter count**: 0.5-5% of total model parameters
- **Quality**: Recovers 90-95% of full fine-tuning quality
- **VRAM**: 16GB for 7B model (vs. 60GB+ for full fine-tuning)
- **Inference**: Adapters can be merged into base weights → zero inference overhead
- **Modularity**: Multiple LoRA adapters can be trained for different tasks and hot-swapped on the same base model
- **Rank selection**: Typical ranks of 8-64; higher rank = more capacity but more compute

## QLoRA (Quantized LoRA)

### How It Works
QLoRA extends LoRA by quantizing the frozen base model to 4-bit NormalFloat (NF4) precision while training LoRA adapters in 16-bit. This achieves a further 4x memory reduction.

### Key Properties
- **Quality**: Achieves 80-90% of full fine-tuning quality
- **VRAM**: 6GB for 7B model (4-bit); enables 70B models in 48GB
- **Tradeoff**: Slight quality loss from quantization; may actually reduce overfitting
- **Use case**: Experimentation, resource-constrained environments, consumer hardware

## Memory Requirements

| Method | 7B | 13B | 30B | 70B |
|--------|-----|-----|-----|------|
| Full (16-bit) | 60GB | 120GB | 300GB | 600GB |
| LoRA (16-bit) | 16GB | 32GB | 64GB | 160GB |
| QLoRA (8-bit) | 10GB | 20GB | 40GB | 80GB |
| QLoRA (4-bit) | 6GB | 12GB | 24GB | 48GB |

## Other PEFT Methods

- **Adapters**: Small bottleneck layers inserted between transformer blocks
- **Prefix Tuning**: Learnable continuous prompts prepended to input
- **Prompt Tuning**: Soft prompts trained as continuous embeddings
- **IA3**: Learned vectors that rescale key, value, and feedforward activations

## Decision Framework

Choose **LoRA** when:
- Production quality is needed
- Sufficient GPU memory available (16GB+ for 7B)
- Multiple task-specific adapters desired

Choose **QLoRA** when:
- Limited GPU memory (consumer hardware, Colab)
- Experimentation and prototyping
- Acceptable quality tradeoff for 4x memory savings

Choose **full fine-tuning** when:
- Maximum quality required
- Abundant compute available
- Significant domain shift from base model

## Connection to Knowledge Bases

PEFT is particularly relevant to [[concepts/llm-knowledge-base]] systems because it enables:
- Fine-tuning domain-specific models for better wiki compilation
- Training small, fast models for linting and Q&A
- Adapting models to specific writing styles and formats
- Creating task-specific adapters (summarization, entity extraction, comparison) on the same base model

## Sources

- [[sources/lora-qlora-efficient-fine-tuning]] — detailed comparison with memory tables

## Related Concepts

- [[concepts/fine-tuning]] — PEFT is the practical default for fine-tuning
- [[concepts/catastrophic-forgetting]] — PEFT mitigates by updating fewer parameters
- [[concepts/knowledge-distillation]] — complementary compression technique
- [[concepts/domain-adaptive-pretraining]] — PEFT can be used for efficient DAPT

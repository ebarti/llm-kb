---
title: "Source: LoRA vs. QLoRA — Efficient Fine-Tuning Techniques for LLMs"
type: source-summary
source: "[[raw/lora-qlora-efficient-fine-tuning]]"
related: ["[[concepts/parameter-efficient-fine-tuning]]", "[[concepts/fine-tuning]]", "[[concepts/catastrophic-forgetting]]"]
last_compiled: 2026-04-05
summary: "Comparison of LoRA (low-rank adapter matrices, 90-95% of full quality) and QLoRA (4-bit quantized base + LoRA, 80-90% quality) with detailed memory requirement tables."
reading_time: "2 min"
---

## Key Points

- Full fine-tuning of 7B model requires 60GB+ VRAM; LoRA reduces to 16GB; QLoRA (4-bit) to 6GB
- LoRA: freeze base weights, train low-rank adapter matrices (0.5-5% of parameters): Y = WX + BAX
- QLoRA: quantize frozen base to 4-bit NormalFloat, train adapters in 16-bit — 4x further memory reduction
- LoRA recovers 90-95% of full fine-tuning quality; QLoRA achieves 80-90%
- LoRA adapters can be merged into base model with zero inference overhead
- Multiple LoRA modules can be swapped for different tasks on same base model
- QLoRA enables fine-tuning 70B models in 48GB VRAM (single A100)

## Detailed Summary

The article provides a practical decision framework for parameter-efficient fine-tuning. LoRA's key insight is that weight updates during fine-tuning have low intrinsic rank — meaning the delta between pre-trained and fine-tuned weights can be well-approximated by the product of two small matrices. This dramatically reduces trainable parameters while maintaining quality.

QLoRA extends this with 4-bit NormalFloat quantization of the frozen base model, achieving another 4x memory reduction. The quality-cost tradeoff is clear: LoRA for production quality, QLoRA for experimentation and resource-constrained environments.

## Notable Quotes

> "Traditional fine-tuning updates every parameter in the base model, demanding 60GB+ of VRAM for a 7B parameter model."

## Related Concepts

- [[concepts/parameter-efficient-fine-tuning]] — LoRA and QLoRA are the leading PEFT methods
- [[concepts/fine-tuning]] — PEFT as a practical alternative to full fine-tuning
- [[concepts/catastrophic-forgetting]] — PEFT reduces forgetting by updating fewer parameters
- [[concepts/knowledge-distillation]] — complementary model compression technique

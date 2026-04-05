---
title: "Source: Which Quantization Method is Right for You?"
type: source-summary
source: "[[raw/quantization-gptq-gguf-awq]]"
related: ["[[concepts/quantization]]", "[[comparisons/gptq-vs-awq-vs-gguf]]", "[[concepts/llm-inference-optimization]]"]
last_compiled: 2026-04-05
summary: "Maarten Grootendorst's comparison of GPTQ (GPU-optimized, most adopted), GGUF (CPU-friendly, Apple), and AWQ (best speed-quality via activation-aware compression) quantization methods."
---

## Key Points
- GPTQ: GPU-optimized, most frequently used, 3.25-4.5x speed improvement
- GGUF: CPU-first with optional GPU offloading, best for Apple/resource-constrained
- AWQ: identifies ~1% salient weights via activation statistics, best speed-quality balance
- Marlin-AWQ: 741 tok/s (10.9x speedup over base AWQ) — overall sweet spot
- Quantization reduces model size by 75% with minimal accuracy loss

## Detailed Summary

Grootendorst compares the three dominant [[concepts/quantization|quantization]] formats for LLM deployment. GPTQ is the GPU-optimized default, compressing weights to 4-bit by minimizing mean squared error and dequantizing to float16 during inference. It has the largest ecosystem (2000+ quantized models on HuggingFace).

GGUF (formerly GGML) targets CPU-first deployments with optional GPU layer offloading, making it ideal for Apple devices and resource-constrained environments. It powers the llama.cpp ecosystem.

AWQ takes a nuanced approach: instead of treating all weights equally, it identifies the ~1% of salient weight channels using activation statistics and scales them up before applying uniform low-bit quantization. This selective approach yields better speed-quality balance. With Marlin kernels, AWQ reaches 741 tok/s (10.9x over base AWQ).

## Related Concepts
- [[concepts/quantization]] — the core technique
- [[comparisons/gptq-vs-awq-vs-gguf]] — detailed comparison
- [[concepts/edge-inference]] — quantization enables on-device deployment

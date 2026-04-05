---
title: "Quantization"
type: concept
sources: ["[[sources/mlx-vs-llamacpp-apple-silicon]]", "[[sources/small-language-models-guide-2026]]", "[[sources/coding-models-comparison-2026]]", "[[sources/quantization-gptq-gguf-awq]]", "[[sources/on-device-llms-2026]]"]
related: ["[[concepts/local-llm-inference]]", "[[concepts/open-source-llms]]", "[[entities/llama-cpp]]", "[[entities/mlx]]", "[[concepts/llm-inference-optimization]]", "[[concepts/edge-inference]]", "[[comparisons/gptq-vs-awq-vs-gguf]]"]
last_compiled: 2026-04-05
summary: "Reducing model weight precision (FP16 → 4-bit) to shrink memory footprint 4x and enable local inference on consumer hardware, with minimal quality loss."
---

## Overview

Quantization is the process of reducing the numerical precision of a model's weights — from 16-bit or 32-bit floating point to lower-bit integer representations (8-bit, 4-bit, or even 1.5-bit). This shrinks the model's memory footprint proportionally and can speed up inference by reducing memory bandwidth requirements.

For [[concepts/local-llm-inference]], quantization is the enabling technology that makes large models fit on consumer hardware. A 7B parameter model that requires ~14GB in FP16 needs only ~3.5-5GB at 4-bit quantization.

## Key Ideas

### GGUF Format

GGUF (GGML Universal File) is the standard format for quantized models, introduced by the [[entities/llama-cpp]] project in August 2023. It stores both tensors and metadata in a single file, ensuring cross-platform portability. Hugging Face provides online tools for converting and quantizing models to GGUF.

### Quantization Levels

[[entities/llama-cpp]] supports a wide range of quantization options:

| Quantization | Bits/Weight | Relative Size | Quality Impact |
|-------------|-------------|---------------|----------------|
| FP16 | 16 | 100% (baseline) | None |
| Q8_0 | 8 | ~50% | Negligible |
| Q6_K | 6 | ~37% | Very small |
| Q5_K_M | 5 | ~31% | Small |
| Q4_K_M | 4 | ~25% | Moderate |
| Q3_K_M | 3 | ~19% | Noticeable |
| Q2_K | 2 | ~12% | Significant |
| IQ1_S | ~1.5 | ~9% | Large |

The sweet spot for most applications is **Q4_K_M** — 4x smaller than FP16 with moderate quality loss that is often imperceptible for conversational tasks.

### VRAM Requirements by Model Size (Q4)

| Model Size | Q4 VRAM | Example Models |
|-----------|---------|----------------|
| 1-2B | 1-2 GB | Gemma 270M, Qwen 0.6B |
| 3-4B | 2-4 GB | Phi-4-mini, Gemma 3 4B |
| 7B | 3.5-5 GB | Mistral 7B, Llama 3.1 8B |
| 14B | 7-10 GB | Phi-4, DeepSeek Coder |
| 32B | 20-24 GB | Qwen 2.5 Coder 32B |
| 70B | 35-45 GB | Llama 3.1 70B |

### MLX Quantization

[[entities/mlx]] supports 4-bit and 8-bit integer quantization with configurable group sizes. Models are distributed through the `mlx-community` on Hugging Face. MLX's approach is simpler but less granular than llama.cpp's extensive options.

### Importance-Matrix Quantization

Advanced technique in llama.cpp: uses activation patterns from representative data to determine which weights are most important, applying higher precision to critical weights and lower precision to less important ones. This produces better quality at the same overall bit rate.

### Impact on KB Applications

For a [[concepts/local-knowledge-base]], quantization determines which models can run on available hardware:
- **8GB Mac**: 3-4B models at Q4 (Phi-4-mini, Qwen 3 4B)
- **16GB Mac**: 7-8B models at Q4 (Llama 3.1 8B, Mistral 7B)
- **32GB Mac**: 14B models at Q4 (Phi-4, DeepSeek Coder)
- **64GB Mac**: 32B models at Q4 or 70B at Q2-Q3

## Production Quantization Methods (GPTQ vs AWQ vs GGUF)

Beyond the llama.cpp quantization levels above, three major methods dominate production deployment:

### GPTQ (GPT-Quantized)
Post-training quantization for GPU inference. Compresses weights to 4-bit by minimizing mean squared error with Cholesky-based Hessian updates. Most widely adopted with 2000+ models on HuggingFace. Marlin-GPTQ kernels reach 712 tok/s.

### AWQ (Activation-Aware Weight Quantization)
Identifies the ~1% of salient weight channels using activation statistics and scales them up before applying uniform low-bit quantization. Marlin-AWQ reaches 741 tok/s (10.9x over base AWQ) — the speed-quality sweet spot. See [[comparisons/gptq-vs-awq-vs-gguf]] for detailed comparison.

### Emerging Sub-4-Bit Techniques
- **BitNet**: Native 1.58-bit training (ternary weights: -1, 0, +1)
- **SpinQuant**: Rotation matrices for 4-bit weights, activations, and KV cache simultaneously
- **SmoothQuant**: Migrates quantization difficulty from activations to weights via per-channel scaling

## Sources
- [[sources/mlx-vs-llamacpp-apple-silicon]] — quantization support comparison between MLX and llama.cpp
- [[sources/small-language-models-guide-2026]] — VRAM requirements for quantized SLMs
- [[sources/coding-models-comparison-2026]] — VRAM for quantized coding models
- [[sources/quantization-gptq-gguf-awq]] — GPTQ/AWQ/GGUF method comparison and benchmarks
- [[sources/on-device-llms-2026]] — quantization for mobile deployment including sub-4-bit techniques

## Related Concepts
- [[concepts/local-llm-inference]] — quantization as the enabling technology
- [[concepts/small-language-models]] — SLMs + quantization = minimal hardware
- [[entities/llama-cpp]] — primary quantization tool with GGUF format
- [[entities/mlx]] — simpler quantization for Apple Silicon
- [[concepts/llm-inference-optimization]] — quantization in the broader optimization stack
- [[concepts/edge-inference]] — quantization enables mobile/on-device deployment
- [[comparisons/gptq-vs-awq-vs-gguf]] — detailed method comparison

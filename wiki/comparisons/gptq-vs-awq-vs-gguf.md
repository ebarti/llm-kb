---
title: "GPTQ vs AWQ vs GGUF"
type: comparison
subjects: ["[[concepts/quantization]]"]
sources: ["[[sources/quantization-gptq-gguf-awq]]", "[[sources/on-device-llms-2026]]"]
last_compiled: 2026-04-05
summary: "Three dominant LLM quantization methods: GPTQ (GPU default, largest ecosystem), GGUF (CPU/Apple-friendly via llama.cpp), AWQ (best speed-quality balance via activation-aware compression)."
---

## Overview

GPTQ, AWQ, and GGUF are the three dominant [[concepts/quantization|quantization]] formats for deploying LLMs efficiently. Each targets different hardware profiles and optimization priorities.

## Comparison Table

| Dimension | GPTQ | AWQ | GGUF |
|-----------|------|-----|------|
| **Target hardware** | GPU (NVIDIA) | GPU (NVIDIA) | CPU + optional GPU |
| **Approach** | Minimize MSE per layer | Activation-aware weight selection | Flexible CPU/GPU split |
| **Speed (Marlin)** | 712 tok/s | **741 tok/s** | Varies by offload |
| **Speed (base)** | 276 tok/s | 68 tok/s | Moderate |
| **Quality preservation** | Good | Good-to-better | Good |
| **Ecosystem size** | **Largest** (2000+ models) | Growing | Large (llama.cpp) |
| **Framework** | auto-gptq, vLLM | vLLM | llama.cpp, ctransformers |
| **Key innovation** | Cholesky-based Hessian | ~1% salient weight identification | CPU inference with GPU offloading |

## How Each Works

### GPTQ
Post-training layer-wise quantization. Compresses all weights to 4-bit by minimizing mean squared error using fast Cholesky-based Hessian updates. Dequantizes to FP16 during inference. Treats all weights uniformly.

### AWQ
Recognizes that **not all weights are equally important**. Uses activation statistics to identify the ~1% of salient weight channels, scales them up before applying uniform low-bit quantization. This selective approach preserves critical information pathways with better quality at equivalent compression.

### GGUF
Format-level innovation rather than algorithmic. Stores tensors and metadata in a single portable file. Enables **CPU-first inference** with the ability to offload specific layers to GPU. Users control the CPU/GPU split via `gpu_layers` parameter.

## When to Use Each

| Scenario | Recommended |
|----------|-------------|
| NVIDIA GPU, production deployment | **GPTQ** — largest ecosystem, well-tested |
| NVIDIA GPU, need best speed + quality | **AWQ** — Marlin kernels, 10.9x speedup |
| Apple Silicon / CPU-first | **GGUF** — llama.cpp integration |
| Resource-constrained / edge | **GGUF** — flexible memory management |
| vLLM serving | **AWQ** — native support, best benchmarks |
| Maximum compatibility | **GPTQ** — most models available |

## Performance Context

With Marlin kernels (optimized CUDA), both GPTQ and AWQ achieve dramatic speedups:
- Marlin-AWQ: **741 tok/s** (10.9x over base AWQ) + **51.8% Pass@1** on code
- Marlin-GPTQ: **712 tok/s** (2.6x over base GPTQ)
- BitsandBytes: **6.67 perplexity** (best quality preservation)

The Marlin kernel is the key differentiator — without it, base AWQ (68 tok/s) is actually much slower than base GPTQ (276 tok/s).

## Sources
- [[sources/quantization-gptq-gguf-awq]] — method comparison and benchmarks
- [[sources/on-device-llms-2026]] — quantization in mobile deployment context

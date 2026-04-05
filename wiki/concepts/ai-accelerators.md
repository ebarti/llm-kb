---
title: "AI Accelerators"
type: concept
sources: ["[[sources/ai-hardware-accelerators-2026-guide]]", "[[sources/nvidia-gpu-specs-ai-training-2026]]", "[[sources/ai-inference-accelerators-compared]]", "[[sources/cerebras-vs-sambanova-vs-groq-chips]]"]
related: ["[[concepts/ai-hardware-landscape]]", "[[concepts/memory-bandwidth-wall]]", "[[concepts/training-vs-inference-hardware]]", "[[entities/nvidia]]", "[[entities/amd]]", "[[entities/google-tpu]]", "[[entities/cerebras]]", "[[entities/groq]]"]
tags: [ai-hardware, gpu, asic, tpu, accelerators]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Purpose-built hardware for neural network computation — from GPUs with tensor cores to custom ASICs; spectrum ranges from NVIDIA's general-purpose Blackwell (1800 TFLOPS) to Taalas's model-weights-in-silicon (17,000 tok/s, single model only)."
---

## Overview

AI accelerators are specialized processors designed to execute neural network computations efficiently. Unlike general-purpose CPUs, they exploit the mathematical structure of deep learning — primarily dense matrix multiplications and convolutions — through hardware features like systolic arrays, tensor cores, and wide memory interfaces. The accelerator landscape in 2026 spans a spectrum from general-purpose (NVIDIA GPUs running any workload) to hyper-specialized (Taalas chips with model weights etched into silicon).

## Key Ideas

### Architectural Approaches

**GPU-based (NVIDIA, AMD)**: Graphics Processing Units repurposed for AI through tensor cores — specialized matrix multiplication units. NVIDIA's Blackwell B200 features a second-generation Transformer Engine with FP4 precision support, delivering 20 PFLOPS peak. AMD's MI300X competes with 192GB HBM3e and 5.2 TB/s bandwidth. The GPU approach maximizes flexibility at the cost of efficiency.

**Systolic Array ASICs ([[entities/google-tpu]])**: Fixed-function matrix multiplication engines with large systolic arrays (TPU v1: 65,536 MACs). Tight hardware-software co-design with XLA compiler and JAX enables optimizations impossible on general-purpose GPUs. Seven generations of TPUs demonstrate consistent 2-5x generational improvements.

**Wafer-Scale ([[entities/cerebras]])**: An entire 300mm silicon wafer as a single processor — 4 trillion transistors, 900,000 cores, 44GB on-chip SRAM. Eliminates inter-chip communication overhead. The WSE-3 claims 7,000x bandwidth advantage over H100 by keeping models entirely in on-chip memory.

**Deterministic Streaming ([[entities/groq]])**: Language Processing Unit (LPU) with "kernel-free" in-order execution — no hardware context switching, deterministic latency regardless of context length. Optimized exclusively for inference.

**Reconfigurable Dataflow ([[entities/sambanova]])**: The Reconfigurable DataFlow Unit (RDU) reshapes its compute fabric at compile time for different neural network layers. Up to 3TB memory per socket — the most memory-dense option.

**Model-Specific ASICs (Taalas, Etched)**: The most extreme specialization. Taalas burns model weights directly into silicon mask ROM. Etched removes all non-transformer circuitry. Maximum speed, zero flexibility.

### The Generality-Efficiency Tradeoff

A fundamental tradeoff governs accelerator design: more specialization yields higher efficiency but reduces flexibility. NVIDIA GPUs run any model but at moderate speed. Taalas runs a single model at extreme speed. The market is sorting itself along this spectrum, with different points optimal for different deployment scenarios:

| Generality | Example | Speed (tok/s) | Flexibility |
|-----------|---------|--------------|-------------|
| Most general | NVIDIA B200 | ~353 | Any model, train + infer |
| Inference-general | Groq LPU | ~594 | Any transformer, infer only |
| Architecture-specific | Etched Sohu | ~62,500 | Transformers only |
| Model-specific | Taalas HC1 | ~17,000 | Single model only |

### Key Specifications (2026 Flagships)

| Accelerator | TFLOPS | Memory | Bandwidth | TDP | Process |
|------------|--------|--------|-----------|-----|---------|
| NVIDIA B200 | 1,800 FP8 | 192GB HBM3e | 8 TB/s | 1,000W | TSMC 4nm |
| AMD MI300X | ~2,000 FP8 | 192GB HBM3e | 5.2 TB/s | 750W | TSMC 5nm |
| Google Ironwood | 4,614 | 192GB HBM | 9.6 Tb/s ICI | N/A | N/A |
| Cerebras WSE-3 | N/A | 44GB SRAM | On-chip mesh | 20-50kW | TSMC 3nm |

## How It Connects

AI accelerators are the physical substrate enabling all AI progress. They determine the [[concepts/memory-bandwidth-wall]] (HBM capacity and bandwidth), influence [[concepts/ai-data-center-energy]] consumption (TDP scaling), and drive [[concepts/ai-infrastructure-investment]] (chip procurement is the largest capex category). The choice of accelerator shapes the entire AI stack from [[concepts/training-vs-inference-hardware]] strategy through [[concepts/custom-silicon]] decisions.

## Open Questions

- Will FP4 precision (NVIDIA Blackwell) become the standard for inference, or will quality concerns push back?
- Can [[entities/cerebras]]'s wafer-scale approach survive the manufacturing yield challenges at scale?
- How will NVIDIA's Groq acquisition ($20B) reshape the inference market?
- Will the transformer architecture's dominance persist long enough to justify transformer-specific ASICs?

## Sources

- [[sources/ai-hardware-accelerators-2026-guide]] — comprehensive landscape overview
- [[sources/nvidia-gpu-specs-ai-training-2026]] — NVIDIA specification reference
- [[sources/ai-inference-accelerators-compared]] — inference benchmark comparison
- [[sources/cerebras-vs-sambanova-vs-groq-chips]] — ASIC startup comparison
- [[sources/google-tpu-architecture-gemini]] — TPU architecture deep dive

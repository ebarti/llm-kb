---
title: "Custom Silicon"
type: concept
sources: ["[[sources/google-tpu-architecture-gemini]]", "[[sources/ai-hardware-accelerators-2026-guide]]", "[[sources/cerebras-vs-sambanova-vs-groq-chips]]"]
related: ["[[concepts/ai-hardware-landscape]]", "[[concepts/ai-accelerators]]", "[[entities/google-tpu]]", "[[entities/cerebras]]", "[[entities/nvidia]]"]
tags: [custom-silicon, asic, tpu, vertical-integration, hyperscaler]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The hyperscaler trend toward designing proprietary AI chips: Google TPU (7 generations), Amazon Trainium/Inferentia, Meta MTIA, Microsoft Maia, Apple-Broadcom Baltra, OpenAI-Broadcom — delivering 30-40% cost advantage over merchant GPUs through hardware-software co-design."
---

## Overview

Custom silicon refers to the growing practice of major technology companies designing their own AI accelerators rather than relying solely on merchant silicon from [[entities/nvidia]] or [[entities/amd]]. By 2026, every major hyperscaler has a custom chip program, and the trend is extending to AI-native companies like [[entities/openai]].

The motivation is straightforward: when you control both the hardware and the software stack, you can co-optimize in ways impossible with general-purpose chips. [[entities/google-tpu]] demonstrates this most clearly — seven generations of TPUs refined alongside JAX, XLA, and Pathways, with Gemini 3 trained entirely on TPUs without GPU fallback.

## Key Ideas

### The Custom Silicon Roster (2026)

| Company | Chip | Focus | Generation | Key Advantage |
|---------|------|-------|-----------|--------------|
| Google | TPU (Ironwood v7) | Training + Inference | 7th | 4,614 TFLOPS, optical interconnect |
| Amazon | Trainium2 / Inferentia2 | Training / Inference | 2nd | AWS integration, cost |
| Meta | MTIA v2 | Inference | 2nd | 5x performance over v1 |
| Microsoft | Maia | Azure workloads | 1st | Azure-native optimization |
| Apple-Broadcom | Baltra | Inference | 1st | Internal use only (2026) |
| OpenAI-Broadcom | TBD | TBD | Pre-production | Custom for OpenAI's models |

### Why Custom Beats Merchant

1. **Hardware-software co-design**: Google's TPU systolic arrays are optimized for the specific computation patterns of their ML frameworks (JAX, XLA). No wasted silicon on features they don't need.

2. **Cost advantage**: [[entities/google-tpu]] cloud instances cost $2.00/FLOPS-hour vs $2.80 for NVIDIA B100 — a 30% saving. At hyperscaler volumes (millions of chips), this translates to billions saved annually.

3. **Supply chain independence**: Custom silicon reduces dependency on NVIDIA's allocation decisions and pricing power. During the 2024-2025 GPU shortage, companies with custom chips had guaranteed supply.

4. **Vertical integration**: When the same organization designs the chip, the compiler, the ML framework, and the model, each layer can be optimized for the others. Google's TPU v4 introduced optical circuit switching — a hardware innovation driven by specific networking needs that no merchant chip vendor would prioritize.

### The CUDA Moat

[[entities/nvidia]]'s strongest defense against custom silicon is not hardware superiority but software ecosystem lock-in. CUDA, cuDNN, TensorRT, and the vast library of optimized kernels represent decades of investment that no single company can replicate. AMD's ROCm attempts portability via HIP but remains less mature. Custom silicon vendors must build their own software stacks — Google has JAX/XLA, Amazon has Neuron SDK — adding significant development cost.

### Walled Gardens vs. Open Ecosystem

A key limitation of custom silicon: most hyperscaler chips are available only through that company's cloud platform. Google TPUs require Google Cloud. Amazon Trainium requires AWS. This creates walled gardens that limit adoption and make custom silicon unavailable for on-premise deployment. The exception is [[entities/cerebras]], which sells systems directly.

## How It Connects

Custom silicon is reshaping [[concepts/ai-hardware-landscape]] by fragmenting NVIDIA's monopoly. It drives [[concepts/ai-infrastructure-investment]] decisions (build vs buy). The tight hardware-software co-design enabled by custom silicon influences [[concepts/ai-accelerators]] design philosophy. Google's TPU success validates the approach for [[concepts/training-vs-inference-hardware]] across both workload types.

## Open Questions

- Will OpenAI's custom chip effort succeed, or will the Broadcom partnership produce something competitive?
- Can custom silicon escape cloud walled gardens to become generally available?
- Will the proliferation of custom chips fragment the AI development ecosystem too far?

## Sources

- [[sources/google-tpu-architecture-gemini]] — the most mature custom silicon program
- [[sources/ai-hardware-accelerators-2026-guide]] — landscape overview
- [[sources/cerebras-vs-sambanova-vs-groq-chips]] — startup custom silicon approaches

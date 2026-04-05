---
title: "Small Language Models (SLMs)"
type: concept
sources: ["[[sources/small-language-models-guide-2026]]"]
related: ["[[concepts/open-source-llms]]", "[[concepts/quantization]]", "[[concepts/local-llm-inference]]", "[[entities/phi]]", "[[entities/gemma]]", "[[concepts/local-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "Models under 10B parameters (Phi-4, Gemma 3, Qwen 3 4B) that run on 4GB RAM with quantization, achieving 10-30x cost reduction vs. LLMs while handling many practical tasks."
---

## Overview

Small Language Models (SLMs) are LLMs with fewer than approximately 10 billion parameters, designed to run on edge devices, consumer hardware, and mobile phones. By 2026, SLMs have reached a quality threshold where 3-4B parameter models can handle many tasks previously requiring 70B+ models, enabled by improved training techniques and [[concepts/quantization]].

SLMs represent the most accessible entry point for [[concepts/local-llm-inference]] and [[concepts/local-knowledge-base]] applications.

## Key Ideas

### Top SLMs (2026)

| Model | Params | MMLU | VRAM (Q4) | Context | Key Strength |
|-------|--------|------|-----------|---------|-------------|
| [[entities/phi]]-4 | 14B | 84.8% | ~10GB | 16K | Beats GPT-4o on MATH |
| [[entities/phi]]-4-mini | 3.8B | 67.3% | ~3GB | 128K | Best reasoning per param |
| [[entities/gemma]] 3 4B | 4B | 59.6% | ~3GB | 128K | 140+ languages, multimodal |
| [[entities/gemma]] 270M | 270M | — | <1GB | — | Mobile: 0.75% battery/25 chats |
| Qwen 3 4B | 4B | ~70% | ~3GB | — | Rivals 72B on some tasks |
| Llama 3.2 3B | 3B | 63.4% | ~2GB | 128K | Best tool-use (67% BFCL) |
| Mistral 7B | 7B | 60.1% | ~5GB | 32K | Proven reliability |

### Cost Advantage

SLMs provide 10-30x cheaper operation versus large models:
- SLM deployment: $150-800/month
- LLM deployment: $15K-75K/month
- Best for: real-time sub-100ms latency, privacy-critical tasks, edge/mobile, domain-specific work

### Edge and Mobile Deployment

- [[entities/gemma]] 270M: 0.75% battery for 25 conversations on Pixel 9 Pro
- WebLLM: browser-based inference retaining 80% of native performance
- 4-bit quantization provides 4x memory traffic reduction for practical mobile use
- ITRI research: edge AI deployment in manufacturing grew 3x between 2025-2026 with SLMs as primary driver

### Dual-Mode Operation

Qwen 3 SLMs support switching between "thinking" mode (deeper reasoning, slower) and "non-thinking" mode (fast responses). This allows dynamic quality/speed tradeoffs within a single model.

### Limitations for KB Applications

For this [[concepts/llm-knowledge-base]], SLMs face real constraints:
- Complex multi-source synthesis (compiling 10+ raw files into a concept article) requires stronger reasoning
- Long context handling (reading entire wiki sections) may exceed smaller context windows
- Quality of generated wiki content may require more human oversight

However, SLMs could serve well for:
- Simple Q&A over the compiled wiki
- Generating first drafts of source summaries
- Linting tasks (checking links, finding orphans)
- Embedding generation for vector search

## Sources
- [[sources/small-language-models-guide-2026]] — comprehensive SLM landscape and benchmarks

## Related Concepts
- [[concepts/open-source-llms]] — SLMs as the lightweight end of the spectrum
- [[concepts/quantization]] — essential for SLM deployment on minimal hardware
- [[concepts/local-llm-inference]] — SLMs as the most accessible entry point
- [[concepts/local-knowledge-base]] — SLMs as potential KB backbone
- [[entities/phi]] — Microsoft's leading SLM family
- [[entities/gemma]] — Google's SLM family with strong multilingual support

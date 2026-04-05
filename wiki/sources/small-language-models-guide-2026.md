---
title: "Source: Best Small Language Models 2026"
type: source-summary
source: "[[raw/small-language-models-guide-2026]]"
related: ["[[concepts/small-language-models]]", "[[entities/phi]]", "[[entities/gemma]]", "[[concepts/quantization]]", "[[concepts/local-llm-inference]]"]
last_compiled: 2026-04-05
summary: "SLMs under 10B params run on 4GB RAM with 4-bit quantization: Phi-4 (14B, beats GPT-4o on MATH), Gemma 3 4B, Qwen 3 4B, Llama 3.2 3B — 10-30x cheaper than LLMs."
---

## Key Points
- SLMs: under 10B parameters, designed for edge devices and consumer hardware
- Phi-4 (14B): 84.8% MMLU, beats GPT-4o on MATH and GPQA
- Phi-4-mini (3.8B): 67.3% MMLU, ~3GB VRAM, 128K context
- Gemma 3 (4B): 128K context, 140+ languages, multimodal vision
- Gemma 270M: 0.75% battery for 25 conversations on mobile
- Qwen 3 (4B): ~70% MMLU, rivals Qwen2.5-72B on specific tasks (18x smaller)
- Llama 3.2 (3B): best tool-use capability (67% BFCL V2)
- VRAM: 3-4B models need 2-4GB (Q4) or 6-8GB (FP16)
- 10-30x cheaper than LLMs ($150-800/month vs $15K-75K)
- WebLLM: browser-based deployment retaining 80% of native performance

## Detailed Summary

[[concepts/small-language-models]] have reached a quality threshold where 3-4B parameter models can handle many tasks previously requiring 70B+ models. The combination of [[concepts/quantization]] (4-bit) and architectural innovations means these models run on laptops, phones, and edge devices.

For [[concepts/local-knowledge-base]] applications, SLMs like Phi-4-mini or Qwen 3 4B could serve as the LLM backbone, though with reduced reasoning capability compared to larger models. The tradeoff is dramatic cost reduction and complete offline operation.

## Related Concepts
- [[concepts/small-language-models]] — core topic
- [[concepts/quantization]] — enables SLMs on minimal hardware
- [[concepts/local-knowledge-base]] — SLMs as potential KB backbone
- [[concepts/local-llm-inference]] — SLMs as the most accessible entry point

---
title: "Source: On-Device LLMs — State of the Union, 2026"
type: source-summary
source: "[[raw/on-device-llms-2026]]"
related: ["[[concepts/edge-inference]]", "[[concepts/quantization]]", "[[entities/executorch]]", "[[concepts/llm-inference-optimization]]"]
last_compiled: 2026-04-05
summary: "Meta AI Research survey: sub-1B to 3B models now practical on mobile with 4-bit quantization, ExecuTorch 1.0, and 20ms/token latency — 10-25x faster than cloud roundtrips."
---

## Key Points
- Practical mobile range: sub-1B to 3B parameters
- Mobile NPUs: 35-60 TOPS (Apple A19, Snapdragon 8 Elite Gen 5, Dimensity 9400+)
- Critical constraint: mobile memory bandwidth (50-90 GB/s) vs datacenter (2-3 TB/s) — 30-50x gap
- ExecuTorch 1.0: 50KB footprint, 12+ hardware backends, serves billions of Meta users
- On-device latency: <20ms/token vs cloud's 200-500ms roundtrip
- Sub-4-bit: BitNet demonstrates native 1.58-bit training

## Detailed Summary

Vikas Chandra's (Meta AI Research) survey maps the [[concepts/edge-inference|on-device LLM]] landscape in 2026. The dominant model range has settled at sub-1B to 3B parameters, with Llama 3.2 (1B/3B), Gemma 3 (270M+), Phi-4 mini (3.8B), and SmolLM2 (135M-1.7B) targeting mobile deployment.

The critical bottleneck is memory bandwidth — mobile devices offer 50-90 GB/s versus datacenter's 2-3 TB/s, making the decode phase severely memory-bound. This drives aggressive [[concepts/quantization|quantization]]: 4-bit AWQ/GPTQ is standard, with emerging sub-4-bit techniques (BitNet's 1.58-bit training, SpinQuant's rotation matrices).

[[entities/executorch|ExecuTorch]] 1.0 (Meta, October 2025) has become the production deployment framework with a 50KB base footprint and 12+ hardware backends. Key use case guidance: frontier reasoning and long conversations remain cloud-suited, while latency-sensitive, privacy-critical, and high-volume applications favor on-device.

## Related Concepts
- [[concepts/edge-inference]] — the central topic
- [[concepts/quantization]] — enabling technology for mobile deployment
- [[concepts/speculative-decoding]] — used on-device for 2.2-3.6x acceleration

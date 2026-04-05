---
title: "Source: Google TPUs Explained — Architecture & Performance for Gemini 3"
type: source-summary
source: "[[raw/google-tpu-architecture-gemini]]"
related: ["[[entities/google-tpu]]", "[[entities/google]]", "[[concepts/custom-silicon]]", "[[concepts/ai-accelerators]]"]
tags: [google, tpu, gemini, custom-silicon, asic]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Complete TPU evolution from v1 (2015, inference-only, 92 TOPS) through Ironwood v7 (2025, 4,614 TFLOPS, 42.5 exaFLOPS per pod); Google trained Gemini 3 entirely on TPUs without GPU fallback."
---

## Key Points

- Seven TPU generations spanning 2015-2025, each with significant architectural innovations
- TPU v4 introduced optical circuit switching (OCS) — replacing fixed electrical fabrics with reconfigurable optical interconnects
- TPU v6e "Trillium": 4.7x peak performance vs v5, 67% energy efficiency gains, Jupiter fabric connecting 100,000+ chips
- Ironwood (v7): ~4,614 TFLOPS per chip, 192GB HBM, ~42.5 exaFLOPS per pod — inference-focused
- Google trained [[entities/gemini]] 3 entirely on TPU v5e and v6e pods — no GPU fallback
- TPU v4 delivers 1.2-1.7x higher throughput than A100 at 53-77% of the power
- TPU deployments use ~3x less electricity and emit ~20x less CO2 than on-premise GPU clusters

## Detailed Summary

Google's TPU program represents the most mature custom silicon effort in AI, with seven generations of chips refined through tight hardware-software co-design. The key insight is vertical integration: by controlling both the chip and the software stack (XLA, JAX, Pathways), Google achieves optimization impossible in NVIDIA's general-purpose ecosystem.

The decision to train Gemini 3 entirely on TPUs — without any GPU fallback — signals a fundamental shift. Hyperscalers increasingly view domain-specific ASICs as superior to general-purpose GPUs when hardware and software can be co-optimized. The cost implications are significant: customers report 4x performance per dollar on TPU v5e compared to equivalent GPU instances.

## Notable Quotes

> "TPU v4 deployments use ~3x less electricity and emit ~20x less CO2 than on-premise GPU clusters for equivalent workloads."

## Concepts Introduced or Discussed

- [[concepts/custom-silicon]] — hyperscaler vertical integration strategy
- [[concepts/ai-accelerators]] — purpose-built AI hardware
- [[concepts/ai-data-center-energy]] — energy efficiency advantages of custom silicon
- [[concepts/training-vs-inference-hardware]] — TPU split into training and inference variants

## Metadata

- **Author**: IntuitionLabs
- **Date Published**: 2025-12-01
- **Format**: article
- **URL**: https://intuitionlabs.ai/articles/google-tpu-architecture-gemini-3

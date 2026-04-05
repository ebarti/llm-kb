---
title: "Groq"
type: entity
entity_type: org
url: "https://groq.com"
related: ["[[concepts/ai-accelerators]]", "[[concepts/training-vs-inference-hardware]]", "[[entities/nvidia]]", "[[entities/cerebras]]"]
tags: [groq, lpu, inference, asic, ai-hardware]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Designed the Language Processing Unit (LPU) for deterministic ultra-low-latency inference; acquired by NVIDIA for $20B to integrate into Rubin platform; 70,000+ developers on GroqCloud; previously valued at $6.9B."
---

## Overview

Groq designed a novel Language Processing Unit (LPU) — a Tensor Streaming Processor with software-defined scheduling optimized exclusively for AI inference. The key innovation is deterministic execution: no hardware context switching, no unpredictable memory access patterns, resulting in consistent sub-millisecond latency regardless of context length.

NVIDIA acquired Groq for $20 billion to integrate its deterministic scheduling technology into the upcoming Vera Rubin platform — a move that validated Groq's approach while demonstrating NVIDIA's determination to defend its inference market.

## Key Facts

- **Type**: Organization (AI chip company, now NVIDIA subsidiary)
- **Founded**: 2016 by Jonathan Ross (formerly Google, helped design TPU v1)
- **Acquisition**: $20B by [[entities/nvidia]]
- **Pre-acquisition valuation**: $6.9B (September 2025, $750M round)
- **Key investors**: Samsung, Cisco, Altimeter, 1789 Capital
- **Flagship product**: Language Processing Unit (LPU)

## LPU Specifications

| Specification | Value |
|--------------|-------|
| Architecture | Tensor Streaming Processor |
| Cores | ~2,600 streaming cores per chip |
| Memory | 32+ GB HBM per board |
| Memory bandwidth | ~5 TB/s (claimed) |
| Process node | TSMC 7nm |
| Power | 1-5 kW per GroqRack |
| Focus | Inference only |

## Performance

- Llama 2 70B at 300 tokens/sec — 10x faster than H100 cluster
- 3-4x faster throughput than comparable GPUs on LLM inference (EE Times benchmark)
- Sub-millisecond latency for transformer layers
- Approximately one-third power consumption of equivalent GPU platforms

## Key Deployments (Pre-Acquisition)

- **Helsinki Data Center**: EU facility (Equinix partnership) for European inference services
- **Saudi Arabia**: $1.5B sovereign fund commitment
- **GroqCloud**: 70,000+ developers using platform
- **Retail/E-commerce**: Reduced recommendation latency from 50ms to 5ms

## Mentioned In

- [[sources/cerebras-vs-sambanova-vs-groq-chips]] — detailed technical comparison
- [[sources/ai-inference-accelerators-compared]] — inference benchmark data

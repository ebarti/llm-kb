---
title: "Inference ASICs Compared: Cerebras vs Groq vs Etched vs Taalas"
type: comparison
subjects: ["[[entities/cerebras]]", "[[entities/groq]]", "[[entities/sambanova]]"]
sources: ["[[sources/ai-inference-accelerators-compared]]", "[[sources/cerebras-vs-sambanova-vs-groq-chips]]"]
related: ["[[concepts/training-vs-inference-hardware]]", "[[concepts/ai-accelerators]]", "[[concepts/ai-hardware-landscape]]"]
tags: [inference, asic, comparison, cerebras, groq, etched, taalas]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Head-to-head inference ASIC comparison: Etched Sohu (62,500 tok/s, transformer-only), Taalas HC1 (17,000 tok/s, single model), Cerebras WSE-3 (2,100, wafer-scale), Groq LPU (594, deterministic), NVIDIA B200 (353, general) — the generality-speed spectrum."
---

## Overview

The AI inference market is fragmenting into specialized hardware niches, each making different bets on the generality-speed tradeoff. This comparison covers the five most notable inference accelerators in 2026, ranging from NVIDIA's general-purpose B200 to Taalas's model-weights-in-silicon approach.

## Comparison Table

| Dimension | NVIDIA B200 | [[entities/groq]] LPU | [[entities/cerebras]] WSE-3 | [[entities/sambanova]] RDU | Etched Sohu | Taalas HC1 |
|-----------|-----------|---------|------------|-----------|-------------|-----------|
| **Speed (tok/s)** | ~353 | ~594 | ~2,100 | ~932 | ~62,500 | ~17,000 |
| **Model support** | Any | Any transformer | Any (with MemoryX) | Any | Transformer only | Single model only |
| **Training** | Yes | No | Yes | Yes | No | No |
| **Architecture** | GPU + tensor cores | Streaming processor | Wafer-scale (900K cores) | Reconfigurable dataflow | Transformer ASIC | Model burned in silicon |
| **Memory** | 192GB HBM3e | 32+GB HBM | 44GB SRAM + MemoryX | 3TB/socket | N/A | Mask ROM |
| **Power** | 1,000W | 1-5 kW/rack | 20-50 kW/system | 10-40 kW/rack | N/A | 2.5 kW/server |
| **Availability** | Ubiquitous | API (NVIDIA now) | Cloud + direct | AWS + direct | Early access | Early access |
| **Obsolescence risk** | Lowest | Low (any transformer) | Low | Low | Medium (transformer bet) | Highest (single model) |

## Analysis

### The Generality-Speed Spectrum

The data reveals a clear pattern: more specialization yields more speed but less flexibility. The spectrum runs:

1. **NVIDIA B200** (353 tok/s): Runs anything, trains and infers, massive ecosystem. Slowest at inference.
2. **Groq LPU** (594 tok/s): Any transformer, inference only. Deterministic latency is unique advantage.
3. **SambaNova RDU** (932 tok/s): Reconfigurable architecture balances speed and flexibility. Most memory per node.
4. **Cerebras WSE-3** (2,100 tok/s): Wafer-scale eliminates memory wall for models that fit. Also trains.
5. **Taalas HC1** (17,000 tok/s): Weights in silicon for single model. 10x power efficiency.
6. **Etched Sohu** (62,500 tok/s): All non-transformer circuitry removed. Fastest, but transformer-only bet.

### Key Insights

**The transformer bet**: Etched and (to a lesser extent) Taalas are betting that the transformer architecture will dominate long enough to justify hardware specialization. If a fundamentally different architecture emerges, these chips become paperweights. [[entities/groq]] and [[entities/cerebras]] hedge this risk by supporting broader workloads.

**The NVIDIA acquisition**: NVIDIA's $20B acquisition of [[entities/groq]] signals that the incumbent views specialized inference as a real threat to its market. By absorbing Groq's deterministic scheduling technology, NVIDIA aims to close the inference gap in its Vera Rubin architecture.

**The asymmetric dependency**: All inference ASICs depend on models trained on NVIDIA GPUs or TPUs. This creates a structural relationship where inference hardware companies are downstream customers of training hardware companies.

## When to Use Each

| Scenario | Best Choice | Why |
|---------|-------------|-----|
| Maximum flexibility needed | NVIDIA B200 | Only option for training + inference + any model |
| Consistent low latency | Groq LPU | Deterministic regardless of context length |
| Largest possible models | SambaNova RDU | 3TB memory per socket |
| Known high-volume model | Etched Sohu | 100x+ speed for transformers |
| Single model at massive scale | Taalas HC1 | Weights in silicon, 10x power savings |
| Models that fit in 44GB | Cerebras WSE-3 | 7,000x bandwidth, no memory wall |

## Sources

- [[sources/ai-inference-accelerators-compared]] — benchmark data
- [[sources/cerebras-vs-sambanova-vs-groq-chips]] — detailed specifications and financials

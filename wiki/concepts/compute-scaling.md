---
title: "Compute Scaling"
type: concept
sources: ["[[sources/epoch-ai-scaling-limits-2030]]", "[[sources/aschenbrenner-situational-awareness]]", "[[sources/sutskever-ssi-safe-superintelligence]]", "[[sources/ai-scaling-paradigm-shift-2026]]", "[[sources/ai-economics-investment-2026]]"]
related: ["[[concepts/path-to-agi]]", "[[concepts/test-time-compute]]", "[[concepts/ai-energy-and-infrastructure]]", "[[concepts/data-wall]]", "[[concepts/ai-economics]]"]
tags: [compute, scaling-laws, infrastructure, chips, power, training]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The multi-dimensional landscape of AI scaling: pre-training scaling shows diminishing returns, but test-time compute and algorithmic efficiency open new dimensions — constrained by power, chips, data, and capital."
---

## Overview

Compute scaling — the relationship between computational resources and AI capability — has been the primary driver of AI progress since 2018. The Kaplan (2020) and Chinchilla (2022) scaling laws established that more compute + more data = predictably better models. This powered the GPT-2 through GPT-4 progression. However, by 2025-2026, this paradigm has fractured into multiple scaling dimensions, each with distinct constraints and implications for [[concepts/path-to-agi]].

## Key Ideas

### The Three Eras

**Era 1: Pre-Training Scaling (2018-2023)**
- More parameters + more data = better, predictably
- GPT-2 (4e21 FLOP) → GPT-4 (8e24-4e25 FLOP): ~3-4 orders of magnitude
- Chinchilla established optimal compute-data ratios
- This era is now hitting diminishing returns

**Era 2: Post-Training Scaling (2023-2025)**
- RLHF, DPO, instruction tuning improve behavior without larger base models
- DeepSeek-R1 proved pure RL produces reasoning matching o1
- Lower marginal cost than pre-training scaling

**Era 3: Test-Time Compute (2024-present)**
- Spending more compute at inference via deliberation and search
- 10-100x more tokens per query for better answers
- New cost structure: per-query rather than per-training-run
- See [[concepts/test-time-compute]]

### Four Physical Constraints (Epoch AI Analysis)

[[sources/epoch-ai-scaling-limits-2030]] identifies the binding constraints for continued scaling through 2030:

| Constraint | Current | 2030 Projection | Severity |
|-----------|---------|-----------------|----------|
| **Power** | 40 GW US data center capacity | 90 GW possible | Most binding |
| **Chips** | 3.76M GPUs (2023) | 20-400M H100-equiv | Second most |
| **Data** | ~500T words indexed | +50%, multimodal 3x | Less binding |
| **Latency** | 110ms inter-DC | 4-20 Pbps bandwidth | Least binding |

A 2e29 FLOP training run (another GPT-2→GPT-4 jump) requires ~6 GW of power and ~20M GPUs — physically possible but requiring hundreds of billions in investment.

### The Scaling Debate

**Aschenbrenner**: Scaling continues to work. AGI by 2027 driven by ~0.5 OOMs/year compute + ~0.5 OOMs/year algorithmic efficiency + unhobbling gains.

**Sutskever**: "The age of scaling is ending." Pre-training has exhausted high-quality text. Breakthroughs require novel learning methods, not more GPUs. "It is back to the age of research again, just with big computers."

**Epoch AI**: Physically possible to continue through 2030 with massive investment. Power is the binding constraint.

**Apple ML Research**: Reasoning models may be "illusion of thinking" — a narrative justifying continued investment without proportional returns.

### Current Supply Constraints (2026)

- GPU lead times: 36-52 weeks for data center GPUs
- NVIDIA Rubin entering production, volume shipments H2 2026
- Rubin output ceiling: 200-300K GPUs for 2026
- Memory chip shortage: AI consumes 70% of DRAM, prices up 20%
- HBM chips sold out through 2026

## How It Connects

- [[concepts/path-to-agi]] — Compute is the primary mechanism in Aschenbrenner's AGI prediction
- [[concepts/test-time-compute]] — The new scaling frontier that may bypass pre-training limits
- [[concepts/ai-energy-and-infrastructure]] — Power as the ultimate bottleneck
- [[concepts/data-wall]] — The complementary constraint on training data
- [[concepts/ai-economics]] — $700B+ Big Tech CapEx in 2026 is a bet on continued scaling returns
- [[concepts/intelligence-explosion]] — Post-AGI compute requirements dwarf current levels

## Open Questions

- Is Sutskever right that pre-training scaling is fundamentally exhausted, or will new data sources reignite it?
- Will test-time compute prove a true new scaling dimension or a diminishing-returns add-on?
- Can distributed training across multiple data centers overcome single-facility power limits?
- At what point does the cost of scaling exceed the economic value of the resulting capabilities?
- Will NVIDIA's Rubin platform deliver the efficiency gains needed to sustain progress?

## Sources

- [[sources/epoch-ai-scaling-limits-2030]] — The definitive four-constraint analysis
- [[sources/aschenbrenner-situational-awareness]] — The bullish scaling extrapolation
- [[sources/sutskever-ssi-safe-superintelligence]] — The "end of scaling" thesis
- [[sources/ai-scaling-paradigm-shift-2026]] — Three eras framework
- [[sources/ai-economics-investment-2026]] — The investment picture

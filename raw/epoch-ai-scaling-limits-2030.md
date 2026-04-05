---
title: "Can AI Scaling Continue Through 2030?"
source: "https://epoch.ai/blog/can-ai-scaling-continue-through-2030/"
author: "Epoch AI"
date_published: 2024-11-01
date_ingested: 2026-04-05
tags: [compute-scaling, power, chips, data-wall, infrastructure]
type: article
status: raw
discovered_via: search
---

# Can AI Scaling Continue Through 2030? — Epoch AI

## Core Conclusion

Epoch AI projects that training runs of 2e29 FLOP will likely be feasible by 2030, representing a scale increase equivalent to GPT-4's advantage over GPT-2. This assumes the current 4x annual growth in training compute continues.

## Four Key Constraints

### 1. Power Supply

Single data center campus: 1-5 GW capacity supports 1e28 to 3e29 FLOP runs.
Geographically distributed networks: 2-45 GW capacity supports 2e28 to 2e30 FLOP runs.
Companies like Microsoft/OpenAI are planning 5 GW facilities by 2030.
US data center power capacity could grow from 40 GW to 90 GW by 2030.

Key efficiency factors reducing power demand:
- Hardware improving ~1.28x per year in FLOP/Watt
- Shift to FP8 precision training (2x more efficient than FP16)
- Training runs extending 3x longer, spreading consumption over time
- Net result: 2e29 FLOP training requires ~200x more power than Llama 3.1 405B (6 GW vs. 27 MW)

### 2. Chip Manufacturing Capacity

Current production: ~3.76M data center GPUs shipped in 2023
2024 projection: 1.5-2M H100 units
2030 requirement for 2e29 FLOP: ~20M H100-equivalent GPUs needed
Realistic production capacity: 100M H100 equivalents possible (range: 20-400M)

Primary bottlenecks:
- CoWoS packaging capacity (TSMC expanding 30-100% annually)
- High-bandwidth memory production (SK Hynix targeting 60% annual growth)
- These constraints likely bind before wafer production

### 3. Data Availability

Indexed web text: ~500 trillion words, projected to increase 50% by 2030
Multimodal data (images, video, audio) could triple available training data
Estimated token pool by 2030: 400 trillion to 20 quadrillion tokens
Training capacity enabled: 6e28 to 2e32 FLOP runs

Limiting factors: Data quality, availability for single training run, synthetic data generation potential remain uncertain.

### 4. Latency Wall

Geographically distributed runs: Inter-data center latency ~110ms round-trip
Bandwidth constraints: 4-20 Petabits/second projected by 2030
Conclusion: Latency and bandwidth unlikely to be primary constraints vs. power/chips

## Which Constraint Binds First?

Power emerges as the most restrictive bottleneck, followed by chip manufacturing capacity. Data scarcity and latency walls pose less severe limitations under current trends.

## Investment Requirements

Achieving 2e29 FLOP scaling "depends on willingness to invest hundreds of billions of dollars." Economic analysis of these decisions lies beyond the report's scope.

## Uncertainty Ranges

Chip manufacturing shows widest uncertainty band (20M-400M H100 equivalents). Power constraints show more defined ranges based on utility company forecasts and announced corporate plans.

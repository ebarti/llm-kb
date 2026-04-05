---
title: "Source: Can AI Scaling Continue Through 2030? — Epoch AI"
type: source-summary
source: "[[raw/epoch-ai-scaling-limits-2030]]"
related: ["[[concepts/compute-scaling]]", "[[concepts/ai-economics]]", "[[concepts/ai-energy-and-infrastructure]]", "[[entities/epoch-ai]]"]
tags: [compute-scaling, power, chips, data-wall, infrastructure]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Epoch AI projects 2e29 FLOP training runs feasible by 2030 — equivalent to another GPT-2→GPT-4 jump — with power as the binding constraint, followed by chip manufacturing capacity."
---

## Key Points

- Training runs of 2e29 FLOP likely feasible by 2030, assuming 4x annual compute growth continues
- Power is the most restrictive bottleneck: single campus needs 1-5 GW, distributed networks 2-45 GW
- Chip manufacturing second constraint: 20M H100-equivalents needed, 100M realistic (range: 20-400M)
- Data scarcity less binding than power/chips under current trends (400T-20Q tokens by 2030)
- Latency and bandwidth unlikely to be primary constraints
- Requires "hundreds of billions of dollars" in investment

## Detailed Summary

[[entities/epoch-ai]] published this analysis examining four constraints on continued [[concepts/compute-scaling]] through 2030. The core finding: another GPT-2-to-GPT-4-sized leap is physically and economically plausible, but depends on massive infrastructure buildout.

### Power (Most Binding)
US data center power capacity could grow from 40 GW to 90 GW by 2030. Microsoft/OpenAI plan 5 GW facilities. Hardware efficiency improves ~1.28x/year in FLOP/Watt. FP8 precision doubles efficiency over FP16. A 2e29 FLOP run would require ~6 GW — 200x more than Llama 3.1 405B (27 MW).

### Chips (Second Most Binding)
~3.76M data center GPUs shipped in 2023; ~1.5-2M H100s in 2024. The 2e29 FLOP target needs ~20M H100-equivalents. TSMC CoWoS packaging and HBM production are primary bottlenecks, expanding 30-100% annually. Widest uncertainty band: 20M-400M H100 equivalents possible.

### Data (Less Binding)
~500 trillion words indexed on web, projected +50% by 2030. Multimodal data could triple the pool. Synthetic data generation offers additional expansion. Quality remains uncertain.

### Latency (Least Binding)
Inter-data center latency (~110ms) and bandwidth (4-20 Pbps by 2030) unlikely to be primary constraints.

## Concepts Introduced or Discussed

- [[concepts/compute-scaling]] — Four-constraint analysis framework
- [[concepts/ai-energy-and-infrastructure]] — Power as binding constraint
- [[concepts/data-wall]] — Training data exhaustion timeline
- [[concepts/ai-economics]] — Investment requirements

## Metadata

- **Author**: Epoch AI research team
- **Date Published**: 2024-11-01
- **Format**: Research analysis / blog post
- **URL**: https://epoch.ai/blog/can-ai-scaling-continue-through-2030/

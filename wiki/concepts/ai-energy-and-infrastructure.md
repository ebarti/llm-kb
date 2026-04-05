---
title: "AI Energy and Infrastructure"
type: concept
sources: ["[[sources/ai-economics-investment-2026]]", "[[sources/epoch-ai-scaling-limits-2030]]", "[[sources/aschenbrenner-situational-awareness]]"]
related: ["[[concepts/compute-scaling]]", "[[concepts/ai-economics]]", "[[concepts/path-to-agi]]"]
tags: [energy, infrastructure, data-centers, power, sustainability]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Data centers consume 415 TWh (1.5% of global electricity) in 2024, doubling to 945 TWh by 2030 — with AI-driven servers growing at 30% annually, making power the binding constraint on AI scaling."
---

## Overview

The physical infrastructure powering AI — data centers, power plants, cooling systems, chip fabrication facilities — has become the primary bottleneck for continued AI progress. [[sources/epoch-ai-scaling-limits-2030]] identifies power as the most binding constraint on compute scaling through 2030. The scale of energy demand is reshaping national power grids, driving inflation, and forcing policymakers to reconsider energy policy.

## Key Ideas

### Current Energy Consumption

IEA data (2024):
- Global data center electricity: ~415 TWh (1.5% of global electricity)
- US data centers: 183 TWh (4%+ of US electricity consumption)
- Annual growth rate: 12% over the past five years, accelerating to 15%

### Projections

By 2030 (IEA Base Case):
- Global: ~945 TWh (3% of global electricity) — a doubling from 2024
- US: 426 TWh (133% growth)
- AI-driven accelerated servers: growing at 30% annually
- Conventional servers: growing at 9% annually

Near-term milestone: AI data centers could need 68 GW of power capacity by 2027 — approximately equivalent to California's total current capacity.

### Geographic Distribution

| Region | 2024 | 2030 Projected | Growth |
|--------|------|----------------|--------|
| United States | 183 TWh | 426 TWh | +133% |
| China | ~100 TWh | ~275 TWh | +170% |
| Europe | ~65 TWh | ~110 TWh | +70% |
| Ireland | 21% of national electricity | Projected 32% | |

Per-capita: US leads at ~540 kWh per capita (2024), projected to exceed 1,200 kWh by 2030 — roughly 10% of an American household's annual use.

### The Power Constraint on Scaling

[[sources/epoch-ai-scaling-limits-2030]] finds power is the most binding constraint for continued AI progress:
- A 2e29 FLOP training run (another GPT-2→GPT-4 jump) requires ~6 GW
- Single campus capacity: 1-5 GW
- Distributed networks: 2-45 GW
- US capacity could grow from 40 GW to 90 GW by 2030 with major investment
- Microsoft/OpenAI planning 5 GW facilities

### Supply Chain Bottlenecks

Beyond power, the physical infrastructure faces multiple constraints:
- GPU lead times: 36-52 weeks
- HBM (high-bandwidth memory) sold out through 2026
- AI consumes 70% of DRAM; prices up 20%
- TSMC CoWoS packaging capacity is a primary chip bottleneck
- NVIDIA Rubin output capped at 200-300K GPUs for 2026

### Economic and Inflationary Impact

Goldman Sachs warns that data center energy demand will boost core inflation by 0.1% in both 2026 and 2027. NPR reports utility customers are beginning to see rate increases attributable to data center construction.

### Aschenbrenner's Vision

[[entities/leopold-aschenbrenner]] frames energy infrastructure as a national security requirement: American electricity production must expand "tens of percent," with natural gas from shale fields as the most plausible expansion path. This implies a scale of infrastructure buildout comparable to post-WWII industrialization.

## How It Connects

- [[concepts/compute-scaling]] — Power is the binding constraint on compute progress
- [[concepts/ai-economics]] — Infrastructure spending dominates AI investment (59% of $2.52T)
- [[concepts/path-to-agi]] — Physical infrastructure determines the pace of progress
- [[concepts/intelligence-explosion]] — Post-AGI compute demands would dwarf current levels

## Open Questions

- Can renewable energy scale fast enough, or does AI progress depend on fossil fuel expansion?
- Will distributed training across geographies overcome single-facility power limits?
- Does the inflationary impact of data center energy demand create political backlash against AI development?
- Will hardware efficiency gains (1.28x/year in FLOP/Watt) outpace demand growth?
- How does nuclear power (particularly SMRs) change the long-term energy picture for AI?

## Sources

- [[sources/ai-economics-investment-2026]] — Energy data from IEA, Goldman Sachs
- [[sources/epoch-ai-scaling-limits-2030]] — Power as binding constraint analysis
- [[sources/aschenbrenner-situational-awareness]] — National infrastructure buildout vision

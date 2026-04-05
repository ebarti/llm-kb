---
title: "AI for Weather and Climate"
type: concept
sources: ["[[sources/gencast-weather-prediction]]", "[[sources/ucsd-nine-ai-breakthroughs]]"]
related: ["[[concepts/ai-for-scientific-discovery]]", "[[entities/gencast]]", "[[entities/google-deepmind]]"]
tags: [weather-prediction, climate-modeling, ai-science, gencast]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "AI weather models (GenCast, WeatherNext 2, NVIDIA Earth-2) outperform traditional supercomputer-based forecasting on 97%+ of metrics while running 100x+ faster. Applications span disaster preparedness, renewable energy, and 100-year climate projections."
---

## Overview

AI weather and climate models use deep learning to predict atmospheric conditions, achieving accuracy that surpasses decades-refined physics-based numerical weather prediction (NWP) systems. The transition from AI-as-research-tool to AI-as-operational-system is happening rapidly, with NOAA deploying AI-driven global models operationally.

## Key Systems

### GenCast (Google DeepMind, 2024)
- Diffusion model adapted for spherical Earth geometry at 0.25-degree resolution.
- Generates 50+ ensemble predictions per forecast.
- Outperforms ECMWF ENS on 97.2% of 1,320 tested combinations (99.8% beyond 36 hours).
- 15-day forecasts in 8 minutes on a single TPU v5 (vs hours on supercomputers).
- Trained on 40 years of ERA5 reanalysis data.

### WeatherNext 2 (Google DeepMind, 2025-2026)
- Successor to GenCast with further accuracy improvements.
- Part of an expanding family of weather AI models.

### NVIDIA Earth-2 (2026)
- Open-source weather AI models.
- Claims superiority over GenCast on 70+ weather variables.
- Provides accessible platform for the weather research community.

### Spherical DYffusion (UC San Diego + Allen Institute, 2025)
- Long-range climate modeling: 100-year projections in 25 hours.
- 25x faster than conventional methods.
- Does not require supercomputers — runs on standard hardware.

## Applications

| Application | Capability | Impact |
|-------------|-----------|--------|
| Tropical cyclone tracking | Superior path predictions | Improved evacuation planning |
| Extreme weather detection | Heat waves, cold snaps, high winds | Early warning systems |
| Renewable energy | Wind farm power generation forecasting | Grid optimization |
| Disaster preparedness | Anticipatory Action programs | Pre-positioned relief funding |
| Climate policy | 100-year projections | Evidence-based policy planning |
| Wildfire response | AI camera networks + spread prediction | Real-time firefighting support |

## Why AI Weather Models Work

The key insight: weather prediction is fundamentally a pattern-matching problem over high-dimensional data. Physics-based NWP solves differential equations from first principles, which is computationally expensive but theoretically principled. AI models learn statistical patterns from decades of observational data, achieving comparable or superior accuracy at a fraction of the computational cost.

The ensemble approach (GenCast generating 50+ predictions) is crucial for uncertainty quantification — essential for high-stakes decisions about evacuation, infrastructure protection, and resource allocation.

## The Speed Advantage

The 100x+ speed advantage is not just about cost savings. It enables:
- **Higher resolution**: More compute budget for finer spatial/temporal resolution.
- **Larger ensembles**: More predictions for better uncertainty estimates.
- **Real-time updates**: Continuous re-forecasting as new data arrives.
- **Democratization**: Developing nations can run sophisticated forecasts on modest hardware.

## Open Questions

- Can AI weather models handle unprecedented extreme events (outside training distribution)?
- Will physics-based and AI models converge into hybrid systems?
- How will operational forecasters integrate AI model outputs into workflows?
- Can AI climate models capture tipping points and non-linear regime changes?

## Sources

- [[sources/gencast-weather-prediction]] — GenCast architecture, benchmarks, and applications
- [[sources/ucsd-nine-ai-breakthroughs]] — Spherical DYffusion and wildfire detection

## Related Concepts

- [[concepts/ai-for-scientific-discovery]] — broader context
- [[entities/gencast]] — primary system

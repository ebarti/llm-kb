---
title: "GenCast"
type: entity
entity_type: tool
url: "https://deepmind.google/blog/gencast-predicts-weather-and-the-risks-of-extreme-conditions-with-sota-accuracy/"
related: ["[[concepts/ai-weather-climate]]", "[[concepts/ai-for-scientific-discovery]]", "[[entities/google-deepmind]]"]
tags: [gencast, weather-prediction, diffusion-model]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "DeepMind's diffusion-based weather forecasting model. Outperforms ECMWF ENS on 97.2% of metrics, produces 15-day ensemble forecasts in 8 minutes on one TPU. Published in Nature (Dec 2024). Successor: WeatherNext 2."
---

## Overview

GenCast is [[entities/google-deepmind]]'s AI weather forecasting system based on diffusion models adapted for spherical Earth geometry. It represents the current state of the art in probabilistic weather prediction, outperforming the world's leading operational system.

## Key Facts

- **Type**: AI system / weather forecasting model
- **Creator**: Google DeepMind
- **Published**: Nature, December 2024
- **Notable for**: Outperforming ECMWF ENS on 97.2% of forecast combinations

## Performance

| Metric | Value |
|--------|-------|
| Accuracy vs ECMWF ENS | 97.2% superior (all combinations) |
| Accuracy beyond 36 hours | 99.8% superior |
| Forecast range | 15 days |
| Resolution | 0.25 degrees global |
| Ensemble size | 50+ predictions |
| Speed | 8 minutes on single TPU v5 |
| Training data | 40 years ERA5 reanalysis |

## Applications

- Tropical cyclone track prediction.
- Extreme weather early warning (heat, cold, wind).
- Wind farm power generation forecasting.
- Humanitarian Anticipatory Action programs.

## Successors and Competitors

- **WeatherNext 2** (Google DeepMind): Next-generation family.
- **NVIDIA Earth-2**: Open-source competitor; claims superiority on 70+ variables.
- **NOAA AI models**: Operational deployment of AI weather models.

## Mentioned In

- [[sources/gencast-weather-prediction]] — technical details and benchmarks

## External References

- [Nature paper](https://www.nature.com/articles/s41586-024-08252-9)
- [DeepMind blog](https://deepmind.google/blog/gencast-predicts-weather-and-the-risks-of-extreme-conditions-with-sota-accuracy/)

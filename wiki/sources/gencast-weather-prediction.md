---
title: "Source: GenCast — AI Weather Prediction with SOTA Accuracy"
type: source-summary
source: "[[raw/gencast-weather-prediction]]"
related: ["[[concepts/ai-weather-climate]]", "[[concepts/ai-for-scientific-discovery]]", "[[entities/gencast]]", "[[entities/google-deepmind]]"]
tags: [gencast, weather-prediction, ai-science, climate]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "DeepMind's GenCast diffusion model outperforms ECMWF's ENS on 97.2% of tested forecast combinations (99.8% beyond 36 hours). Produces 15-day ensemble forecasts in 8 minutes on a single TPU vs hours on supercomputers. Now used for humanitarian Anticipatory Action programs."
---

## Key Points

- GenCast is a diffusion model adapted for spherical Earth geometry at 0.25-degree global resolution.
- Generates 50+ ensemble predictions per forecast (vs single deterministic predictions).
- 97.2% more accurate than ECMWF's ENS across 1,320 tested combinations; 99.8% beyond 36-hour lead times.
- Produces 15-day forecasts in 8 minutes on a single TPU v5 vs hours on supercomputers.
- Superior tropical cyclone track predictions, wind energy forecasting, and extreme weather detection.

## Detailed Summary

[[entities/gencast]] represents the culmination of [[entities/google-deepmind]]'s weather AI program, applying diffusion models to probabilistic weather forecasting. Trained on four decades of ECMWF ERA5 data, it generates ensemble forecasts that capture uncertainty — essential for high-stakes decisions around extreme weather.

The performance improvement over the world's best operational system (ECMWF ENS) is dramatic: 97.2% superiority across all tested forecast combinations, reaching 99.8% for longer lead times. The speed advantage is equally significant — a single TPU producing in 8 minutes what previously required hours on supercomputers.

By 2025, international aid organizations began using GenCast data for [[concepts/ai-weather-climate|Anticipatory Action]] programs, releasing disaster relief funds before storms hit. The successor WeatherNext 2 family further extends capabilities, while NVIDIA's Earth-2 provides open-source competition.

## Concepts Introduced or Discussed

- [[concepts/ai-weather-climate]] — core application
- [[concepts/ai-for-scientific-discovery]] — GenCast as exemplar

## Metadata

- **Author**: Google DeepMind
- **Date Published**: December 2024
- **Format**: article
- **URL**: https://deepmind.google/blog/gencast-predicts-weather-and-the-risks-of-extreme-conditions-with-sota-accuracy/

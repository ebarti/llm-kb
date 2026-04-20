---
title: "GenCast: AI Weather Prediction with State-of-the-Art Accuracy"
source: "https://deepmind.google/blog/gencast-predicts-weather-and-the-risks-of-extreme-conditions-with-sota-accuracy/"
author: "Google DeepMind"
date_published: 2024-12-04
date_ingested: 2026-04-05
tags: [gencast, weather-prediction, ai-science, deepmind, climate]
type: article
status: raw
discovered_via: search
---

# GenCast: Technical Details and Performance

## Architecture & Design

GenCast is a diffusion model adapted for spherical Earth geometry. Unlike deterministic models providing single forecasts, GenCast generates ensemble forecasts of 50+ predictions, each representing a possible weather trajectory. Operates at 0.25 degree resolution globally. Trained on four decades of historical weather data from ECMWF's ERA5 archive.

## Performance Benchmarks

- 97.2% superior accuracy across 1,320 tested forecast combinations vs ECMWF's ENS system.
- 99.8% better performance at lead times exceeding 36 hours.
- Forecasts extend 15 days in advance.

## Speed Advantages

A single Google Cloud TPU v5 produces one 15-day forecast in just 8 minutes. Traditional physics-based ensemble forecasts require hours on a supercomputer with tens of thousands of processors.

## Extreme Weather Applications

- **Tropical Cyclones**: Superior track predictions, increasingly accurate as storms approach landfall.
- **Heat/Cold Events & High Winds**: Consistently outperformed ENS.
- **Wind Energy**: Improved accuracy in predicting global wind farm power generation.

## Successors

- **WeatherNext 2**: Google DeepMind's next-generation family surpassing GenCast.
- **NVIDIA Earth-2**: Open-source competitor claiming superiority on 70+ weather variables.
- **NOAA**: Deploying AI-driven global weather models operationally.

## Real-World Impact

By 2025, international aid organizations began using GenCast-derived data for Anticipatory Action programs, releasing disaster relief funds based on high-probability AI forecasts before storms hit.

---
title: "Gaussian Splatting"
type: concept
sources: ["[[sources/nerf-vs-gaussian-splatting-2025]]"]
related: ["[[concepts/neural-radiance-fields]]", "[[concepts/3d-generation]]", "[[concepts/diffusion-models]]"]
tags: [gaussian-splatting, 3d-generation, real-time-rendering, 3d-reconstruction]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Explicit 3D scene representation using millions of anisotropic Gaussian primitives rendered via GPU rasterization -- 10-50x faster than NeRF with 90% less memory, achieving 60fps+ real-time rendering and adopted by Zillow, Esri, and DJI in production."
---

## Overview

3D Gaussian Splatting represents scenes as collections of millions of anisotropic 3D Gaussian distributions, each with position, covariance, opacity, and color (via spherical harmonics). Unlike [[concepts/neural-radiance-fields]] which encode scenes as implicit neural functions, Gaussian Splatting uses explicit primitives that can be directly rasterized by GPU hardware, enabling real-time rendering at 60fps+.

Introduced in 2023, Gaussian Splatting became the breakout technology of 2025-2026, crossing from research into commercial production with adoption by Zillow, Esri, DJI, and Matterport.

## Key Ideas

### How It Works

1. **Initialization**: From Structure-from-Motion point cloud or random placement
2. **Optimization**: Gradient descent adjusts each Gaussian's position, covariance, opacity, and color to match input images
3. **Adaptive density control**: Split large Gaussians, clone small ones, prune transparent ones
4. **Rendering**: Tile-based rasterization sorts Gaussians by depth and alpha-composites them per pixel

### Performance vs. NeRF

| Metric | Gaussian Splatting | NeRF |
|--------|-------------------|------|
| Training | 30 min - 2 hours | Hours to days |
| Rendering | 60fps+ real-time | Seconds per frame |
| Memory | 90% reduction | High |
| Quality | High | Ultra-high (4K/8K) |
| Editing | Real-time manipulation | Requires retraining |
| Hardware | Consumer GPU | Research GPU |

### Commercial Applications

- **Real estate**: Zillow SkyTours, Apartments.com (Matterport 3D Exteriors)
- **GIS**: Esri ArcGIS Pro 2.6
- **Drone mapping**: DJI Terra
- **Gaming**: Real-time environment creation
- **AR/VR**: Mobile device deployment
- **Live streaming**: Real-time 3D content delivery

## How It Connects

Gaussian Splatting provides the real-time rendering layer for [[concepts/3d-generation]], complementing [[concepts/diffusion-models]]-guided text-to-3D pipelines. Future NeRF-GS hybrids aim to combine NeRF's quality with Gaussian Splatting's speed.

## Sources

- [[sources/nerf-vs-gaussian-splatting-2025]] -- NeRF vs GS comparison

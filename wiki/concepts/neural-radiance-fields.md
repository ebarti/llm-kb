---
title: "Neural Radiance Fields (NeRF)"
type: concept
sources: ["[[sources/nerf-vs-gaussian-splatting-2025]]"]
related: ["[[concepts/gaussian-splatting]]", "[[concepts/3d-generation]]", "[[concepts/diffusion-models]]"]
tags: [nerf, 3d-generation, neural-rendering, implicit-representation]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Implicit neural scene representation mapping 3D coordinates to color and density via neural networks -- produces photorealistic 4K/8K reconstructions but requires hours of training and seconds per frame to render, being supplanted by Gaussian Splatting for real-time applications."
---

## Overview

Neural Radiance Fields (NeRF), introduced by Mildenhall et al. (2020), represent 3D scenes as continuous implicit functions encoded in neural networks. Given a 3D coordinate and viewing direction, the network outputs the color and volume density at that point. Rendering involves casting rays through the scene, sampling points along each ray, querying the network, and compositing the results via volumetric rendering.

NeRF produces the highest-quality 3D reconstructions available, supporting ultra-high-resolution (4K/8K) outputs with precise material and texture fidelity. However, its reliance on neural network evaluation per pixel makes it fundamentally slow compared to [[concepts/gaussian-splatting]]'s explicit rasterization approach.

## Key Ideas

### How It Works

1. **Input**: Multiple photographs of a scene from known camera positions
2. **Network**: An MLP maps (x, y, z, viewing direction) to (color, density)
3. **Volume rendering**: Rays cast through scene; points sampled along ray; network queried at each sample
4. **Training**: Photometric loss between rendered and actual images optimizes network weights
5. **Inference**: Render novel viewpoints by casting rays from new camera positions

### Acceleration Techniques

The original NeRF was very slow. Key accelerations include:
- **Instant-NGP**: Multi-resolution hash encoding achieves 1000x training speedup
- **ZipNeRF**: Combines hash grids with anti-aliased rendering
- **TensoRF**: Tensor decomposition for compact, fast representations

### Applications

NeRF excels where quality trumps speed:
- High-end film and advertising production
- Medical imaging and scientific visualization
- Archaeological and cultural heritage reconstruction
- Virtual tourism experiences

### Relationship to 3D Generation

NeRF serves as a 3D representation in text-to-3D pipelines where [[concepts/diffusion-models]] provide 2D priors via Score Distillation Sampling (SDS). The generated NeRF can then be rendered from any viewpoint.

## How It Connects

NeRF is the quality benchmark for [[concepts/3d-generation]], now increasingly complemented by [[concepts/gaussian-splatting]] for real-time applications. NeRF-GS hybrids aim to combine the best of both approaches.

## Sources

- [[sources/nerf-vs-gaussian-splatting-2025]] -- NeRF vs GS comparison

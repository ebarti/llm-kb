---
title: "3D Generation"
type: concept
sources: ["[[sources/nerf-vs-gaussian-splatting-2025]]"]
related: ["[[concepts/neural-radiance-fields]]", "[[concepts/gaussian-splatting]]", "[[concepts/diffusion-models]]", "[[concepts/image-generation]]"]
tags: [3d-generation, text-to-3d, nerf, gaussian-splatting, generative-ai]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "AI-driven synthesis of 3D content from text, images, or captured scenes -- split between NeRF (implicit neural, ultra-high quality) and Gaussian Splatting (explicit primitives, 10-50x faster), with text-to-3D enabled by diffusion-guided optimization like Hunyuan3D-2."
---

## Overview

3D generation encompasses AI systems that create three-dimensional content -- meshes, point clouds, radiance fields, or Gaussian representations -- from text descriptions, 2D images, or real-world captures. The field is split between two fundamental representation paradigms: [[concepts/neural-radiance-fields]] (implicit neural functions) and [[concepts/gaussian-splatting]] (explicit Gaussian primitives), with the latter dominating practical applications in 2025-2026 due to 10-50x speed advantages.

Text-to-3D generation combines [[concepts/diffusion-models]] with 3D optimization techniques, using 2D diffusion priors to guide the construction of 3D representations.

## Key Ideas

### Two Representation Paradigms

**[[concepts/neural-radiance-fields]] (NeRF)**
- Represents scenes as continuous implicit functions mapping 3D coordinates to color and density
- Requires neural network evaluation for each pixel during rendering
- Produces ultra-high quality (4K/8K) reconstructions with precise material fidelity
- Training: hours to days; rendering: seconds per frame
- Excels in: high-end film, medical imaging, cultural heritage preservation

**[[concepts/gaussian-splatting]]**
- Represents scenes as millions of explicit 3D Gaussian distributions
- Rendered via GPU rasterization, not neural network inference
- Real-time rendering at 60fps+ with 90% memory reduction vs. NeRF
- Training: 30 minutes to 2 hours
- Excels in: game development, AR/VR, live streaming, real-time editing

### Text-to-3D Methods

Text-to-3D generation leverages pre-trained 2D [[concepts/diffusion-models]] as optimization guides:

- **Score Distillation Sampling (SDS)**: Uses a 2D diffusion model to provide gradients that optimize a 3D representation (NeRF or mesh) to look realistic from all viewpoints
- **Multi-view diffusion**: Generates consistent multi-view images from text, then reconstructs 3D from these views
- **Direct 3D diffusion**: Models like Tencent's Hunyuan3D-2 apply hierarchical diffusion directly in 3D space, creating textured meshes with 500K+ vertices in under 10 seconds

### Commercial Adoption

Gaussian Splatting has crossed from research to production:
- **Real estate**: Zillow SkyTours, Apartments.com (via Matterport)
- **GIS/Mapping**: Esri ArcGIS Pro 2.6, DJI Terra
- **Market size**: $4.5B projected, growing at 35%+

### Future Convergence

By 2026-2027, 2D, 3D, and video models are expected to merge into unified systems enabling:
- Full scene understanding with physics
- Agents that reason in 3D space
- Text/video to interactive 3D environments

## How It Connects

3D generation builds on the same [[concepts/diffusion-models]] foundations as [[concepts/image-generation]], using 2D diffusion priors to guide 3D optimization. The [[concepts/diffusion-transformer]] architectures extend naturally to 3D (DiT-3D). [[concepts/gaussian-splatting]] and [[concepts/neural-radiance-fields]] provide the 3D representation layer, while [[concepts/video-generation]] shares the challenge of temporal and spatial coherence.

## Open Questions

- When will text-to-3D quality match text-to-image quality?
- Will NeRF-Gaussian Splatting hybrids eliminate the quality-speed tradeoff?
- How will 3D generation integrate with physics simulation and game engines?
- What is the path to real-time text-to-3D for interactive applications?

## Sources

- [[sources/nerf-vs-gaussian-splatting-2025]] -- NeRF vs Gaussian Splatting comparison

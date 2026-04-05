---
title: "Source: NeRF vs Gaussian Splatting (2025)"
type: source-summary
source: "[[raw/nerf-vs-gaussian-splatting-2025]]"
related: ["[[concepts/3d-generation]]", "[[concepts/neural-radiance-fields]]", "[[concepts/gaussian-splatting]]"]
tags: [3d-generation, nerf, gaussian-splatting, 3d-reconstruction]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Technical comparison of NeRF (implicit neural scene representation) vs Gaussian Splatting (explicit 3D Gaussian primitives): Gaussian Splatting is 10-50x faster with 90% less memory, achieving 60fps+ rendering, while NeRF retains quality advantages for ultra-high-resolution reconstruction."
---

## Key Points

- [[concepts/gaussian-splatting]] represents scenes with explicit 3D Gaussian primitives rendered via rasterization, achieving real-time 60fps+ rendering
- [[concepts/neural-radiance-fields]] uses implicit neural networks mapping coordinates to color/density, requiring seconds per frame but producing ultra-high 4K/8K quality
- Gaussian Splatting trains in 30 min to 2 hours vs. hours to days for NeRF, with 90% memory reduction
- Commercial adoption is underway: Zillow, Apartments.com, Esri ArcGIS, DJI Terra all ship Gaussian Splatting
- Tencent's Hunyuan3D-2 creates textured meshes with 500K+ vertices in under 10 seconds using hierarchical diffusion
- $4.5B market projected, growing at 35%+
- Future convergence expected: NeRF-GS hybrids, AI acceleration, real-time ray tracing integration

## Detailed Summary

Sparc3D's analysis documents the 2025 breakthrough moment for [[concepts/3d-generation]]. Gaussian Splatting has emerged as the practical choice for most applications, offering NeRF-quality results at dramatically faster speeds. The architectural difference is fundamental: NeRF encodes scenes as continuous neural functions requiring network evaluation per pixel, while Gaussian Splatting represents scenes as millions of anisotropic Gaussian distributions that can be directly rasterized by GPU hardware.

The commercial adoption section reveals that Gaussian Splatting has crossed from research into production. Real estate (Zillow SkyTours), GIS (Esri ArcGIS Pro), and drone mapping (DJI Terra) all now support the technology natively.

For text-to-3D generation, Tencent's Hunyuan3D-2 represents the state of the art, using hierarchical [[concepts/diffusion-models]] to generate textured 3D meshes from text or image inputs.

## Concepts Introduced or Discussed

- [[concepts/neural-radiance-fields]] -- implicit neural 3D representation
- [[concepts/gaussian-splatting]] -- explicit Gaussian 3D representation
- [[concepts/3d-generation]] -- text/image to 3D synthesis
- [[concepts/diffusion-models]] -- used for text-to-3D generation

## Metadata

- **Author**: Sparc3D
- **Date Published**: 2025-12-01
- **Format**: article
- **URL**: https://sparc3d.art/posts/nerf-gaussian-splatting-breakthrough-2025

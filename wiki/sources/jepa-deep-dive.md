---
title: "Source: Deep Dive into Yann LeCun's JEPA Architecture"
type: source-summary
source: "[[raw/jepa-deep-dive-bandaru]]"
related: ["[[concepts/jepa]]", "[[concepts/self-supervised-learning]]", "[[entities/yann-lecun]]", "[[concepts/world-models]]"]
tags: [JEPA, I-JEPA, V-JEPA, H-JEPA, energy-based-models, self-supervised-learning]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Comprehensive technical walkthrough of the JEPA family: energy-based formulation, four training criteria without contrastive loss, I-JEPA (images), V-JEPA (video), H-JEPA (hierarchical planning), and MC-JEPA (motion-content), with mathematical foundations."
---

## Key Points

- JEPA predicts in representation space, not pixel space — avoiding the intractability of predicting exact futures
- Four training criteria without contrastive loss: maximize input/output information, minimize prediction error, regularize latent capacity
- I-JEPA: masked image patches with EMA target encoder (like BYOL)
- V-JEPA: 64-frame spatiotemporal patches with dual short/long-range masks
- H-JEPA: two-tier for hierarchical planning — short-term detail + long-horizon abstraction
- MC-JEPA: combines optical flow (motion) + SSL (content) — possibly first H-JEPA realization
- V-JEPA 2 scaled from 630M to 1B params, 2M to 22M videos, with progressive-resolution training

## Detailed Summary

This source provides the most technically detailed account of the [[concepts/jepa]] family. The mathematical foundation is energy-based: E_w(x, y, z) with latent variables z enabling multiple plausible futures. The critical distinction from generative models is that JEPA never predicts raw outputs — only their representations. As LeCun notes, "predicting exactly what will happen is intractable" but understanding "what is possible and what is not" remains feasible.

The collapse problem — where encoders output constant values for trivially zero prediction error — is the central technical challenge. JEPA avoids contrastive methods (which need exponentially many negative samples) in favor of regularization approaches that constrain the volume of low-energy regions in representation space.

I-JEPA processes images as non-overlapping patches, using a context encoder to predict target patches' representations. V-JEPA extends this to video with spatiotemporal patches and temporal mask repetition to prevent shortcut learning. H-JEPA proposes hierarchical prediction at different abstraction levels for planning. The V-JEPA 2 line scales this up dramatically while adding action conditioning for [[concepts/embodied-ai]] applications.

## Metadata

- **Author**: Rohit Bandaru
- **Date Published**: 2025-06-01
- **Format**: technical blog
- **URL**: https://rohitbandaru.github.io/blog/JEPA-Deep-Dive/

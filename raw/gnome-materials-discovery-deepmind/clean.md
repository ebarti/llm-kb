---
title: "GNoME: Millions of New Materials Discovered with Deep Learning"
source: "https://deepmind.google/blog/millions-of-new-materials-discovered-with-deep-learning/"
author: "Google DeepMind"
date_published: 2023-11-29
date_ingested: 2026-04-05
tags: [gnome, materials-science, ai-science, deepmind, crystals]
type: article
status: raw
discovered_via: search
---

# GNoME: AI-Powered Materials Discovery

## Technology Overview

GNoME (Graph Networks for Materials Exploration) is a state-of-the-art graph neural network (GNN) model specifically suited for crystalline materials. It uses two discovery pipelines:
1. **Structural approach**: Creates candidates similar to known crystals.
2. **Compositional method**: Uses randomized chemical formulas.

## Active Learning Process

Iterative training cycles where GNoME generated predictions tested via Density Functional Theory (DFT), then fed results back into model training. This elevated discovery rates from approximately 50% to 80% on external MatBench Discovery benchmarks, and computational efficiency from under 10% to over 80%.

## Discovery Scale

- 2.2 million new crystal predictions (equivalent to nearly 800 years of knowledge).
- 380,000 identified as most stable candidates suitable for experimental synthesis.
- 421,000 total stable materials when combined with previous computational discoveries.
- 52,000 layered compounds similar to graphene (previously only ~1,000 known).
- 528 potential lithium-ion conductors (25x increase from previous studies).
- 736 independent external validations by research teams worldwide.

## A-Lab Integration

Berkeley Lab's autonomous robotic facility (A-Lab) successfully synthesized more than 41 new materials using GNoME's predictions alongside the Materials Project database, validating AI-guided manufacturing processes.

## Applications

- Next-generation superconductors
- Advanced battery technologies (lithium-ion conductors)
- Solar panel efficiency improvements
- Computing power optimization
- Energy-GNoME database: 38,500+ materials for energy applications from GNoME's predictions.

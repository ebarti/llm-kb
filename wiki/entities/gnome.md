---
title: "GNoME"
type: entity
entity_type: tool
url: "https://github.com/google-deepmind/materials_discovery"
related: ["[[concepts/ai-materials-science]]", "[[concepts/ai-for-scientific-discovery]]", "[[concepts/self-driving-labs]]", "[[entities/google-deepmind]]"]
tags: [gnome, materials-science, graph-neural-networks, crystals]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Graph Networks for Materials Exploration — DeepMind's GNN-based system that discovered 2.2M new crystal structures (800 years equivalent). 380K stable candidates, 52K graphene-like compounds, 528 lithium-ion conductors. Published in Nature (2023)."
---

## Overview

GNoME (Graph Networks for Materials Exploration) is [[entities/google-deepmind]]'s deep learning system for materials discovery. Using graph neural networks and active learning, it predicted 2.2 million new crystal structures — equivalent to approximately 800 years of conventional research.

## Key Facts

- **Type**: AI system / materials discovery tool
- **Creator**: Google DeepMind
- **URL**: https://github.com/google-deepmind/materials_discovery
- **Notable for**: Discovering 2.2M crystal structures, 10x expansion of known stable materials
- **Published**: Nature, November 2023

## Technical Details

- **Architecture**: Graph neural network (GNN) — atoms as nodes, bonds as edges.
- **Pipelines**: Structural (variations on known crystals) + Compositional (randomized formulas).
- **Active learning**: Iterative DFT validation feeding back into training.
- **Accuracy**: 50% to 80% stability prediction on MatBench Discovery benchmarks.

## Key Discoveries

| Category | Count |
|----------|-------|
| Total crystal predictions | 2.2 million |
| Most stable candidates | 380,000 |
| Graphene-like layered compounds | 52,000 (prev. ~1,000 known) |
| Lithium-ion conductors | 528 (25x previous) |
| Energy materials (Energy-GNoME) | 38,500+ |
| Externally validated | 736 |

## Real-World Integration

Predictions validated by Berkeley Lab's A-Lab robotic facility (41+ materials synthesized autonomously), establishing the AI-to-lab pipeline for [[concepts/ai-materials-science]].

## Mentioned In

- [[sources/gnome-materials-discovery]] — detailed technical overview
- [[sources/self-driving-labs-revolution]] — A-Lab integration

## External References

- [Nature paper](https://www.nature.com/articles/s41586-023-06735-9)
- [GitHub repository](https://github.com/google-deepmind/materials_discovery)
- [DeepMind blog post](https://deepmind.google/blog/millions-of-new-materials-discovered-with-deep-learning/)

---
title: "Source: GNoME — Millions of New Materials Discovered with Deep Learning"
type: source-summary
source: "[[raw/gnome-materials-discovery-deepmind]]"
related: ["[[concepts/ai-materials-science]]", "[[concepts/ai-for-scientific-discovery]]", "[[entities/gnome]]", "[[entities/google-deepmind]]", "[[concepts/self-driving-labs]]"]
tags: [gnome, materials-science, ai-science, crystals]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "DeepMind's GNoME discovered 2.2M new crystal structures using graph neural networks and active learning — equivalent to 800 years of research. 380K stable materials identified; 528 lithium-ion conductors (25x previous); 52K graphene-like compounds. Berkeley A-Lab autonomously synthesized 41+ materials."
---

## Key Points

- GNoME (Graph Networks for Materials Exploration) is a GNN model using two pipelines: structural (similar to known crystals) and compositional (randomized chemical formulas).
- Active learning elevated discovery rates from ~50% to 80% on MatBench Discovery benchmarks.
- 2.2M new crystal predictions; 380K most stable; 52K graphene-like layered compounds; 528 lithium-ion conductors.
- Berkeley Lab's [[concepts/self-driving-labs|A-Lab]] autonomously synthesized 41+ new materials from GNoME predictions.
- Energy-GNoME database: 38,500+ materials for energy applications.

## Detailed Summary

[[entities/gnome]] represents a paradigm shift in [[concepts/ai-materials-science]]. The graph neural network architecture is naturally suited to crystalline materials because input data resembles connections between atoms. Two complementary pipelines — structural (creating candidates similar to known crystals) and compositional (using randomized formulas) — generate candidates validated through Density Functional Theory (DFT).

The active learning loop feeds DFT results back into training, dramatically improving both accuracy and efficiency. The 2.2 million predicted crystals represent roughly 800 years of conventional research effort.

The most significant real-world validation came through integration with Berkeley Lab's A-Lab, an autonomous robotic facility that physically synthesized 41+ new materials with minimal human input, establishing a critical AI-to-lab pipeline that demonstrates the complete loop from [[concepts/ai-for-scientific-discovery|AI prediction to experimental validation]].

## Concepts Introduced or Discussed

- [[concepts/ai-materials-science]] — core topic
- [[concepts/self-driving-labs]] — A-Lab integration
- [[concepts/ai-for-scientific-discovery]] — GNoME as exemplar

## Metadata

- **Author**: Google DeepMind
- **Date Published**: November 2023
- **Format**: article
- **URL**: https://deepmind.google/blog/millions-of-new-materials-discovered-with-deep-learning/

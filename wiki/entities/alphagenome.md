---
title: "AlphaGenome"
type: entity
entity_type: tool
url: "https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/"
related: ["[[concepts/ai-genomics]]", "[[concepts/ai-for-scientific-discovery]]", "[[entities/alphafold]]", "[[entities/google-deepmind]]"]
tags: [alphagenome, genomics, genetic-variants, gene-regulation]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "DeepMind's AI tool for genomic analysis. Processes up to 1M base-pair DNA sequences, predicting thousands of molecular properties for non-coding regions (98% of genome). Outperforms best models on 22/24 evaluations. Published in Nature (2025)."
---

## Overview

AlphaGenome is [[entities/google-deepmind]]'s AI model for understanding the non-coding genome — the 98% of DNA that regulates gene activity. It predicts how genetic variants impact biological processes across different cell types and tissues.

## Key Facts

- **Type**: AI system / genomics tool
- **Creator**: Google DeepMind
- **Published**: Nature, 2025
- **Notable for**: Only model jointly predicting all genomic regulatory modalities

## Technical Specifications

- **Input**: DNA sequences up to 1,000,000 base-pairs.
- **Architecture**: Convolutional layers + Transformers + modality-specific outputs.
- **Predictions**: Gene locations, RNA splicing, production amounts, accessibility, protein binding, variant effects.
- **Training**: Distributed across TPUs.

## Performance

- 22/24 superior on single-sequence evaluations.
- 24/26 matched or exceeded top models on variant effect prediction.
- Only model to jointly predict all assessed modalities.

## Ecosystem Position

| Tool | Genome Coverage | Focus |
|------|----------------|-------|
| AlphaGenome | Non-coding (98%) | Gene regulation |
| AlphaMissense | Coding (2%) | Mutation pathogenicity |
| [[entities/alphafold]] | Protein structures | 3D structure prediction |
| AlphaProteo | Protein design | De novo binder creation |

## Mentioned In

- [[sources/alphagenome-genomics]] — architecture, performance, applications

## External References

- [DeepMind blog](https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/)

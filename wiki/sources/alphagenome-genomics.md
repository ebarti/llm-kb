---
title: "Source: AlphaGenome — AI for Understanding the Genome"
type: source-summary
source: "[[raw/alphagenome-genomics-deepmind]]"
related: ["[[concepts/ai-genomics]]", "[[concepts/ai-for-scientific-discovery]]", "[[entities/alphagenome]]", "[[entities/google-deepmind]]"]
tags: [alphagenome, genomics, ai-biology, genetic-variants]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "DeepMind's AlphaGenome processes up to 1M base-pair DNA sequences to predict thousands of molecular properties — outperforming best external models on 22/24 evaluations. Focuses on the 98% non-coding genome that regulates gene activity, complementing AlphaMissense's protein-coding focus."
---

## Key Points

- Processes DNA sequences up to 1 million base-pairs, predicting thousands of molecular properties.
- Outperformed best external models on 22 of 24 single-sequence evaluations.
- Matched or exceeded top models on 24 of 26 variant effect prediction evaluations.
- Only model that jointly predicts all assessed modalities (gene locations, splicing, RNA production, accessibility, binding).
- Focuses on non-coding regions (98% of genome) complementing AlphaMissense (protein-coding 2%).

## Detailed Summary

[[entities/alphagenome]] addresses a critical gap in [[concepts/ai-genomics]]: while most AI tools focus on the 2% of the genome that codes for proteins, 98% of DNA consists of regulatory regions that control gene activity. AlphaGenome's architecture combines convolutional layers (short-range patterns), transformers (long-range communication), and modality-specific output layers.

The model's practical value lies in disease variant interpretation. In a cancer mutation study, it correctly predicted that mutations in T-cell acute lymphoblastic leukemia would activate the TAL1 gene by introducing a MYB DNA binding motif. It is also the first model to explicitly predict splice-junction locations from sequence, relevant to diseases like spinal muscular atrophy and cystic fibrosis.

AlphaGenome builds on the earlier Enformer model, processing longer sequences at higher resolution with less training time. Together with [[entities/alphafold]], AlphaMissense, and AlphaProteo, it forms [[entities/google-deepmind]]'s expanding toolkit for [[concepts/ai-for-scientific-discovery|AI-driven biology]].

## Concepts Introduced or Discussed

- [[concepts/ai-genomics]] — core topic
- [[concepts/ai-for-scientific-discovery]] — DeepMind biology ecosystem

## Metadata

- **Author**: Google DeepMind
- **Date Published**: June 2025
- **Format**: article
- **URL**: https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/

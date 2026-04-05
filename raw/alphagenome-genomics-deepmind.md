---
title: "AlphaGenome: AI for Better Understanding the Genome"
source: "https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/"
author: "Google DeepMind"
date_published: 2025-06-15
date_ingested: 2026-04-05
tags: [alphagenome, genomics, ai-biology, deepmind, genetic-variants]
type: article
status: raw
discovered_via: search
---

# AlphaGenome: AI for Genome Understanding

## What It Does

AlphaGenome predicts how genetic mutations affect biological processes regulating genes. It analyzes DNA sequences and determines the impact of variants on gene regulation across different tissues and cell types.

## How It Works

Accepts DNA sequences up to 1 million base-pairs as input. Architecture combines:
- Convolutional layers for short pattern detection.
- Transformers for information communication across sequence positions.
- Final layers converting patterns into predictions across different modalities.

Training distributed across multiple interconnected Tensor Processing Units (TPUs).

## Outputs

Predictions include:
- Gene start and end locations across cell types.
- RNA splicing patterns.
- RNA production amounts.
- DNA base accessibility.
- Protein-DNA binding sites.
- Genetic variant effects on all these properties.

## Accuracy Performance

- Outperformed the best external models on 22 out of 24 evaluations for single DNA sequences.
- Matched or exceeded top-performing external models on 24 out of 26 evaluations for variant effect prediction.
- Only model that could jointly predict all assessed modalities.

## Disease Understanding Applications

- Cancer mutation study: predicted T-cell acute lymphoblastic leukemia mutations would activate nearby gene TAL1 by introducing a MYB DNA binding motif, confirming known disease mechanisms.
- First model to explicitly model splice-junction locations and expression levels directly from sequence, relevant to spinal muscular atrophy and cystic fibrosis.

## Relationship to Other DeepMind Tools

- Complementary to **AlphaMissense**: AlphaMissense analyzes protein-coding regions (2% of genome); AlphaGenome focuses on non-coding regions (98%).
- Builds on **Enformer**: Processes longer sequences at higher resolution with less training time.

## Availability

Accessible via API for non-commercial research use. Published in Nature.

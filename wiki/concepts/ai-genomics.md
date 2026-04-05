---
title: "AI for Genomics"
type: concept
sources: ["[[sources/alphagenome-genomics]]", "[[sources/ucsd-nine-ai-breakthroughs]]"]
related: ["[[concepts/ai-for-scientific-discovery]]", "[[concepts/ai-protein-structure-prediction]]", "[[entities/alphagenome]]"]
tags: [genomics, ai-biology, genetic-variants, gene-regulation]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "AI tools for genomics analyze DNA sequences to predict gene regulation, variant effects, and disease mechanisms. AlphaGenome processes 1M base-pairs predicting thousands of molecular properties; Evo2 is the largest biology model (128K+ genomes). AI now designs genomes, not just reads them."
---

## Overview

AI for genomics applies deep learning to understand, interpret, and increasingly design genetic sequences. The field has evolved from simple sequence alignment to models that predict complex regulatory interactions, variant effects, and even generate novel genetic sequences.

## Major AI Genomics Tools

### AlphaGenome (Google DeepMind, 2025)
- Processes up to 1 million base-pair DNA sequences.
- Predicts thousands of molecular properties: gene locations, RNA splicing, production levels, accessibility, protein binding.
- Focuses on non-coding regions (98% of genome) — the regulatory "dark matter" that controls gene activity.
- Outperformed best external models on 22/24 single-sequence evaluations.
- Complements AlphaMissense (protein-coding 2%) to cover the full genome.

### Evo2 (Arc Institute + NVIDIA, 2025)
- Largest AI biology model: trained on 128,000+ whole genomes.
- Generates novel DNA sequences with biological function.
- Represents the shift from genomic analysis to genomic design.

### AlphaMissense (Google DeepMind)
- Assesses pathogenicity of genetic variants in protein-coding regions.
- Classified 89% of all possible missense variants.
- Structural context from [[entities/alphafold]] informs predictions.

## Key Applications

- **Disease variant interpretation**: Identifying which genetic variants cause disease vs benign variation. AlphaGenome predicted cancer mutation mechanisms in T-cell acute lymphoblastic leukemia.
- **Splicing disorders**: First model to predict splice-junction locations from sequence — relevant to spinal muscular atrophy, cystic fibrosis.
- **CRISPR optimization**: AI predicts off-target effects and optimizes guide RNA design.
- **Pharmacogenomics**: Predicting drug response from genetic variation.
- **Synthetic biology**: Evo2 and similar models design novel genomes with desired properties.

## The Genome-to-Clinic Pipeline

1. **Sequence** the patient genome (now ~$200 per whole genome).
2. **Predict** variant effects using AlphaMissense + AlphaGenome.
3. **Interpret** regulatory impact on gene expression.
4. **Design** targeted therapies using [[concepts/ai-protein-design]] and [[concepts/ai-drug-discovery]].

## Open Questions

- Can AI capture distant regulatory elements beyond 100K base-pairs?
- Will AI-designed genomes raise new biosafety and ethical concerns?
- How reliable are AI variant predictions for clinical decision-making?
- Can models account for environmental and developmental factors in gene expression?

## Sources

- [[sources/alphagenome-genomics]] — AlphaGenome architecture, performance, and applications
- [[sources/ucsd-nine-ai-breakthroughs]] — Alzheimer's gene discovery via AI structural modeling

## Related Concepts

- [[concepts/ai-for-scientific-discovery]] — broader context
- [[concepts/ai-protein-structure-prediction]] — structural context for variants
- [[concepts/ai-drug-discovery]] — pharmacogenomics applications

---
title: "Nemotron-CC: Transforming Common Crawl into a Refined Long-Horizon Pretraining Dataset"
source: "https://arxiv.org/abs/2412.02595"
author: "NVIDIA ADLR"
date_published: 2024-12-03
date_ingested: 2026-04-05
tags: [training-data, dataset-curation, common-crawl, synthetic-data, classifier-ensembling, nvidia]
type: paper
status: raw
discovered_via: search
---

# Nemotron-CC

## Motivation

Previous datasets (DCLM, FineWeb-Edu) achieved strong benchmarks through aggressive model-based filtering but discarded ~90% of data. Both contain ~80% near-duplicates. This creates a bottleneck for training larger models over extended token horizons (e.g., 15T tokens).

## Dataset Scale

6.3 trillion tokens total: 4.4T globally deduplicated original tokens + 1.9T synthetically generated tokens. Four times more unique real tokens than DCLM.

## Pipeline Architecture

### 1. HTML Extraction & Filtering Optimization
Justext vs Trafilatura: Justext yielded 28.6% more high-quality tokens. Strategically disables heuristic filters for high-quality segments while retaining them for lower-quality portions.

### 2. Classifier Ensembling
Combines three classifiers trained on different quality concepts:
- FineWeb-Edu classifier (educational value)
- DCLM classifier (informativeness)
- Custom models with different annotation standards

Ensemble increases recall of quality documents from ~9-11% to 25%.

### 3. Synthetic Data Generation
Differentiated strategies by quality tier:
- Low-quality docs: Wikipedia-style rephrasing
- High-quality docs: Four specialized approaches — diverse Q&A pairs, distillation, knowledge extraction, organized knowledge lists

1.8T synthetic tokens generated using Mistral NeMo 12B with FP8 inference.

## Performance

Short Horizon (1T tokens): Nemotron-CC-HQ achieves +5.6 MMLU over DCLM on 8B models.

Long Horizon (15T tokens): 8B model reaches MMLU 70.3 vs Llama 3.1's 65.3.

## Key Insight: Learned Flywheel

Shift from static heuristic-based pipelines toward "learned flywheels" where improved data enables better models, which in turn improve data quality through enhanced synthesis and classification. Maximizing unique token diversity, rather than aggressive pruning, better serves long-horizon training.

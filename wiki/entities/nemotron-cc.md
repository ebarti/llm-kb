---
title: "Nemotron-CC"
type: entity
entity_type: dataset
sources: ["[[sources/nemotron-cc-nvidia]]"]
related: ["[[concepts/training-data-curation]]", "[[concepts/synthetic-data-in-pretraining]]", "[[entities/common-crawl]]", "[[entities/dclm]]", "[[entities/nvidia]]"]
last_compiled: 2026-04-05
summary: "NVIDIA's 6.3T-token dataset (4.4T real + 1.9T synthetic) using classifier ensembling and differentiated synthetic generation — 4x more unique tokens than DCLM while exceeding Llama 3.1 8B on MMLU."
---

## Overview

Nemotron-CC is NVIDIA ADLR's Common Crawl-derived pretraining dataset designed for long-horizon training (15T+ tokens). It addresses the limitation of prior datasets (DCLM, FineWeb-Edu) that achieved quality through aggressive filtering but discarded ~90% of available data.

## Key Innovations

- **Classifier ensembling**: combines FineWeb-Edu, DCLM, and custom classifiers to increase quality recall from 9-11% to 25%
- **Differentiated synthetic generation**: Wikipedia-style rephrasing for low-quality docs; Q&A, distillation, knowledge extraction for high-quality docs
- **Learned flywheel concept**: better data → better models → better data curation → better data

## Scale

- 6.3T total tokens: 4.4T globally deduplicated original + 1.9T synthetic
- 1.8T synthetic tokens generated using Mistral NeMo 12B (FP8 inference)
- 4x more unique real tokens than DCLM

## Performance

| Metric | Nemotron-CC 8B (15T) | Llama 3.1 8B |
|--------|---------------------|--------------|
| MMLU | 70.3 | 65.3 |
| Short horizon (1T): MMLU advantage over DCLM | +5.6 | N/A |

## Variants

- Nemotron-CC-v2, v2.1 (HuggingFace)
- Nemotron-CC-Code-v1 (code-focused)
- Nemotron-CC-Math-v1 (133B math tokens, LaTeX-standardized)

## Mentioned In

- [[sources/nemotron-cc-nvidia]] — primary source

---
title: "Source: Nemotron-CC — Transforming Common Crawl into a Refined Long-Horizon Dataset"
type: source-summary
source: "[[raw/nemotron-cc-nvidia]]"
related: ["[[concepts/training-data-curation]]", "[[concepts/synthetic-data-in-pretraining]]", "[[concepts/model-based-filtering]]", "[[entities/nemotron-cc]]", "[[entities/nvidia]]", "[[entities/common-crawl]]"]
last_compiled: 2026-04-05
summary: "NVIDIA's 6.3T-token dataset using classifier ensembling and synthetic rephrasing to achieve 4x more unique tokens than DCLM while exceeding Llama 3.1 8B on MMLU by 5 points."
---

## Key Points

- 6.3T tokens: 4.4T deduplicated original + 1.9T synthetically generated
- Addresses the "90% discard" problem of aggressive filtering (DCLM, FineWeb-Edu)
- Classifier ensembling combines FineWeb-Edu, DCLM, and custom classifiers — increases quality recall from 9-11% to 25%
- Differentiated synthetic generation: Wikipedia-style rephrasing for low-quality docs; Q&A, distillation, knowledge extraction for high-quality docs
- 1.8T synthetic tokens via Mistral NeMo 12B with FP8 inference
- Short horizon: +5.6 MMLU over DCLM on 8B models
- Long horizon (15T tokens): MMLU 70.3 vs Llama 3.1's 65.3

## Detailed Summary

Nemotron-CC identifies a critical limitation in prior work: [[entities/dclm]] and [[entities/fineweb]] achieved benchmark gains through aggressive filtering that discards ~90% of available Common Crawl data. This works for short training runs but creates a data bottleneck for long-horizon training (15T+ tokens), where unique token diversity matters more than per-token quality.

The key innovations are classifier ensembling (combining multiple quality classifiers trained on different annotation standards to capture diverse notions of "quality") and differentiated synthetic generation (applying different synthesis strategies depending on the quality tier of the source document).

The paper introduces the "learned flywheel" concept: improved data enables better models, which improve data quality through better synthesis and classification, creating a virtuous cycle. This contrasts with static, heuristic-driven pipelines.

## Notable Quotes

> "Maximizing unique token diversity, rather than aggressive pruning, better serves long-horizon training scenarios."

## Related Concepts

- [[concepts/training-data-curation]] — classifier ensembling as an advance over single-classifier filtering
- [[concepts/synthetic-data-in-pretraining]] — differentiated synthesis strategies by quality tier
- [[concepts/data-deduplication]] — 80% near-duplicates in DCLM and FineWeb-Edu
- [[concepts/scaling-laws]] — long-horizon training requires different curation strategy

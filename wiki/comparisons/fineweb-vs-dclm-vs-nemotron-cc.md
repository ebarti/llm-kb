---
title: "FineWeb vs DCLM vs Nemotron-CC"
type: comparison
subjects: ["[[entities/fineweb]]", "[[entities/dclm]]", "[[entities/nemotron-cc]]"]
sources: ["[[sources/fineweb-dataset-huggingface]]", "[[sources/dclm-datacomp-language-models]]", "[[sources/nemotron-cc-nvidia]]"]
last_compiled: 2026-04-05
summary: "The three leading open LLM pretraining datasets compared: FineWeb prioritizes scale (15T tokens), DCLM prioritizes rigorous filtering (2T tokens, 64% MMLU), and Nemotron-CC combines both with synthetic augmentation (6.3T tokens, 70.3% MMLU)."
---

## Overview

FineWeb, DCLM, and Nemotron-CC represent the current state of the art in open LLM pretraining datasets, all derived from [[entities/common-crawl]] but with fundamentally different curation philosophies. Understanding their differences is essential for choosing the right data strategy.

## Comparison Table

| Dimension | FineWeb | DCLM-Baseline | Nemotron-CC |
|-----------|---------|---------------|-------------|
| **Creator** | HuggingFace | Apple/UW et al. | NVIDIA ADLR |
| **Total tokens** | ~15T | ~2T | 6.3T (4.4T real + 1.9T synthetic) |
| **Source** | 96 CC dumps | 240T-token CC pool | CC + synthetic generation |
| **Primary filtering** | Heuristic + per-dump dedup | fastText classifier (top 10%) | Classifier ensemble (3 classifiers) |
| **Dedup strategy** | Per-dump MinHash | Bloom filter | Global dedup |
| **Synthetic component** | None | None | 1.9T tokens (Mistral NeMo 12B) |
| **MMLU (7-8B model)** | Competitive baseline | 64% (2.6T tokens) | 70.3% (15T tokens) |
| **Multilingual** | FineWeb-2 (1,000+ langs) | English only | English only |
| **Key innovation** | Per-dump dedup discovery | Model-based filtering benchmark | Classifier ensembling + synthetic augmentation |
| **Data retention rate** | Moderate | ~10% (aggressive) | ~25% (balanced) |
| **Best for** | General pretraining, multilingual | Short training runs, benchmarking | Long-horizon training (15T+) |

## Philosophy Differences

### FineWeb: Scale and Openness
FineWeb prioritizes making the largest possible clean dataset publicly available. Its curation is less aggressive than DCLM's, retaining more data at the cost of some per-token quality. The key insight — per-dump deduplication over cross-dump — prioritizes data diversity. FineWeb-2's multilingual extension makes it unique among the three.

### DCLM: Rigorous Filtering
DCLM prioritizes benchmark rigor: by holding everything constant except the dataset, it enables controlled A/B testing of curation strategies. Its aggressive top-10% filtering produces the highest per-token quality but limits total unique tokens to ~2T. Best for researchers who need clean experimental methodology.

### Nemotron-CC: Balanced Long-Horizon
Nemotron-CC addresses the data bottleneck created by aggressive filtering. By ensembling classifiers and augmenting with synthetic data, it achieves 4x more unique tokens than DCLM while maintaining or exceeding quality. The "learned flywheel" philosophy points toward iterative, self-improving pipelines.

## When to Use Each

| Use Case | Recommended |
|----------|-------------|
| Short pretraining run (<3T tokens) | DCLM-Baseline |
| Long pretraining (>10T tokens) | Nemotron-CC |
| Multilingual model | FineWeb (+ FineWeb-2) |
| Curation research / ablations | DCLM (benchmark framework) |
| Educational/knowledge-intensive tasks | FineWeb-Edu or Nemotron-CC-HQ |
| Code or math specialization | Nemotron-CC-Code or Nemotron-CC-Math |

## Key Takeaway

These datasets are not simply "better or worse" — they optimize for different tradeoffs. DCLM's aggressive filtering is ideal for compute-constrained short runs. Nemotron-CC's balanced approach serves long-horizon frontier training. FineWeb's breadth and multilingual coverage serve the open-source community's diverse needs.

## Sources

- [[sources/fineweb-dataset-huggingface]] — FineWeb methodology and results
- [[sources/dclm-datacomp-language-models]] — DCLM benchmark and filtering analysis
- [[sources/nemotron-cc-nvidia]] — Nemotron-CC pipeline and performance

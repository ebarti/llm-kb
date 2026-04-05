---
title: "Training Data Curation"
type: concept
sources: ["[[sources/dclm-datacomp-language-models]]", "[[sources/fineweb-dataset-huggingface]]", "[[sources/nemotron-cc-nvidia]]", "[[sources/scaling-laws-data-quality]]", "[[sources/nebius-llm-data-preparation]]", "[[sources/synthetic-data-llm-pretraining-study]]"]
related: ["[[concepts/model-based-filtering]]", "[[concepts/data-deduplication]]", "[[concepts/scaling-laws]]", "[[concepts/data-quality-bottleneck]]", "[[concepts/benchmark-contamination]]", "[[concepts/synthetic-data-in-pretraining]]", "[[concepts/copyright-and-training-data]]"]
last_compiled: 2026-04-05
summary: "The process of transforming raw web crawls into high-quality LLM training datasets through text extraction, heuristic filtering, model-based quality scoring, deduplication, and data mixing — the single highest-leverage activity in LLM development."
---

## Overview

Training data curation is the process of transforming raw data sources (primarily web crawls from [[entities/common-crawl]]) into clean, high-quality datasets suitable for LLM pretraining. Research consistently shows this is the highest-leverage activity in LLM development: a well-curated dataset enables a 7B model to match or exceed models trained on 10x more compute with less careful data ([[sources/dclm-datacomp-language-models]]).

The field has evolved from simple heuristic filtering toward sophisticated model-based approaches, with three major open datasets — [[entities/fineweb]], [[entities/dclm]], and [[entities/nemotron-cc]] — representing the current state of the art.

## The Curation Pipeline

A typical training data curation pipeline involves five sequential stages:

### 1. Text Extraction

Raw HTML from web crawls must be converted to clean text. The choice of extraction tool matters significantly — [[sources/dclm-datacomp-language-models]] found that re-extracting Common Crawl with resiliparse instead of using pre-extracted WET files improved downstream performance by 2.5+ points. [[sources/nemotron-cc-nvidia]] found Justext yielded 28.6% more high-quality tokens than Trafilatura.

### 2. Heuristic Filtering

Rule-based filters remove obvious low-quality content: documents that are too short/long, contain excessive special characters, lack proper punctuation, or match known noise patterns (lorem ipsum, JavaScript notices, cookie banners). These filters are necessary but insufficient — they capture only the most obviously bad content.

### 3. Model-Based Quality Filtering

The most impactful step. [[sources/dclm-datacomp-language-models]] tested seven strategies and found fastText classifiers trained on instruction-formatted data decisively outperformed alternatives (30.2 vs 26.1 Core accuracy for PageRank). Key insight: training the classifier on examples of "what good looks like" from instruction data (OpenHermes, ELI5) outperforms using Wikipedia or OpenWebText as positive examples.

[[sources/nemotron-cc-nvidia]] advances this with classifier ensembling — combining multiple quality classifiers trained on different standards to increase recall from 9-11% to 25%. See [[concepts/model-based-filtering]] for full treatment.

### 4. Deduplication

Removing duplicate and near-duplicate content prevents wasted compute, overfitting, and memorization. Methods range from exact matching (fast but incomplete) through [[entities/minhash-lsh]] (practical at scale) to semantic deduplication (accurate but expensive). See [[concepts/data-deduplication]] for details.

A counterintuitive finding from [[sources/fineweb-dataset-huggingface]]: per-dump deduplication outperforms cross-dump deduplication, because temporal repetition of high-quality content can be beneficial.

### 5. Data Mixing and Synthetic Augmentation

The final stage involves combining filtered web data with other sources and potentially synthetic data. [[sources/dclm-datacomp-language-models]] found that mixing curated sources (Wikipedia, arXiv) into an already well-filtered dataset degraded performance. [[sources/synthetic-data-llm-pretraining-study]] found the optimal mixture is ~30% rephrased synthetic + 70% natural web text.

## The Quality Cascade

Data quality operates as a cascade: errors at each stage compound downstream. [[sources/scaling-laws-data-quality]] formalizes this with a quality-aware scaling law showing that quality (Q) modulates effective dataset size. When Q is high, compute is best spent on model scaling; when Q is low, no amount of scaling compensates.

This echoes the [[concepts/data-quality-bottleneck]] concept from the knowledge base domain, but at the much larger scale of LLM pretraining.

## Key Findings Across Sources

| Finding | Source |
|---------|--------|
| Model-based filtering is the single most impactful technique | [[sources/dclm-datacomp-language-models]] |
| Quality rankings transfer across model scales (r=0.885-0.919) | [[sources/dclm-datacomp-language-models]] |
| Per-dump dedup outperforms cross-dump dedup | [[sources/fineweb-dataset-huggingface]] |
| Classifier ensembling increases quality recall from 9% to 25% | [[sources/nemotron-cc-nvidia]] |
| 30% synthetic + 70% natural is the optimal data mixture | [[sources/synthetic-data-llm-pretraining-study]] |
| Quality-aware scaling: L(N,D,Q) with gamma 0.17-0.40 | [[sources/scaling-laws-data-quality]] |
| Human quality judgments have limited predictive value | [[sources/dclm-datacomp-language-models]] |

## Open Challenges

1. **Data exhaustion**: high-quality web data may be approaching limits for frontier model training
2. **Synthetic pollution**: AI-generated content on the web degrades future crawl quality
3. **Copyright constraints**: legal uncertainty around using copyrighted works (see [[concepts/copyright-and-training-data]])
4. **Multilingual equity**: most curation research focuses on English (see [[concepts/multilingual-training-data]])
5. **Evaluation reliability**: [[concepts/benchmark-contamination]] makes it hard to trust results

## Sources

- [[sources/dclm-datacomp-language-models]] — the definitive benchmark for curation strategy comparison
- [[sources/fineweb-dataset-huggingface]] — largest open dataset, key deduplication insights
- [[sources/nemotron-cc-nvidia]] — classifier ensembling and synthetic augmentation
- [[sources/scaling-laws-data-quality]] — quality-aware scaling law framework
- [[sources/nebius-llm-data-preparation]] — practical pipeline overview
- [[sources/synthetic-data-llm-pretraining-study]] — optimal synthetic/natural data mixture

## Related Concepts

- [[concepts/model-based-filtering]] — the most impactful curation technique
- [[concepts/data-deduplication]] — removing redundant content at scale
- [[concepts/scaling-laws]] — how data quality interacts with model and compute scaling
- [[concepts/synthetic-data-in-pretraining]] — augmenting curated data with synthetic content
- [[concepts/benchmark-contamination]] — evaluating whether curation gains are genuine
- [[concepts/copyright-and-training-data]] — legal constraints on data sourcing
- [[concepts/data-quality-bottleneck]] — the broader principle that quality dominates scale

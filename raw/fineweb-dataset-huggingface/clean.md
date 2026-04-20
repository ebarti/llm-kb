---
title: "FineWeb: Decanting the Web for the Finest Text Data at Scale"
source: "https://huggingface.co/datasets/HuggingFaceFW/fineweb"
author: "HuggingFace FineData Team"
date_published: 2024-04-01
date_ingested: 2026-04-05
tags: [training-data, dataset-curation, common-crawl, deduplication, web-data, open-source]
type: paper
status: raw
discovered_via: search
---

# FineWeb Dataset

## Overview

FineWeb is the largest publicly available clean LLM pretraining dataset at ~15 trillion tokens (GPT-2 tokenizer). Built by processing 96 CommonCrawl dumps from summer 2013 to April 2024. Outperforms C4, RefinedWeb, Dolma, The Pile, SlimPajama, and RedPajama across multiple evaluations.

## Key Discovery: Deduplication Nuance

Aggressive deduplication doesn't necessarily improve quality. When MinHash deduplication was applied across 90+ CommonCrawl dumps in chronological order, one dump experienced a 94% reduction in tokens (490B to 31B), yet models trained on the removed data actually performed better than those on retained data.

Solution: individual dump deduplication — processing each dataset separately rather than comparing across dumps — preserved more unique data while maintaining quality.

## Filtering Strategy

Multi-level heuristic filtering combined with statistical analysis:
- Benchmarked against high-quality datasets
- Custom filters for domain-specific noise (lorem ipsum, JavaScript notices)
- Iterative validation rather than one-shot filtering

## FineWeb-Edu Variant

1.3T tokens filtered for educational content. Uses classifier-based filtering to identify web pages with high educational value. FineWeb-Edu v1.4.0 (2025-07-11) covers through June 2025.

## FineWeb-2 (Multilingual)

Second iteration bringing high quality pretraining data to over 1,000 languages.

## Evaluation Approach

Early-signal benchmarking on smaller models as cost-efficient proxies:
- CommonSense QA, HellaSwag, PIQA, MMLU, WinoGrande

## Versions

- v1.2.0 (2025-03-01): 8 new snapshots (May-December 2024)
- v1.3.0 (2025-01-31): Fixed processing issues, ~400B additional tokens
- v1.4.0 (2025-07-11): 6 new snapshots (January-June 2025)

## Central Lesson

Dataset curation demands meticulous approach to data collection, filtering, and deduplication combined with rigorous iterative validation rather than executing predetermined strategies at scale.

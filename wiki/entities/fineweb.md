---
title: "FineWeb"
type: entity
entity_type: dataset
sources: ["[[sources/fineweb-dataset-huggingface]]", "[[sources/nemotron-cc-nvidia]]"]
related: ["[[concepts/training-data-curation]]", "[[concepts/data-deduplication]]", "[[entities/common-crawl]]", "[[entities/huggingface]]", "[[entities/dclm]]", "[[concepts/pretraining-data-pipeline]]", "[[concepts/llm-pretraining]]"]
last_compiled: 2026-04-05
summary: "HuggingFace's 15T-token open LLM pretraining dataset from 96 CommonCrawl dumps — the largest publicly available clean dataset, with FineWeb-Edu (1.3T educational tokens) and FineWeb-2 (1,000+ languages) variants."
---

## Overview

FineWeb is the largest publicly available clean LLM pretraining dataset, containing approximately 15 trillion tokens (GPT-2 tokenizer). Created by the HuggingFace FineData team by processing 96 CommonCrawl dumps from summer 2013 to April 2024.

## Key Achievements

- Outperforms C4, RefinedWeb, Dolma, The Pile, SlimPajama, and RedPajama across multiple evaluation tasks
- Discovered that per-dump deduplication outperforms cross-dump deduplication
- Iteratively refined filtering pipeline rather than one-shot processing

## Variants

- **FineWeb** (15T tokens): full English web dataset
- **FineWeb-Edu** (1.3T tokens): educational content filtered by classifier — particularly strong on knowledge-intensive benchmarks
- **FineWeb-2**: multilingual extension covering 1,000+ languages

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.2.0 | 2025-03-01 | 8 new snapshots (May-Dec 2024) |
| v1.3.0 | 2025-01-31 | Processing fix, ~400B additional tokens |
| v1.4.0 | 2025-07-11 | 6 new snapshots (Jan-Jun 2025) |

## Significance

FineWeb established the standard for open pretraining datasets. Its discovery about deduplication granularity (per-dump vs cross-dump) changed best practices across the field. The FineWeb-Edu classifier became a component of [[entities/nemotron-cc]]'s ensemble filtering approach.

## Mentioned In

- [[sources/fineweb-dataset-huggingface]] — primary source
- [[sources/nemotron-cc-nvidia]] — FineWeb-Edu classifier used in ensemble
- [[sources/multilingual-llm-training-data]] — FineWeb-2 for multilingual data

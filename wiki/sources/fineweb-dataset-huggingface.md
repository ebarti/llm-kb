---
title: "Source: FineWeb — Decanting the Web for the Finest Text Data at Scale"
type: source-summary
source: "[[raw/fineweb-dataset-huggingface]]"
related: ["[[concepts/training-data-curation]]", "[[concepts/data-deduplication]]", "[[entities/fineweb]]", "[[entities/common-crawl]]", "[[entities/huggingface]]"]
last_compiled: 2026-04-05
summary: "HuggingFace's 15T-token open dataset from 96 CommonCrawl dumps; discovered that aggressive cross-dump deduplication can harm quality and that per-dump dedup preserves more useful data."
---

## Key Points

- FineWeb is the largest publicly available clean LLM pretraining dataset at ~15 trillion tokens
- Built from 96 CommonCrawl dumps (summer 2013 to April 2024)
- Outperforms C4, RefinedWeb, Dolma, The Pile, SlimPajama, and RedPajama
- **Key discovery**: aggressive MinHash deduplication across dumps can remove valuable data — one dump lost 94% of tokens, yet the removed data trained better models
- Solution: per-dump deduplication rather than cross-dump comparison
- FineWeb-Edu variant: 1.3T tokens filtered for educational content using classifier
- FineWeb-2: multilingual extension covering 1,000+ languages
- Evaluation uses early-signal benchmarking on smaller models as cost-efficient proxies

## Detailed Summary

FineWeb represents HuggingFace's attempt to create an open replication of RefinedWeb with enhanced filtering. The project revealed that data curation is deeply non-obvious — the team's initial assumption that more aggressive deduplication would yield better data proved wrong in important ways.

When MinHash deduplication was applied chronologically across 90+ dumps, later dumps were heavily deduplicated against earlier ones. In the most extreme case, a dump went from 490B to 31B tokens (94% reduction). But controlled experiments showed models trained on the "duplicate" data actually performed better, suggesting that temporal repetition of high-quality content can be beneficial.

The final pipeline uses multi-level heuristic filtering with custom filters for domain-specific noise (lorem ipsum, JavaScript notices, boilerplate) combined with iterative validation. The FineWeb-Edu variant adds a classifier trained to identify educational web pages, dramatically improving performance on knowledge-intensive benchmarks.

## Notable Quotes

> "Dataset curation demands meticulous approach to data collection, filtering, and deduplication combined with rigorous iterative validation rather than executing predetermined strategies at scale."

## Related Concepts

- [[concepts/training-data-curation]] — FineWeb as the reference open pretraining dataset
- [[concepts/data-deduplication]] — the per-dump vs cross-dump dedup discovery
- [[concepts/multilingual-training-data]] — FineWeb-2 extends to 1,000+ languages
- [[concepts/model-based-filtering]] — FineWeb-Edu classifier for educational content

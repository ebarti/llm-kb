---
title: "Common Crawl"
type: entity
entity_type: dataset
sources: ["[[sources/dclm-datacomp-language-models]]", "[[sources/fineweb-dataset-huggingface]]", "[[sources/nemotron-cc-nvidia]]", "[[sources/nebius-llm-data-preparation]]"]
related: ["[[concepts/training-data-curation]]", "[[entities/fineweb]]", "[[entities/dclm]]", "[[entities/nemotron-cc]]"]
last_compiled: 2026-04-05
summary: "Non-profit web crawl archive releasing monthly snapshots of petabytes of raw web data — the foundational data source for virtually all open LLM pretraining datasets."
---

## Overview

Common Crawl is a non-profit organization that crawls the web and freely provides its archives and datasets. It releases new crawl snapshots monthly (or every two months), each containing petabytes of raw web page data, metadata, and extracted text.

Since GPT-2, Common Crawl has been the primary data source for LLM pretraining. GPT-3, LLaMA, T5, and virtually all open-source LLMs incorporate Common Crawl data in their training mixtures.

## Data Formats

- **WARC** (Web ARChive): complete HTTP request/response pairs including HTML
- **WAT**: metadata about each crawled page
- **WET** (WARC Encapsulated Text): pre-extracted plain text with heuristic boilerplate removal

WET files are the most common starting point for LLM data pipelines, though [[sources/dclm-datacomp-language-models]] found that re-extracting from WARC with resiliparse improved quality by 2.5+ points over WET files.

## Scale

- Petabytes of raw data per crawl
- Billions of web pages per snapshot
- [[entities/dclm]]'s DCLM-Pool extracted 240 trillion tokens from multiple crawl snapshots

## Quality Challenges

Raw Common Crawl is "sufficient for training but of much lower quality" than curated sources. It contains:
- Spam, SEO content, and advertising
- Boilerplate (navigation, headers, footers, cookie notices)
- Duplicate and near-duplicate content across domains
- Machine-generated content of varying quality
- Content in 1,000+ languages with highly uneven quality distribution

This is why [[concepts/training-data-curation]] — the process of transforming raw Common Crawl into usable training data — is so critical and has become a research field in its own right.

## Downstream Datasets

| Dataset | Tokens | Method | Notable Feature |
|---------|--------|--------|----------------|
| [[entities/fineweb]] | 15T | Heuristic + per-dump dedup | Largest open dataset |
| [[entities/dclm]] | 2T (filtered from 240T pool) | fastText model-based filtering | Best benchmark methodology |
| [[entities/nemotron-cc]] | 6.3T (4.4T real + 1.9T synthetic) | Classifier ensembling + synthesis | Long-horizon training |
| C4 | 750B | Basic heuristic filtering | Historical baseline |
| RefinedWeb | 5T | Quality filtering | FineWeb's predecessor |

## Mentioned In

- [[sources/dclm-datacomp-language-models]] — 240T-token DCLM-Pool extraction
- [[sources/fineweb-dataset-huggingface]] — 96 dumps processed (2013-2024)
- [[sources/nemotron-cc-nvidia]] — long-horizon dataset construction
- [[sources/nebius-llm-data-preparation]] — standard large-scale data source

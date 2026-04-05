---
title: "Pretraining Data Pipeline"
type: concept
sources: ["[[sources/analyticsvidhya-llm-pretraining-guide]]", "[[sources/mlops-pretraining-pipeline]]", "[[sources/raschka-pretraining-post-training-paradigms]]"]
related: ["[[concepts/llm-pretraining]]", "[[concepts/tokenization]]", "[[concepts/data-quality-bottleneck]]", "[[entities/fineweb]]"]
last_compiled: 2026-04-05
summary: "The multi-stage pipeline for preparing LLM training data: web crawling, URL filtering, text extraction, language filtering, quality filtering, deduplication (MinHash), PII removal, and domain balancing. FineWeb exemplifies this with 15T tokens from 36T after filtering."
---

## Overview

The pretraining data pipeline transforms raw web crawls and other sources into clean, tokenized training data. This pipeline has become one of the primary non-compute costs of LLM training, as data quality directly determines model quality (see [[concepts/data-quality-bottleneck]]).

## Pipeline Stages (FineWeb Example)

The [[entities/fineweb]] dataset (Hugging Face) provides the most documented example:

| Stage | Purpose | Method |
|-------|---------|--------|
| 1. URL Filtering | Block undesirable domains | Blocklists for adult/spam content |
| 2. Text Extraction | Remove HTML/JavaScript | Content extraction preserving meaning |
| 3. Language Filtering | Identify target language | fastText classifier (confidence >= 0.65) |
| 4. Quality Filtering | Remove low-quality text | Gopher filters for repetitive/nonsensical content |
| 5. Deduplication | Remove near-duplicates | MinHash approximate matching |
| 6. C4 Filtering | Remove boilerplate | Regex-based boilerplate/repetition removal |
| 7. PII Removal | Strip personal information | Scrub names, addresses, contact details |

**Result**: From raw CommonCrawl, ~36T tokens survive the full pipeline. FineWeb contains 15T tokens in 44TB.

## Data Sources and Mix

Modern LLMs train on a mix of:
- **Web data** (dominant): CommonCrawl, proprietary crawls
- **Books**: Diverse, high-quality prose
- **Code**: GitHub, StackOverflow
- **Academic papers**: ArXiv, PubMed
- **Conversational data**: Forums, social media
- **Curated datasets**: Wikipedia, StackExchange

The **data mix** — the proportion of each source — significantly affects model capabilities. [[sources/raschka-pretraining-post-training-paradigms]] shows that leading models up-weight math and code data in later training stages.

## Curriculum and Multi-Stage Data

All leading 2024 models use [[concepts/multi-stage-pretraining]] with evolving data mixes:
1. **Stage 1**: Dominated by massive web data for broad knowledge
2. **Stage 2**: Up-weight high-quality data (math, code, curated text)
3. **Stage 3**: Synthetic long-context data for context extension

## Challenges

- **Data exhaustion**: High-quality text may be running out — total internet text is estimated at ~30-100T tokens
- **Copyright**: Legal uncertainty around training on copyrighted web content
- **Bias**: Web data reflects societal biases
- **Synthetic data**: Increasingly used to augment natural data, but risks model collapse if poorly managed

## Sources

- [[sources/analyticsvidhya-llm-pretraining-guide]] — detailed FineWeb pipeline (7 stages)
- [[sources/mlops-pretraining-pipeline]] — data curation as major cost
- [[sources/raschka-pretraining-post-training-paradigms]] — data mix strategies across models

## Related Concepts

- [[concepts/tokenization]] — the next step after data cleaning
- [[concepts/data-quality-bottleneck]] — quality > quantity
- [[concepts/llm-pretraining]] — the process consuming this data
- [[entities/fineweb]] — the exemplar dataset

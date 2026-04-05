---
title: "Source: A Comprehensive Guide to LLM Pretraining"
type: source-summary
source: "[[raw/analyticsvidhya-llm-pretraining-guide]]"
related: ["[[concepts/llm-pretraining]]", "[[concepts/pretraining-data-pipeline]]", "[[concepts/tokenization]]", "[[concepts/next-token-prediction]]"]
last_compiled: 2026-04-05
summary: "Analytics Vidhya end-to-end pretraining guide: FineWeb dataset (15T tokens, 44TB), 7-stage data pipeline (URL filtering through PII removal), BPE tokenization (GPT-4's 100K vocabulary), and transformer training mechanics."
---

## Key Points

- FineWeb: 15 trillion tokens, 44TB, from CommonCrawl
- 7-stage preprocessing: URL filtering, text extraction, language filtering, quality filtering, deduplication (MinHash), C4 filtering, PII removal
- BPE tokenization: GPT-4 uses 100,277 tokens
- GPT-2: 1.6B params, 100B tokens; Llama 3: 405B params, 15T tokens
- Base models are "statistical pattern recognizers" without explicit intent understanding

## Detailed Summary

This source provides the most detailed look at the **data preprocessing pipeline** among the ingested sources.

**[[concepts/pretraining-data-pipeline]]** for FineWeb:
1. URL Filtering: block adult/spam domains
2. Text Extraction: strip HTML/JavaScript
3. Language Filtering: fastText classifiers (confidence >= 0.65)
4. Quality Filtering: Gopher filters for low-quality text
5. Deduplication: MinHash for near-duplicate detection
6. C4 Filtering: remove boilerplate/repetition
7. PII Removal: scrub personal information

Result: 36T tokens remain from raw web data after the full pipeline.

**[[concepts/tokenization]]**: BPE iteratively merges frequent byte pairs. GPT-4's vocabulary of 100,277 tokens balances sequence length against token granularity. Initial vocabulary is 256 (byte values).

**Training mechanics**: Cross-entropy loss between predicted and actual next-token probabilities, optimized via Adam. Output is a probability distribution over the entire vocabulary at each position.

## Related Concepts

- [[concepts/pretraining-data-pipeline]] — the 7-stage data pipeline
- [[concepts/tokenization]] — BPE and vocabulary design
- [[concepts/next-token-prediction]] — the training objective
- [[entities/fineweb]] — the dataset described in detail

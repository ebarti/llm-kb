---
title: "Source: Data Preparation for LLMs — Techniques, Tools, and Pipeline"
type: source-summary
source: "[[raw/nebius-llm-data-preparation]]"
related: ["[[concepts/training-data-curation]]", "[[concepts/data-deduplication]]", "[[concepts/model-based-filtering]]", "[[entities/common-crawl]]"]
last_compiled: 2026-04-05
summary: "End-to-end LLM data preparation pipeline: source selection, heuristic and similarity-based filtering, MapReduce deduplication, language handling (90% English default), and subword tokenization."
---

## Key Points

- "Data is half the battle" in ML success
- Pipeline: source selection → quality assessment → deduplication → language handling → tokenization
- Heuristic filtering: document length, numeral ratios, punctuation patterns
- Similarity-based filtering: classifiers scoring relevance to known high-quality sources
- MapReduce for honest distributed deduplication (vs partition-local dedup)
- Default language split: 90% English, remainder distributed across other languages
- Subword tokenization as the standard encoding approach
- Three emerging challenges: insufficient crawl data, synthetic internet pollution, copyright restrictions

## Detailed Summary

This source provides a practical overview of the end-to-end LLM data preparation pipeline. While less research-focused than the DCLM or Nemotron-CC papers, it captures the operational reality that most practitioners face.

The distinction between heuristic-based and similarity-based (model-based) filtering parallels the findings in [[sources/dclm-datacomp-language-models]], where model-based approaches consistently outperform heuristics. The note about MapReduce enabling "honest" deduplication (across all partitions, not just within individual machines) is an important practical detail often overlooked in academic papers.

The three emerging challenges — insufficient data, synthetic pollution, and copyright — represent existential threats to the current training data paradigm and drive the need for the innovations described in other sources.

## Related Concepts

- [[concepts/training-data-curation]] — practical pipeline overview
- [[concepts/data-deduplication]] — MapReduce distributed dedup
- [[concepts/copyright-and-training-data]] — copyright as a data sourcing constraint
- [[concepts/multilingual-training-data]] — the 90/10 English-to-other-language split

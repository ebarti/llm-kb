---
title: "Source: DataComp-LM — In Search of the Next Generation of Training Sets"
type: source-summary
source: "[[raw/dclm-datacomp-language-models]]"
related: ["[[concepts/training-data-curation]]", "[[concepts/model-based-filtering]]", "[[concepts/data-deduplication]]", "[[entities/dclm]]", "[[entities/common-crawl]]"]
last_compiled: 2026-04-05
summary: "DCLM benchmark provides 240T-token Common Crawl testbed; finds fastText model-based filtering is the single most impactful curation technique, enabling a 7B model to reach 64% MMLU with 6.6x less compute than Llama 2."
---

## Key Points

- DCLM provides a standardized testbed for dataset experiments at five scales (412M to 7B parameters) with 53 downstream evaluations
- The DCLM-Pool contains 240 trillion tokens from Common Crawl (200 billion documents, 370TB compressed)
- Re-extracting text with resiliparse instead of standard WET files improved performance by 2.5+ points
- **Model-based filtering is the most impactful curation technique**: fastText classifiers trained on instruction-formatted data outperformed all alternatives
- Optimal configuration retains only the top 10% of documents by quality score
- The resulting DCLM-Baseline (2T tokens) trains a 7B model to 64% MMLU — matching far larger models at a fraction of compute
- Dataset quality rankings are consistent across scales (Pearson r=0.885-0.919), meaning small-scale experiments reliably predict large-scale results
- Counterintuitively, mixing curated sources (Wikipedia, arXiv) into DCLM-baseline degraded performance by 1.6-1.7 points

## Detailed Summary

DCLM addresses a fundamental gap in LLM research: it is often unclear what data curation strategies work best because researchers compare models trained with different architectures, compute budgets, and hyperparameters. The benchmark holds everything constant except the dataset, enabling rigorous A/B testing of curation strategies.

Seven filtering strategies were tested: PageRank, semantic dedup, BGE embeddings, AskLLM, perplexity filtering, top-k logits, and fastText classifiers. FastText won decisively at 30.2 Core accuracy vs 26.1 for PageRank. A key insight was that training the fastText classifier on instruction-formatted data (from [[entities/openhermes]] and ELI5) produced a 3.5-point lift over conventional approaches using Wikipedia/OpenWebText as positive examples.

For deduplication, MinHash-based approaches and modified Bloom filtering performed comparably (within 0.2 points), but Bloom filters scaled better beyond 10TB datasets.

Contamination analysis was rigorous: removing detected MMLU overlaps from DCLM-baseline actually improved performance (52.7% vs 51.8%), confirming gains came from genuine quality improvements, not data leakage.

## Notable Quotes

> "Human quality judgments showed limited predictive value for identifying beneficial training data."

> "Sufficiently aggressive filtering may obviate the benefits of specialized curated data."

## Related Concepts

- [[concepts/training-data-curation]] — DCLM is the definitive benchmark for comparing curation strategies
- [[concepts/model-based-filtering]] — fastText classifiers as the dominant filtering approach
- [[concepts/data-deduplication]] — MinHash vs Bloom filter comparison at scale
- [[concepts/scaling-laws]] — quality rankings transfer across model scales
- [[concepts/benchmark-contamination]] — rigorous decontamination methodology

---
title: "Heuristic vs Model-Based Filtering"
type: comparison
subjects: ["[[concepts/model-based-filtering]]", "[[concepts/training-data-curation]]"]
sources: ["[[sources/dclm-datacomp-language-models]]", "[[sources/nemotron-cc-nvidia]]", "[[sources/nebius-llm-data-preparation]]"]
last_compiled: 2026-04-05
summary: "Heuristic filters (rule-based) handle obvious noise cheaply but miss subtle quality differences; model-based filters (fastText, LLM scorers) capture quality nuances and dominate performance — the decisive finding from DCLM."
---

## Overview

The two main approaches to filtering web data for LLM pretraining are rule-based heuristic filters and trained model-based classifiers. Research consistently shows model-based approaches are far more impactful, but heuristics remain useful as a complementary first pass.

## Comparison Table

| Dimension | Heuristic Filtering | Model-Based Filtering |
|-----------|-------------------|---------------------|
| **Approach** | Hand-crafted rules | Trained classifiers |
| **Examples** | Length thresholds, symbol ratios, stopword counts, URL blocklists | fastText classifier, perplexity scoring, AskLLM, embedding similarity |
| **What it catches** | Obvious noise: too short, too long, excessive symbols, boilerplate | Subtle quality: informativeness, educational value, relevance |
| **Compute cost** | Very low | Low (fastText) to high (LLM-based) |
| **Performance** | Necessary baseline | Decisive differentiator |
| **DCLM Core accuracy** | Not separately reported (baseline) | 30.2 (fastText) vs 26.1 (PageRank) |
| **Scalability** | Trivially parallel | fastText: highly scalable; LLM: expensive at scale |
| **Interpretability** | High — rules are explicit | Moderate (fastText) to low (LLM) |
| **Maintenance** | Manual rule updates | Retraining on new examples |

## Key Finding

[[sources/dclm-datacomp-language-models]] provides definitive evidence: model-based filtering using fastText classifiers achieves 30.2 Core accuracy versus the best heuristic-like approach (PageRank at 26.1). The 4.1-point gap is substantial and consistent across scales.

The most important insight is WHAT to train the classifier on: instruction-formatted data (OpenHermes 2.5, ELI5) outperformed traditional positive examples (Wikipedia, OpenWebText) by 3.5 points. This suggests the classifier should learn "what good instruction-following data looks like" rather than "what encyclopedic content looks like."

## Complementary Use

[[sources/nemotron-cc-nvidia]] demonstrates the optimal combined approach: use heuristic filters on lower-quality segments (where they effectively remove obvious noise) while disabling them on high-quality segments (where they incorrectly remove valuable content). This recovers tokens that aggressive heuristic pipelines would have discarded.

## When to Use Each

| Scenario | Recommended Approach |
|----------|---------------------|
| Quick first pass on raw crawl | Heuristics (cheap, fast) |
| Final quality selection | Model-based (decisive) |
| Resource-constrained | fastText (low compute, high quality) |
| Maximum quality | Classifier ensemble (Nemotron-CC style) |
| Domain-specific curation | Model-based with domain-specific positive examples |

## Sources

- [[sources/dclm-datacomp-language-models]] — definitive comparison of 7 filtering strategies
- [[sources/nemotron-cc-nvidia]] — complementary heuristic + model-based approach
- [[sources/nebius-llm-data-preparation]] — practical heuristic-first pipeline

---
title: "Model-Based Filtering"
type: concept
sources: ["[[sources/dclm-datacomp-language-models]]", "[[sources/nemotron-cc-nvidia]]", "[[sources/fineweb-dataset-huggingface]]", "[[sources/nebius-llm-data-preparation]]"]
related: ["[[concepts/training-data-curation]]", "[[concepts/data-quality-bottleneck]]", "[[concepts/scaling-laws]]"]
last_compiled: 2026-04-05
summary: "Using trained classifiers (fastText, LLM-based scorers) to filter web data for LLM pretraining — the single most impactful curation technique, outperforming heuristics, perplexity filtering, and human judgment."
---

## Overview

Model-based filtering uses trained classifiers to score and filter web documents for inclusion in LLM pretraining datasets. It has emerged as the most impactful single technique in the [[concepts/training-data-curation]] pipeline, consistently outperforming heuristic rules, perplexity-based methods, and even human quality judgments.

## The DCLM Comparison

[[sources/dclm-datacomp-language-models]] provides the most rigorous comparison of filtering approaches, testing seven strategies on a controlled benchmark:

| Strategy | Core Accuracy (1B-1x) | Notes |
|----------|----------------------|-------|
| PageRank scoring | 26.1 | Structural web signal |
| Semantic deduplication | 27.1 | Embedding-based |
| BGE embedding classifiers | 27.2 | Dense retrieval model |
| AskLLM prompting | 28.6 | LLM-as-judge |
| Perplexity filtering | 29.0 | Language model perplexity |
| Top-k average logits | 29.2 | Token-level confidence |
| **fastText classifiers** | **30.2** | **Simple but effective** |

FastText classifiers won decisively, achieving a 4.1-point advantage over PageRank and a 1.2-point lead over the nearest competitor. The key insight was the training data for the classifier: instruction-formatted examples from OpenHermes 2.5 and ELI5 subreddit posts produced a 3.5-point lift over conventional approaches using Wikipedia/OpenWebText as positive examples.

## Classifier Ensembling

[[sources/nemotron-cc-nvidia]] advances single-classifier filtering with **classifier ensembling**: combining three classifiers trained on different quality concepts (educational value from FineWeb-Edu, informativeness from DCLM, and custom annotation standards). This increases recall of quality documents from ~9-11% (single classifier) to 25%, capturing diverse content that any single classifier would miss.

This is particularly important for long-horizon training where aggressive single-classifier filtering (retaining only top 10%) creates a data bottleneck — there simply aren't enough unique tokens for 15T+ token training runs.

## What Makes Good Training Data

A counterintuitive finding from [[sources/dclm-datacomp-language-models]]: **human quality judgments showed limited predictive value** for identifying beneficial training data. What humans consider "high quality" (well-written, informative) doesn't perfectly correlate with what improves model performance. The most effective positive examples for classifier training were instruction-formatted dialogues, not encyclopedia articles.

Additionally, mixing curated "high-quality" sources (Wikipedia, arXiv, Stack Exchange) into an already well-filtered dataset degraded performance by 1.6-1.7 points, suggesting that sufficiently aggressive model-based filtering from web data can produce datasets that outperform hand-curated collections.

## Practical Implementation

The dominant approach uses fastText classifiers because:
1. **Speed**: processes millions of documents per hour on commodity hardware
2. **Simplicity**: single training step, no GPU required for inference
3. **Effectiveness**: outperforms more complex approaches including LLM-based scoring
4. **Reproducibility**: deterministic scores enable easy ablation studies

The typical workflow: train fastText binary classifier on positive examples (instruction data, educational content) vs negative examples (random web text), score all documents, retain top k% (usually 10-25%).

## Sources

- [[sources/dclm-datacomp-language-models]] — definitive filtering strategy comparison
- [[sources/nemotron-cc-nvidia]] — classifier ensembling innovation
- [[sources/fineweb-dataset-huggingface]] — FineWeb-Edu educational content classifier
- [[sources/nebius-llm-data-preparation]] — practical overview of filtering approaches

## Related Concepts

- [[concepts/training-data-curation]] — model-based filtering as the key pipeline stage
- [[concepts/data-quality-bottleneck]] — quality filtering as the bottleneck intervention
- [[concepts/scaling-laws]] — quality gains from filtering interact with model scaling

---
title: "DataComp-LM: In Search of the Next Generation of Training Sets for Language Models"
source: "https://arxiv.org/abs/2406.11794"
author: "Li et al. (Apple, University of Washington, et al.)"
date_published: 2024-06-17
date_ingested: 2026-04-05
tags: [training-data, dataset-curation, benchmark, common-crawl, model-based-filtering, deduplication]
type: paper
status: raw
discovered_via: search
---

# DataComp-LM (DCLM)

## Overview

DCLM is a testbed for controlled dataset experiments with the goal of improving language models. It provides a standardized corpus of 240T tokens extracted from Common Crawl (DCLM-Pool), effective pretraining recipes based on the OpenLM framework, and a broad suite of 53 downstream evaluations.

## Benchmark Architecture

Five competition scales spanning ~600x in compute:
- 400M-1x: 412M params, 8.2B tokens (~26 H100 hours)
- 1B-1x: 1.4B params, 28.8B tokens (~240 hours)
- 1B-5x: 1.4B params, 144B tokens (~1,200 hours)
- 7B-1x: 6.9B params, 138B tokens (~3,700 hours)
- 7B-2x: 6.9B params, 276B tokens (~7,300 hours)

Two tracks: filtering (optimizing datasets from DCLM-Pool) and mixing (combining multiple data sources).

## DCLM-Pool

240 trillion tokens from Common Crawl, representing 200 billion documents (370TB compressed). Re-extracted content using resiliparse rather than standard WET files, improving performance by 2.5+ points on Core metric.

## Dataset Construction Pipeline

### Text Extraction
Three approaches tested: resiliparse, trafilatura, WET files. Resiliparse offered best practical tradeoff of quality and speed.

### Deduplication
MinHash-based suffix array approaches compared with modified Bloom filtering. Comparable performance (within 0.2 points) with Bloom filters scaling better to datasets exceeding 10TB.

### Quality Filtering (most impactful component)
Seven strategies tested at 1B-1x scale:
1. PageRank scoring: 26.1 Core accuracy
2. Semantic deduplication: 27.1
3. BGE embedding classifiers: 27.2
4. AskLLM prompting: 28.6
5. Perplexity-based filtering: 29.0
6. Top-k average logits: 29.2
7. fastText classifiers: 30.2

FastText classifiers significantly outperformed alternatives. Training on instruction-formatted data from OpenHermes 2.5 and ELI5 subreddit posts produced a 3.5 percentage point lift.

Optimal configuration: retain top 10% of documents by fastText scores.

## DCLM-Baseline Results

~2 trillion tokens after deduplication (top 10% of filtered Common Crawl).

7B model on 2.6T tokens:
- MMLU 5-shot: 64%
- 6.6 percentage points above MAP-Neo on MMLU
- 40% less compute than MAP-Neo
- Performance approaching Mistral-7B-v0.3 (63%) and Llama 3 8B (66%) with 6.6x less compute

## Key Findings

- Dataset quality rankings consistent across scales (Pearson's r=0.885-0.919)
- Mixing high-quality sources (Wikipedia, arXiv) actually degraded DCLM-baseline by 1.6-1.7 points
- Contamination analysis: removing MMLU overlaps improved performance (52.7% vs 51.8%)
- Model-based filtering is the single most impactful curation technique
- Human quality judgments showed limited predictive value for identifying beneficial training data

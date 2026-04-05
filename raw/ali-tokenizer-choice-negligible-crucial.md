---
title: "Tokenizer Choice For LLM Training: Negligible or Crucial?"
source: "https://arxiv.org/html/2310.08754v4"
author: "Mehdi Ali et al."
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [tokenization, research-paper, vocabulary-size, multilingual, bpe, unigram]
type: paper
status: raw
discovered_via: search
---

# Tokenizer Choice For LLM Training: Negligible or Crucial?

## Overview

This comprehensive study investigates whether tokenizer selection significantly impacts large language model performance, challenging the assumption that tokenizers are a minor consideration.

## Methodology

Trained 24 mono- and multilingual 2.6B-parameter decoder-only models, systematically varying:
- Tokenizer algorithms: BPE and Unigram
- Libraries: Huggingface and SentencePiece
- Vocabulary sizes: 33k-100k tokens
- Training data: 70 billion word datasets — one English-only, one covering five European languages

## Key Findings

### Intrinsic Metrics (Fertility & Parity)
Fertility measures average tokens needed per word; parity assesses tokenization fairness across languages. These traditional metrics "are not always predictive of model downstream performance" — a critical limitation in conventional tokenizer evaluation.

### Vocabulary Size Impact
- **English models**: Smaller vocabularies (33k) performed better, suggesting convergence at lower sizes
- **Multilingual models**: Larger vocabularies (100k) yielded superior results
- Multilingual tokenizers require vocabulary size increases of factor three compared to English

### Computational Costs
English-centric tokenizers applied to multilingual training generated "additional training costs of up to 68%" for non-English languages due to inefficient tokenization.

### Downstream Performance
Results across 41 tasks revealed significant variability:
- **Monolingual English**: BPE-SP-33 performed best (50.81% average accuracy)
- **Multilingual**: BPE-SP-100 excelled (41.44% accuracy)
- Task-specific performance gaps: up to 9 percentage points between best and worst tokenizer on ARC-Easy

## Conclusions

Tokenizer choice is **crucial**, not negligible:
1. Traditional intrinsic metrics require contextual bounds — low fertility is necessary but insufficient for downstream success
2. Language-specific optimization matters; monolingual and multilingual settings demand different vocabulary strategies
3. Library implementation differences meaningfully affect performance despite identical algorithms
4. Implications for LLM democratization across languages and carbon footprint reduction

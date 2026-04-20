---
title: "Jina Reader-LM: Small Language Models for HTML to Markdown"
source: "https://jina.ai/news/reader-lm-small-language-models-for-cleaning-and-converting-html-to-markdown/"
author: "Jina AI"
date_published: 2024-09-01
date_ingested: 2026-04-05
tags: [jina, reader-lm, html-to-markdown, content-extraction, small-language-models]
type: article
status: raw
discovered_via: search
---

# Jina Reader-LM: Small Language Models for HTML to Markdown

Jina AI released Reader-LM-0.5B and Reader-LM-1.5B in September 2024 — specialized small language models for converting raw HTML into clean markdown. An alternative to the traditional rule-based Jina Reader pipeline.

## The Problem

The original Jina Reader API used headless Chrome + Mozilla Readability + regex + Turndown (JS library) to extract and convert content. This heuristic approach required constant patching and lacked multilingual flexibility.

## The Neural Approach

The task is fundamentally a "selective-copy" operation: the model primarily needs to skip over HTML markup, sidebars, headers, footers, with minimal new content generation.

## Model Architecture

### Reader-LM-0.5B
- 494M parameters, 24 transformer layers, 896 hidden size
- 256K token context length
- 14 query heads, 2 KV heads

### Reader-LM-1.5B
- 1.54B parameters, 28 transformer layers, 1536 hidden size
- 256K token context length
- 12 query heads, 2 KV heads

## Performance Benchmarks

| Model | ROUGE-L | WER | TER |
|-------|---------|-----|-----|
| Reader-LM-1.5B | **0.72** | **1.87** | **0.19** |
| GPT-4o | 0.43 | 5.88 | 0.50 |
| Gemini-1.5-Pro | 0.42 | 3.16 | 0.48 |
| LLaMA-3.1-70B | 0.40 | 9.87 | 0.50 |

Reader-LM-1.5B dramatically outperforms models 50x its size on this specialized task.

## Training Methodology

### Data: 2.5 billion tokens
- Generated training pairs using Jina Reader API
- Supplemented with synthetic examples from GPT-4o
- Chat template format

### Two-Stage Training
1. Short-and-simple HTML (32K max sequence, 1.5B tokens)
2. Long-and-hard HTML (128K max, 1.2B tokens, ring flash attention)

## ReaderLM v2 (January 2025)

1.5B parameters built on Qwen2.5-1.5B-Instruction. 512K token context. 29 languages.

### Key Improvements over v1
- 3x quality improvement
- HTML-to-JSON generation (schema-based extraction directly from HTML)
- Contrastive loss training eliminates degeneration/repetition
- Better long-context stability

### v2 Benchmarks
- ROUGE-L: 0.86 (vs 0.69 for Gemini 2.0 Flash)
- Outperforms Qwen2.5-32B-Instruct and GPT-4o on markdown conversion
- Comparable JSON extraction (F1: 0.81-0.82)

### v2 Training (4 stages)
1. Long-context pretraining (32K → 256K progressive expansion)
2. Supervised fine-tuning on instruction datasets
3. Direct Preference Optimization (DPO) on draft/refined pairs
4. Self-play reinforcement tuning with model-generated critique

### v2 Dataset
- html-markdown-1m: 1 million HTML documents, averaging 56K tokens each
- 3-stage synthetic pipeline using Qwen2.5-32B (draft → refine → critique)

## Technical Challenges Solved

### Degeneration/Repetition
Models would generate same tokens repeatedly. Solutions:
- Contrastive search decoding with contrastive loss during training
- Automatic repetition detection to stop decoding early

### Encoder-Only Alternative (Failed)
Token classification approach (like NER) was explored but abandoned because:
- Sparse labeling in noisy HTML made learning difficult
- Markdown syntax doesn't exist in raw HTML
- Token reordering couldn't be represented in binary classification

## Significance

Reader-LM demonstrates that specialized small language models can dramatically outperform general-purpose LLMs on specific tasks. The shift from heuristic pipelines (Readability + regex + Turndown) to neural approaches represents a paradigm change in content extraction.

## Jina Reader API

The Reader API converts any URL to LLM-friendly text:
- Prefix any URL with `r.jina.ai/` to get clean markdown
- `s.jina.ai/` performs live web search with content extraction
- Pipeline: headless Chrome → Readability → Turndown → markdown
- ReaderLM v2 available as alternative engine via `x-engine: readerlm-v2` header

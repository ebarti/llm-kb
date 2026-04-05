---
title: "Source: Jina Reader-LM — HTML to Markdown via Small Language Models"
type: source-summary
source: "[[raw/jina-reader-lm-html-to-markdown]]"
related: ["[[concepts/html-to-markdown-conversion]]", "[[concepts/content-extraction]]", "[[entities/jina-reader]]", "[[entities/reader-lm]]"]
tags: [jina, reader-lm, html-to-markdown, small-language-models, content-extraction]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Jina's Reader-LM (0.5B-1.5B params) outperforms GPT-4o at HTML-to-markdown conversion by treating it as a selective-copy task — a paradigm shift from heuristic pipelines to neural content extraction."
---

## Key Points

- Reader-LM-1.5B achieves ROUGE-L 0.72 vs GPT-4o's 0.43 on HTML-to-markdown — a 1.5B model beating a model 100x+ its size
- ReaderLM v2 (built on Qwen2.5-1.5B) further improves to ROUGE-L 0.86, adds HTML-to-JSON extraction
- The task is "selective-copy": skip markup/boilerplate, retain content — no creative generation needed
- Training used 2.5B tokens from Jina Reader API + GPT-4o synthetic pairs
- The original Jina Reader pipeline (Chrome → Readability → regex → Turndown) required constant patching; neural approach is more robust
- v2 uses 4-stage training: long-context pretraining, SFT, DPO, self-play reinforcement

## Detailed Summary

This article documents a fundamental paradigm shift in content extraction: from heuristic rule-based pipelines to neural approaches using specialized small language models.

The Jina Reader API originally used a multi-stage heuristic pipeline: headless Chrome fetches the page, [[entities/mozilla-readability]] extracts the article, regex patterns clean up artifacts, and Turndown converts HTML to markdown. This worked but required constant maintenance as websites evolved.

Reader-LM replaces this entire pipeline with a single model inference. The insight is that HTML-to-markdown is a "selective-copy" task — the model mostly copies text from input to output while skipping markup and boilerplate. This makes it amenable to small, specialized models rather than general-purpose LLMs.

The v2 improvements are substantial: a 3-stage synthetic data pipeline (draft → refine → critique using Qwen2.5-32B) overcame the ceiling of rule-based training data. DPO and self-play reinforcement further refined quality. The model now handles 512K token contexts, 29 languages, and can extract structured JSON directly from HTML using schemas.

For [[concepts/document-processing-pipeline]] design, Reader-LM represents a third option alongside rule-based extraction (Readability, Trafilatura) and API-based services (Firecrawl): run a local 1.5B model that outperforms both.

## Concepts Introduced or Discussed

- [[concepts/html-to-markdown-conversion]] — the core task
- [[concepts/content-extraction]] — neural vs. heuristic approaches
- [[concepts/boilerplate-removal]] — what the model learns to skip
- [[concepts/small-language-models]] — specialized SLMs outperforming general LLMs

## Quotes & Evidence

> "The model primarily needs to selective-copy from the input to the output, with minimal effort spent on generating new content."
> "Training an SLM from scratch is particularly challenging... continued task-specific training from pretrained models significantly improved efficiency."

## Metadata

- **Author**: Jina AI
- **Date Published**: 2024-09 (v1), 2025-01 (v2)
- **Format**: article
- **URL**: https://jina.ai/news/reader-lm-small-language-models-for-cleaning-and-converting-html-to-markdown/

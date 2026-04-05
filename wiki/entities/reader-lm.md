---
title: "Reader-LM (Jina)"
type: entity
entity_type: tool
url: "https://huggingface.co/jinaai/ReaderLM-v2"
related: ["[[concepts/html-to-markdown-conversion]]", "[[concepts/content-extraction]]", "[[entities/jina-reader]]"]
tags: [reader-lm, jina, small-language-models, html-to-markdown]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Jina's 1.5B-parameter specialized language model for HTML-to-markdown conversion — outperforms GPT-4o (ROUGE-L 0.86 vs 0.43) by treating the task as selective-copy, with 512K token context and 29-language support."
---

## Overview

Reader-LM is a family of small language models specifically trained to convert raw HTML into clean markdown (and, in v2, structured JSON). It demonstrates that specialized small models dramatically outperform general-purpose LLMs on domain-specific tasks.

## Key Facts

- **Type**: Small Language Model (SLM)
- **URL**: https://huggingface.co/jinaai/ReaderLM-v2
- **Developer**: Jina AI
- **License**: CC BY-NC 4.0 (commercial requires separate agreement)
- **Notable for**: A 1.5B model beating GPT-4o, Gemini, and LLaMA-70B at HTML-to-markdown

## Model Versions

### Reader-LM v1 (September 2024)
- 0.5B and 1.5B parameter variants
- 256K token context
- ROUGE-L: 0.72 (1.5B) vs GPT-4o's 0.43

### Reader-LM v2 (January 2025)
- 1.5B parameters, built on Qwen2.5-1.5B-Instruction
- 512K token context (combined I/O)
- ROUGE-L: 0.86 (vs 0.69 for Gemini 2.0 Flash)
- Adds HTML-to-JSON extraction via schemas
- 29-language support
- 4-stage training: long-context pretraining → SFT → DPO → self-play reinforcement

## Key Insight

HTML-to-markdown is a "selective-copy" task: the model mostly copies text from input to output while skipping markup and boilerplate. This makes it amenable to small, specialized models rather than large general-purpose ones. Training used a 3-stage synthetic data pipeline (draft → refine → critique using Qwen2.5-32B).

## Deployment Options

- **Jina Reader API**: Set `x-engine: readerlm-v2` header
- **Google Colab**: Free T4 GPU tier (67 tokens/sec input, 36 tokens/sec output)
- **Cloud**: AWS SageMaker, Azure, Google Cloud Marketplace

## Mentions

- [[sources/jina-reader-lm-html-to-markdown]] — detailed technical analysis and benchmarks
- [[concepts/html-to-markdown-conversion]] — as Generation 3 neural approach
- [[concepts/content-extraction]] — paradigm shift from heuristic to neural

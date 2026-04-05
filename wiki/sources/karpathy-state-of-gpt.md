---
title: "Source: State of GPT — Microsoft Build 2023"
type: source-summary
source: "[[raw/karpathy-state-of-gpt]]"
related: ["[[entities/andrej-karpathy]]", "[[entities/openai]]", "[[concepts/fine-tuning]]", "[[concepts/prompt-engineering]]"]
tags: [karpathy, GPT, training-pipeline, RLHF, Microsoft-Build]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Karpathy's Microsoft Build 2023 keynote explaining the full GPT training pipeline (pretraining → SFT → RLHF) and practical LLM usage tips — became the definitive accessible introduction to how ChatGPT works."
---

## Key Points

- Full GPT training pipeline: pretraining → tokenization → SFT → RLHF
- Pretraining is the computational bottleneck (thousands of GPUs, months, millions of dollars)
- SFT and RLHF are lightweight but critical for alignment
- Practical tips: try multiple samples, ask reflective questions, use retrieval augmentation
- Covered the emerging ecosystem of plugins, tool use, and fine-tuning
- Became one of the most widely referenced introductions to LLM training

## Detailed Summary

Delivered at Microsoft Build in May 2023, this keynote became the canonical accessible introduction to how GPT models are trained and used. Karpathy, still at OpenAI at the time, walked through the full pipeline with characteristic clarity.

The training explanation covers four stages. Pretraining consumes most resources — training on web-scale data (CommonCrawl, Wikipedia, GitHub) to learn general language patterns. Tokenization converts text to integer sequences. Supervised Fine-Tuning (SFT) teaches the model to follow instructions using curated prompt-response pairs. RLHF uses human preference rankings to create a reward model, then optimizes the language model against it via PPO.

The practical section offered concrete advice that became widely adopted: generate multiple completions to overcome sampling variance, prompt models to self-check their work, use retrieval augmentation for grounding, and apply chain-of-thought for complex reasoning. These tips anticipated the [[concepts/context-engineering]] discipline that Karpathy would promote two years later.

## Concepts Introduced or Discussed

- [[concepts/fine-tuning]] — SFT stage of the pipeline
- [[concepts/prompt-engineering]] — Practical usage tips
- [[concepts/context-engineering]] — Foreshadowed by retrieval augmentation advice

## Metadata

- **Author**: Andrej Karpathy
- **Date Published**: 2023-05-23
- **Format**: conference keynote (video)
- **URL**: https://community.openai.com/t/build-talk-state-of-gpt-andrej-karpathy/226110

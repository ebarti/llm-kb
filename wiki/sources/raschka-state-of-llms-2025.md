---
title: "Source: The State of LLMs 2025"
type: source-summary
source: "[[raw/raschka-state-of-llms-2025]]"
related: ["[[concepts/benchmark-saturation]]", "[[concepts/llm-evaluation-metrics]]", "[[entities/chatbot-arena]]", "[[entities/mmlu]]"]
last_compiled: 2026-04-05
summary: "Sebastian Raschka's annual review identifies 'benchmaxxing' as the defining 2025 trend: benchmark scores are no longer trustworthy indicators of LLM performance due to training data contamination and direct optimization."
---

## Key Points

- "Benchmaxxing" defined as pushing leaderboard numbers at the expense of genuine capability
- "Benchmark numbers are no longer trustworthy indicators of LLM performance"
- Test set data often part of training corpus (intentionally or unintentionally)
- MMLU saturated above 88%; GPT-5.3 Codex at 93%
- 15 major benchmarks in active use in 2026; only 4 reliably predict production outcomes
- Reasoning models achieved gold-level IMO performance in 2025
- Solutions: continuous real-world testing, generating new benchmarks regularly

## Detailed Summary

Sebastian Raschka's analysis is the most authoritative assessment of the [[concepts/benchmark-saturation]] crisis in LLM evaluation. The central thesis is devastating for the evaluation field: benchmark scores, the primary tool for comparing LLMs, have become unreliable.

The problem is twofold. First, **data contamination**: benchmark test sets frequently appear in training data, either intentionally or through web crawling. Second, **direct optimization**: labs explicitly optimize for benchmark performance during development, making scores reflect optimization effort rather than genuine capability.

The parallel to 2019 image classification is illuminating: benchmark inflation occurred without actual ranking changes, meaning all models improved on the benchmark without improving relative to each other. Raschka argues LLM evaluation has deteriorated even further.

The fundamental challenge is that LLMs are **multi-task** systems. Unlike image classifiers with a single metric, LLMs handle translation, summarization, coding, math, brainstorming, and more — making any single benchmark inadequate.

Despite this, notable progress occurred: multiple reasoning models achieved gold-level mathematical competition performance (IMO-equivalent), and [[entities/chatbot-arena]] crowdsourced evaluation provides a partial counterweight to static benchmarks.

## Related Concepts

- [[concepts/benchmark-saturation]] — the core crisis identified
- [[concepts/llm-evaluation-metrics]] — the broader evaluation landscape
- [[concepts/data-quality-bottleneck]] — related quality issue in KB context

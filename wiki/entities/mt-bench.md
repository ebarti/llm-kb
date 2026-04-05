---
title: "MT-Bench"
type: entity
entity_type: dataset
sources: ["[[sources/cameron-wolfe-llm-as-judge]]", "[[sources/eugeneyan-llm-evaluators]]"]
related: ["[[concepts/llm-benchmarks]]", "[[concepts/llm-as-judge]]", "[[entities/chatbot-arena]]"]
last_compiled: 2026-04-05
summary: "Fixed 80-question multi-turn benchmark spanning 8 categories (writing, roleplay, extraction, reasoning, math, coding, knowledge, stem), created by LMSYS for evaluating LLM conversation quality."
---

## Overview

MT-Bench is a benchmark dataset of 80 carefully curated multi-turn questions spanning eight categories: writing, roleplay, extraction, reasoning, math, coding, knowledge, and STEM. Created by the LMSYS team alongside [[entities/chatbot-arena]], it is designed for evaluating LLM conversation quality using [[concepts/llm-as-judge]] evaluation.

## Key Properties

- **80 questions** across 8 genres
- **Multi-turn**: Tests ability to maintain coherence across conversation turns
- **Curated for quality**: High-quality, diverse questions
- **GPT-4 as default judge**: Standard evaluation uses GPT-4 scoring

## Significance

MT-Bench demonstrated that GPT-4 achieves **85% agreement with human experts** (excluding ties), exceeding the 81% human-human agreement rate. This result was instrumental in establishing [[concepts/llm-as-judge]] as a viable evaluation paradigm.

## Limitations

- Fixed question set (vulnerable to contamination over time)
- Only 80 questions (limited coverage)
- Predefined topics (may not reflect real user needs)
- Contrast with [[entities/chatbot-arena]]'s organic queries

## Mentioned In

- [[sources/cameron-wolfe-llm-as-judge]] — as primary LLM-as-Judge benchmark
- [[sources/eugeneyan-llm-evaluators]] — agreement data from MT-Bench evaluations

---
title: "TruthfulQA"
type: entity
entity_type: dataset
sources: ["[[sources/responsible-ai-labs-benchmarks-2025]]"]
related: ["[[concepts/llm-benchmarks]]", "[[concepts/hallucination-detection]]", "[[concepts/automated-fact-checking]]"]
last_compiled: 2026-04-05
summary: "817-question benchmark testing whether LLMs propagate common misconceptions; notable for revealing that state-of-the-art models score 'surprisingly low on truthfulness.'"
---

## Overview

TruthfulQA is a benchmark of 817 questions specifically designed to test whether LLMs produce truthful answers or propagate common misconceptions. Unlike knowledge benchmarks (which test what models know), TruthfulQA tests whether models resist generating plausible-sounding but false information.

## Significance

The benchmark revealed that "many state-of-the-art models score surprisingly low on truthfulness," demonstrating that larger models are not necessarily more truthful — they may simply be better at producing convincing-sounding answers regardless of accuracy.

This finding is directly relevant to [[concepts/hallucination-contamination]] in [[concepts/llm-knowledge-base]] systems.

## Mentioned In

- [[sources/responsible-ai-labs-benchmarks-2025]] — as a key safety benchmark

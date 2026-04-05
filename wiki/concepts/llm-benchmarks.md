---
title: "LLM Benchmarks"
type: concept
sources: ["[[sources/responsible-ai-labs-benchmarks-2025]]", "[[sources/raschka-state-of-llms-2025]]", "[[sources/chatbot-arena-methodology]]"]
related: ["[[concepts/benchmark-saturation]]", "[[concepts/llm-evaluation-metrics]]", "[[concepts/llm-as-judge]]", "[[entities/mmlu]]", "[[entities/chatbot-arena]]", "[[entities/helm]]", "[[entities/truthfulqa]]", "[[entities/mt-bench]]"]
last_compiled: 2026-04-05
summary: "Standardized evaluation datasets for comparing LLM capabilities: MMLU (knowledge), HELM (holistic), TruthfulQA (factuality), HumanEval (code), MT-Bench (conversation), Chatbot Arena (crowdsourced), with 15 benchmarks in active use by 2026."
---

## Overview

LLM benchmarks are standardized evaluation datasets and protocols used to compare language model capabilities. They serve as the primary tool for ranking models, tracking progress, and communicating capabilities to users. By 2026, approximately **15 major benchmarks** are in active use, though Sebastian Raschka notes that **only 4 reliably predict production outcomes**.

The benchmark landscape faces a fundamental tension: benchmarks need to be standardized to enable comparison, but standardization enables gaming and contamination (see [[concepts/benchmark-saturation]]).

## Major Benchmarks by Category

### General Knowledge & Reasoning

| Benchmark | Size | What It Tests | Status (2026) |
|-----------|------|--------------|---------------|
| **[[entities/mmlu]]** | 15,908 questions, 57 subjects | Broad knowledge from elementary math to professional law | **Saturated** — frontier models exceed 90% |
| **GPQA** | Graduate-level questions | Expert-level reasoning | Active; not yet saturated |
| **MMMU** | Multimodal questions | Combined text and image reasoning | Active |

### Mathematics

| Benchmark | What It Tests | Notable Scores |
|-----------|--------------|----------------|
| **MATH-500** | Competition-level mathematical reasoning (AMC, AIME) | Multi-step symbolic reasoning required |
| **AIME 2025** | Hardest math benchmark | Scores up to 95.7 |
| **GSM8K** | Grade-school math | Largely solved; not discriminative |

### Coding

| Benchmark | Size | What It Tests |
|-----------|------|--------------|
| **HumanEval** | 164 problems | Code generation (Pass@k metric) |
| **MBPP** | 1,000 problems | More Bugs, Please — broader coding tasks |
| **LiveCodeBench** | Continuously updated | Best for tracking real improvement (anti-memorization) |
| **SWE-bench** | Real GitHub issues | Software engineering capability |
| **Aider Polyglot** | Multi-language | Practical coding across languages |

### Safety & Alignment

| Benchmark | Size | What It Tests |
|-----------|------|--------------|
| **[[entities/truthfulqa]]** | 817 questions | Hallucination tendencies, common misconception propagation |
| **HEx-PHI** | 330 harmful instructions | Safety across 11 harm categories |
| **RAIL-HH-10K** | 10K examples | All 5 responsible AI dimensions |

### Conversation & Human Preference

| Benchmark | Methodology | Scale |
|-----------|------------|-------|
| **[[entities/mt-bench]]** | Fixed 80 questions, 8 genres | Controlled, multi-turn |
| **[[entities/chatbot-arena]]** | Crowdsourced anonymous pairwise battles | 300+ models, 1.5M+ votes |
| **AlpacaEval** | Automated evaluation vs reference model | Fast, automated |
| **TAU-bench** | Task-oriented evaluation | Practical task completion |

### Holistic

| Benchmark | Coverage | Approach |
|-----------|----------|----------|
| **[[entities/helm]]** | 42 scenarios, 7 metrics | Most comprehensive academic evaluation |

## Static vs. Dynamic Benchmarks

A crucial distinction:

**Static benchmarks** (MMLU, HumanEval, TruthfulQA) use fixed test sets. They enable precise comparison but are vulnerable to contamination and gaming. Once a benchmark is published, it can appear in training data.

**Dynamic benchmarks** (LiveCodeBench, Chatbot Arena) continuously refresh. LiveCodeBench uses newly-created problems to prevent memorization. Chatbot Arena uses organic user queries that change daily. These resist contamination but make historical comparison harder.

The field is moving toward **dynamic evaluation** as the solution to [[concepts/benchmark-saturation]].

## Limitations

1. **Contamination**: Test sets frequently appear in training data
2. **Optimization**: Labs directly optimize for benchmark scores
3. **Multi-task gap**: No single benchmark captures all LLM capabilities
4. **Production gap**: Benchmark scores don't reliably predict real-world performance
5. **Cultural bias**: Most benchmarks are English-centric and Western-focused
6. **Snapshot problem**: Benchmarks capture a moment in time, not ongoing capability

## Sources

- [[sources/responsible-ai-labs-benchmarks-2025]] — comprehensive benchmark taxonomy
- [[sources/raschka-state-of-llms-2025]] — benchmark saturation and gaming analysis
- [[sources/chatbot-arena-methodology]] — crowdsourced evaluation approach

## Related Concepts

- [[concepts/benchmark-saturation]] — the crisis of benchmark reliability
- [[concepts/llm-evaluation-metrics]] — metrics used beyond benchmarks
- [[concepts/llm-as-judge]] — automated evaluation complementing benchmarks
- [[concepts/evaluation-bias]] — biases in both automated and human evaluation

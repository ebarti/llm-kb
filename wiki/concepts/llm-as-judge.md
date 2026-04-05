---
title: "LLM-as-a-Judge"
type: concept
sources: ["[[sources/cameron-wolfe-llm-as-judge]]", "[[sources/eugeneyan-llm-evaluators]]", "[[sources/confident-ai-llm-evaluation-metrics]]", "[[sources/datadog-hallucination-detection]]"]
related: ["[[concepts/llm-evaluation-metrics]]", "[[concepts/evaluation-bias]]", "[[concepts/hallucination-detection]]", "[[concepts/rag-evaluation]]", "[[concepts/faithfulness-and-groundedness]]"]
last_compiled: 2026-04-05
summary: "Using powerful LLMs (GPT-4, Claude) to evaluate outputs from other LLMs; achieves 80-85% human agreement but exhibits position, verbosity, and self-enhancement biases requiring active mitigation."
---

## Overview

LLM-as-a-Judge is a reference-free evaluation technique where a powerful language model (the "judge") assesses the quality of outputs from other LLMs. Rather than relying on traditional metrics like BLEU or ROUGE that measure surface-level text similarity, this approach directly prompts an evaluator model to rate performance using natural language reasoning.

The technique emerged following GPT-4's release and has become the **dominant paradigm** for LLM evaluation because it enables rapid iteration — requiring only prompt engineering rather than expensive human annotation campaigns. It is now standard alongside (not replacing) human evaluation.

## Three Scoring Approaches

### Pairwise Comparison
The judge receives two model outputs for the same prompt and selects the superior response. Better for relative assessment, especially on subjective tasks, but doesn't scale well (requires evaluating all output combinations). More stable than pointwise scoring because comparative judgments are easier than absolute ratings.

### Pointwise Scoring
A single response receives a numerical score, typically on a Likert scale (1-5). More scalable but inherently unstable — LLMs lack consistent internal scoring mechanisms, so absolute scores fluctuate more than comparative judgments. [[entities/g-eval]] uses chain-of-thought reasoning and optional token probability normalization to improve stability.

### Reference-Guided Scoring
The judge receives a reference solution alongside the response being evaluated. This hybrid approach improves accuracy on technical questions where there is a clear correct answer. Particularly useful for coding, math, and factual domains.

**Key implementation detail**: rationales must precede scores for meaningful explanations. When the score comes first, the explanation merely rationalizes the number.

## Effectiveness

GPT-4 achieves **80-85% agreement with human preferences**, which matches human-to-human agreement rates. However, this aggregate figure masks significant variation:

| Task | Human Agreement | LLM Agreement |
|------|----------------|---------------|
| General preference (MT-Bench) | 81% | 85% |
| General preference (Arena) | — | 83-87% |
| Summarization quality | 80-90% | 30-60% |
| Factual consistency | — | 58.5% accuracy |
| Faithfulness | — | 0.55 Spearman's rho |
| Instruction following (AlpacaEval) | — | 0.98 Spearman |

LLM judges excel at **style and format assessment** but struggle with **factual verification**. They align better with non-expert annotators than with domain experts, suggesting agreement may be inflated when annotation quality varies.

## Critical Biases

(See [[concepts/evaluation-bias]] for a dedicated deep-dive.)

### Position Bias
The judge's preference depends on where outputs appear in the prompt. One study showed a model's win-rate swinging from **2.5% to 82.5%** depending solely on position. GPT-4 favors first position; ChatGPT favors second.

### Verbosity Bias
LLM judges systematically rate longer outputs higher, regardless of content quality. Both Claude-v1 and GPT-3.5 preferred the longer response **more than 90% of the time**. This creates exploitable metrics where models can game scores by simply being verbose.

### Self-Enhancement Bias
Judges strongly prefer outputs they themselves generated. GPT-4 chose its own responses **87.76%** of the time vs 47.61% for human evaluators. Claude-v1 showed a **25% higher win rate** for self-generated content.

### Additional Weaknesses
- Struggle with questions they themselves cannot answer well
- Easily misled by factually incorrect context in responses
- Biased toward lower scores at certain temperature settings
- Less reliable on subjective characteristics (likability, cultural nuance)

## Bias Mitigation Strategies

| Strategy | What It Addresses | Effectiveness |
|----------|------------------|---------------|
| **Position switching** | Position bias | Nearly eliminates it |
| **Multiple judges** (GPT-4 + Claude + Gemini) | Self-enhancement bias | Reduces significantly |
| **Few-shot examples** | Scoring instability | Calibrates internal scoring |
| **Reference solutions** | Factual accuracy | Improves technical evaluation |
| **Length normalization** | Verbosity bias | Spearman r: 0.94 to 0.98 |
| **Binary classification** | Likert scale instability | Clearer interpretation |
| **Panel of LLMs (PoLL)** | All biases | Better correlation at 1/7th cost |
| **Cohen's kappa** | Measurement validity | More precise than % agreement |

## When to Use (and When Not To)

**Works well for:**
- General instruction-following assessment
- Dialogue and conversation quality evaluation
- Style, format, and alignment detection
- Quick development iteration (sub-minute, sub-$10)
- Multi-turn interaction evaluation

**Fails for:**
- Factuality verification (judges accept false information)
- Specialized expertise domains (complex math, domain knowledge)
- Subjective preferences (likability, aesthetics)
- Fine-grained quality distinctions
- Adversarial inputs (vulnerable to prompt injection)

## Key Frameworks

- **[[entities/g-eval]]** — Chain-of-thought scoring with probability normalization
- **[[entities/prometheus]]** — Open-source, fine-tuned on 100K GPT-4 examples
- **CriticGPT** — Specialized code critique (80-85% bug detection)
- **PoLL** — Ensemble of diverse smaller models with max voting
- **[[entities/deepeval]]** — Open-source framework with 14+ built-in metrics

## Sources

- [[sources/cameron-wolfe-llm-as-judge]] — methodology, biases, and mitigation
- [[sources/eugeneyan-llm-evaluators]] — effectiveness data and framework comparison
- [[sources/confident-ai-llm-evaluation-metrics]] — metric taxonomy including LLM-judge methods
- [[sources/datadog-hallucination-detection]] — LLM-as-judge for hallucination detection specifically

## Related Concepts

- [[concepts/evaluation-bias]] — the systematic biases in LLM-based evaluation
- [[concepts/llm-evaluation-metrics]] — the broader metric taxonomy
- [[concepts/hallucination-detection]] — a key application (and limitation) of LLM judges
- [[concepts/rag-evaluation]] — LLM judges applied to RAG-specific metrics
- [[concepts/automated-fact-checking]] — where LLM judges need supplementation

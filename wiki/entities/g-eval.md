---
title: "G-Eval"
type: entity
entity_type: paper
sources: ["[[sources/confident-ai-llm-evaluation-metrics]]", "[[sources/cameron-wolfe-llm-as-judge]]"]
related: ["[[concepts/llm-as-judge]]", "[[concepts/llm-evaluation-metrics]]", "[[entities/deepeval]]"]
last_compiled: 2026-04-05
summary: "LLM-as-a-Judge scoring method using chain-of-thought reasoning before evaluation; generates evaluation steps from task criteria, produces scores (1-5), and optionally normalizes via token probabilities for stability."
---

## Overview

G-Eval is an [[concepts/llm-as-judge]] method that uses chain-of-thought (CoT) reasoning to improve evaluation quality. Rather than asking an LLM to directly score an output, G-Eval first generates a set of evaluation steps, then uses those steps to guide scoring.

## Algorithm

1. **Generate evaluation steps** from task criteria (e.g., "evaluate coherence of this summary")
2. **Create evaluation prompt** incorporating the generated steps
3. **Produce score** (typically 1-5 Likert scale)
4. **Optionally normalize** using token probabilities for consistency

The key insight is that generating a reasoning chain before scoring produces more consistent and human-aligned evaluations than direct scoring.

## Strengths

- Correlates significantly better with human judgment than traditional metrics
- Flexible: works for subjective criteria (helpfulness, coherence, style)
- Can define custom evaluation criteria via prompt engineering
- Token probability normalization reduces scoring instability

## Limitations

- Inherits all [[concepts/evaluation-bias]] issues (position, verbosity, self-enhancement)
- Costs more than statistical metrics (requires LLM inference per evaluation)
- Scoring stability depends on temperature and prompt design

## When to Use

- Subjective quality assessment (helpfulness, coherence, tone)
- Custom evaluation criteria specific to your use case
- When traditional metrics (BLEU, ROUGE) miss important quality dimensions
- As part of the "5-Metric Rule" (1-2 custom G-Eval metrics + 2-3 generic metrics)

## Mentioned In

- [[sources/confident-ai-llm-evaluation-metrics]] — detailed algorithm description
- [[sources/cameron-wolfe-llm-as-judge]] — as a key scoring approach within LLM-as-Judge

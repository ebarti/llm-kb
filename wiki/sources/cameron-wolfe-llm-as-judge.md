---
title: "Source: Using LLMs for Evaluation (LLM-as-a-Judge)"
type: source-summary
source: "[[raw/cameron-wolfe-llm-as-judge]]"
related: ["[[concepts/llm-as-judge]]", "[[concepts/evaluation-bias]]", "[[entities/mt-bench]]", "[[entities/chatbot-arena]]"]
last_compiled: 2026-04-05
summary: "Deep dive into LLM-as-a-Judge methodology: three scoring approaches (pairwise, pointwise, reference-guided), critical biases with quantified severity, and practical mitigation strategies including position switching and length normalization."
---

## Key Points

- Three scoring approaches: pairwise comparison, pointwise scoring (Likert), and reference-guided scoring
- Position bias can swing win-rates from 2.5% to 82.5% depending on output placement
- Self-enhancement: GPT-4 chose its own responses 87.76% vs 47.61% for human evaluators
- Rationales must precede scores for meaningful explanations (chain-of-thought)
- GPT-4 achieves 80% agreement with humans, matching human-to-human rates
- Works well for instruction-following (0.98 Spearman on AlpacaEval) but fails on factuality verification
- Length normalization via regression debiasing improves Spearman r from 0.94 to 0.98

## Detailed Summary

Cameron Wolfe provides the most pedagogically clear explanation of [[concepts/llm-as-judge]] methodology. The article structures the approach around three scoring paradigms:

**Pairwise comparison** gives the judge two outputs and asks it to choose. Better for relative assessment but scales poorly (all combinations needed). **Pointwise scoring** assigns numerical scores to individual outputs — more scalable but unstable since LLMs lack consistent internal scoring mechanisms. **Reference-guided scoring** adds a correct answer, improving accuracy especially on technical domains.

The bias analysis is particularly sharp. [[concepts/evaluation-bias]] is quantified with alarming specificity: position bias alone can make a model appear to go from 2.5% to 82.5% win rate simply by changing where its output appears in the prompt. Self-enhancement bias is even more dramatic at 87.76% self-preference.

The practical mitigation section is the most actionable: position switching nearly eliminates position bias; using multiple judges (GPT-4 + Claude + Gemini) reduces self-enhancement; length normalization via regression debiasing yields Spearman improvements from 0.94 to 0.98.

## Related Concepts

- [[concepts/llm-as-judge]] — methodology detailed
- [[concepts/evaluation-bias]] — biases quantified
- [[concepts/llm-evaluation-metrics]] — broader context
- [[entities/chatbot-arena]] — crowdsourced alternative discussed

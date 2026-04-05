---
title: "Faithfulness and Groundedness"
type: concept
sources: ["[[sources/deepset-rag-groundedness]]", "[[sources/datadog-hallucination-detection]]", "[[sources/confident-ai-llm-evaluation-metrics]]"]
related: ["[[concepts/hallucination-detection]]", "[[concepts/rag-evaluation]]", "[[concepts/llm-as-judge]]", "[[concepts/hallucination-contamination]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "Faithfulness measures whether LLM outputs are factually consistent with provided context; groundedness measures the degree to which answers are supported by retrieved documents — the positive framing of 'not hallucinating.'"
---

## Overview

Faithfulness and groundedness are two closely related metrics that measure the same underlying quality: **whether an LLM's output is supported by its source material**. They represent the positive framing of what [[concepts/hallucination-detection]] measures negatively.

- **Faithfulness**: The proportion of claims in an output that can be supported by the provided context. Ranges from 0 to 1.
- **Groundedness**: The degree to which a RAG pipeline's answer is supported by the retrieved documents.

These are arguably the **most critical metrics** for [[concepts/llm-knowledge-base]] systems, where every wiki article should be grounded in the raw sources from which it was compiled.

## How Faithfulness Is Measured

### NLI-Based Approach
Natural Language Inference models classify each claim as "entailment" (supported), "contradiction" (contradicted), or "neutral" (neither). The faithfulness score is the proportion of claims classified as entailment.

Recent work introduces **PrefixNLI**, which provides entailment scoring feedback during autoregressive generation — detecting unfaithfulness as it emerges rather than after the fact.

### QAG-Based Approach (used by [[entities/deepeval]] and [[entities/ragas]])
1. Extract individual claims from the LLM output
2. For each claim, generate a yes/no question
3. Check whether the context entails a "yes" answer
4. Faithfulness = proportion of claims supported by context

### LLM-as-Judge Approach
A judge LLM directly evaluates whether each claim in the output is supported by the context. Less principled than NLI but often more accurate for complex reasoning chains.

### Rubric-Based Approach (Datadog)
Classify disagreements between context and answer as contradictions, unsupported claims, or acceptable agreements. Achieved 0.81-0.84 F1 on production benchmarks.

## Production Monitoring

[[sources/deepset-rag-groundedness]] describes a production monitoring framework:

- **Groundedness Score**: Computed for each response, tracked over time via observability dashboards
- **Document Reference Analysis**: Tracks which document positions support answers, revealing retrieval quality
- **Reference Predictor**: Decomposes responses into individual claims with source citations
- **Cost Optimization**: Analysis showed limiting retrieved docs from 10 to 6 eliminated 40% of LLM processing costs without quality loss

Monitoring across 1-60 day timeframes enables **degradation detection** before users notice quality drops.

## Faithfulness vs. Factuality

A critical distinction:

- **Faithfulness** = consistent with provided context (even if the context itself is wrong)
- **Factuality** = consistent with real-world truth

A response can be perfectly faithful to its context but factually wrong if the source material contains errors. This is why [[concepts/automated-fact-checking]] is needed in addition to faithfulness evaluation — faithfulness alone cannot catch errors in the sources themselves.

For [[concepts/llm-knowledge-base]] systems, this distinction maps to:
- **Faithfulness checking** during [[concepts/wiki-compilation]]: are wiki articles consistent with raw sources?
- **Factuality checking** during [[concepts/linting-and-health-checks]]: are the raw sources themselves accurate?

## Sources

- [[sources/deepset-rag-groundedness]] — production groundedness monitoring and cost optimization
- [[sources/datadog-hallucination-detection]] — rubric-based faithfulness evaluation
- [[sources/confident-ai-llm-evaluation-metrics]] — faithfulness as a RAG evaluation metric

## Related Concepts

- [[concepts/hallucination-detection]] — the inverse measurement (detecting unfaithfulness)
- [[concepts/rag-evaluation]] — faithfulness as a core RAG metric
- [[concepts/automated-fact-checking]] — verifying factuality beyond context faithfulness
- [[concepts/hallucination-contamination]] — the risk when unfaithful content enters the KB
- [[concepts/data-quality-bottleneck]] — source quality limits faithfulness ceiling

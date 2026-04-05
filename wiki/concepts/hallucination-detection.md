---
title: "Hallucination Detection"
type: concept
sources: ["[[sources/datadog-hallucination-detection]]", "[[sources/confident-ai-llm-evaluation-metrics]]", "[[sources/eugeneyan-llm-evaluators]]"]
related: ["[[concepts/hallucination-contamination]]", "[[concepts/faithfulness-and-groundedness]]", "[[concepts/llm-as-judge]]", "[[concepts/automated-fact-checking]]", "[[concepts/rag-evaluation]]"]
last_compiled: 2026-04-05
summary: "Methods for detecting LLM hallucinations: white-box (token probability, semantic entropy), black-box (perturbation, SLM/LLM-as-judge), and rubric-based approaches achieving 0.81-0.86 F1 on production benchmarks."
---

## Overview

Hallucination detection identifies cases where LLMs generate content that is not grounded in provided context or factual reality. This is distinct from but closely related to [[concepts/faithfulness-and-groundedness]] (which measures the degree of grounding) and [[concepts/automated-fact-checking]] (which verifies claims against external knowledge).

For [[concepts/llm-knowledge-base]] systems, hallucination detection is existential: undetected hallucinations written into wiki articles can propagate through future queries and compilations, creating [[concepts/hallucination-contamination]] that permanently corrupts the knowledge base.

## Detection Approach Taxonomy

### White-Box Methods (Require Model Internals)

| Method | How It Works | Trade-offs |
|--------|-------------|------------|
| **Token probability** | Estimates confidence from final-layer logits | Requires model access; not available for API models |
| **Attention mapping** | Identifies neural activations correlated with hallucination | Research-stage; not production-ready |
| **Semantic entropy** | Measures uncertainty by sampling multiple outputs and clustering semantically similar answers | Published in Nature (2024); unsupervised; requires multiple forward passes |

**Semantic entropy** (published in Nature, 2024) is the most principled white-box method. It generates multiple answers, clusters them by semantic similarity, and computes entropy over the clusters. High entropy indicates the model is uncertain — a strong hallucination signal. This is **unsupervised** (no labels needed) and works across tasks.

### Black-Box Methods (Input/Output Only)

| Method | How It Works | Trade-offs |
|--------|-------------|------------|
| **Perturbation-based** | Regenerates answers under varied conditions; measures consistency | 5-10x cost increase |
| **SLM-as-judge** | Small language model (BERT-style) classifies hallucinations | Limited reasoning capability |
| **LLM-as-judge** | Distinct judge model evaluates correctness | Best accuracy; relies on judge quality |
| **SelfCheckGPT** | Samples multiple responses; hallucinated content inconsistent across samples | Reference-free; moderate cost |
| **Cross-examination** | Multi-turn dialogue to reveal inconsistencies | 0.75-0.84 recall, 0.82-0.87 precision |

### Production Approaches

Datadog's rubric-based system represents the state of the art for production hallucination detection. The key insight is that "LLMs are better at guided summarization than complex reasoning." Rather than asking a judge to detect hallucinations directly, the system:

1. **Identifies disagreement claims** between context and answer
2. **Extracts quotes** from both context and answer
3. **Classifies disagreements** as contradictions, unsupported claims, or acceptable agreements

Technical enhancements include:
- **Structured output** via finite state machines ensuring JSON compliance
- **Two-stage prompting**: unrestricted chain-of-thought, then structured reformatting
- **Semantic framing**: context as "expert advice," answer as "candidate answer"

## Benchmark Results

| Benchmark | Best Method | F1 Score |
|-----------|------------|----------|
| HaluBench (n=14,900) | Patronus/GPT-4o | 0.862 |
| HaluBench | Datadog/GPT-4o | 0.844 |
| RAGTruth (n=2,700) | Datadog/GPT-4o | 0.810 |
| RAGTruth | Patronus/GPT-4o | 0.777 |

Key finding: Datadog's rubric-based method shows the **smallest F1 drop** between easy and hard benchmarks, indicating robustness when hallucinations are subtler and harder to detect.

## Critical Limitation

A recent EMNLP finding revealed that **ROUGE-based evaluation systematically overestimates hallucination detection performance**, with some methods showing performance drops of up to **45.9% AUROC** when evaluated with human-aligned metrics instead of ROUGE. This means many published hallucination detection results are more optimistic than actual performance.

## Application to LLM Knowledge Bases

For [[concepts/llm-knowledge-base]] systems:

1. **Compile-time detection**: Run hallucination detection on every article during [[concepts/wiki-compilation]] to catch fabricated claims before they enter the wiki
2. **Cross-source validation**: Compare claims across multiple sources to identify unsupported assertions
3. **Continuous monitoring**: Re-check existing articles periodically, especially after model updates
4. **Layered approach**: Combine SelfCheckGPT (reference-free, catches generation-time hallucinations) with rubric-based checking (catches context-grounding failures)

## Sources

- [[sources/datadog-hallucination-detection]] — production rubric-based approach with benchmark results
- [[sources/confident-ai-llm-evaluation-metrics]] — SelfCheckGPT and other detection metrics
- [[sources/eugeneyan-llm-evaluators]] — effectiveness data for LLM-based detection

## Related Concepts

- [[concepts/hallucination-contamination]] — the risk when hallucinations go undetected
- [[concepts/faithfulness-and-groundedness]] — the positive measure (opposite of hallucination)
- [[concepts/automated-fact-checking]] — external fact verification beyond context grounding
- [[concepts/llm-as-judge]] — the evaluation paradigm used for detection
- [[concepts/data-quality-bottleneck]] — hallucinations as a data quality issue

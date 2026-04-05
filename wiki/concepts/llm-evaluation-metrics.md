---
title: "LLM Evaluation Metrics"
type: concept
sources: ["[[sources/confident-ai-llm-evaluation-metrics]]", "[[sources/eugeneyan-llm-evaluators]]", "[[sources/evidentlyai-llm-evaluation-guide]]", "[[sources/responsible-ai-labs-benchmarks-2025]]"]
related: ["[[concepts/llm-as-judge]]", "[[concepts/rag-evaluation]]", "[[concepts/faithfulness-and-groundedness]]", "[[concepts/hallucination-detection]]", "[[concepts/benchmark-saturation]]", "[[concepts/evaluation-bias]]", "[[concepts/llm-benchmarks]]"]
last_compiled: 2026-04-05
summary: "Taxonomy of metrics for evaluating LLM output quality: statistical scorers (BLEU, ROUGE, BERTScore), LLM-as-a-Judge methods (G-Eval, QAG), and domain-specific metrics for RAG, agents, safety, and factuality."
---

## Overview

LLM evaluation metrics quantify the quality of language model outputs across multiple dimensions: correctness, relevance, factual accuracy, safety, and helpfulness. The field has evolved from simple n-gram overlap measures to sophisticated LLM-based evaluation, reflecting the increasing complexity of what LLMs are asked to do.

The fundamental challenge is that LLMs are **multi-task systems** — they handle translation, summarization, coding, math, brainstorming, and open-ended conversation simultaneously. No single metric captures all dimensions of quality, and the right evaluation strategy depends on the specific use case.

## Metric Taxonomy

### Tier 1: Statistical Scorers

The oldest and simplest metrics measure surface-level text similarity:

| Metric | What It Measures | How It Works | Limitations |
|--------|-----------------|--------------|-------------|
| **BLEU** | N-gram precision | Compares n-gram overlap with brevity penalty | No semantic understanding |
| **ROUGE** | N-gram recall | Measures recall via n-gram overlap proportions (0-1) | Misses paraphrases |
| **METEOR** | Precision + recall | Adds synonym matching via WordNet | Still surface-level |
| **Levenshtein** | Edit distance | Counts minimum character edits | Character-level only |

These are fast and deterministic but "perform poorly whenever reasoning is required." They remain useful as **sanity checks** and for **regression testing** where outputs should be similar across versions.

### Tier 2: Model-Based Scorers (Non-LLM)

Neural models provide deeper semantic understanding:

| Metric | What It Measures | How It Works |
|--------|-----------------|--------------|
| **BERTScore** | Semantic similarity | Cosine similarity between contextual embeddings |
| **BLEURT** | Learned quality | BERT-based pre-trained quality estimator |
| **NLI** | Entailment | Classifies output as entailment/contradiction/neutral |
| **MoverScore** | Distribution distance | Earth Mover's Distance between word distributions |

BERTScore captures meaning beyond surface overlap — "the cat sat on the mat" and "a feline rested on the rug" score high despite zero n-gram overlap. However, these models struggle with lengthy texts and are limited by training data.

A May 2025 study found BERTScore averaged 0.75 on summarization tasks vs 0.65 for ROUGE, confirming its semantic advantage.

### Tier 3: LLM-as-a-Judge Methods

The state of the art uses powerful LLMs as evaluators (see [[concepts/llm-as-judge]] for details):

| Method | How It Works | Best For |
|--------|-------------|----------|
| **[[entities/g-eval]]** | Chain-of-thought reasoning before scoring (1-5 scale) | Subjective criteria |
| **DAG** | Decision-tree of LLM judgments | Clear success criteria |
| **QAG** | Extract claims, ask binary questions | Objective evaluation |
| **[[entities/prometheus]]** | Open-source, fine-tuned on 100K GPT-4 examples | Cost-effective evaluation |
| **SelfCheckGPT** | Sample consistency for hallucination detection | Reference-free detection |

LLM-as-a-Judge methods "correlate significantly better with human judgment" than traditional metrics. GPT-4 achieves 80-85% agreement with human experts, matching human-to-human agreement rates.

### Domain-Specific Metrics

**RAG Metrics** (see [[concepts/rag-evaluation]]):
- Faithfulness, answer relevancy, contextual precision/recall/relevancy

**Agent Metrics**:
- Task completion, tool correctness, argument correctness, plan quality, step efficiency

**Safety Metrics**:
- Toxicity (via Detoxify or [[entities/g-eval]]), bias detection, harm assessment

**Factuality Metrics** (see [[concepts/automated-fact-checking]]):
- Claim-level verification, factual consistency, [[concepts/faithfulness-and-groundedness]]

## The 5-Metric Rule

A practical guideline from [[sources/confident-ai-llm-evaluation-metrics]]:
- **1-2 custom metrics** (G-Eval or DAG) targeting your specific use case
- **2-3 generic metrics** matching your system architecture (RAG, agentic, conversational)

This balances comprehensiveness with evaluation efficiency.

## Seven Evaluation Dimensions

[[sources/responsible-ai-labs-benchmarks-2025]] identifies seven dimensions for holistic LLM assessment:

1. **Accuracy & Knowledge** — factual correctness, domain expertise
2. **Safety & Harm Prevention** — toxicity avoidance, jailbreak resistance
3. **Fairness & Bias** — demographic bias, stereotyping
4. **Robustness** — adversarial resilience
5. **Calibration & Uncertainty** — confidence alignment
6. **Efficiency** — latency, cost, token usage
7. **Alignment & Helpfulness** — instruction following, conversational coherence

## Relevance to LLM Knowledge Bases

For [[concepts/llm-knowledge-base]] systems, the most critical metrics are:

- **[[concepts/faithfulness-and-groundedness]]** — are wiki articles grounded in source material?
- **[[concepts/hallucination-detection]]** — are there fabricated claims? (see [[concepts/hallucination-contamination]])
- **Factual consistency** — do articles contradict each other or their sources?
- **Completeness** — are key concepts from sources adequately covered?
- **Currency** — is information up-to-date?

These map directly to the [[concepts/linting-and-health-checks]] operations in the KB maintenance cycle.

## Sources

- [[sources/confident-ai-llm-evaluation-metrics]] — comprehensive metric taxonomy and the 5-Metric Rule
- [[sources/eugeneyan-llm-evaluators]] — effectiveness data for LLM-based evaluation
- [[sources/evidentlyai-llm-evaluation-guide]] — practical evaluation workflow
- [[sources/responsible-ai-labs-benchmarks-2025]] — seven evaluation dimensions

## Related Concepts

- [[concepts/llm-as-judge]] — the dominant modern evaluation paradigm
- [[concepts/evaluation-bias]] — systematic biases in LLM-based evaluation
- [[concepts/llm-benchmarks]] — standardized benchmark datasets
- [[concepts/benchmark-saturation]] — the crisis of benchmark reliability
- [[concepts/rag-evaluation]] — evaluation specific to RAG systems
- [[concepts/hallucination-detection]] — detecting fabricated content
- [[concepts/evaluation-workflow]] — how to set up evaluation pipelines

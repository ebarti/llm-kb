---
title: "Source: LLM Evaluation Metrics — The Ultimate Guide"
type: source-summary
source: "[[raw/confident-ai-llm-evaluation-metrics]]"
related: ["[[concepts/llm-evaluation-metrics]]", "[[concepts/llm-as-judge]]", "[[concepts/faithfulness-and-groundedness]]", "[[concepts/rag-evaluation]]", "[[entities/deepeval]]", "[[entities/g-eval]]"]
last_compiled: 2026-04-05
summary: "Comprehensive taxonomy of LLM evaluation metrics: statistical scorers (BLEU, ROUGE), model-based (BERTScore, NLI), LLM-as-a-Judge (G-Eval, DAG, QAG), and domain-specific RAG/agent metrics."
---

## Key Points

- LLM evaluation metrics fall into three tiers: statistical scorers (BLEU, ROUGE, METEOR), model-based scorers (BERTScore, NLI, BLEURT), and LLM-as-a-Judge methods (G-Eval, DAG, QAG)
- Statistical methods "perform poorly whenever reasoning is required" and are inadequate for complex LLM evaluation
- LLM-as-a-Judge approaches correlate significantly better with human judgment than traditional metrics
- The "5-Metric Rule" recommends 1-2 custom metrics plus 2-3 generic metrics matching your system architecture
- RAG-specific metrics include faithfulness, answer relevancy, contextual precision, contextual recall, and contextual relevancy
- Agent-specific metrics now cover task completion, tool correctness, plan quality, and step efficiency

## Detailed Summary

The guide from Confident AI (makers of [[entities/deepeval]]) provides the most comprehensive taxonomy of LLM evaluation metrics available. It organizes metrics into a clear hierarchy:

**Statistical scorers** (BLEU, ROUGE, METEOR, Levenshtein) are the simplest but least capable. They measure surface-level text overlap and struggle with semantic understanding. ROUGE calculates recall via n-gram overlap; BLEU measures precision with brevity penalties; METEOR adds synonym matching via WordNet.

**Model-based scorers** (NLI, BERTScore, BLEURT, MoverScore) use neural models for deeper semantic comparison. BERTScore computes cosine similarity between contextual embeddings, capturing meaning beyond surface overlap. However, these struggle with lengthy texts.

**LLM-as-a-Judge methods** represent the state of the art. [[entities/g-eval]] uses chain-of-thought reasoning before scoring, generating evaluation steps from task criteria. DAG provides decision-tree-based deterministic evaluation. QAG extracts claims and asks binary questions, avoiding arbitrary LLM-generated scores. [[entities/prometheus]] is an open-source alternative fine-tuned on 100K GPT-4 feedback samples. [[concepts/selfcheckgpt]] enables reference-less [[concepts/hallucination-detection]] via sampling consistency.

For [[concepts/rag-evaluation]], the guide defines five core metrics: **faithfulness** (truthful claims relative to context), **answer relevancy** (conciseness), **contextual precision** (relevant context ranking), **contextual recall** (expected content coverage), and **contextual relevancy** (relevant sentence proportion).

## Notable Quotes

> "Statistical methods performs poorly whenever reasoning is required."

> "Great evaluation metrics are: Quantitative... Reliable... Accurate."

## Related Concepts

- [[concepts/llm-evaluation-metrics]] — the central taxonomy this article defines
- [[concepts/llm-as-judge]] — the dominant modern evaluation paradigm
- [[concepts/rag-evaluation]] — RAG-specific evaluation metrics
- [[concepts/faithfulness-and-groundedness]] — core quality dimension for RAG systems
- [[entities/deepeval]] — the open-source framework implementing these metrics

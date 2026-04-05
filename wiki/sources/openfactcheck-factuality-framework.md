---
title: "Source: OpenFactCheck — Unified Factuality Evaluation"
type: source-summary
source: "[[raw/openfactcheck-factuality-framework]]"
related: ["[[concepts/automated-fact-checking]]", "[[concepts/hallucination-detection]]", "[[entities/openfactcheck]]"]
last_compiled: 2026-04-05
summary: "OpenFactCheck unifies LLM factuality evaluation with three modules: ResponseEvaluator (claim-level fact-checking), LLMEvaluator (FactQA dataset, 6,480 examples), and FactCheckerEvaluator (FactBench, 4,507 human-annotated examples)."
---

## Key Points

- Addresses the problem that different papers use different evaluation benchmarks, making comparison difficult
- Three-step Response Evaluator pipeline: claim processing, evidence retrieval, verification
- Supports mixing components from RARR, FacTool, FactCheckGPT via YAML configuration
- FactQA dataset: 6,480 examples across 482 domains from seven sources
- FactBench: 4,507 human-annotated examples for evaluating fact-checking systems
- Available as pip install and web dashboard

## Detailed Summary

[[entities/openfactcheck]] addresses a meta-problem in [[concepts/automated-fact-checking]]: the lack of standardized evaluation. Different papers use different benchmarks, making it impossible to compare approaches fairly.

The three-module architecture is elegant. The **Response Evaluator** decomposes LLM outputs into individual claims, retrieves evidence for each, and verifies accuracy — a modular pipeline where users can mix claim processors, retrievers, and verifiers from different systems. The **LLM Evaluator** provides the FactQA dataset spanning 482 domains, combining questions from Snowball, SelfAware, FreshQA, and other sources. The **Fact Checker Evaluator** uses FactBench to assess the fact-checking systems themselves, creating a meta-evaluation layer.

This framework is particularly relevant for [[concepts/llm-knowledge-base]] quality assessment: it provides a principled way to measure whether an LLM-generated knowledge base contains factual content, decomposing the problem into claim-level verification rather than holistic quality judgments.

## Related Concepts

- [[concepts/automated-fact-checking]] — the domain this tool addresses
- [[concepts/hallucination-detection]] — closely related capability
- [[concepts/faithfulness-and-groundedness]] — what fact-checking ultimately measures
- [[concepts/llm-knowledge-base]] — a key application domain

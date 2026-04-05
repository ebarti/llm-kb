---
title: "Source: Large Language Models Hallucination — A Comprehensive Survey"
type: source-summary
source: "[[raw/llm-hallucination-comprehensive-survey]]"
related: ["[[concepts/llm-hallucination]]", "[[concepts/hallucination-contamination]]", "[[concepts/ai-safety]]", "[[concepts/rag-vs-index-based-retrieval]]"]
last_compiled: 2026-04-05
summary: "Exhaustive 2025 survey by Alansari & Luqman covering hallucination taxonomy, causes across the full LLM lifecycle, 5 detection approaches, and 4 mitigation categories."
---

## Key Points
- Defines hallucinations as fluent text that is factually inaccurate or unsupported by evidence
- Classifies causes across 6 stages: data curation, architecture, pre-training, fine-tuning, evaluation, inference
- Identifies 5 detection families: retrieval-based, uncertainty-based, embedding-based, learning-based, self-consistency
- Proposes 4 mitigation categories: prompt-based, retrieval-based, reasoning-based, model-centric
- Key finding: no single approach eliminates hallucination; complementary combinations show greatest promise

## Detailed Summary

This survey provides the most comprehensive taxonomy of LLM hallucinations available. It distinguishes **intrinsic** hallucinations (contradicting source documents) from **extrinsic** hallucinations (introducing unverified content), and **factuality** errors (wrong real-world facts) from **faithfulness** errors (drifting from input).

Critical causes include sycophantic behavior during fine-tuning (generating responses evaluators will approve regardless of accuracy), capability misalignment (alignment training encouraging definitive answers despite insufficient knowledge), and exposure bias from teacher forcing during pre-training.

Detection approaches range from span-level retrieval verification (FAVA, KnowHalu) through semantic entropy and belief tree propagation to self-consistency methods like SelfCheckGPT and MetaQA.

Mitigation spans the full spectrum from prompt engineering (Chain-of-Thought, in-context learning) through knowledge graph grounding (ERNIE 3.0, KGLM) to model-centric contrastive learning and hallucination-aware fine-tuning.

## Notable Quotes
> "No single approach completely eliminates hallucination; complementary combinations show greatest promise."

## Related Concepts
- [[concepts/llm-hallucination]] — the core phenomenon surveyed
- [[concepts/hallucination-contamination]] — downstream risk when hallucinations enter knowledge bases
- [[concepts/ai-content-verification]] — detection methods described here
- [[concepts/grounding-and-faithfulness]] — retrieval and KG-based mitigation approaches

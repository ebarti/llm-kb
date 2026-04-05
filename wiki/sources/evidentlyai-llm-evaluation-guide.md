---
title: "Source: LLM Evaluation — A Beginner's Guide"
type: source-summary
source: "[[raw/evidentlyai-llm-evaluation-guide]]"
related: ["[[concepts/llm-evaluation-metrics]]", "[[concepts/evaluation-workflow]]", "[[concepts/llm-as-judge]]"]
last_compiled: 2026-04-05
summary: "Evidently AI's practical evaluation framework: distinguishes model vs product evaluation, defines six evaluation scenarios (experiments, stress-testing, red-teaming, production monitoring, regression, guardrails), and provides a phased implementation workflow."
---

## Key Points

- Distinguishes LLM model evaluations (raw capabilities) from LLM product evaluations (system performance)
- Six evaluation scenarios: comparative experiments, stress testing, red-teaming, production observability, regression testing, guardrails
- Automated evaluation splits into reference-based (ground truth) and reference-free (no ground truth)
- Five-phase implementation: foundation, development, pre-launch, production, iteration
- "Each LLM product requires tailored evaluation criteria" — no one-size-fits-all approach
- Manual and automated methods work hand-in-hand; human judgment defines success criteria, automation scales insights

## Detailed Summary

Evidently AI's guide provides the most practical, workflow-oriented framework for [[concepts/evaluation-workflow]]. Where other sources focus on individual metrics, this guide addresses the meta-question: **how do you set up an evaluation pipeline from scratch?**

The key distinction between **model evaluation** (comparing raw LLM capabilities with benchmarks like MMLU) and **product evaluation** (assessing your full system on your specific tasks) is foundational. Most teams over-invest in the former and under-invest in the latter.

The six evaluation scenarios map to the LLM product lifecycle: **comparative experiments** during development, **stress testing** and **red-teaming** pre-launch, **production observability** post-launch, and **regression testing** before updates. **Guardrails** operate continuously at runtime (PII detection, unsafe content blocking).

The phased implementation workflow is particularly valuable: start by defining success criteria and creating evaluation datasets (Phase 1), run automated experiments (Phase 2), expand to edge cases (Phase 3), deploy production monitoring (Phase 4), then continuously iterate (Phase 5).

## Related Concepts

- [[concepts/evaluation-workflow]] — the phased approach this article defines
- [[concepts/llm-evaluation-metrics]] — metrics used within each phase
- [[concepts/llm-as-judge]] — the primary automated evaluation method
- [[concepts/hallucination-detection]] — a key capability evaluated

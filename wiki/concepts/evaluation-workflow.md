---
title: "Evaluation Workflow"
type: concept
sources: ["[[sources/evidentlyai-llm-evaluation-guide]]", "[[sources/confident-ai-llm-evaluation-metrics]]"]
related: ["[[concepts/llm-evaluation-metrics]]", "[[concepts/llm-as-judge]]", "[[concepts/hallucination-detection]]", "[[concepts/rag-evaluation]]", "[[concepts/linting-and-health-checks]]"]
last_compiled: 2026-04-05
summary: "A phased approach to LLM evaluation: define success criteria, build evaluation datasets, run automated experiments, stress-test and red-team, deploy production monitoring, and continuously iterate."
---

## Overview

An evaluation workflow is a structured process for assessing LLM system quality across the product lifecycle. Unlike individual [[concepts/llm-evaluation-metrics]], which measure specific quality dimensions, the evaluation workflow addresses the meta-question: **how do you set up and maintain an evaluation pipeline from scratch?**

The key insight from [[sources/evidentlyai-llm-evaluation-guide]] is that "each LLM product requires tailored evaluation criteria" — there is no one-size-fits-all approach.

## Model Evaluation vs. Product Evaluation

A foundational distinction:

| Dimension | Model Evaluation | Product Evaluation |
|-----------|-----------------|-------------------|
| **What** | Raw LLM capabilities | Full system performance |
| **How** | Standardized [[concepts/llm-benchmarks]] | Custom evaluation on your tasks |
| **When** | Model selection | Throughout product lifecycle |
| **Metrics** | MMLU, HumanEval, etc. | Faithfulness, task completion, etc. |
| **Gap** | Academic performance | Real-world performance |

Most teams over-invest in model evaluation and under-invest in product evaluation.

## Five-Phase Implementation

### Phase 1: Foundation
1. **Define success criteria** for your specific use case
2. **Create evaluation datasets**: manual curation from real examples, synthetic data for edge cases, production log samples
3. **Establish baseline performance** using current system (or manual process)

### Phase 2: Development
1. **Run comparative experiments** with test datasets
2. **Implement automated evaluation** matching methods
3. **Track progress** with quantitative metrics
4. **Manual spot-checks** for calibration (verify automated metrics align with human judgment)

### Phase 3: Pre-Launch
1. **Expand coverage** to edge cases
2. **Stress testing** across scenarios (unusual inputs, languages, typos)
3. **Red-teaming** for safety (prompt injection, jailbreaks)
4. **Implement guardrails** for critical risks (PII detection, unsafe content blocking)

### Phase 4: Production
1. **Set up trace collection** (inputs and outputs)
2. **Deploy online evaluations** (sampling-based [[concepts/llm-as-judge]])
3. **Monitor key metrics** continuously
4. **Regular manual reviews** for calibration
5. **A/B testing** for improvements

### Phase 5: Iteration
1. **Fix based on failures** discovered in production
2. **Regression testing** before updates
3. **Refresh datasets** with new patterns from production
4. **Refine evaluation criteria** as understanding deepens

## Six Evaluation Scenarios

| Scenario | When | Purpose |
|----------|------|---------|
| **Comparative experiments** | Development | Model selection, prompt engineering |
| **Stress testing** | Pre-launch | Edge cases, robustness |
| **Red-teaming** | Pre-launch | Safety, adversarial resilience |
| **Production observability** | Post-launch | Continuous quality monitoring |
| **Regression testing** | Before updates | Prevent capability degradation |
| **Guardrails** | Runtime | Real-time safety filtering |

## Application to LLM Knowledge Bases

For [[concepts/llm-knowledge-base]] systems, the evaluation workflow maps to:

| Phase | KB Equivalent |
|-------|--------------|
| Foundation | Define what makes a "good" wiki article; create reference articles |
| Development | Test compilation pipeline on sample sources |
| Pre-Launch | Stress-test with diverse source types; red-team with adversarial sources |
| Production | [[concepts/linting-and-health-checks]] as continuous monitoring |
| Iteration | Update compilation prompts based on detected failures |

The [[concepts/linting-and-health-checks]] operation in this KB is essentially Phase 4 (production monitoring) applied to wiki content.

## Sources

- [[sources/evidentlyai-llm-evaluation-guide]] — five-phase workflow and six evaluation scenarios
- [[sources/confident-ai-llm-evaluation-metrics]] — the 5-Metric Rule for evaluation efficiency

## Related Concepts

- [[concepts/llm-evaluation-metrics]] — metrics used within the workflow
- [[concepts/llm-as-judge]] — primary automated evaluation method
- [[concepts/linting-and-health-checks]] — KB-specific continuous evaluation
- [[concepts/rag-evaluation]] — RAG-specific evaluation within the workflow

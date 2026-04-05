---
title: "LLM Evaluation: A Beginner's Guide"
source: "https://www.evidentlyai.com/llm-guide/llm-evaluation"
author: "Evidently AI"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [llm-evaluation, framework, production-monitoring, evaluation-workflow, best-practices]
type: article
status: raw
discovered_via: search
---

# LLM Evaluation: Complete Framework

## Types of Evaluation

### LLM Model Evaluations
Focus on raw LLM capabilities (coding, translation, reasoning) using standardized benchmarks like MMLU. Compare models directly but don't assess real-world product performance.

### LLM Product Evaluations
Assess full system performance on specific tasks including prompts, integrations, and knowledge bases. Two dimensions:
- **Capabilities**: Can the system perform its intended function well?
- **Safety**: Could outputs cause harm?

## Evaluation Methods

### Manual Approaches
- **Vibe checks**: Initial informal review
- **Formal labeling**: Structured annotation with clear rubrics
- **Multiple reviewers**: Consensus-based grading

### Automated — With Ground Truth (Reference-based)
- Exact match, word/item match, semantic similarity, n-gram overlap (BLEU, ROUGE, METEOR), LLM-as-a-judge

### Automated — Without Ground Truth (Reference-free)
- LLM judges with rubrics, ML models (sentiment, toxicity), semantic similarity, regex, format validation, text statistics

## Evaluation Scenarios

1. **Comparative Experiments**: Model selection, prompt engineering, baseline establishment
2. **Stress Testing**: Edge cases, robustness, coverage expansion
3. **Red-Teaming**: Prompt injection, jailbreaks, safety guardrails
4. **Production Observability**: Real-time monitoring, user feedback, A/B testing
5. **Regression Testing**: Validating updates don't break functionality
6. **Guardrails**: Real-time PII detection, unsafe request blocking

## Practical Setup Workflow

- Phase 1: Define success criteria, create evaluation datasets, establish baselines
- Phase 2: Run experiments, implement automated evaluation, track progress
- Phase 3: Expand to edge cases, stress-test, red-team, implement guardrails
- Phase 4: Set up traces, deploy online evaluations, monitor continuously
- Phase 5: Fix based on failures, run regressions, refresh datasets

## Best Practices

- Each LLM product requires tailored evaluation criteria
- Prioritize discriminative metrics that reveal performance differences
- Combine manual reviews with automated scoring
- Continuously update datasets from production
- Reserve held-out data to prevent overfitting
- Focus on highest-stakes failure modes
- Validate automated evaluators against manual labels

---
title: "Source: When Benchmarks Lie — Why Contamination Breaks LLM Evaluation"
type: source-summary
source: "[[raw/benchmark-data-contamination]]"
related: ["[[concepts/benchmark-contamination]]", "[[concepts/training-data-curation]]", "[[concepts/data-deduplication]]"]
last_compiled: 2026-04-05
summary: "Analysis of the fidelity-resistance tradeoff in benchmark contamination: no mitigation strategy achieves both high resistance to memorization and high fidelity to the original evaluation task."
---

## Key Points

- Data contamination: benchmark datasets leak into training corpora, inflating scores
- Public benchmarks (MMLU, ARC-Challenge, TruthfulQA, GSM8K) are freely available on the web and likely in training data
- Fundamental fidelity-resistance tradeoff: surface edits maintain fidelity but fail to prevent memorization; deep transformations block contamination but distort the task
- Single transformations: ~0.90 fidelity but zero resistance
- Combined strategies (MPA): ~0.89 resistance but 0.686 fidelity
- Semantic-altering: >0.95 resistance but 0.66-0.75 fidelity
- Previous evaluations using accuracy drop metrics were "over-optimistic"
- LessLeak-Bench and Inference-Time Decontamination (ITD) as emerging solutions

## Detailed Summary

This source provides the most rigorous framework for understanding why benchmark contamination is so difficult to solve. The key contribution is formalizing the tradeoff between fidelity (does the modified benchmark still test the same capability?) and resistance (does the modification prevent contaminated models from cheating?).

The findings are sobering: no existing strategy lands in the desirable quadrant of high fidelity AND high resistance. This means that any benchmark result on a publicly available evaluation should be interpreted with caution. The DCLM paper's approach of removing detected overlaps and showing performance improvement (rather than degradation) is one of the few ways to build confidence that gains are genuine.

## Related Concepts

- [[concepts/benchmark-contamination]] — this is the primary source for the concept
- [[concepts/training-data-curation]] — decontamination as a curation step
- [[concepts/data-deduplication]] — overlap detection between training and evaluation data

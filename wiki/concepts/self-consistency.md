---
title: "Self-Consistency"
type: concept
sources: ["[[sources/raschka-state-of-reasoning-inference]]", "[[sources/snell-test-time-compute-scaling]]"]
related: ["[[concepts/chain-of-thought]]", "[[concepts/test-time-compute]]", "[[concepts/llm-reasoning]]", "[[concepts/process-reward-models]]"]
last_compiled: 2026-04-05
summary: "A reasoning enhancement technique that samples multiple chain-of-thought solutions to the same problem and selects the most frequent answer via majority voting, improving accuracy on arithmetic and commonsense reasoning benchmarks."
---

## Overview

Self-consistency (Wang et al., 2023) is a follow-up to [[concepts/chain-of-thought|chain-of-thought]] prompting that improves reasoning by sampling multiple solutions and taking the majority vote. The intuition: if a model arrives at the same answer via different reasoning paths, that answer is more likely correct.

## How It Works

1. For a given problem, sample N chain-of-thought completions (e.g., N=64) using temperature sampling.
2. Extract the final answer from each completion.
3. Return the most frequent answer (the mode / plurality vote).

This is equivalent to a plurality vote across the sampled outputs, selecting the empirical mode of the LLM's answer distribution.

## Why It Works

- Different reasoning paths may make different errors, but correct reasoning paths tend to converge on the same answer.
- Majority voting averages out random errors in individual reasoning chains.
- It exploits the diversity of the model's sampling distribution.

## Performance

- Consistently improves over single-sample CoT on arithmetic, commonsense, and symbolic reasoning benchmarks.
- Standard self-consistency requires ~18.6 sampled responses on average.
- Recent improvements (ranked voting, confidence-weighted voting) match the same accuracy with only ~10 samples -- a 46% reduction in compute.

## Relationship to Test-Time Compute

Self-consistency is the simplest form of [[concepts/test-time-compute|parallel test-time compute scaling]]: spend N times the compute to get a better answer. More sophisticated approaches replace majority voting with [[concepts/process-reward-models|process reward model]] selection, which can select higher-quality answers from fewer samples.

## Recent Advances

- **Ranked voting**: Incorporates ranking information among candidate answers, outperforming simple majority voting.
- **Confidence-weighted voting**: Weight votes by model confidence scores.
- **Dynamic self-consistency**: Adaptively determine how many samples to generate based on agreement level.
- **Certified self-consistency**: Provides statistical guarantees on output quality.

## Sources

- [[sources/raschka-state-of-reasoning-inference]] -- self-consistency as a parallel scaling technique
- [[sources/snell-test-time-compute-scaling]] -- self-consistency vs. compute-optimal approaches

## Related Concepts

- [[concepts/chain-of-thought]] -- the base technique self-consistency builds on
- [[concepts/test-time-compute]] -- self-consistency as the simplest form of parallel scaling
- [[concepts/process-reward-models]] -- a more sophisticated alternative to majority voting
- [[concepts/reasoning-models]] -- models that incorporate self-verification internally

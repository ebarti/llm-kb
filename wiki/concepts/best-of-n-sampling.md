---
title: "Best-of-N Sampling"
type: concept
sources: ["[[sources/wu-inference-scaling-laws]]", "[[sources/snell-test-time-compute-scaling]]", "[[sources/zhang-test-time-scaling-survey]]", "[[sources/agarwal-art-of-scaling-test-time-compute]]"]
related: ["[[concepts/test-time-compute]]", "[[concepts/process-reward-models]]", "[[concepts/self-consistency]]", "[[concepts/adaptive-compute-allocation]]", "[[concepts/inference-scaling-laws]]"]
last_compiled: 2026-04-05
summary: "The fundamental parallel test-time scaling technique: generate N candidate solutions, select the best via a verifier or reward model -- simple but effective, serving as the baseline against which all other inference scaling methods are measured."
---

## Overview

Best-of-N (BoN) sampling is the most straightforward parallel [[concepts/test-time-compute]] technique: generate N independent solutions to a problem, then select the best one using a verifier (typically a [[concepts/process-reward-models|process reward model]] or outcome reward model). It is the baseline against which all more sophisticated inference scaling methods are compared.

## How It Works

1. **Generate**: Sample N complete solutions from the LLM with temperature > 0.
2. **Score**: Evaluate each solution with a reward/verifier model.
3. **Select**: Return the highest-scoring solution.

Variants include majority voting (no verifier, just consensus), weighted voting (weight by model confidence), and pass@k (report whether any of k samples is correct).

## Scaling Properties

BoN scales inference compute linearly with N, but accuracy improvements follow a roughly logarithmic curve -- doubling N does not double accuracy. [[sources/wu-inference-scaling-laws|Wu et al. (ICLR 2025)]] establish formal scaling relationships.

Key finding: **compute-optimal BoN favors scaling solution generation over scaling verification** ([[sources/wu-inference-scaling-laws]]). The bottleneck is solution diversity, not verification quality.

## When BoN Beats More Complex Methods

- Verifier-guided search (PRM + beam search) initially outperforms BoN by 20%+ at N=1, but this advantage erodes and inverts by N=16-32. At large N, simple repeated sampling catches up.
- BoN is embarrassingly parallel -- all N samples can be generated simultaneously.
- BoN requires no search infrastructure (no tree maintenance, no backtracking).

## When More Complex Methods Beat BoN

- For small compute budgets (N < 16), PRM-guided search significantly outperforms BoN.
- Sequential methods (extended CoT, beam search) can achieve better per-token efficiency.
- [[concepts/mcts-llm-reasoning|MCTS]] enables structured exploration that random sampling cannot.

## Co-Scaling Laws

Recent research identifies a co-scaling law for BoN that jointly optimizes:
- **Temperature**: Higher temperature increases diversity but reduces per-sample quality.
- **Sample size N**: More samples improve selection quality but increase compute.
- Inference-aware fine-tuning trains LLMs specifically to generate diverse, high-quality outputs for BoN inference.

## Relationship to T2 Scaling

[[sources/roberts-train-to-test-scaling-laws|Roberts et al. (2026)]] use pass@k modeling for their T2 scaling laws, showing that when BoN is the deployment strategy, optimal training shifts toward heavily overtraining smaller models.

## Sources

- [[sources/wu-inference-scaling-laws]] -- formal scaling relationships for BoN
- [[sources/snell-test-time-compute-scaling]] -- BoN as baseline for compute-optimal comparison
- [[sources/zhang-test-time-scaling-survey]] -- BoN in the TTS taxonomy (parallel scaling)
- [[sources/agarwal-art-of-scaling-test-time-compute]] -- empirical BoN results at scale

## Related Concepts

- [[concepts/test-time-compute]] -- the paradigm BoN instantiates
- [[concepts/process-reward-models]] -- the verifiers used to select the best sample
- [[concepts/self-consistency]] -- majority voting variant of BoN
- [[concepts/adaptive-compute-allocation]] -- choosing N based on difficulty
- [[concepts/inference-scaling-laws]] -- the scaling relationships BoN follows

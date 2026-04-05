---
title: "Reward Model"
type: concept
sources: ["[[sources/wolfe-reward-models-llm]]", "[[sources/huggingface-rlhf-illustrated]]", "[[sources/lilianweng-reward-hacking]]"]
related: ["[[concepts/rlhf]]", "[[concepts/bradley-terry-model]]", "[[concepts/preference-data]]", "[[concepts/reward-hacking]]", "[[concepts/process-reward-model]]", "[[concepts/dpo]]"]
last_compiled: 2026-04-05
summary: "A learned preference function -- typically an LLM with a linear head producing scalar scores -- trained on human preference data to serve as the optimization target in RLHF, bridging human judgments and RL training signals."
---

## Overview

A reward model (RM) is the critical bridge between human preferences and RL training in [[concepts/rlhf]]. It learns to predict which outputs humans would prefer, converting subjective human judgments into a scalar signal that reinforcement learning can optimize against.

Conceptually, think of it as a "learned preference function": where a language model predicts words, a reward model predicts human approval.

## Architecture

Reward models are repurposed LLMs with a modified output layer:
- **Base**: Standard LLM decoder architecture
- **Modification**: Replace the language modeling head with a linear classification head
- **Output**: The final token's hidden state passes through the linear head to produce a single scalar score
- **Initialization**: Parameters typically drawn from the SFT model (same weights, different head)

Size varies: OpenAI used a 6B RM for a 175B policy; Anthropic used matched sizes (10B-52B for both). RewardBench research shows the RM and policy should derive from the **same model family** for best results.

## Training

Training data consists of [[concepts/preference-data]]: triplets of (prompt, chosen response, rejected response). The loss function derives from the [[concepts/bradley-terry-model]]:

```
Loss = -log(sigmoid(r_chosen - r_rejected))
```

This is minimized when the RM assigns higher scores to chosen responses. Post-training, outputs are normalized to mean zero across the training dataset.

**Scale**: Typically ~50k labeled preference samples. Quality dominates quantity -- modern high-quality datasets (UltraFeedback) dramatically improve results versus legacy datasets.

## Types of Reward Models

| Type | How It Works | Best For |
|------|-------------|----------|
| **Classifier RM** | LLM + linear head, scalar output | Structured tasks, production RLHF |
| **LLM-as-a-Judge** | Prompt a frontier model for preference scores | Quick evaluation, competitive with classifier RMs |
| **DPO Implicit RM** | Policy encodes reward via log probability ratios | Reward-free training (see [[concepts/dpo]]) |
| **Outcome RM (ORM)** | Predicts per-token correctness probability | Math/coding verification |
| **Process RM (PRM)** | Scores each reasoning step individually | Step-level reasoning supervision |

[[concepts/process-reward-model]]s (PRMs) are particularly important for reasoning tasks but require expensive step-level annotations. They provide finer-grained feedback than outcome-level rewards.

## Best Practices (from RewardBench)

1. **Data quality dominates**: The single most important factor. High-quality preference data outweighs model size, training epochs, or architectural choices.
2. **Base model matters**: RM performance correlates with base model capabilities. Skills in the base model transfer to the RM.
3. **Model lineage alignment**: RM and policy should come from the same model family. Cross-family RMs cause distribution mismatch.
4. **Two epochs can beat one**: On structured data, training for two epochs sometimes outperforms single-epoch training.
5. **Avoid length bias**: Ensure preference pairs contain similar-length responses.
6. **Scale matters conditionally**: Larger RMs help only on challenging data (reasoning, coding); diminishing returns on simple tasks.

## Challenges

- **[[concepts/reward-hacking]]**: The policy finds exploits in the RM that produce high proxy reward but low true quality. The most fundamental limitation of reward-based alignment.
- **Evaluation gap**: High scores on RM benchmarks are necessary but not sufficient for good downstream RL performance.
- **Distribution mismatch**: Performance degrades when the RL policy diverges from the RM's training distribution.
- **Complexity**: Hosting a separate model during training adds latency and orchestration overhead.

## Alternatives

- **[[concepts/dpo]]**: Learns an implicit reward without a separate RM
- **RLVR**: Uses deterministic, verifiable rewards (e.g., code test results) -- eliminates the RM entirely and avoids [[concepts/reward-hacking]]
- **LLM-as-a-Judge**: Uses prompted foundation models instead of trained classifiers

## Sources
- [[sources/wolfe-reward-models-llm]] -- comprehensive architecture and best practices
- [[sources/huggingface-rlhf-illustrated]] -- reward model's role in the RLHF pipeline
- [[sources/lilianweng-reward-hacking]] -- failure modes of reward models

## Related Concepts
- [[concepts/rlhf]] -- the pipeline reward models serve
- [[concepts/bradley-terry-model]] -- mathematical foundation
- [[concepts/preference-data]] -- what reward models learn from
- [[concepts/reward-hacking]] -- the primary failure mode
- [[concepts/process-reward-model]] -- step-level variant

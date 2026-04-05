---
title: "Source: Reward Models for LLM Alignment"
type: source-summary
source: "[[raw/wolfe-reward-models-llm]]"
related: ["[[concepts/reward-model]]", "[[concepts/bradley-terry-model]]", "[[concepts/reward-hacking]]", "[[concepts/rlhf]]"]
last_compiled: 2026-04-05
summary: "Cameron Wolfe's technical deep-dive into reward model architecture, training, types (classifier, LLM-as-judge, DPO implicit, ORM, PRM), challenges (reward hacking, distribution mismatch), and best practices from RewardBench."
---

## Key Points
- Reward models are repurposed LLMs with a linear classification head producing scalar preference scores
- Five types: classifier-based, LLM-as-a-Judge, DPO implicit, Outcome RMs, Process RMs
- Data quality is the dominant factor in RM performance (per RewardBench)
- RM and policy should derive from the same model family to avoid distribution mismatch
- RM benchmark accuracy does not reliably predict downstream RL performance
- RLVR (verifiable rewards) is an emerging alternative that eliminates the RM entirely

## Detailed Summary

The article establishes that [[concepts/reward-model]]s are the critical bridge between human preferences and RL training signals. Architecturally, they are LLM decoders with an added linear head that maps the final token's hidden state to a scalar score. Training uses the [[concepts/bradley-terry-model]]: the loss minimizes `-log(sigmoid(r_chosen - r_rejected))`.

Five distinct RM types serve different purposes. Process Reward Models (PRMs) provide step-level feedback for reasoning chains but require expensive step-level supervision. Outcome Reward Models (ORMs) predict per-token correctness. LLM-as-a-Judge approaches have become competitive with classifier RMs for frontier models.

RewardBench research reveals that data quality dominates all other factors, base model capabilities transfer to RM performance, and model lineage alignment between RM and policy is critical. Two training epochs can outperform single-epoch training on structured data.

## Related Concepts
- [[concepts/reward-model]] -- the central concept
- [[concepts/reward-hacking]] -- a key challenge for reward models
- [[concepts/bradley-terry-model]] -- mathematical foundation
- [[concepts/process-reward-model]] -- step-level reward variant

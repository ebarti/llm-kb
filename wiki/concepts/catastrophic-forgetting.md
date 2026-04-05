---
title: "Catastrophic Forgetting"
type: concept
sources: ["[[sources/lora-qlora-efficient-fine-tuning]]", "[[sources/rome-memit-knowledge-editing]]"]
related: ["[[concepts/fine-tuning]]", "[[concepts/parameter-efficient-fine-tuning]]", "[[concepts/knowledge-editing]]", "[[concepts/domain-adaptive-pretraining]]"]
last_compiled: 2026-04-05
summary: "Models losing previously learned knowledge when fine-tuned on new data — mitigated by PEFT (LoRA), regularization (EWC), experience replay, parameter isolation, and careful learning rate selection."
---

## Overview

Catastrophic forgetting is the phenomenon where a neural network, when fine-tuned on new data, loses or overwrites knowledge acquired during pretraining or previous fine-tuning. It is the primary risk of [[concepts/fine-tuning]] and a fundamental tension in putting knowledge into model weights: the very mechanism that enables learning new information (gradient descent on parameters) simultaneously degrades existing knowledge.

This risk is particularly acute for [[concepts/llm-knowledge-base]] systems where Karpathy suggested fine-tuning models on accumulated wiki content — if done carelessly, the model could lose general capabilities while acquiring domain knowledge.

## Why It Happens

Neural networks store knowledge distributed across shared parameters. When gradient updates optimize for new task performance, they inevitably modify parameters that encode existing knowledge. The degree of forgetting is related to:

- **Magnitude of weight updates**: Larger updates → more forgetting
- **Overlap of parameter usage**: Tasks sharing parameters compete for capacity
- **Loss landscape flatness**: Sharp minima are more susceptible to perturbation
- **Training duration**: More epochs on new data → more overwriting

## Mitigation Strategies

### 1. Parameter-Efficient Fine-Tuning (PEFT)
[[concepts/parameter-efficient-fine-tuning|LoRA and QLoRA]] update only 0.5-5% of parameters via low-rank adapter matrices, keeping the vast majority of base model weights frozen. This is the most practical and widely used mitigation.

### 2. Regularization-Based Approaches
- **Elastic Weight Consolidation (EWC)**: Penalizes changes to parameters important for prior tasks, based on Fisher information matrix
- **Sharpness-Aware Minimization (SAM)**: Flattens the loss landscape, making the model more robust to parameter perturbation
- **EWCLoRA**: Combines EWC with LoRA for additional forgetting reduction

### 3. Parameter Isolation
Train separate adapter modules for each task while keeping the base model frozen. Prevents competition for shared parameters entirely, at the cost of maintaining multiple adapter sets.

### 4. Knowledge Distillation
**Learning without Forgetting (LwF)**: Use the original model's outputs as soft targets when training on new data, preserving existing behavior while adding new capabilities.

### 5. Experience Replay
Retain a subset of old training data and mix it into new training batches. Simple but effective — forces the model to maintain performance on historical examples.

### 6. Low-Perplexity Token Masking
Mask high-perplexity tokens in training data to preserve non-target task robustness. A recent finding that offers a simple, training-data-level intervention.

### 7. CURLoRA
Uses CUR matrix decomposition in the context of LoRA for more stable adaptation. A 2025 advancement specifically targeting forgetting during continual fine-tuning.

## Scaling Laws for Forgetting

Research has established scaling relationships: forgetting during fine-tuning follows predictable patterns based on model size, dataset size, and training steps. Larger models tend to be more resistant to forgetting, but no model size eliminates the problem entirely.

## In Knowledge Editing

[[concepts/knowledge-editing|ROME and MEMIT]] face their own version of catastrophic forgetting: sequential edits induce gradual forgetting of prior facts, with neighborhood specificity being lost progressively until an abrupt catastrophic failure phase. This limits the practical number of knowledge edits that can be applied to a single model.

## Practical Recommendations

1. **Start with PEFT** (LoRA/QLoRA) as the default — it dramatically reduces forgetting
2. **Monitor general capabilities** alongside domain-specific metrics during fine-tuning
3. **Use experience replay** if you have access to representative pretraining-style data
4. **Keep learning rates low** — high learning rates amplify forgetting
5. **Limit training epochs** — early stopping based on validation across both old and new tasks
6. **Consider the three-layer architecture**: Put stable knowledge in weights, dynamic knowledge in context (RAG)

## Sources

- [[sources/lora-qlora-efficient-fine-tuning]] — PEFT as forgetting mitigation
- [[sources/rome-memit-knowledge-editing]] — forgetting in knowledge editing

## Related Concepts

- [[concepts/fine-tuning]] — catastrophic forgetting is the primary fine-tuning risk
- [[concepts/parameter-efficient-fine-tuning]] — primary mitigation technique
- [[concepts/knowledge-editing]] — sequential edits cause analogous forgetting
- [[concepts/domain-adaptive-pretraining]] — careful DAPT can reduce forgetting during later fine-tuning

---
title: "Chain-of-Thought Prompting"
type: concept
sources: ["[[sources/wei-chain-of-thought-prompting]]", "[[sources/li-system1-system2-reasoning-survey]]", "[[sources/raschka-state-of-reasoning-inference]]"]
related: ["[[concepts/llm-reasoning]]", "[[concepts/tree-of-thought]]", "[[concepts/self-consistency]]", "[[concepts/reasoning-models]]", "[[concepts/emergent-abilities]]"]
last_compiled: 2026-04-05
summary: "A prompting technique that elicits step-by-step reasoning in LLMs by providing worked exemplars or instructions like 'think step by step,' dramatically improving performance on arithmetic, commonsense, and symbolic reasoning tasks at 100B+ parameter scale."
---

## Overview

Chain-of-thought (CoT) prompting is the technique of encouraging LLMs to generate intermediate reasoning steps before producing a final answer. Introduced by [[entities/jason-wei|Wei et al.]] in January 2022, it is arguably the single most impactful discovery in LLM reasoning research, demonstrating that prompting alone -- without fine-tuning or architectural changes -- could unlock substantial reasoning capabilities.

## How It Works

Instead of asking a model to produce an answer directly, CoT prompting encourages the model to "show its work." This can be achieved in several ways:

### Few-Shot CoT
Provide exemplar problems with step-by-step solutions in the prompt. The model learns the pattern and applies it to new problems. Wei et al. showed that just 8 exemplars were sufficient for state-of-the-art GSM8K performance.

### Zero-Shot CoT
Simply append "Let's think step by step" to the prompt (Kojima et al., 2022). Remarkably effective despite requiring no exemplars -- suggesting the reasoning capability is latent in the model and just needs to be activated.

### Automatic CoT
Use the model itself to generate CoT exemplars, reducing the need for human-crafted demonstrations.

### Multimodal CoT
Extends CoT to incorporate visual data alongside language (Meta/AWS, 2024+).

## Scale Dependence

CoT is an [[concepts/emergent-abilities|emergent ability]]:

- **Below ~100B parameters**: Models generate illogical chains that actually hurt performance compared to direct answering.
- **Above ~100B parameters**: CoT dramatically improves performance, with gains increasing at larger scales.
- **Threshold**: Approximately 10^22 FLOPs of training compute.

This scale dependence has important implications: CoT is not a general-purpose technique but one that requires sufficient model capacity to be useful.

## Why It Works (Hypotheses)

Several theories explain CoT's effectiveness:

1. **Decomposition**: Breaking complex problems into simpler sub-problems that are individually within the model's capability.
2. **Working memory extension**: The generated text serves as external working memory, allowing the model to track intermediate results.
3. **Distribution matching**: Training data contains step-by-step solutions; CoT shifts the generation distribution toward that pattern.
4. **Attention focusing**: Each reasoning step narrows the relevant context for the next step.

## Limitations

CoT is not a silver bullet:

- **Single-path**: Only explores one reasoning trajectory. If the initial approach is wrong, CoT cannot recover. [[concepts/tree-of-thought|Tree of Thoughts]] addresses this.
- **Fragility**: CoT reasoning can be derailed by irrelevant information ([[sources/mirzadeh-gsm-symbolic|GSM-Symbolic]] showed up to 65% drops).
- **Faithfulness**: The displayed reasoning chain may not reflect the model's actual computation -- it may arrive at answers through different internal processes than the stated steps.
- **Cost**: Generating reasoning tokens increases latency and compute cost.

## Legacy and Impact

CoT opened the door to the entire field of LLM reasoning research:

- [[concepts/tree-of-thought]] generalized CoT to multi-path exploration
- [[concepts/self-consistency]] used majority voting over multiple CoT samples
- [[concepts/process-reward-models]] added learned verification of reasoning steps
- [[concepts/reasoning-models]] (o1, o3, R1) internalized CoT through RL training
- [[concepts/test-time-compute]] formalized the compute economics of reasoning

## Sources

- [[sources/wei-chain-of-thought-prompting]] -- the original paper
- [[sources/li-system1-system2-reasoning-survey]] -- CoT as the bridge from System 1 to System 2
- [[sources/raschka-state-of-reasoning-inference]] -- CoT in the context of inference-time scaling

## Related Concepts

- [[concepts/llm-reasoning]] -- the broader capability CoT enables
- [[concepts/tree-of-thought]] -- multi-path generalization
- [[concepts/self-consistency]] -- majority voting enhancement
- [[concepts/reasoning-models]] -- models that internalize CoT via training
- [[concepts/emergent-abilities]] -- CoT as an emergent capability

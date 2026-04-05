---
title: "Source: RT-2 Vision-Language-Action Model (Google DeepMind)"
type: source-summary
source: "[[raw/google-deepmind-rt2-vla-model]]"
related: ["[[concepts/vision-language-action-models]]", "[[concepts/embodied-intelligence]]", "[[concepts/foundation-models-for-robotics]]", "[[entities/google-deepmind]]", "[[entities/rt-2]]", "[[entities/palm-e]]"]
tags: [rt-2, vla, google-deepmind, robotics, foundation-models]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Google DeepMind's RT-2 is a pioneering VLA model that co-trains on web-scale vision-language data and robotics demonstrations; improved generalization from 32% to 62% on novel scenarios vs RT-1; introduced emergent reasoning, symbol understanding, and chain-of-thought for robotic control."
---

## Key Points

- RT-2 is the first major [[concepts/vision-language-action-models]] -- a single model that processes vision, understands language, and outputs robot actions
- Built on PaLI-X or PaLM-E backbones; actions encoded as text tokens in the same format as natural language
- Generalization on novel objects/backgrounds improved from 32% (RT-1) to 62% (RT-2)
- Demonstrates emergent capabilities transferred from web pre-training: symbol understanding, mathematical reasoning, contextual human need recognition
- The PaLM-E variant acts as LLM + VLM + robot controller in a single neural network with chain-of-thought reasoning

## Detailed Summary

RT-2 represents a paradigm shift in robotic control by demonstrating that vision-language models pre-trained on internet-scale data can be directly adapted for robotic action generation. The key insight is encoding robot actions as text tokens, allowing the model to leverage its language understanding for physical world interaction.

The model uses either [[entities/palm-e]] (an embodied language model) or PaLI-X as its backbone. Actions are represented as strings containing episode continuation/termination flags, end-effector position and rotation deltas, and gripper parameters. This encoding allows standard NL tokenizers to handle robotic actions.

Training combines 17 months of RT-1 demonstrations (13 robots in an office kitchen) with web-scale vision-language data. The result dramatically improves generalization: in 6,000 evaluation trials, RT-2 achieved 62% success on unseen scenarios where RT-1 managed only 32%, and showed >3x improvement on emergent capabilities versus VC-1 and RT-1 baselines.

Three categories of emergent capabilities appeared from web knowledge transfer: (1) symbol understanding -- recognizing novel objects in unfamiliar contexts, (2) reasoning -- performing mathematical operations and logical deductions, (3) human recognition -- understanding contextual needs (e.g., selecting an "energy drink" for a tired person, identifying a rock as an improvised hammer).

The chain-of-thought variant augments actions with intermediate "Plan" steps describing action purposes in natural language, enabling multi-stage reasoning within a single model for long-horizon tasks.

## Concepts Introduced or Discussed

- [[concepts/vision-language-action-models]] -- the VLA paradigm RT-2 pioneered
- [[concepts/foundation-models-for-robotics]] -- web-scale pre-training for robot control
- [[concepts/language-grounding-for-robots]] -- connecting language to physical actions
- [[concepts/embodied-intelligence]] -- intelligence that acts in the physical world

## Quotes & Evidence

> "RT-2 shows that vision-language models can be transformed into powerful vision-language-action models, which can directly control a robot."

> Actions encoded as text tokens: "converting it to a string representation makes it possible to train VLM models on robotic data."

## Metadata

- **Author**: Google DeepMind
- **Date Published**: 2023-07-28
- **Format**: article (research blog)
- **URL**: https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/

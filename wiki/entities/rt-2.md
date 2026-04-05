---
title: "RT-2 (Robotic Transformer 2)"
type: entity
entity_type: paper
url: "https://robotics-transformer2.github.io/"
related: ["[[concepts/vision-language-action-models]]", "[[concepts/foundation-models-for-robotics]]", "[[entities/google-deepmind]]", "[[entities/palm-e]]", "[[entities/saycan]]", "[[entities/pi0]]"]
tags: [rt-2, vla, google-deepmind, robotics]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Google DeepMind's pioneering Vision-Language-Action model (July 2023) that showed VLMs can directly control robots; built on PaLM-E/PaLI-X; encodes actions as text tokens; improved generalization from 32% to 62% vs RT-1; demonstrated emergent reasoning from web pre-training."
---

## Overview

RT-2 (Robotic Transformer 2) is a [[concepts/vision-language-action-models]] developed by Google DeepMind, published in July 2023. It demonstrated for the first time that pre-trained vision-language models could be directly adapted for robotic control by encoding actions as text tokens, fundamentally establishing the VLA paradigm that now dominates robot foundation model research.

## Key Facts

- **Type**: paper / model
- **Organization**: [[entities/google-deepmind]]
- **Published**: July 28, 2023
- **Parameters**: Up to 55B (PaLM-E variant)
- **Backbone**: PaLI-X or [[entities/palm-e]]
- **Notable for**: Establishing the VLA paradigm; demonstrating emergent capabilities from web pre-training

## Technical Details

**Architecture**: Extends VLMs by encoding robot actions (position/rotation deltas, gripper state) as text tokens processable by standard NL tokenizers. The PaLM-E variant serves as LLM + VLM + robot controller in a single neural network.

**Training**: 17 months of RT-1 demonstrations (13 robots in office kitchen) + web-scale vision-language data.

**Performance**: 62% success on novel scenarios (vs 32% for RT-1); >3x improvement on emergent capabilities; 6,000 evaluation trials.

**Emergent Capabilities**: Symbol understanding, mathematical reasoning, contextual human need recognition -- all transferred from web pre-training data.

**Chain-of-Thought**: PaLM-E variant supports intermediate "Plan" steps in natural language for multi-stage reasoning.

## Role in Knowledge Base

RT-2 is the foundational model in the [[concepts/vision-language-action-models]] evolution. It preceded and influenced [[entities/pi0]], OpenVLA, and [[entities/nvidia-groot]]. Together with [[entities/saycan]] (affordance grounding) and [[entities/palm-e]] (embodied language model), it forms Google DeepMind's progression toward general-purpose robot intelligence.

## Mentions

- [[sources/google-deepmind-rt2-vla-model]] -- primary source
- [[sources/llms-for-robotics-survey-2025]] -- in VLA evolution survey
- [[sources/deloitte-physical-ai-humanoid-robots-2026]] -- as key technology enabler

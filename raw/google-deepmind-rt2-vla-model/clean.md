---
title: "RT-2: New Model Translates Vision and Language into Action"
source: "https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/"
author: "Google DeepMind"
date_published: 2023-07-28
date_ingested: 2026-04-05
tags: [rt-2, vla, robotics, foundation-models, google-deepmind, vision-language-action]
type: article
status: raw
discovered_via: search
---

# RT-2: Vision-Language-Action Model — Google DeepMind

RT-2 (Robotic Transformer 2) is a vision-language-action (VLA) model that learns from both web and robotics data, translating knowledge into generalized instructions for robotic control.

## Architecture

RT-2 adapts pre-trained VLMs (PaLI-X or PaLM-E) for robotic control by extending them to output action tokens. Actions are encoded as strings processable by standard NL tokenizers. The action string format includes: episode continuation/termination flag, end-effector position/rotation changes, gripper extension parameters.

The RT-2 PaLM-E version acts as LLM, VLM, and robotic controller all in a single neural network, performing chain-of-thought reasoning for control.

## Training Data

- **Robotics data**: RT-1 demonstrations collected over 17 months using 13 robots in an office kitchen environment
- **Web-scale data**: Pre-trained knowledge from large-scale vision-language datasets

## Performance

- Unseen scenarios: improved from 32% to 62% success rate on novel objects/backgrounds (vs RT-1)
- Language Table tasks: 90% success in simulation
- More than 3x improvement versus baselines (VC-1, RT-1) on emergent capabilities
- Extensive evaluation: 6,000 evaluation trials

## Emergent Capabilities

Three skill categories from web pre-training knowledge transfer:
1. **Symbol understanding**: Recognizing novel objects
2. **Reasoning**: Mathematical operations, logical deductions
3. **Human recognition**: Understanding contextual human needs

e.g., identifying "a rock" as improvised hammer, selecting "an energy drink" for tired individuals.

## Key Differences from RT-1

- Incorporates web-scale VLM pre-training for superior generalization
- Demonstrates emergent skills absent from robotics training data
- Supports visual grounding for planning
- Chain-of-thought reasoning via intermediate "Plan" steps

---
title: "Large Language Models for Robotics: A Survey"
source: "https://arxiv.org/html/2311.07226v2"
author: "Multiple authors"
date_published: 2025-06-15
date_ingested: 2026-04-05
tags: [llm-robotics, survey, vla, embodied-ai, foundation-models, robot-planning]
type: paper
status: raw
discovered_via: search
---

# Large Language Models for Robotics: A Comprehensive Survey

## Taxonomy

Four core components of LLM-based robotics:
1. **Perception**: VLMs, scene understanding, indirect perception
2. **Decision-Making**: Policy learning, multi-robot collaboration, task planning
3. **Control**: Action execution, VLA models
4. **Interaction**: Human-robot dialogue, language interfaces

## Key Models

### VLA Models
- **RT-1** (2022): End-to-end model, 340K trajectory dataset
- **RT-2** (2023): Instruction tuning + RLHF, 55B parameters
- **OpenVLA** (2024): Performance parity with RT-2-X despite 10x smaller parameters
- **π0 Series**: Flow-based, 50Hz control for dexterous tasks
- **GR00T-N1**: NVIDIA open-source, dual System 1/System 2 architecture

### Agent Frameworks
- **ELLMER**: Integrating LLM with advanced sensor feedback
- **COHERENT**: Heterogeneous multi-robot with Proposal-Execution-Feedback-Adjustment mechanism
- **EMOS**: LLM-based multi-agent for complex household environments
- **RoCo**: Multi-arm manipulation with RoCoBench (6-task benchmark)

## Planning & Reasoning

- **SayCan**: Grounding language in robotic affordances (84% plan success, 74% execution)
- **SayPlan**: 3D scene graphs for scalable task planning
- **Code as Policies**: LLMs generating executable robot code
- Chain-of-thought, tree-based planning, in-context learning

## Datasets & Benchmarks

- **LIBERO**: 100+ tasks, 31.64GB (spatial reasoning, manipulation, goal-conditioned)
- **Open X-Embodiment**: 800K trajectories from diverse platforms
- **RoCoBench**: 6-task multi-robot benchmark
- **Agibot-World**: World's largest open-source humanoid robot dataset

## Key Challenges

1. **Hallucination in Planning**: LLMs generate infeasible/harmful actions
2. **Sim-to-real gap**: Persistent performance degradation in transfer
3. **Real-time constraints**: Sub-300ms latency for dexterous control
4. **Data scarcity**: Limited diversity in real robot data
5. **Cross-embodiment transfer**: Different robot morphologies
6. **Safety**: LLMs may generate harmful content in physical context

## Future Directions

- Security of task execution via formal verification
- Unified modal formats for perception-action
- Modular composable skill libraries
- Autonomous self-supervised perception

---
title: "Source: Large Language Models for Robotics — A Survey"
type: source-summary
source: "[[raw/llms-for-robotics-survey-2025]]"
related: ["[[concepts/embodied-intelligence]]", "[[concepts/vision-language-action-models]]", "[[concepts/language-grounding-for-robots]]", "[[concepts/foundation-models-for-robotics]]", "[[concepts/sim-to-real-transfer]]", "[[entities/rt-2]]", "[[entities/pi0]]", "[[entities/nvidia-groot]]"]
tags: [survey, llm-robotics, embodied-ai, vla, robot-planning]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Comprehensive 2025 survey organizing LLM-based robotics into four pillars (perception, decision-making, control, interaction); covers VLA evolution from RT-1 through π0 and GR00T-N1; identifies hallucination in planning, sim-to-real gap, and real-time constraints as key open challenges."
---

## Key Points

- Organizes the field into four pillars: perception (VLMs, scene understanding), decision-making (policy learning, task planning), control (VLA models, action execution), interaction (human-robot dialogue)
- Traces VLA evolution: RT-1 (2022, 340K trajectories) → RT-2 (2023, 55B params, emergent reasoning) → OpenVLA (2024, 10x smaller, same performance) → π0 (flow-based, 50Hz) → GR00T-N1 (dual System 1/2)
- Key planning approaches: [[entities/saycan]] (affordance grounding, 84% plan success), SayPlan (3D scene graphs), Code as Policies (executable code generation)
- Major benchmarks: LIBERO (100+ tasks, 31.64GB), Open X-Embodiment (800K trajectories), Agibot-World (largest humanoid dataset)
- Critical challenges: LLM hallucination producing infeasible/harmful robot actions, sub-300ms latency requirements for dexterous control, limited real-world training data diversity

## Detailed Summary

This comprehensive survey maps the rapidly expanding intersection of LLMs and robotics. The authors position [[concepts/embodied-intelligence]] as "the future of intelligent systems" with LLM-based robotics as "one of the most promising yet challenging paths."

**Perception** has been transformed by VLMs: CLIP enables zero-shot object recognition, [[entities/palm-e]] treats images and text as latent vectors, and PhysVLM introduces spatial accessibility maps integrating robot operational ranges.

**Decision-making** connects perception to control. [[entities/saycan]] scores skill likelihood against affordance functions (84% plan success, 74% execution on 101 kitchen tasks). SayPlan uses 3D scene graphs with expand/contract API calls to manage token budgets. Multi-agent systems like COHERENT use Proposal-Execution-Feedback-Adjustment mechanisms for heterogeneous robot coordination.

**Control** has been revolutionized by [[concepts/vision-language-action-models]]. The survey traces a clear evolution: RT-1's end-to-end approach (340K trajectories), RT-2's web-scale pre-training (55B params, emergent reasoning), OpenVLA's efficiency breakthrough (parity with RT-2-X at 10x fewer parameters), [[entities/pi0]]'s flow matching (50Hz dexterous control), and [[entities/nvidia-groot]]'s dual System 1/System 2 architecture.

The survey identifies persistent challenges: LLM hallucination in planning (generating infeasible or dangerous actions), real-time execution constraints (sub-300ms for dexterous control), and data scarcity (limited real-world robot data diversity versus web-scale text/image data).

## Concepts Introduced or Discussed

- [[concepts/embodied-intelligence]] -- the overarching paradigm
- [[concepts/vision-language-action-models]] -- direct perception-to-action models
- [[concepts/language-grounding-for-robots]] -- connecting language to physical capabilities
- [[concepts/foundation-models-for-robotics]] -- general-purpose robot models
- [[concepts/robot-learning-from-demonstration]] -- imitation and behavior cloning
- [[concepts/sim-to-real-transfer]] -- closing the simulation gap

## Metadata

- **Author**: Multiple authors
- **Date Published**: 2025
- **Format**: paper (survey)
- **URL**: https://arxiv.org/html/2311.07226v2

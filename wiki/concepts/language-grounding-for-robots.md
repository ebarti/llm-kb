---
title: "Language Grounding for Robots"
type: concept
sources: ["[[sources/saycan-grounding-language-robotic-affordances]]", "[[sources/llms-for-robotics-survey-2025]]", "[[sources/google-deepmind-rt2-vla-model]]"]
related: ["[[concepts/embodied-intelligence]]", "[[concepts/vision-language-action-models]]", "[[concepts/foundation-models-for-robotics]]", "[[entities/saycan]]", "[[entities/rt-2]]"]
tags: [language-grounding, robotics, affordances, llm-planning]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The challenge of connecting abstract language understanding to concrete physical capabilities in robots — addressed through affordance grounding (SayCan), 3D scene graphs (SayPlan), closed-loop feedback, and end-to-end VLA models (RT-2, π0)."
---

## Overview

Language grounding for robots is the challenge of connecting what an LLM "knows" (language, common sense, task knowledge) with what a robot can physically "do" in its current environment. An LLM might suggest "put the cup in the dishwasher," but the robot needs to determine whether a cup is visible, reachable, and graspable given its current state. Despite rapid progress, grounding LLMs in a given physical environment remains an open problem.

## Key Ideas

### Affordance Grounding (SayCan)

[[entities/saycan]] (Google, 2022) introduced the foundational approach: multiply the LLM's semantic relevance score for a skill by a learned affordance function measuring physical feasibility. This ensures the robot selects actions that are both useful and executable. Result: 84% plan success, 74% execution success on 101 kitchen tasks.

### Scene Graph Grounding (SayPlan)

SayPlan uses 3D scene graphs to provide LLMs with structured spatial understanding. The LLM manipulates graph nodes via expand/contract API calls, maintaining focus on task-relevant subgraphs without exceeding token limits. This scales to large environments where flat descriptions would overflow context windows.

### Closed-Loop State Feedback

A persistent limitation of early systems (including SayCan) was open-loop planning -- feedback only at decision points. Closed-loop approaches like BrainBody-LLM use hierarchical two-LLM systems where one handles high-level reasoning and another handles low-level control with continuous state feedback, enabling re-planning upon execution failures.

### Code as Policies

Rather than selecting from predefined skills, LLMs generate executable code (Python programs) that directly compose primitive robot functions. This provides maximum flexibility but introduces code safety challenges -- the generated program runs on a physical system.

### End-to-End VLA Grounding

[[concepts/vision-language-action-models]] like [[entities/rt-2]] and [[entities/pi0]] sidestep explicit grounding modules entirely. By training on both web data and robot trajectories, they learn implicit grounding: the model directly maps language instructions + visual observations to motor commands. RT-2's emergent capabilities (using a rock as a hammer) suggest deep implicit grounding from web pre-training.

## How It Connects

- [[concepts/embodied-intelligence]] -- grounding is the central challenge of embodied AI
- [[concepts/vision-language-action-models]] -- end-to-end grounding through VLAs
- [[concepts/foundation-models-for-robotics]] -- web pre-training provides implicit grounding
- [[concepts/grounding-and-faithfulness]] -- parallels with document grounding in NLP (anchoring outputs to sources)

## Open Questions

- Is explicit grounding (affordance functions) necessary, or will end-to-end VLAs subsume it?
- How should robots handle instructions for actions they physically cannot perform?
- Can 3D scene graphs generalize across diverse environments, or are they too brittle?
- How to ground abstract temporal and causal language (e.g., "after the water boils")?

## Sources

- [[sources/saycan-grounding-language-robotic-affordances]] -- foundational affordance grounding
- [[sources/llms-for-robotics-survey-2025]] -- comprehensive survey of grounding approaches
- [[sources/google-deepmind-rt2-vla-model]] -- implicit grounding via VLA pre-training

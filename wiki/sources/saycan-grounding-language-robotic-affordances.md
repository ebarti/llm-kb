---
title: "Source: SayCan — Grounding Language in Robotic Affordances"
type: source-summary
source: "[[raw/saycan-grounding-language-robotic-affordances]]"
related: ["[[concepts/language-grounding-for-robots]]", "[[concepts/embodied-intelligence]]", "[[concepts/foundation-models-for-robotics]]", "[[entities/saycan]]", "[[entities/google-deepmind]]"]
tags: [saycan, language-grounding, affordances, robotics, google]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Google's SayCan bridges LLMs and robot execution by combining semantic skill scoring with physical affordance functions; achieves 84% plan success and 74% execution success on 101 kitchen tasks with 8-16 step sequences; foundational work for language-grounded robotics."
---

## Key Points

- Introduces the affordance grounding paradigm: LLM semantic scores multiplied by physical feasibility scores to select robot actions
- Achieves 84% plan success rate, 74% execution success, 50% error reduction vs FLAN baseline
- Handles long-horizon tasks with 8-16 sequential steps on a mobile manipulator
- Supports multilingual commands (English, Chinese, French, Spanish) with minimal degradation
- Foundational work leading to RT-2, PaLM-E, and the broader [[concepts/language-grounding-for-robots]] research area

## Detailed Summary

[[entities/saycan]] addresses a fundamental challenge in [[concepts/embodied-intelligence]]: LLMs have broad knowledge about tasks but lack grounding in what a specific robot can physically do in its current environment. The solution combines two probability distributions at each planning step:

1. **Language Model Score**: How likely is a skill to make progress toward the instruction?
2. **Affordance Function**: How likely is the skill to succeed from the current physical state?

By multiplying these scores, SayCan selects actions that are both semantically relevant and physically executable. The algorithm iterates until task completion.

Using PaLM as the language backbone, SayCan achieved 84% plan success and 74% execution success across 101 test tasks in kitchen environments. Tasks involved 8-16 sequential steps (e.g., "bring me something to clean up a spill" requires finding a sponge, picking it up, navigating to the user, and delivering it).

The system extends gracefully: new skills are added by defining new options with corresponding affordance functions. Chain-of-thought reasoning enables multi-step logical inference. The approach laid groundwork for subsequent systems including [[entities/rt-2]], [[entities/palm-e]], and the inner monologue framework for closed-loop planning.

## Concepts Introduced or Discussed

- [[concepts/language-grounding-for-robots]] -- the affordance grounding approach
- [[concepts/embodied-intelligence]] -- physical world interaction
- [[concepts/foundation-models-for-robotics]] -- LLMs as robot planners

## Metadata

- **Author**: Google Research, Everyday Robots
- **Date Published**: 2022-04-04
- **Format**: paper
- **URL**: https://say-can.github.io/

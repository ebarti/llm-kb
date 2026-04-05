---
title: "SayCan"
type: entity
entity_type: paper
url: "https://say-can.github.io/"
related: ["[[concepts/language-grounding-for-robots]]", "[[concepts/embodied-intelligence]]", "[[entities/google-deepmind]]", "[[entities/rt-2]]", "[[entities/palm-e]]"]
tags: [saycan, language-grounding, affordances, google, robotics]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Google's foundational system for grounding language in robotic affordances — combines LLM semantic scores with physical feasibility functions; 84% plan success, 74% execution on 101 kitchen tasks with 8-16 steps; precursor to RT-2 and the broader VLA paradigm."
---

## Overview

SayCan is a robot planning system developed by Google Research and Everyday Robots (2022) that grounds LLM task knowledge in physical robot capabilities. It established the foundational paradigm of combining LLM semantic understanding with learned affordance functions, influencing all subsequent work on [[concepts/language-grounding-for-robots]].

## Key Facts

- **Type**: paper / system
- **Organization**: Google Research, Everyday Robots
- **Published**: April 2022
- **Method**: LLM semantic score x affordance function score
- **Performance**: 84% plan success, 74% execution success, 50% error reduction vs FLAN
- **Task complexity**: 8-16 sequential steps on mobile manipulator
- **Test scale**: 101 tasks in kitchen environments

## How It Works

At each planning step, SayCan:
1. Asks the LLM: "Which skill helps progress toward the goal?" (semantic score)
2. Asks the affordance function: "Can this skill succeed from the current state?" (feasibility score)
3. Multiplies both scores to select the best action
4. Executes and repeats

## Legacy

SayCan directly influenced [[entities/rt-2]] (end-to-end VLA replacing separate affordance functions), [[entities/palm-e]] (embodied language model), and the inner monologue framework (closed-loop feedback). The concept of grounding LLMs in physical affordances remains central to [[concepts/embodied-intelligence]].

## Mentions

- [[sources/saycan-grounding-language-robotic-affordances]] -- primary source
- [[sources/llms-for-robotics-survey-2025]] -- as foundational planning approach

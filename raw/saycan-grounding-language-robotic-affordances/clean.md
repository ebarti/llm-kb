---
title: "SayCan: Grounding Language in Robotic Affordances"
source: "https://say-can.github.io/"
author: "Google Research, Everyday Robots"
date_published: 2022-04-04
date_ingested: 2026-04-05
tags: [saycan, language-grounding, robotics, llm-planning, affordances, google]
type: paper
status: raw
discovered_via: search
---

# SayCan: Grounding Language in Robotic Affordances

## Core Concept

SayCan bridges LLMs and robotic execution by combining semantic knowledge with physical feasibility. Rather than asking an LLM to directly plan robotic actions, it scores the likelihood that an individual skill makes progress toward a high-level instruction.

## Architecture

Combined scoring of two distributions:
1. **Language Model Score**: Probability that a skill is semantically useful for the instruction
2. **Affordance Function Score**: Probability of successfully executing that skill from current state (learned value function)

The algorithm iteratively selects and executes skills by combining these scores until task termination.

## Performance (PaLM-SayCan)

- 84% plan success rate
- 74% execution success rate
- 50% error reduction vs FLAN baseline
- Long-horizon tasks: 8-16 sequential steps on mobile manipulator
- 101 test tasks in kitchen environments

## Capabilities

- New skills added by extending skill options + value functions
- Chain-of-thought reasoning for multi-step logical inference
- Multilingual support (English, Chinese, French, Spanish) with minimal degradation

## Limitations

Environmental feedback only at decision steps. Follow-up "inner monologue" work addresses closed-loop planning with continuous environment feedback.

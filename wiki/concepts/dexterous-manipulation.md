---
title: "Dexterous Manipulation"
type: concept
sources: ["[[sources/physical-intelligence-pi0-foundation-model]]", "[[sources/figure-ai-humanoid-robots]]", "[[sources/deloitte-physical-ai-humanoid-robots-2026]]", "[[sources/llms-for-robotics-survey-2025]]"]
related: ["[[concepts/humanoid-robots]]", "[[concepts/vision-language-action-models]]", "[[concepts/embodied-intelligence]]", "[[concepts/sim-to-real-transfer]]", "[[concepts/flow-matching]]", "[[concepts/robot-learning-from-demonstration]]"]
tags: [dexterous-manipulation, robot-hands, tactile-sensing, robotics]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Teaching robots human-level hand skills — the frontier challenge of embodied AI; breakthrough enabled by VLA models (π0 achieves laundry folding), high-DOF hands (22 DOF in Optimus Gen 3, 16 DOF per hand in Figure 02), and tactile sensors detecting forces as small as 3 grams."
---

## Overview

Dexterous manipulation -- the ability of robots to perform complex, fine-grained physical tasks with human-like hand skills -- is widely considered the most important unsolved problem in [[concepts/embodied-intelligence]]. While navigation and simple grasping are largely solved, tasks like folding laundry, assembling boxes, using tools, and handling deformable objects remain at the frontier.

The challenge is multi-faceted: it requires high-DOF hardware (human hands have 27 DOF), precise tactile sensing, real-time control at 50Hz+, and planning that accounts for contact dynamics and material deformation. Recent breakthroughs from [[entities/pi0]] (first to fold laundry), advances in robot hand hardware, and tactile sensing have made this a rapidly moving field.

## Key Ideas

### Hardware State of the Art (2026)

| Robot Hand | Active DOF | Key Feature |
|-----------|-----------|-------------|
| [[entities/tesla-optimus]] Gen 3 | 22 (+ 3 wrist) | Planetary roller screws |
| [[entities/figure-ai]] Figure 02 | 16 per hand | Five-fingered, human-like |
| ZWHAND B20 | 20 | Mass-producible, anthropomorphic |
| Sharpa Wave | 22 | 1:1 human scale, tactile feedback |
| MATRIX-3 | 27 | Cable-driven, tool-use capable |
| F-TAC Hand | -- | 0.1mm tactile resolution, 70% surface coverage |

### Tactile Sensing

The F-TAC Hand (Nature Machine Intelligence, 2025) embeds high-resolution touch sensing (0.1mm spatial resolution) across 70% of its surface area, significantly outperforming other approaches in complex manipulation. [[entities/figure-ai]]'s Figure 03 detects forces as small as 3 grams. This dense tactile feedback is enabling adaptive grasping that responds to slip, deformation, and unexpected contacts.

### AI Approaches

**[[concepts/flow-matching]]**: [[entities/pi0]] uses flow matching to produce smooth, continuous action trajectories at 50Hz -- the high temporal resolution required for dexterous tasks. This was the key to achieving laundry folding (1.0 success rate) and box assembly where all prior models scored 0.

**[[concepts/imitation-learning]]**: Teleoperation and motion capture data provide the demonstrations needed for dexterous skills. Figure AI's Helix 02 was trained using motion-capture data combined with simulation-based ML.

**Reinforcement Learning**: In simulation with domain randomization, then transferred to real hardware. AutoMate's assembly tasks demonstrate 84.5% generalist success with zero-shot [[concepts/sim-to-real-transfer]].

**Semantic-Driven Gesture Generation**: LLMs and VLMs enable robots to interpret environmental cues and generate contextually appropriate grasps, shifting from rule-based to context-aware manipulation.

### Breakthrough Tasks

[[entities/pi0]] achieved what no prior system could:
- **Laundry folding** from hamper to neat stack (1.0 success)
- **Box assembly** with multi-stage manipulation and failure recovery
- **Table bussing** with emergent dish stacking and pre-cleaning
- **Grocery bagging** of diverse deformable items

These require reasoning about deformable objects, multi-step sequencing, and adaptive re-planning -- the hallmarks of true dexterity.

## How It Connects

- [[concepts/humanoid-robots]] -- dexterous hands are the critical capability gap for humanoid deployment
- [[concepts/vision-language-action-models]] -- VLAs (especially π0) first achieved complex dexterous tasks
- [[concepts/flow-matching]] -- the temporal resolution enabling smooth dexterous control
- [[concepts/sim-to-real-transfer]] -- most dexterous skills are trained in simulation first
- [[concepts/robot-learning-from-demonstration]] -- teleoperation provides dexterous training data
- [[concepts/embodied-intelligence]] -- dexterity is the frontier of physical intelligence

## Open Questions

- Rodney Brooks argues current humanoids "won't learn dexterity" -- is the hardware-software co-design fundamentally limited?
- Can sim-to-real transfer work for deformable objects (cloth, food) where physics simulation is least accurate?
- What level of tactile resolution is "enough" for human-level dexterity?
- Will bimanual coordination (two-handed tasks) require fundamentally different architectures?

## Sources

- [[sources/physical-intelligence-pi0-foundation-model]] -- first system to achieve complex dexterous tasks
- [[sources/figure-ai-humanoid-robots]] -- hardware evolution and tactile sensing
- [[sources/deloitte-physical-ai-humanoid-robots-2026]] -- industry perspective on dexterous requirements
- [[sources/llms-for-robotics-survey-2025]] -- survey of manipulation approaches

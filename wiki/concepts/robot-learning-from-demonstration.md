---
title: "Robot Learning from Demonstration"
type: concept
sources: ["[[sources/llms-for-robotics-survey-2025]]", "[[sources/physical-intelligence-pi0-foundation-model]]", "[[sources/nvidia-automate-sim-to-real-assembly]]", "[[sources/nvidia-isaac-groot-n1-foundation-model]]"]
related: ["[[concepts/imitation-learning]]", "[[concepts/foundation-models-for-robotics]]", "[[concepts/dexterous-manipulation]]", "[[concepts/humanoid-robots]]", "[[concepts/sim-to-real-transfer]]"]
tags: [learning-from-demonstration, imitation-learning, teleoperation, robotics]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Teaching robots through expert demonstrations — via teleoperation, motion capture, or human video; π0 needs 1-20 hours per task; NVIDIA generates 780K synthetic demos in 11h; growing gig economy of remote teleoperators training humanoids from home."
---

## Overview

Robot learning from demonstration (LfD) encompasses techniques where robots acquire skills by observing expert behavior rather than through reward-based trial-and-error. It is the primary mechanism for fine-tuning [[concepts/foundation-models-for-robotics]] to specific tasks, and the dominant approach for training [[concepts/humanoid-robots]] and [[concepts/dexterous-manipulation]] skills.

## Key Ideas

### Demonstration Sources

1. **Teleoperation**: Human operators remotely control the robot, generating paired observation-action data. MIT Technology Review reports a growing gig economy of workers training humanoid robots from home using teleoperation rigs.

2. **Motion Capture**: Human movements captured via body tracking and mapped to robot kinematics. [[entities/figure-ai]]'s Helix 02 was trained using mocap data combined with simulation ML.

3. **Human Video**: Learning from videos of humans performing tasks, without requiring a robot in the loop. Emerging approaches use video generation models as cost-effective data generators and can use human demonstration video as a policy prompt.

4. **Synthetic Demonstrations**: [[entities/nvidia-groot]] generated 780,000 synthetic trajectories in 11 hours (= 9 months of continuous human demonstration) using Omniverse simulation, achieving 40% improvement.

5. **Assembly-by-Disassembly**: AutoMate records easy disassembly trajectories in simulation and reverses them, cleverly avoiding the difficulty of forward demonstration.

### Efficiency

[[entities/pi0]] requires remarkably little task-specific data: 1-20 hours of demonstration suffices to fine-tune the foundation model for new tasks. This contrasts sharply with the thousands of hours previously needed.

### Behavior Cloning vs. Interactive Methods

**Behavior Cloning**: Supervised learning on demonstration data. Simple but suffers from distribution shift (compound errors).

**DAgger** (Dataset Aggregation): The learner runs its policy, and the expert provides corrections at states the learner visits. AutoMate's generalist pipeline uses DAgger between behavior cloning and curriculum RL.

**Inverse RL**: Infers the reward function from demonstrations, then optimizes. More robust to distribution shift but computationally expensive.

### One-Shot and Few-Shot Learning

Recent work enables learning from a single demonstration: one-shot visual imitation frameworks integrate hand detection, object detection, and trajectory segmentation, using Dynamic Movement Primitives to generalize to new object positions.

## How It Connects

- [[concepts/foundation-models-for-robotics]] -- demonstrations are the fine-tuning mechanism
- [[concepts/dexterous-manipulation]] -- most dexterous skills are demonstrated
- [[concepts/humanoid-robots]] -- teleoperation and mocap are primary training sources
- [[concepts/sim-to-real-transfer]] -- synthetic demonstrations bridge the data gap
- [[concepts/imitation-learning]] -- the ML framework underlying LfD

## Sources

- [[sources/llms-for-robotics-survey-2025]] -- comprehensive survey of LfD approaches
- [[sources/physical-intelligence-pi0-foundation-model]] -- 1-20 hours per task fine-tuning
- [[sources/nvidia-automate-sim-to-real-assembly]] -- assembly-by-disassembly and DAgger
- [[sources/nvidia-isaac-groot-n1-foundation-model]] -- massive synthetic demonstration generation

---
title: "Source: AutoMate — Sim-to-Real Robotic Assembly (NVIDIA/USC)"
type: source-summary
source: "[[raw/nvidia-automate-sim-to-real-assembly]]"
related: ["[[concepts/sim-to-real-transfer]]", "[[concepts/reinforcement-learning]]", "[[concepts/imitation-learning]]", "[[entities/nvidia]]"]
tags: [sim-to-real, robotics, assembly, reinforcement-learning, nvidia]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "AutoMate achieves zero-shot sim-to-real transfer for robotic assembly with only 4.2% performance gap; trains specialist (86.5% real success) and generalist (84.5% real success) policies over 100 diverse assemblies using assembly-by-disassembly, RL with imitation, and curriculum learning."
---

## Key Points

- First simulation-based framework for learning specialist and generalist assembly skills across 100 diverse assemblies
- Assembly-by-Disassembly trick: record disassembly in simulation, reverse for training data
- Specialist policies: ~90% sim success, 86.5% real-world (only 4.2% sim-to-real gap)
- Generalist policies: 80.4% sim, 84.5% real-world (real actually exceeded sim by 4.1%)
- Zero-shot transfer: no post-real-world tuning needed
- Three-stage generalist training: Behavior Cloning → DAgger → Curriculum RL

## Detailed Summary

AutoMate from NVIDIA Seattle Robotics Lab and USC demonstrates that [[concepts/sim-to-real-transfer]] can work with minimal gap for complex robotic assembly. The framework addresses high-mix, low-volume manufacturing where robots must handle diverse parts.

The clever "assembly-by-disassembly" approach avoids the difficulty of collecting forward assembly demonstrations. Instead, 100 disassembly trajectories per assembly are recorded in simulation and reversed. RL with an imitation learning term (using Dynamic Time Warping to match demonstrations) trains specialist policies.

Generalist policies that handle multiple assemblies use a three-stage pipeline: behavior cloning from specialist demonstrations, DAgger (actively querying specialists), and curriculum RL with gradually increasing difficulty.

The real-world results are remarkable: specialist policies achieved 86.5% success with only a 4.2% sim-to-real gap, and the generalist policy actually performed better in reality (84.5%) than in simulation (80.4%). Deployment uses a Franka Panda arm with Intel RealSense camera and FoundationPose for 6D pose estimation.

## Metadata

- **Author**: NVIDIA, USC
- **Date Published**: 2025-06-10
- **Format**: article (technical blog)
- **URL**: https://developer.nvidia.com/blog/training-sim-to-real-transferable-robotic-assembly-skills-over-diverse-geometries/

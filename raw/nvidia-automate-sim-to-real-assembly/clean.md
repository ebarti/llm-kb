---
title: "AutoMate: Sim-to-Real Transferable Robotic Assembly Skills"
source: "https://developer.nvidia.com/blog/training-sim-to-real-transferable-robotic-assembly-skills-over-diverse-geometries/"
author: "NVIDIA, USC"
date_published: 2025-06-10
date_ingested: 2026-04-05
tags: [sim-to-real, robotics, assembly, domain-randomization, nvidia, reinforcement-learning]
type: article
status: raw
discovered_via: search
---

# AutoMate: Sim-to-Real Transfer for Robotic Assembly

First simulation-based framework for learning specialist and generalist assembly skills over a wide range of assemblies. Collaborative effort between USC and NVIDIA's Seattle Robotics Lab.

## Key Components

**Dataset**: 100 assemblies compatible with simulation and 3D-printable. Parts categorized as "plugs" and "sockets."

**Assembly-by-Disassembly**: Records 100 disassembly trajectories per assembly in simulation, then reverses for training data (avoids difficult forward assembly demonstrations).

**RL with Imitation Learning**: Imitation term augments reward function using maximum reward over all demonstrations. Dynamic Time Warping (DTW) maps end-effector paths to demonstration trajectories.

## Generalist Policy (3-stage)

1. Behavior Cloning from specialist demonstrations
2. DAgger: actively queries specialists at states visited by generalist
3. Curriculum RL: gradually reduces initial engagement difficulty

## Results

- Specialist (simulation): ~90% success on 55+ assemblies
- Specialist (real-world): 86.5% mean success (20 assemblies), sim-to-real gap only 4.2%
- Generalist (simulation): 80.4% success on 20 assemblies jointly
- Generalist (real-world): 84.5% mean success (exceeded simulation by 4.1%)

## Real-World Setup

Franka Panda arm + Intel RealSense camera. 6D pose estimation via FoundationPose. Zero-shot sim-to-real transfer without post-real-world tuning.

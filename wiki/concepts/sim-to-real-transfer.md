---
title: "Sim-to-Real Transfer"
type: concept
sources: ["[[sources/nvidia-automate-sim-to-real-assembly]]", "[[sources/deloitte-physical-ai-humanoid-robots-2026]]", "[[sources/nvidia-isaac-groot-n1-foundation-model]]", "[[sources/llms-for-robotics-survey-2025]]"]
related: ["[[concepts/foundation-models-for-robotics]]", "[[concepts/embodied-intelligence]]", "[[concepts/reinforcement-learning]]", "[[concepts/domain-randomization]]", "[[concepts/humanoid-robots]]"]
tags: [sim-to-real, simulation, robotics, domain-randomization, transfer-learning]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Training robot policies in simulation and deploying in the real world — addressing the persistent gap via domain randomization, digital twins, synthetic data at scale (NVIDIA: 780K trajectories in 11h), and curriculum learning; AutoMate achieves only 4.2% sim-to-real gap on assembly."
---

## Overview

Sim-to-real transfer is the practice of training robot control policies in simulated environments and deploying them on physical robots. Simulation offers a potentially infinite, safe, cheap data source -- but the gap between simulated and real-world physics consistently degrades transferred policy performance. Closing this gap is one of the critical infrastructure challenges for [[concepts/foundation-models-for-robotics]] and [[concepts/humanoid-robots]].

As Deloitte notes: "A robot might learn to grab something in simulation, but when it enters physical space, it's not a one-to-one match."

## Key Ideas

### The Sim-to-Real Gap

The gap arises from approximations in physics engines (friction, deformation, contact dynamics), visual differences (lighting, textures, sensor noise), and unmodeled real-world phenomena. Even small discrepancies accumulate across multi-step tasks.

### Key Techniques

**Domain Randomization**: Randomize simulation parameters (colors, textures, dynamics, lighting) to produce robust policies that generalize to real conditions. The policy learns to ignore variable aspects and focus on task-relevant features.

**Digital Twins**: High-fidelity virtual replicas of real environments. The virtual output corrects real-world output. NVIDIA Omniverse is the primary commercial platform.

**Massive Synthetic Data**: [[entities/nvidia-groot]] N1 generated 780,000 synthetic trajectories in 11 hours (= 9 months of continuous human demonstration), yielding 40% performance improvement when combined with real data. Scale compensates for individual trajectory fidelity.

**Curriculum Learning**: AutoMate's three-stage pipeline gradually reduces task difficulty in simulation, then transfers to increasingly realistic conditions. Generalist policy achieved 84.5% real-world success.

**Assembly-by-Disassembly**: A creative workaround -- record easy disassembly trajectories and reverse them, avoiding the difficulty of planning forward assembly paths in simulation.

### State of the Art: AutoMate Results

| Policy Type | Sim Success | Real Success | Sim-to-Real Gap |
|------------|-------------|-------------|-----------------|
| Specialist (20 assemblies) | ~90% | 86.5% | 4.2% |
| Generalist (20 assemblies) | 80.4% | 84.5% | -4.1% (real > sim!) |

The generalist policy performing better in reality than simulation is remarkable and suggests that real-world physical compliance can sometimes help where simulation dynamics are conservative.

### Physics Engines

- **NVIDIA Isaac Sim / Omniverse**: Commercial platform for high-fidelity simulation
- **Newton**: Open-source engine co-developed by NVIDIA, Google DeepMind, and Disney Research; optimized for robot learning
- **MuJoCo**: Long-standing research standard, now open-source (Google DeepMind)
- **Isaac Lab**: NVIDIA's RL framework built on Isaac Sim

## How It Connects

- [[concepts/foundation-models-for-robotics]] -- synthetic data is essential for scaling robot training
- [[concepts/embodied-intelligence]] -- sim-to-real is the training pipeline for embodied systems
- [[concepts/reinforcement-learning]] -- primary learning algorithm used in simulation
- [[concepts/humanoid-robots]] -- all major humanoid programs rely heavily on simulation
- [[concepts/physical-ai]] -- simulation gap is a primary implementation barrier

## Open Questions

- Will physics engines ever be accurate enough to eliminate the sim-to-real gap entirely?
- Is massive synthetic data (780K trajectories) a viable long-term substitute for real-world demonstrations?
- How should sim-to-real transfer handle deformable objects (cloth, food) where physics simulation is weakest?
- Can real-to-sim-to-real cycles (iteratively refining simulation from real-world failures) become automated?

## Sources

- [[sources/nvidia-automate-sim-to-real-assembly]] -- state-of-the-art results with 4.2% gap
- [[sources/deloitte-physical-ai-humanoid-robots-2026]] -- industry perspective on the gap as a barrier
- [[sources/nvidia-isaac-groot-n1-foundation-model]] -- massive synthetic data generation
- [[sources/llms-for-robotics-survey-2025]] -- survey of transfer approaches

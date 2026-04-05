---
title: "Humanoid Robots"
type: concept
sources: ["[[sources/deloitte-physical-ai-humanoid-robots-2026]]", "[[sources/tesla-optimus-humanoid-robot]]", "[[sources/figure-ai-humanoid-robots]]", "[[sources/nvidia-isaac-groot-n1-foundation-model]]"]
related: ["[[concepts/physical-ai]]", "[[concepts/embodied-intelligence]]", "[[concepts/dexterous-manipulation]]", "[[concepts/vision-language-action-models]]", "[[concepts/sim-to-real-transfer]]"]
tags: [humanoid-robots, robotics, market-analysis, form-factor]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Human-shaped robots designed to navigate existing infrastructure without modification; market projected at $30-50B by 2035 (UBS); key players include Tesla Optimus ($20-30K target), Figure AI ($39B valuation), Boston Dynamics Atlas, 1X NEO, and Unitree; form factor wins on infrastructure compatibility."
---

## Overview

Humanoid robots are designed in human form primarily for infrastructure compatibility: they can navigate doorways, staircases, factory floors, and home kitchens without costly modifications to existing environments. The market is at an inflection point, with UBS projecting 2 million humanoids in workplaces by 2035, growing to 300 million by 2050, with a total addressable market of $30-50 billion by 2035 and $1.4-1.7 trillion by 2050.

## Key Ideas

### Why Humanoid Form?

Jonathan Hurst (Oregon State / Agility Robotics) explains: "People are very compliant in how they interact with the world and constantly make contact with their environment. That's very hard for a commercial robot...a bipedal pair of legs is the most effective way to be dynamically stable."

The humanoid form factor wins when:
- The task requires navigating human-designed spaces
- [[concepts/dexterous-manipulation]] with two arms is needed
- The robot must use existing human tools
- Human-robot interaction is a key requirement

### Major Players (2026)

| Company | Robot | Key Specs | Price Target | Status |
|---------|-------|-----------|-------------|--------|
| [[entities/tesla-optimus]] | Optimus Gen 3 | 22 DOF hands, 125 lb, FSD AI | $20-30K | Production summer 2026 |
| [[entities/figure-ai]] | Figure 02/03 | 35 DOF, 16 DOF hands, Helix VLA | -- | BotQ: 12K/year target |
| [[entities/boston-dynamics]] | Electric Atlas | Full-body, DeepMind Gemini AI | $140-150K | Commercial 2026-2028 |
| 1X Technologies | NEO | Consumer-oriented | -- | First deliveries 2026 |
| Unitree Robotics | G1, H2, R1 | Mass-market lineup | -- | Commercial |
| Agility Robotics | Digit | Warehouse-focused | -- | Deployed (Amazon) |

### Cost Trajectory

- Current material cost: ~$35,000 (2025)
- Goldman Sachs: 40% manufacturing cost drop 2023-2024
- Bank of America: $13,000-17,000 per unit next decade
- [[entities/tesla-optimus]] long-term target: under $20,000

### Training Approaches

Humanoid robots are trained through a combination of:
- [[concepts/imitation-learning]] from human demonstrations (teleoperation, motion capture)
- [[concepts/sim-to-real-transfer]] using massive synthetic data (NVIDIA: 780K trajectories in 11h)
- [[concepts/reinforcement-learning]] in simulation with domain randomization
- [[concepts/foundation-models-for-robotics]] providing general capabilities

MIT Technology Review reports a growing gig economy of workers training humanoid robots from home using teleoperation rigs.

### Deployment Timeline

- 2025-2026: Hundreds to low thousands deployed industrially (factories, warehouses)
- 2027-2028: Scaling to tens of thousands
- 2027-2030: First home humanoid robots ($20-50K)
- 2035: 2 million in workplaces (UBS)
- 2050: 300 million (UBS)

## How It Connects

- [[concepts/physical-ai]] -- humanoids are the flagship form factor
- [[concepts/dexterous-manipulation]] -- the critical capability gap for humanoids
- [[concepts/vision-language-action-models]] -- the AI "brains" (RT-2, π0, GR00T, Helix)
- [[concepts/sim-to-real-transfer]] -- essential training infrastructure
- [[concepts/embodied-intelligence]] -- the underlying paradigm
- [[concepts/foundation-models-for-robotics]] -- enabling generalist capabilities

## Open Questions

- Will humanoid form factor dominate, or will task-specific morphologies win for most applications?
- Can manufacturing costs reach the $10-20K level needed for consumer adoption?
- How will safety be certified for robots operating alongside humans?
- Will teleoperation remain a dependency, or will full autonomy arrive at scale?
- Rodney Brooks (2025): "pure fantasy thinking" -- is the skepticism warranted?

## Sources

- [[sources/deloitte-physical-ai-humanoid-robots-2026]] -- market projections and deployment analysis
- [[sources/tesla-optimus-humanoid-robot]] -- Tesla's development and criticism
- [[sources/figure-ai-humanoid-robots]] -- Figure AI's rapid rise and Helix pivot
- [[sources/nvidia-isaac-groot-n1-foundation-model]] -- NVIDIA's open platform adopted by major players

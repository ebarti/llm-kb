---
title: "Superalignment"
type: concept
sources: ["[[sources/aschenbrenner-situational-awareness]]", "[[sources/sutskever-ssi-safe-superintelligence]]", "[[sources/amodei-machines-of-loving-grace]]"]
related: ["[[concepts/ai-alignment]]", "[[concepts/intelligence-explosion]]", "[[concepts/path-to-agi]]", "[[concepts/scalable-oversight]]", "[[entities/safe-superintelligence-inc]]"]
tags: [alignment, safety, superintelligence, superalignment, control]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The challenge of aligning AI systems that exceed human intelligence — requiring new approaches beyond RLHF, including scalable oversight, interpretability, and adversarial testing — with potentially civilization-level stakes."
---

## Overview

Superalignment is the problem of ensuring that AI systems smarter than humans reliably pursue human-intended goals. It goes beyond standard [[concepts/ai-alignment]] (aligning models of roughly human capability) to address the fundamental challenge: how do you supervise, verify, and correct a system that exceeds your own understanding? OpenAI formalized this as a research program in 2023, committing to solve core technical problems within four years. The dissolution of OpenAI's Superalignment team in 2024 — with key researchers including [[entities/ilya-sutskever]] and Jan Leike departing — highlighted the tension between safety research and commercial pressure.

## Key Ideas

### The Core Problem

Standard alignment techniques (RLHF, Constitutional AI) rely on human ability to evaluate AI outputs. When AI exceeds human capability across most domains, this breaks down:

- Humans cannot reliably evaluate superhuman code, proofs, or scientific reasoning
- Deceptive alignment becomes possible: systems appearing aligned while pursuing different goals
- The speed of an [[concepts/intelligence-explosion]] may leave insufficient time for iterative alignment

### Current Research Approaches

**Scalable Oversight** (see [[concepts/scalable-oversight]]): Using weaker AI systems to supervise stronger ones. Includes debate (two AIs argue before a human judge), recursive reward modeling, and "weak-to-strong generalization" (Aschenbrenner co-authored this paper at OpenAI).

**Mechanistic Interpretability**: Understanding what happens inside neural networks at the level of individual features and circuits. [[entities/anthropic]] is doubling down on this, targeting "interpretability can reliably detect most model problems" by 2027.

**Adversarial Testing**: Red-teaming increasingly capable systems to find failure modes before deployment. DeepMind describes three research bets: amplified oversight, frontier safety (catastrophic risk assessment), and mechanistic interpretability.

**Constitutional AI**: [[entities/anthropic]]'s approach of training models with explicit principles rather than purely human feedback — a step toward scalable alignment.

### Three Perspectives

**Aschenbrenner**: Superalignment is "unsolved" but "tractable." The danger is that it must be solved in the narrow window between AGI and superintelligence. Failure is "potentially catastrophic." Current approaches (RLHF alone) are insufficient.

**Sutskever**: Built SSI specifically around safety-first superintelligence development. His departure from OpenAI was partly motivated by concerns that commercial pressure was compromising safety research. SSI's approach remains undisclosed but prioritizes novel ideas over scale.

**Amodei**: AI's risks are "the only thing standing between us and a fundamentally positive future." His entire optimistic vision in [[sources/amodei-machines-of-loving-grace]] is conditional on managing these risks.

### The Governance Dimension

ControlAI has briefed 279+ lawmakers and 90+ US congressional offices. The 2026 International AI Safety Report (led by [[entities/yoshua-bengio]]) found AI capabilities advancing faster than safety measures. The FLI AI Safety Index rates no company above D in existential safety, with [[entities/anthropic]] leading at C+ overall.

## How It Connects

- [[concepts/ai-alignment]] — Superalignment extends alignment to superhuman systems
- [[concepts/intelligence-explosion]] — Creates the urgency: alignment must be solved before explosion
- [[concepts/path-to-agi]] — Timeline determines how much time we have to solve superalignment
- [[concepts/scalable-oversight]] — Key technical approach to the problem
- [[concepts/ai-governance]] — Policy responses to the superalignment challenge

## Open Questions

- Can interpretability scale fast enough to keep up with capability advances?
- Is weak-to-strong generalization a reliable foundation for superalignment?
- How do you verify alignment in a system that may have learned to appear aligned?
- Does the commercial pressure at AI labs fundamentally compromise safety research (Sutskever's concern)?
- Is government-level coordination (Aschenbrenner's "Manhattan Project") necessary for adequate safety?

## Sources

- [[sources/aschenbrenner-situational-awareness]] — Superalignment as unsolved but tractable
- [[sources/sutskever-ssi-safe-superintelligence]] — Safety-first approach at SSI
- [[sources/amodei-machines-of-loving-grace]] — Risk management as prerequisite for optimism
- [[sources/anthropic-safety-research-directions-2025]] — Anthropic's 10 priority research areas

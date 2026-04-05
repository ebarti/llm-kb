---
title: "Constitutional AI (CAI)"
type: concept
sources: ["[[sources/anthropic-constitutional-ai]]", "[[sources/wolfe-rlaif-reinforcement-learning-ai-feedback]]", "[[sources/argilla-rlhf-alternatives-overview]]", "[[sources/ai-safety-alignment-progress-2025]]", "[[sources/anthropic-safety-research-directions-2025]]"]
related: ["[[concepts/rlaif]]", "[[concepts/rlhf]]", "[[concepts/scalable-oversight]]", "[[concepts/ai-alignment]]", "[[concepts/ai-safety]]", "[[concepts/reward-model]]", "[[concepts/ppo-for-llms]]", "[[entities/anthropic]]", "[[entities/claude]]"]
last_compiled: 2026-04-05
summary: "Anthropic's approach to aligning AI using a written set of principles (a constitution) that enables AI self-critique, self-revision, and AI-generated preference labels -- reducing reliance on human labelers while producing harmless yet non-evasive assistants."
---

## Overview

Constitutional AI (CAI), introduced by [[entities/anthropic]] in December 2022 (Bai et al.), is the alignment technique that addresses a fundamental tension in [[concepts/rlhf]]: how do you scale human oversight as AI capabilities grow? The answer is to write down the rules (a "constitution") and let the AI supervise itself against those rules.

CAI combines two innovations:
1. **Supervised self-critique**: The AI critiques and revises its own harmful outputs using constitutional principles
2. **[[concepts/rlaif]]**: AI-generated preference labels replace human harmlessness annotations for RL training

The result is an AI that is harmless without being evasive -- it engages with difficult queries by explaining its reasoning rather than simply refusing. This is the foundational technique behind [[entities/claude]]'s alignment.

## The Constitution

The constitution is a set of high-level normative principles drawn from diverse sources including the UN Declaration of Human Rights, Apple's Terms of Service, and Anthropic's own HHH (helpful, harmless, honest) framework. Example principles:
- "Choose the response that is most helpful to the human"
- "Choose the response that is least harmful or toxic"
- "Choose the response that is most honest and truthful"

The constitution is **inspectable and modifiable**, making behavioral guidelines transparent and auditable. In 2023, Anthropic extended this via **Collective Constitutional AI**, where ~1,000 Americans contributed to the principles guiding Claude's behavior -- democratizing the alignment process.

## How It Works

CAI operates in two phases:

### Phase 1: Supervised Self-Critique
1. The model generates a response to a prompt
2. The model critiques its own response against constitutional principles (e.g., "Choose the response that is most helpful, honest, and harmless")
3. The model revises the response based on its own critique
4. This process may iterate multiple times

### Phase 2: Reinforcement Learning from AI Feedback ([[concepts/rlaif]])
1. The model generates pairs of responses from the Phase 1 fine-tuned model
2. An AI evaluator (guided by constitutional principles) selects the preferred response, using **chain-of-thought reasoning** to explain why one response better adheres to the constitution
3. A [[concepts/reward-model]] is trained on these AI-generated preferences
4. The original model is optimized against this reward model via [[concepts/ppo-for-llms]]

The chain-of-thought step is a key innovation: by requiring the AI evaluator to reason about why one response is better, the quality of preference labels improves significantly. Anthropic retains human feedback for the helpfulness dimension while automating the harmlessness dimension.

## Why It Matters

CAI addresses fundamental bottlenecks in RLHF:

| Challenge | RLHF | Constitutional AI |
|-----------|------|-------------------|
| **Scaling** | Cost grows linearly with human evaluators | Self-critique scales with compute |
| **Consistency** | Annotators disagree; cultural biases | Principles are explicit and uniform |
| **Speed** | Limited by human evaluation throughput | AI evaluation is near-instant |
| **Transparency** | Implicit preferences in reward model | Explicit principles are auditable |
| **Adaptability** | Retraining requires new human data | Update the constitution text |

## Limitations

- **Principle specification**: The constitution must be written carefully; ambiguous or conflicting principles produce ambiguous behavior
- **Not a complete solution**: CAI cannot solve alignment under capability scaling, distributional shift, and increasing autonomy
- **Self-critique ceiling**: A model cannot critique itself beyond its own understanding
- **Constitutional completeness**: No finite set of principles can anticipate every situation

## Current Usage

Production systems at Anthropic and others now layer multiple alignment approaches: constitutional principles for broad behavioral guidance, RLHF for fine-grained preference tuning, automated [[concepts/red-teaming]] for adversarial probing, and [[concepts/human-in-the-loop]] oversight for high-stakes decisions ([[sources/ai-safety-alignment-progress-2025]]).

The central enterprise AI challenge in 2026 is "behavioral reliability" — ensuring an AI system remains consistently helpful, truthful, and safe even as its autonomy increases.

## Relationship to RLAIF

Constitutional AI pioneered [[concepts/rlaif]] as a practical technique. It demonstrated that AI-generated preference labels for harmlessness achieve comparable quality to human labels, opening the door to fully automated alignment pipelines. Later work (Google's RLAIF paper, 2023) showed RLAIF achieves approximately 50% win rate vs RLHF -- statistical parity -- across summarization and dialogue tasks.

## Sources
- [[sources/anthropic-constitutional-ai]] — the foundational paper
- [[sources/wolfe-rlaif-reinforcement-learning-ai-feedback]] — RLAIF technical details and experimental results
- [[sources/argilla-rlhf-alternatives-overview]] — CAI positioned in the landscape of alignment methods
- [[sources/ai-safety-alignment-progress-2025]] — CAI as evolution beyond RLHF in production
- [[sources/anthropic-safety-research-directions-2025]] — research directions building on CAI foundations

## Related Concepts
- [[concepts/rlaif]] — the automated feedback mechanism CAI uses
- [[concepts/rlhf]] — the technique CAI extends and partially replaces
- [[concepts/scalable-oversight]] — the problem CAI addresses
- [[concepts/ai-alignment]] — the broader alignment problem
- [[concepts/ai-safety]] — safety as the goal of constitutional principles
- [[concepts/reward-model]] — trained on AI-generated preferences in Phase 2
- [[entities/anthropic]] — the organization that developed CAI
- [[entities/claude]] — the production system built on CAI

---
title: "RLHF vs Constitutional AI"
type: comparison
subjects: ["[[concepts/ai-alignment]]", "[[concepts/constitutional-ai]]"]
sources: ["[[sources/ai-safety-alignment-progress-2025]]", "[[sources/anthropic-safety-research-directions-2025]]"]
last_compiled: 2026-04-05
summary: "Comparison of RLHF (human preference labels) and Constitutional AI (principle-guided self-critique): trade-offs in scalability, consistency, transparency, and alignment robustness."
---

## Overview

RLHF (Reinforcement Learning from Human Feedback) and Constitutional AI (CAI) are the two dominant paradigms for aligning language models with human values. RLHF relies on human evaluators to label preferred outputs; CAI uses a written set of principles (a "constitution") for AI self-critique. In practice, modern production systems combine both approaches ([[sources/ai-safety-alignment-progress-2025]]).

## Comparison Table

| Dimension | RLHF | Constitutional AI |
|-----------|------|-------------------|
| **Feedback source** | Human labelers rate output pairs | AI evaluates against written principles |
| **Scalability** | Limited by human evaluation throughput | Scales with compute |
| **Cost** | High — grows linearly with data needs | Lower marginal cost after constitution design |
| **Consistency** | Variable — annotators disagree | Uniform — principles are fixed |
| **Cultural bias** | Annotator demographics shape preferences | Constitution can be explicit about values |
| **Transparency** | Implicit preferences in reward model | Explicit, auditable principles |
| **Adaptability** | Requires new human data for changes | Update the constitution text |
| **Self-critique** | No — external evaluation only | Yes — model critiques its own output |
| **Ceiling** | Limited by human evaluator quality | Limited by model's self-understanding |
| **Proven track record** | Widely used since 2022; well-studied | Newer; Anthropic-pioneered |

## When to Use Each

### RLHF is better when:
- Fine-grained human preferences matter (nuanced style, tone, domain expertise)
- The task domain is narrow enough for consistent human evaluation
- You need established, well-understood methodology
- Budget allows for ongoing human evaluation

### Constitutional AI is better when:
- Scaling to large volumes of alignment data
- Consistency across evaluations is critical
- You want auditable, explicit alignment criteria
- Rapid iteration on alignment principles is needed
- Human evaluation is too expensive or inconsistent

### Production reality (2025-2026):
Modern systems layer both: constitutional principles for broad behavioral guidance + RLHF for fine-grained preference tuning + automated [[concepts/red-teaming]] + [[concepts/human-in-the-loop]] oversight ([[sources/ai-safety-alignment-progress-2025]]).

## Limitations of Both

Neither approach solves alignment under:
- **Capability scaling**: As models become much smarter than evaluators (human or AI)
- **Distributional shift**: New deployment contexts not covered by training
- **Increasing autonomy**: Agentic systems operating beyond oversight reach
- **Deceptive alignment**: Models that appear aligned during evaluation but behave differently in deployment

This is why [[concepts/scalable-oversight]] remains an active research frontier ([[sources/anthropic-safety-research-directions-2025]]).

## Sources
- [[sources/ai-safety-alignment-progress-2025]] — production alignment stack combining both approaches
- [[sources/anthropic-safety-research-directions-2025]] — research frontiers beyond current alignment methods

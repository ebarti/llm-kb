---
title: "Democratic AI Alignment"
type: concept
sources: ["[[sources/cip-whitepaper-collective-intelligence]]", "[[sources/cip-generative-ai-digital-commons]]", "[[sources/wisdom-of-the-crowd]]"]
related: ["[[concepts/collective-intelligence]]", "[[concepts/wisdom-of-crowds]]", "[[concepts/knowledge-commons]]", "[[entities/collective-intelligence-project]]"]
last_compiled: 2026-04-05
summary: "Using collective intelligence mechanisms — citizens' assemblies, quadratic voting, liquid democracy, deliberative platforms — to align AI systems with collective values rather than designer preferences or market incentives alone."
---

## Overview

Democratic AI alignment applies [[concepts/collective-intelligence]] mechanisms to the problem of aligning AI systems with human values. Rather than relying on a small team of AI developers to define what AI should optimize for, democratic alignment gathers structured input from diverse publics to shape AI behavior, governance, and values.

The key insight: if AI systems are trained on the collective outputs of humanity and impact all of humanity, their alignment should reflect collective input — not just the preferences of their creators.

## Key Ideas

### Collective Constitutional AI

The landmark project: Anthropic and the [[entities/collective-intelligence-project]] ran a deliberative process with ~1,000 Americans to draft a constitution for Claude. Participants debated, voted, and refined principles that were then used to fine-tune the AI system. This demonstrated that:
- Public deliberation can produce actionable AI alignment specifications
- Crowd-sourced values differ meaningfully from developer-chosen values
- The process is operationally feasible at scale

### Value Elicitation Mechanisms

CIP's toolkit ([[sources/cip-whitepaper-collective-intelligence]]):
- **Quadratic voting**: Participants allocate a budget of "voice credits" across options; cost increases quadratically, preventing domination by intense minorities
- **Liquid democracy**: Delegate your vote to trusted experts on specific topics; recursive delegation
- **Citizens' assemblies**: Representative samples deliberate on specific questions
- **Pol.is**: Open-ended deliberative platform that identifies clusters of agreement
- **Prediction markets**: Aggregate beliefs about likely outcomes

### Global Dialogues

CIP's Global Dialogues bring 1,000 participants from 70+ countries every two months for conversations about AI's societal role. Using Remesh's platform, these sessions capture real-time perspectives across language barriers — scaling deliberation beyond any single national or cultural context.

### Alignment Assemblies

Since February 2023, CIP has run "alignment assemblies" with AI labs and government partners: structured deliberations that help "create AI that supports the public good by involving the public in defining what 'good' is."

### The Aggregation Challenge

Democratic alignment inherits all the challenges of [[concepts/wisdom-of-crowds]]:
- **Diversity requirement**: Participants must represent genuinely diverse perspectives
- **Independence**: Deliberation processes must prevent herding and social influence
- **Aggregation quality**: Mechanisms must combine perspectives without flattening them
- **Strategic behavior**: Participants may misrepresent preferences

The "surprisingly popular" algorithm and other advanced aggregation methods may help extract collective wisdom more effectively than simple majority voting.

## Relationship to Existing Alignment Approaches

| Approach | Source of Values | Scale | Diversity |
|----------|-----------------|-------|-----------|
| RLHF (standard) | Trained annotators | Hundreds | Low |
| Constitutional AI (original) | Developer-written | One team | Very low |
| **Collective Constitutional AI** | Public deliberation | Thousands | High |
| **Alignment Assemblies** | Representative samples | Hundreds per session | Designed high |
| **Global Dialogues** | International participants | Thousands | Very high |

## Sources

- [[sources/cip-whitepaper-collective-intelligence]] — the CI framework for alignment
- [[sources/cip-generative-ai-digital-commons]] — governance proposals for AI/commons relationship
- [[sources/wisdom-of-the-crowd]] — the aggregation mechanisms underlying democratic alignment

## Related Concepts

- [[concepts/collective-intelligence]] — the capability democratic alignment deploys
- [[concepts/wisdom-of-crowds]] — the aggregation mechanisms used
- [[concepts/knowledge-commons]] — the shared resources alignment protects
- [[concepts/collaborative-knowledge-building]] — deliberative knowledge creation

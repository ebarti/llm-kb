---
title: "Source: ReAct — Synergizing Reasoning and Acting in Language Models"
type: source-summary
source: "[[raw/react-prompting-framework]]"
related: ["[[concepts/react-pattern]]", "[[concepts/agent-planning]]", "[[concepts/reflection-pattern]]"]
last_compiled: 2026-04-05
summary: "Foundational ReAct paper (Yao et al. 2022): interleaving reasoning traces and actions enables LLM agents to plan dynamically, outperforming CoT and action-only approaches."
reading_time: "1 min"
---

## Key Points

- ReAct interleaves reasoning traces and task-specific actions: Thought → Action → Observation → repeat
- Outperforms Chain-of-Thought on tasks requiring external information (less hallucination)
- Outperforms action-only methods on complex decision-making tasks (better planning)
- Hybrid ReAct + CoT + self-consistency yields best overall performance
- ReAct + Reflexion completes 130/134 tasks vs. ReAct alone

## Detailed Summary

The ReAct framework (Yao et al., 2022) introduced a paradigm for [[concepts/llm-agent-architecture]] that interleaves reasoning and acting. The key insight is that reasoning traces help the model track and update action plans, while actions allow it to retrieve real-world information — creating a dynamic feedback loop.

Compared to Chain-of-Thought (CoT), ReAct mitigates fact hallucination through information retrieval. Compared to action-only approaches, ReAct maintains strategic planning by articulating goals before acting. The combination of ReAct with Reflexion achieves near-perfect task completion (130/134 tasks).

## Related Concepts

- [[concepts/react-pattern]] — the core pattern described
- [[concepts/agent-planning]] — ReAct as a planning mechanism
- [[concepts/reflection-pattern]] — Reflexion builds on ReAct

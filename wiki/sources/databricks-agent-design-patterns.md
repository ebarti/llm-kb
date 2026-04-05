---
title: "Source: Agent System Design Patterns (Databricks)"
type: source-summary
source: "[[raw/databricks-agent-design-patterns]]"
related: ["[[concepts/agent-orchestration]]", "[[concepts/llm-agent-architecture]]", "[[concepts/multi-agent-systems]]"]
last_compiled: 2026-04-05
summary: "Databricks design pattern spectrum from simple LLM+prompt through deterministic chains, single-agent, to multi-agent systems with orchestrator-worker, supervisor, and router patterns."
reading_time: "1 min"
---

## Key Points

- Four-level pattern spectrum: LLM+Prompt → Deterministic Chain → Single-Agent → Multi-Agent
- Single-agent often optimal for enterprise: simpler than multi-agent yet allowing dynamic logic
- Multi-agent orchestration patterns: orchestrator-worker, supervisor, router
- Four core orchestration components: registry, router, state store, supervisor
- Best practice: start with simplest pattern meeting requirements, add complexity gradually

## Detailed Summary

Databricks provides a pragmatic guide to [[concepts/agent-orchestration]] with a clear progression from simplest to most complex patterns. The single-agent system is highlighted as often optimal for enterprise use cases — complex enough for dynamic decision-making but simpler than multi-agent overhead.

The multi-agent patterns (orchestrator-worker, supervisor, router) each have specific use cases. The orchestrator-worker is "the most deployed multi-agent pattern in production." Advanced routers use multi-armed bandit algorithms to balance exploration and exploitation.

Practical guidance includes starting simple, maintaining clear prompts, sandboxing risky actions, pinning model versions, and implementing comprehensive logging.

## Related Concepts

- [[concepts/agent-orchestration]] — the core topic
- [[concepts/llm-agent-architecture]] — the design pattern spectrum
- [[concepts/multi-agent-systems]] — multi-agent patterns detailed

---
title: "Source: Agentic Memory — Unified LTM and STM Management for LLM Agents"
type: source-summary
source: "[[raw/agentic-memory-unified-framework]]"
related: ["[[concepts/agent-memory]]", "[[concepts/llm-agent-architecture]]"]
last_compiled: 2026-04-05
summary: "AgeMem paper (2026): unified framework exposing memory operations as tool-based actions, trained via three-stage RL, outperforming baselines across five long-horizon benchmarks."
reading_time: "1 min"
---

## Key Points

- AgeMem unifies long-term and short-term memory as integrated agent tool actions
- Progressive three-stage reinforcement learning handles sparse reward signals
- Agent autonomously decides what to store, retrieve, update, summarize, or discard
- Consistent improvements over memory-augmented baselines across five benchmarks
- Shifts from fixed heuristics to learned, adaptive memory behavior

## Detailed Summary

The AgeMem paper (January 2026, arXiv:2601.01885) addresses the critical challenge that LLMs are stateless — they don't retain information between API calls. Rather than treating memory as a separate middleware layer, AgeMem exposes memory operations (store, retrieve, update, summarize, discard) as callable tools within the agent's action space.

The key innovation is that the agent learns when and what to memorize through reinforcement learning, rather than relying on hard-coded heuristics. A three-stage progressive training strategy handles the challenge of sparse and discontinuous reward signals from memory operations.

This represents a convergence between [[concepts/agent-memory]] and [[concepts/tool-use]] — memory becomes just another tool the agent can invoke.

## Related Concepts

- [[concepts/agent-memory]] — the core concept
- [[concepts/tool-use]] — memory as tool actions
- [[concepts/llm-agent-architecture]] — memory as architectural component

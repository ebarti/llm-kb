---
title: "Source: Andrew Ng on Agentic Design Patterns"
type: source-summary
source: "[[raw/ng-agentic-design-patterns]]"
related: ["[[concepts/agentic-workflows]]", "[[concepts/reflection-pattern]]", "[[concepts/tool-use]]", "[[concepts/agent-planning]]", "[[entities/andrew-ng]]"]
last_compiled: 2026-04-05
summary: "Andrew Ng's four agentic design patterns (reflection, tool use, planning, multi-agent collaboration) plus enterprise strategy: architecture matters more than model size."
reading_time: "2 min"
---

## Key Points

- Four core patterns: Reflection, Tool Use, Planning, Multi-Agent Collaboration
- Key insight: GPT-3.5 with agentic workflow outperforms GPT-4 zero-shot — architecture > model size
- Reflection is "relatively quick to implement" with "surprising performance gains"
- Enterprise advice: build applications, don't chase models; costs decreasing ~80% YoY
- Start with best available model, optimize later

## Detailed Summary

Andrew Ng's influential framework identifies four [[concepts/agentic-workflows]] design patterns that drive AI progress "perhaps even more than the next generation of foundation models."

The [[concepts/reflection-pattern]] is the most immediately actionable: prompt the LLM to generate output, then critique it, then rewrite based on the critique, iterating. This can be implemented with two agents (generator + critic) and extended with tool integration (running code against tests). Ng describes it as quick to implement with surprising performance gains.

The remaining three patterns — [[concepts/tool-use]], [[concepts/agent-planning]], and [[concepts/multi-agent-systems]] collaboration — complete the framework. Together they enable AI systems to decompose complex problems, leverage external capabilities, and collaborate through specialization.

Ng's strategic message to enterprises is clear: stop chasing model leaderboards and start building applications. An older model running inside an agentic workflow can outperform a more advanced model using zero-shot prompting.

## Notable Quotes

> "GPT-3.5 with an agentic workflow could outperform a more advanced foundational model like GPT-4 using a zero-shot approach."

## Related Concepts

- [[concepts/agentic-workflows]] — the overarching paradigm Ng advocates
- [[concepts/reflection-pattern]] — first and most accessible pattern
- [[concepts/tool-use]] — second pattern
- [[concepts/agent-planning]] — third pattern
- [[concepts/multi-agent-systems]] — fourth pattern (already exists, to be updated)

---
title: "Agent Memory"
type: concept
sources: ["[[sources/agentic-memory-unified-framework]]", "[[sources/superannotate-llm-agents-guide]]"]
related: ["[[concepts/llm-agent-architecture]]", "[[concepts/tool-use]]", "[[concepts/temporal-knowledge]]"]
last_compiled: 2026-04-05
summary: "Short-term and long-term memory systems for LLM agents: from simple conversation history to learned, adaptive memory management via AgeMem's tool-based RL approach."
---

## Overview

Memory is a core component of [[concepts/llm-agent-architecture]] that provides contextual continuity across an agent's interactions. LLMs are fundamentally stateless — they don't retain information between API calls. Memory systems must be built on top to give agents the ability to recall past interactions, learn from experience, and maintain context during multi-step tasks.

The memory challenge is acute because of the tension between context window limits (finite attention span) and the need for agents to reason over long histories of actions and observations.

## Memory Types

### Short-Term Memory (Working Memory)

Short-term memory holds information relevant to the agent's current task. Analogous to human working memory or computer RAM, it:

- Maintains the current conversation history
- Tracks immediate task goals and progress
- Stores intermediate reasoning steps and tool results
- Is cleared upon task completion or session end
- Typically implemented as the LLM's context window content

The main limitation is the context window size. As conversations grow, older context must be summarized or dropped, potentially losing important information.

### Long-Term Memory (Persistent Memory)

Long-term memory persists across sessions and tasks. It enables agents to:

- Learn user preferences and adapt behavior over time
- Recall relevant past interactions
- Build accumulated knowledge and expertise
- Store reusable skills and procedures

Implementation approaches include:
- **Vector databases**: Semantic search over past interactions (see [[concepts/vector-databases]])
- **Key-value stores**: Explicit fact storage (e.g., user preferences)
- **Knowledge graphs**: Structured relationships between entities (see [[concepts/knowledge-graph]])
- **Temporal graphs**: Time-windowed facts (see [[concepts/temporal-knowledge]])

### Episodic vs. Semantic Memory

Some frameworks further distinguish:
- **Episodic memory**: Specific past experiences (what happened in conversation X)
- **Semantic memory**: General knowledge extracted from experiences (user prefers Python over Java)
- **Procedural memory**: Learned skills and procedures (how to deploy a service)

## AgeMem: Unified Memory as Tool Use

The AgeMem framework (January 2026, arXiv:2601.01885) represents a significant advance by treating memory operations as tools the agent can invoke:

- **Store**: Save information to long-term memory
- **Retrieve**: Query long-term memory for relevant information
- **Update**: Modify existing memory entries
- **Summarize**: Compress detailed memories into summaries
- **Discard**: Remove outdated or irrelevant memories

Rather than using hard-coded heuristics (e.g., "always summarize after 10 turns"), AgeMem trains the agent via reinforcement learning to autonomously decide what to remember and when. This produces better task performance, higher-quality memory retention, and more efficient context utilization across five long-horizon benchmarks.

This approach represents a convergence of [[concepts/agent-memory]] and [[concepts/tool-use]] — memory becomes just another tool in the agent's action space.

## The Fundamental Challenge

The core tension in agent memory design:
- **Too much memory**: Overloads the context window, slowing inference and increasing cost
- **Too little memory**: Loses important context, making the agent forgetful
- **Wrong memory**: Retrieving irrelevant information wastes context space and can mislead reasoning

Products like ChatGPT and Claude solve this at the application layer, but developers building custom agents must implement memory management themselves.

## Sources

- [[sources/agentic-memory-unified-framework]] — AgeMem unified framework
- [[sources/superannotate-llm-agents-guide]] — memory as agent component

## Related Concepts

- [[concepts/llm-agent-architecture]] — memory as core component
- [[concepts/tool-use]] — memory operations as tool actions (AgeMem)
- [[concepts/temporal-knowledge]] — time-aware memory management

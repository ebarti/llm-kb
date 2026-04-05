---
title: "Agent Planning"
type: concept
sources: ["[[sources/superannotate-llm-agents-guide]]", "[[sources/ng-agentic-design-patterns]]", "[[sources/react-prompting-framework]]", "[[sources/databricks-agent-design-patterns]]"]
related: ["[[concepts/llm-agent-architecture]]", "[[concepts/react-pattern]]", "[[concepts/reflection-pattern]]", "[[concepts/agentic-workflows]]", "[[concepts/multi-agent-systems]]"]
last_compiled: 2026-04-05
summary: "How LLM agents decompose complex goals into executable subtask sequences using Chain of Thought, Tree of Thought, and task decomposition, with feedback loops via ReAct and Reflexion."
---

## Overview

Planning is the capability that enables LLM agents to break down complex goals into manageable, executable steps. Without planning, an agent would attempt to solve every problem in a single action — which fails for any task requiring multiple steps, information gathering, or iterative refinement.

Planning operates at two levels within [[concepts/llm-agent-architecture]]:

1. **Formulation**: Decomposing objectives into subtasks
2. **Reflection**: Evaluating and improving plans based on feedback

## Formulation Approaches

### Chain of Thought (CoT)
The simplest planning approach: prompt the LLM to "think step by step." The model generates a linear sequence of reasoning steps before producing a final answer. Effective for straightforward multi-step problems but limited by its sequential, single-path nature.

### Tree of Thought (ToT)
Extends CoT by exploring multiple solution pathways simultaneously. The model generates several possible next steps, evaluates each, and selects the most promising path. This allows backtracking when a path proves unproductive — more robust but more expensive.

### Task Decomposition
Explicitly break a complex objective into a list of subtasks, optionally with dependencies between them. Each subtask can be assigned to a different tool or sub-agent. This is the approach used in [[concepts/agent-orchestration]] patterns like orchestrator-worker.

### Hierarchical Planning
For very complex goals, planning can be hierarchical: a high-level plan decomposes into subgoals, each of which is further decomposed into concrete actions. This mirrors how human project management works.

## Feedback Mechanisms

Plans rarely survive first contact with reality. Feedback mechanisms enable adaptive planning:

### ReAct Loop
The [[concepts/react-pattern]] interleaves planning with execution: the agent reasons about the next step, takes an action, observes the result, and adjusts its plan accordingly. This is inherently adaptive — plans evolve based on real-world feedback.

### Reflexion
After a complete execution attempt, the [[concepts/reflection-pattern]] evaluates what worked and what failed, generating verbal feedback that informs the next planning cycle. This enables learning from mistakes without weight updates.

### External Feedback
Plans can be evaluated against external criteria:
- Code plans tested against unit tests
- Research plans validated against search results
- Mathematical plans checked against calculators

## Planning Challenges

- **Horizon length**: LLMs struggle to maintain coherent plans over many steps — performance degrades as plan complexity increases
- **Error accumulation**: Early planning errors compound through subsequent steps
- **Irreversibility**: Some actions cannot be undone, making planning errors costly
- **Context consumption**: Detailed plans consume context window space needed for execution
- **Over-planning**: Spending too many tokens on planning vs. execution

## Sources

- [[sources/superannotate-llm-agents-guide]] — CoT, ToT, ReAct, Reflexion as planning approaches
- [[sources/ng-agentic-design-patterns]] — planning as third agentic design pattern
- [[sources/react-prompting-framework]] — ReAct as adaptive planning mechanism
- [[sources/databricks-agent-design-patterns]] — planning in single-agent and multi-agent systems

## Related Concepts

- [[concepts/llm-agent-architecture]] — planning as core component
- [[concepts/react-pattern]] — adaptive plan-execute-observe loop
- [[concepts/reflection-pattern]] — plan evaluation and improvement
- [[concepts/agentic-workflows]] — planning as a design pattern
- [[concepts/multi-agent-systems]] — distributed planning across agents

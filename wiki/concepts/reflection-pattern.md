---
title: "Reflection Pattern"
type: concept
sources: ["[[sources/ng-agentic-design-patterns]]", "[[sources/react-prompting-framework]]", "[[sources/superannotate-llm-agents-guide]]"]
related: ["[[concepts/agentic-workflows]]", "[[concepts/react-pattern]]", "[[concepts/agent-planning]]", "[[concepts/llm-agent-architecture]]"]
last_compiled: 2026-04-05
summary: "Automated self-critique pattern where LLMs evaluate and iteratively improve their own outputs, delivering surprising performance gains with relatively simple implementation."
---

## Overview

The reflection pattern is one of [[entities/andrew-ng]]'s four [[concepts/agentic-workflows]] design patterns and arguably the most immediately impactful. Instead of accepting the LLM's first output as final, the reflection pattern prompts the model to critique its own work and iteratively improve it. Ng describes it as "relatively quick to implement" with "surprising performance gains."

The pattern automates what a skilled human would do naturally: generate a draft, review it critically, identify weaknesses, and revise. By making this cycle explicit and repeatable, reflection consistently produces higher-quality outputs than single-pass generation.

## How It Works

### Basic Self-Reflection

1. **Generate**: Prompt the LLM to produce initial output (code, text, analysis)
2. **Critique**: Ask the same model to evaluate its work: "Check this code carefully for correctness, style, and efficiency, and give constructive criticism"
3. **Revise**: Have the model rewrite based on its critique
4. **Iterate**: Repeat the critique-revise cycle (typically 2-3 iterations suffice)

### Tool-Augmented Reflection

Extend basic reflection with external validation:
- Run generated code against unit tests
- Search the web to verify factual claims
- Execute calculations to check mathematical reasoning
- The model then reflects on identified errors and proposes improvements

### Multi-Agent Reflection

Create two specialized agents:
- **Generator**: Produces outputs
- **Critic**: Provides constructive criticism
- The resulting adversarial dialogue leads to improved responses, as each agent pushes the other toward higher quality

## Reflexion: The Research Foundation

Reflexion (Shinn et al., 2023) formalizes reflection as "verbal reinforcement learning." The key innovation: convert environmental feedback into linguistic feedback that persists in the agent's memory. The three components:

1. **Actor**: Generates text and actions based on state observations
2. **Evaluator**: Scores the outputs
3. **Self-Reflection**: Generates verbal reinforcement cues for improvement

Critically, learning happens at the knowledge and planning level through natural language — no model weight updates required. ReAct + Reflexion achieves 130/134 tasks, dramatically outperforming ReAct alone.

## Performance Impact

Reflection delivers gains across multiple domains:
- **Code generation**: Self-critique catches bugs, improves style and efficiency
- **Writing**: Iterative revision produces more coherent, accurate text
- **Question answering**: Factual verification reduces hallucination
- **Problem solving**: Step-by-step review catches logical errors

## Related Papers

- Self-Refine: Iterative Refinement with Self-Feedback (Madaan et al., 2023)
- Reflexion: Language Agents with Verbal Reinforcement Learning (Shinn et al., 2023)
- CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing (Gou et al., 2024)

## Sources

- [[sources/ng-agentic-design-patterns]] — reflection as first agentic design pattern
- [[sources/react-prompting-framework]] — Reflexion performance results
- [[sources/superannotate-llm-agents-guide]] — reflection within planning component

## Related Concepts

- [[concepts/agentic-workflows]] — reflection is the first design pattern
- [[concepts/react-pattern]] — Reflexion builds on ReAct
- [[concepts/agent-planning]] — reflection as planning feedback mechanism
- [[concepts/llm-agent-architecture]] — reflection within the agent loop

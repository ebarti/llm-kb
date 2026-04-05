---
title: "ReAct vs Reflection vs Planning"
type: comparison
subjects: ["[[concepts/react-pattern]]", "[[concepts/reflection-pattern]]", "[[concepts/agent-planning]]"]
sources: ["[[sources/react-prompting-framework]]", "[[sources/ng-agentic-design-patterns]]", "[[sources/superannotate-llm-agents-guide]]"]
last_compiled: 2026-04-05
summary: "Three complementary agent reasoning patterns: ReAct (interleaved reasoning-action loops), Reflection (self-critique and iterative improvement), and Planning (upfront task decomposition)."
---

## Overview

ReAct, Reflection, and Planning are three distinct but complementary patterns within [[concepts/agentic-workflows]]. They are not mutually exclusive — the most effective agents combine all three. Understanding when each pattern shines helps design better agent systems.

## Comparison Table

| Dimension | ReAct | Reflection | Planning |
|-----------|-------|------------|----------|
| Core idea | Interleave reasoning with action | Critique and iteratively improve | Decompose goals into subtasks |
| When it runs | During task execution | After initial generation | Before execution |
| Loop | Thought → Action → Observation | Generate → Critique → Revise | Decompose → Execute → Synthesize |
| Key strength | Grounding in real-world data | Quality improvement through iteration | Managing complex multi-step tasks |
| Key weakness | Can loop indefinitely | Doesn't gather new information | Plans may not survive reality |
| Implementation | Agent loop with tools | Two-pass (or two-agent) setup | Task decomposition prompt |
| Ease of implementation | Moderate | Easy (Ng: "quick to implement") | Moderate to difficult |
| Best combined with | Reflexion (for learning from failures) | Tool validation (tests, search) | ReAct (for adaptive execution) |

## How They Compose

The three patterns layer naturally:

1. **Planning** first: Decompose the complex goal into subtasks
2. **ReAct** during execution: For each subtask, interleave reasoning and action
3. **Reflection** after execution: Evaluate the overall result, critique, and revise

For example, an [[concepts/agentic-coding]] agent might:
1. **Plan**: Break "implement login feature" into subtasks (create model, add routes, write tests, etc.)
2. **ReAct per subtask**: For "write tests" — think about what to test, write tests, run them, observe failures, fix
3. **Reflect**: Review the complete implementation for correctness, style, and edge cases; revise

## Performance Comparison

| Approach | Task Completion |
|----------|----------------|
| ReAct alone | Good on knowledge tasks |
| Reflection alone | Surprising gains on generation tasks |
| ReAct + Reflexion | 130/134 tasks (near-perfect) |
| ReAct + CoT + self-consistency | Best overall knowledge performance |

The combination consistently outperforms any single pattern.

## Sources

- [[sources/react-prompting-framework]] — ReAct framework and performance
- [[sources/ng-agentic-design-patterns]] — reflection and planning as design patterns
- [[sources/superannotate-llm-agents-guide]] — all three as components of agent planning

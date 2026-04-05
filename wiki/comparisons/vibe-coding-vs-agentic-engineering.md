---
title: "Vibe Coding vs Agentic Engineering"
type: comparison
subjects: ["[[concepts/vibe-coding]]", "[[concepts/agentic-coding]]"]
sources: ["[[sources/wikipedia-vibe-coding]]", "[[sources/osmani-ai-productivity-reality]]", "[[sources/greptile-state-of-ai-coding-2025]]"]
related: ["[[concepts/software-2-0]]", "[[concepts/ai-code-generation]]", "[[concepts/post-code-ai-workflow]]", "[[concepts/ai-productivity-paradox]]", "[[entities/andrej-karpathy]]"]
tags: [comparison, vibe-coding, agentic-engineering, ai-programming]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Two approaches to AI-assisted programming -- both coined/popularized by Karpathy -- compared: vibe coding (accept AI output with minimal review) vs agentic engineering (orchestrate agents with engineering discipline), representing the maturation from hype to production."
---

## Overview

[[concepts/vibe-coding]] and [[concepts/agentic-coding]] (agentic engineering) represent two successive philosophies of AI-assisted programming, both popularized by [[entities/andrej-karpathy]]. Vibe coding (February 2025) embraced letting AI generate code with minimal human review. Agentic engineering (early 2026) retained the AI-does-the-typing premise but added human oversight, engineering discipline, and agent orchestration. This comparison captures the field's maturation from experimental enthusiasm to production-grade methodology.

## Comparison Matrix

| Dimension | Vibe Coding | Agentic Engineering |
|-----------|------------|-------------------|
| **Coined** | February 2025 | Early 2026 |
| **By** | Karpathy | Karpathy |
| **Human role** | Prompter | Orchestrator / reviewer |
| **Code understanding** | Explicitly optional ("forget the code exists") | Essential ("engineering" emphasis) |
| **Quality assurance** | Test output, hope for the best | CI/CD, test suites, multi-model review |
| **Intended scope** | Weekend projects, prototypes | Production software |
| **Mindset** | "Give in to the vibes" | "Art & science and expertise" |
| **Code review** | Minimal to none | AI-on-AI + human oversight |
| **Agent count** | Single LLM conversation | Multiple orchestrated agents |
| **Failure mode** | Unmaintainable code, security vulnerabilities | Slower but more reliable |
| **Industry reception** | Collins Word of the Year 2025, then "hangover" | Emerging consensus as best practice |

## Analysis

### The Maturation Arc

Karpathy's evolution from vibe coding to agentic engineering mirrors the classic technology adoption pattern:

1. **Innovation trigger**: LLMs can generate working code from English descriptions
2. **Peak of inflated expectations**: "Forget the code exists!" -- 95% AI-generated startups
3. **Trough of disillusionment**: "Development hell," 2.74x security vulnerabilities, METR slowdown
4. **Slope of enlightenment**: Agentic engineering -- AI writes code but humans architect, review, and orchestrate
5. **Plateau of productivity**: Disciplined AI-augmented workflows (Osmani's model)

### Why Vibe Coding Failed at Scale

Evidence from [[sources/osmani-ai-productivity-reality]] and [[sources/wikipedia-vibe-coding]]:

- **Security**: 2.74x more vulnerabilities, no systematic review
- **Maintainability**: Code duplication up 4x, refactoring down from 25% to under 10%
- **Productivity paradox**: Experienced developers 19% slower (METR), review times up 91% (DORA/Faros)
- **Organizational failure**: Sentry CEO's 2-month experiment produced "absolutely unmaintainable" code
- **Open source damage**: Homogenizes dependencies, reduces community engagement

### Why Agentic Engineering Works Better

- **Human oversight**: Reviews architecture, security, edge cases
- **Multi-agent**: Parallel agents with coordination (Claude Code's Agent Teams)
- **Spec-driven**: Detailed specifications before code generation (Osmani's "waterfall in 15 minutes")
- **CI/CD integration**: Automated testing as safety net, not afterthought
- **Iterative**: Small chunks, frequent commits, incremental validation

### The Common Thread

Both approaches share a fundamental premise: **the human should not be typing most of the code**. Where they differ is whether the human still needs to *understand* the code. Vibe coding says no; agentic engineering says understanding is what makes the orchestration possible.

## When to Use Each

| Scenario | Recommended |
|----------|-------------|
| Personal throwaway projects | Vibe coding is acceptable |
| Prototyping/proof-of-concept | Vibe coding, then rewrite |
| Production software | Agentic engineering |
| Team collaboration | Agentic engineering |
| Security-sensitive applications | Agentic engineering (mandatory) |
| Learning/exploration | Vibe coding for speed, then review for understanding |

## Sources

- [[sources/wikipedia-vibe-coding]] -- comprehensive history and evidence for both approaches
- [[sources/osmani-ai-productivity-reality]] -- why disciplined approaches outperform vibe coding
- [[sources/greptile-state-of-ai-coding-2025]] -- adoption data showing shift toward agentic patterns

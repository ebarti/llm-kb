---
title: "Vibe Coding"
type: concept
sources: ["[[sources/wikipedia-vibe-coding]]", "[[sources/osmani-ai-productivity-reality]]", "[[sources/greptile-state-of-ai-coding-2025]]", "[[sources/karpathy-vibe-coding]]", "[[sources/karpathy-2025-llm-year-review]]"]
related: ["[[concepts/software-2-0]]", "[[concepts/agentic-coding]]", "[[concepts/ai-code-generation]]", "[[concepts/ai-productivity-paradox]]", "[[concepts/natural-language-programming]]", "[[concepts/post-code-ai-workflow]]", "[[entities/andrej-karpathy]]"]
tags: [vibe-coding, ai-programming, karpathy, natural-language]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Karpathy's February 2025 term for natural-language-driven development with minimal code review -- Collins Word of the Year 2025 -- which followed a clear arc from excitement to 'hangover' to Karpathy himself declaring it passe in favor of agentic engineering."
---

## Overview

Vibe coding is a software development approach coined by [[entities/andrej-karpathy]] in February 2025 where developers describe desired functionality in natural language and accept LLM-generated code with minimal review. Karpathy described it as "fully give in to the vibes, embrace exponentials, and forget that the code even exists." The term built on his 2023 claim that "the hottest new programming language is English."

Vibe coding represents the practical consumer-facing manifestation of [[concepts/software-2-0]]'s paradigm shift: if neural networks are the new programs and data is the new source code, then natural language is the new programming language. Collins English Dictionary named it Word of the Year for 2025, signaling its cultural penetration far beyond the developer community.

## The Arc: Excitement to Hangover to Evolution

Vibe coding followed a remarkably clear lifecycle:

| Period | Phase | Key Events |
|--------|-------|------------|
| Feb 2025 | **Coinage** | Karpathy's tweet; Merriam-Webster trending |
| Mar 2025 | **Hype** | Y Combinator: 25% of Winter 2025 startups had 95% AI-generated codebases |
| Jul 2025 | **Commercial adoption** | Wall Street Journal documents professional use; METR study shows 19% slowdown |
| Sep 2025 | **Hangover** | Fast Company: "development hell" managing AI-generated code |
| Dec 2025 | **Quality reckoning** | CodeRabbit: AI code has 2.74x more security vulnerabilities |
| Jan 2026 | **Evolution** | Karpathy declares vibe coding "passe," proposes "agentic engineering" |

## How It Works

1. Developer describes desired functionality in natural language to an LLM (via [[entities/cursor]], [[entities/claude-code]], [[entities/github-copilot]], or Replit)
2. LLM generates source code
3. Developer runs the code, tests output
4. If it doesn't work, developer prompts modifications
5. Cycle repeats until the output satisfies requirements

The critical distinction (per [[entities/simon-willison]]): vibe coding means accepting code you don't fully understand. If you thoroughly review and comprehend the output, you're using an LLM as a typing assistant, not vibe coding.

## The Quality Problem

Empirical evidence reveals serious quality concerns:

- **Security**: AI co-authored code contains 2.74x more security vulnerabilities and 1.7x more "major" issues (CodeRabbit, 470 GitHub PRs)
- **Maintainability**: GitClear's analysis of 211 million code changes found refactoring dropped from 25% (2021) to under 10% (2024), while code duplication increased 4x
- **Productivity**: The [[concepts/ai-productivity-paradox]] -- METR found experienced developers 19% slower, despite believing they were 24% faster
- **Reliability**: SaaStr founder reported Replit's AI agent deleted a database despite explicit preservation instructions

David Cramer (Sentry CEO) attempted two months of 100% agent-driven development and concluded the code was "absolutely unmaintainable" with "duplicate code, unused sections, and incorrect abstractions."

## From Vibe Coding to Agentic Engineering

Karpathy's evolution encapsulates the field's maturation:

> "'Agentic' because the new default is that you are not writing the code directly 99% of the time, you are orchestrating agents who do and acting as oversight -- 'engineering' to emphasize that there is an art & science and expertise to it."

The key differences between vibe coding and [[concepts/agentic-coding]]:

| Dimension | Vibe Coding | Agentic Engineering |
|-----------|------------|-------------------|
| Human role | Prompter | Orchestrator/reviewer |
| Code understanding | Optional | Essential |
| Quality assurance | Test-and-pray | CI/CD, test suites, multi-model review |
| Scope | Weekend projects | Production software |
| Mindset | "Forget the code" | "Own the architecture, delegate the typing" |

## Connection to the Knowledge Shift

Vibe coding is the most visible symptom of [[concepts/software-2-0]]'s deeper transformation. The progression is:

1. **Software 2.0** (2017): Programs are learned weights, not written code
2. **"English is the programming language"** (2023): LLMs as the interface between human intent and machine execution
3. **Vibe coding** (2025): The extreme end -- just talk and accept what comes out
4. **Agentic engineering** (2026): The mature form -- orchestrate AI agents with human oversight and engineering discipline

This is the same shift Karpathy described in the [[concepts/post-code-ai-workflow]] context: developers are no longer manipulating code, they are manipulating knowledge -- specifications, context, architectural decisions, and domain expertise.

## Open Questions

- Will vibe coding persist as a legitimate approach for prototyping and throwaway projects?
- Can improved AI capabilities eventually make the quality concerns obsolete?
- Does vibe coding's "development hell" outcome reflect fundamental limitations or merely immature tooling?

## Sources

- [[sources/wikipedia-vibe-coding]] -- comprehensive history and evidence
- [[sources/osmani-ai-productivity-reality]] -- productivity research context
- [[sources/greptile-state-of-ai-coding-2025]] -- adoption metrics
- [[sources/karpathy-vibe-coding]] -- detailed Wikipedia article on vibe coding
- [[sources/karpathy-2025-llm-year-review]] -- Karpathy's own retrospective on vibe coding's role in 2025

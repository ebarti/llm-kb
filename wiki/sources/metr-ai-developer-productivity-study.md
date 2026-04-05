---
title: "Source: METR AI Developer Productivity Study"
type: source-summary
source: "[[raw/metr-ai-developer-productivity-study]]"
related: ["[[concepts/ai-productivity-paradox]]", "[[concepts/ai-coding-assistants]]", "[[concepts/ai-pair-programming]]", "[[entities/cursor]]", "[[entities/metr]]"]
last_compiled: 2026-04-05
summary: "Landmark RCT finding experienced open-source developers are 19% slower with AI tools, despite believing they were 20% faster — the most rigorous challenge to AI productivity claims."
---

## Key Points

- First randomized controlled trial (RCT) measuring AI tool impact on experienced developers working on their own repositories
- 16 developers, 246 real issues, primarily using [[entities/cursor]] Pro with Claude 3.5/3.7 Sonnet
- Core finding: developers took **19% longer** when using AI tools
- Developers **believed** AI sped them up by 20% — a striking perception-reality gap
- Tasks averaged ~2 hours each across bugs, features, and refactors in repos with 22K+ stars

## Detailed Summary

METR's study stands as the most rigorous empirical test of AI coding tool productivity. By randomly assigning real issues from developers' own repositories to "AI allowed" vs "AI disallowed" conditions, the researchers eliminated the selection bias that plagues self-reported surveys and benchmark evaluations.

The 19% slowdown is explained by several factors: time spent crafting prompts, reviewing AI output, debugging AI-generated code, and context-switching between the AI interface and the development environment. Critically, the developers had substantial prior LLM experience (dozens to hundreds of hours) but limited Cursor-specific proficiency (~50 hours).

The study explicitly does not claim AI is useless for all developers or all tasks. It highlights that experienced developers working on familiar, high-quality codebases represent a particularly challenging test case for AI tools — the developers already know their codebases deeply, and the overhead of communicating context to the AI may exceed the benefit.

A 2026 follow-up study showed results still inconclusive, with estimated speedup of -18% (CI: -38% to +9%), though researchers believe tools have likely improved.

## Notable Quotes

> "Developers estimated they were sped up by 20% on average when using AI — so they were mistaken about AI's impact."

## Related Concepts

- [[concepts/ai-productivity-paradox]] — This study is the most cited evidence for the paradox between perceived and measured AI productivity
- [[concepts/ai-coding-assistants]] — The tools tested (Cursor + Claude) are market leaders
- [[concepts/ai-pair-programming]] — Challenges the dominant narrative about AI as beneficial pair programmer
- [[concepts/developer-experience-ai]] — Highlights how subjective experience diverges from objective measurement

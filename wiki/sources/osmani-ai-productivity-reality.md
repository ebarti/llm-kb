---
title: "Source: The Reality of AI-Assisted Software Engineering Productivity"
type: source-summary
source: "[[raw/osmani-ai-productivity-reality]]"
related: ["[[concepts/ai-productivity-paradox]]", "[[concepts/ai-pair-programming]]", "[[concepts/ai-code-generation]]", "[[concepts/vibe-coding]]"]
tags: [ai-productivity, research, developer-tools]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Osmani's meta-analysis of AI coding productivity research: rigorous studies show 20-30% gains (not 10x), with the DORA/Faros paradox revealing that PR review times balloon 91% and bug rates increase 9% despite individual output gains."
---

## Key Points

- 84% adoption but only 60% favorable views (down from 70% in 2023); 46% distrust accuracy
- 66% cite "almost right, but not quite" code as biggest time sink
- Google internal trial: 21% faster (96 min vs 114 min) on enterprise tasks
- Multi-company study (~5,000 devs): 26% average improvement; newer devs 35-39%, seniors only 8-16%
- METR study: 19% slower for experienced developers on large codebases
- DORA/Faros (10,000+ devs): 21% more tasks but 91% longer review times, 9% more bugs, 154% larger PRs
- No significant correlation between AI adoption and organizational DORA metrics
- David Cramer (Sentry CEO): "you cannot use these agents to build software today" after 2 months of 100% agent-driven development
- 95% of AI tool value comes from straightforward interactive chat, not autonomous features

## Detailed Summary

This is the most comprehensive meta-analysis of AI coding productivity research published to date. Osmani synthesizes findings from Google, Microsoft, Accenture, METR, and DORA/Faros into a coherent picture: AI tools provide real but modest productivity gains (20-30%) at the individual level, while organizational metrics show no improvement or even degradation.

The DORA/Faros finding is the most damning: despite high-AI teams completing 21% more tasks and merging 98% more PRs, review times ballooned 91%, bug rates increased 9%, and there was no improvement in deployment frequency, lead time, change failure rate, or mean time to recovery. The bottleneck has shifted from code generation to code review and integration.

The article directly challenges the [[concepts/vibe-coding]] approach by documenting David Cramer's failed experiment at Sentry, where two months of fully autonomous agent-driven development produced "absolutely unmaintainable" code.

## Concepts Introduced or Discussed

- [[concepts/ai-productivity-paradox]] -- the central thesis
- [[concepts/ai-pair-programming]] -- the recommended approach (interactive chat, not autonomous)
- [[concepts/vibe-coding]] -- critiqued via Cramer's experiment
- [[concepts/ai-code-review]] -- identified as the key bottleneck

## Metadata

- **Author**: Addy Osmani
- **Date Published**: ~December 2025
- **Format**: article (Substack)
- **URL**: https://addyo.substack.com/p/the-reality-of-ai-assisted-software

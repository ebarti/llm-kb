---
title: "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
source: "https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/"
author: "METR"
date_published: 2025-07-10
date_ingested: 2026-04-05
tags: [ai-productivity, developer-tools, randomized-controlled-trial, cursor, claude, coding-assistants]
type: paper
status: raw
discovered_via: search
---

# Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity

## Study Overview

METR conducted a randomized controlled trial examining how early-2025 AI tools affect experienced open-source developers working on actual repository issues.

## Methodology

- **Sample:** 16 experienced developers from large open-source projects (averaging 22,000+ stars, 1M+ lines of code)
- **Design:** Developers received 246 real issues (bugs, features, refactors) randomly assigned to allow or disallow AI use. Tasks averaged approximately two hours each.
- **Tools:** Developers primarily used Cursor Pro with Claude 3.5/3.7 Sonnet models
- **Compensation:** $150/hour for participation

## Key Findings

- **Core Result:** When permitted to use AI tools, developers took significantly longer — approximately 19% slower than working without AI assistance.
- **Self-Perception Gap:** Developers anticipated AI would "speed them up by 24%" but actually experienced slowdown. Even after the study concluded, they "still believed AI had sped them up by 20%."

## Factor Analysis

Researchers identified five likely contributing factors explaining the slowdown, ruling out experimental artifacts including model quality, treatment compliance, selective task dropout, and output quality differences.

## What the Study Does NOT Claim

The authors explicitly clarify their findings don't demonstrate:
- AI fails to benefit most software developers generally
- AI lacks value across non-development domains
- Future AI systems won't accelerate developers
- No optimization approaches exist for current systems

## Limitations and Context

- **Statistical Power:** While using 246 completed issues across 16 developers, the study acknowledges sampling bias concerns
- **Experience Level:** Developers had substantial prior LLM prompting experience (dozens to hundreds of hours) but potentially limited Cursor-specific proficiency (~50 hours typical)
- **Generalizability:** Results apply specifically to experienced developers working on familiar codebases with high-quality standards

## Reconciliation with Other Evidence

The findings create apparent contradictions with:
- Strong benchmark performance (SWE-Bench Verified, RE-Bench)
- Widespread anecdotal reports of AI helpfulness
- Significant industry adoption

Researchers propose three hypotheses: their RCT underestimates capabilities, benchmarks/anecdotes overestimate them, or all three methodologies accurately measure different task subsets with varying difficulty levels for AI systems.

## Follow-Up (Early 2026)

METR updated their study design. For the subset of original developers, the estimated speedup is -18% with a confidence interval between -38% and +9%. Researchers believe it is likely that developers are more sped up from AI tools now in early 2026 compared to early 2025, though results remain inconclusive.

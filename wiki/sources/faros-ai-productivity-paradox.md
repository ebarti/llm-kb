---
title: "Source: The AI Productivity Paradox Research Report"
type: source-summary
source: "[[raw/faros-ai-productivity-paradox]]"
related: ["[[concepts/ai-productivity-paradox]]", "[[concepts/ai-coding-assistants]]", "[[concepts/ai-code-review]]"]
last_compiled: 2026-04-05
summary: "Faros AI telemetry from 10,000+ developers reveals the paradox: 21% more tasks completed but 9% more bugs, 154% larger PRs, 91% longer reviews, and no organizational-level productivity gain."
---

## Key Points

- 21% more tasks completed individually, 98% more PRs merged
- But: 9% more bugs per developer, PR size up 154%, review time up 91%
- No significant correlation between AI adoption and company-level improvements
- Amdahl's Law: review bottlenecks, testing, and deployment pipelines neutralize coding velocity gains
- Analysis based on telemetry from 1,255 teams and 10,000+ developers

## Detailed Summary

The Faros AI Productivity Paradox report is the largest empirical study of AI tool impact at the organizational level. While the [[sources/metr-ai-developer-productivity-study]] examined individual task performance, this study examines what happens when those individual gains (or losses) aggregate across teams and organizations.

The core finding is devastating for simple "AI makes developers faster" narratives: individual developers do complete more tasks and merge more PRs, but the downstream effects — larger PRs, longer review cycles, more bugs — mean that organizations see no net improvement in delivery velocity or quality.

Four adoption patterns explain this: recent critical mass (usage only widespread for 2-3 quarters), uneven distribution across teams, demographic skew (junior developers adopt more readily), and surface-level implementation (most use only autocomplete, not advanced features).

The Amdahl's Law framing is particularly powerful: if code writing is only 20-30% of the software delivery lifecycle, then even a 2x improvement in coding speed yields only a 10-15% overall improvement — which is easily consumed by the increased review burden.

## Related Concepts

- [[concepts/ai-productivity-paradox]] — This is the defining study
- [[concepts/ai-code-review]] — Review bottleneck is the key constraint identified
- [[concepts/agentic-coding]] — Surface-level adoption vs. deep integration

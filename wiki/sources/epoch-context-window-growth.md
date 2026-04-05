---
title: "Source: LLMs Now Accept Longer Inputs — Epoch AI"
type: source-summary
source: "[[raw/epoch-context-window-growth]]"
related: ["[[concepts/context-windows]]", "[[concepts/long-context-models]]", "[[concepts/needle-in-a-haystack]]"]
last_compiled: 2026-04-05
summary: "Epoch AI analysis showing frontier LLM context windows growing ~30x/year since mid-2023, with effective usage growing even faster at ~250x in 9 months."
reading_time: "2 min"
---

## Key Points

- Frontier LLM context windows have grown approximately **30x annually** since mid-2023 (10x-50x CI, 123 models analyzed)
- Effective usage — the input length where top performers reach 80% accuracy — has increased over **250x in nine months**
- Even leading models like Gemini 2.5 Pro only score above 80% on the 8K input length setting in the hardest multi-needle MRCR variant
- Growth in effective usage outpaces growth in raw window size, suggesting architectural and training improvements matter as much as simply making windows bigger

## Detailed Summary

Epoch AI's systematic tracking of 123 models reveals that the LLM context window race is progressing on two parallel tracks. The first is raw capacity: advertised context windows are growing at roughly 30x per year. The second, more interesting track is effective utilization — how much of that window models can actually use productively. Effective usage is growing even faster, meaning models are getting better at using the context they have, not just accepting more tokens.

The analysis uses two primary benchmarks: Fiction.liveBench (37 models, narrative comprehension) and MRCR (49 models, multi-needle retrieval with distractors). These represent "moderately challenging" tasks — real-world applications likely demand even more from long-context capabilities.

A sobering finding: even the best frontier models struggle on harder retrieval variants. This suggests that raw context window size is a necessary but insufficient condition for practical long-context applications.

## Notable Quotes

> "Since mid-2023, the longest LLM context windows have grown by about 30x per year."

## Related Concepts

- [[concepts/context-windows]] — directly measures context window growth trends
- [[concepts/long-context-models]] — tracks which models lead in long-context capabilities
- [[concepts/needle-in-a-haystack]] — MRCR is a multi-needle variant of the classic NIAH benchmark
- [[concepts/lost-in-the-middle]] — even frontier models show degradation on harder retrieval tasks

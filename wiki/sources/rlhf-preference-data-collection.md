---
title: "Source: Preference Data — RLHF Book"
type: source-summary
source: "[[raw/rlhf-preference-data-collection]]"
related: ["[[concepts/preference-data]]", "[[concepts/rlhf]]", "[[entities/anthropic-hh-rlhf]]", "[[entities/nathan-lambert]]"]
last_compiled: 2026-04-05
summary: "Definitive guide to RLHF preference data: collection interfaces, on-policy vs off-policy data, quality metrics, operational complexity, and the reality that millions in data collection spend goes unused."
---

## Key Points

- Preference data captures relative judgments between model outputs as a proxy for human values
- Chosen response is "better relative to alternatives," not necessarily globally correct
- Collection interfaces: pairwise comparison (dominant), Likert scales, unary feedback, arena-style
- On-policy data (from current model) significantly outperforms off-the-shelf datasets
- Common biases: prefix bias, sycophancy, verbosity bias, formatting bias — all transfer to final models
- "No open models with fully open human preference data released with the methods used to collect it"
- Collection costs millions; much data goes unused in final models
- Phased delivery over 6+ weeks with calibration periods

## Detailed Summary

Nathan Lambert's RLHF Book chapter provides the most comprehensive public treatment of how preference data is actually collected and used in practice. The core insight is that preference data serves as a proxy signal because directly specifying human values as loss functions is effectively impossible.

The on-policy vs off-policy distinction is particularly important: data collected from the model currently being trained is far more effective than generic preference datasets. This creates operational complexity — models must generate completions during each training phase, requiring live inference endpoints and careful scheduling with data collection vendors.

The chapter is refreshingly honest about the operational reality: data collection is expensive, vendor relationships are supply-constrained, early batches are often discarded during calibration, and "millions of dollars spent on these datasets are wasted." This underscores how critical [[concepts/preference-data]] quality is to the alignment pipeline.

## Related Concepts

- [[concepts/preference-data]] — the central concept this source defines
- [[concepts/rlhf]] — preference data as the engine of RLHF
- [[concepts/instruction-tuning]] — upstream of preference tuning in the training pipeline
- [[concepts/data-quality-bottleneck]] — preference data quality directly constrains alignment quality

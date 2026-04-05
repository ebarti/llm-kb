---
title: "Source: Spike No More — Stabilizing the Pre-training of Large Language Models"
type: source-summary
source: "[[raw/spike-no-more-training-stability]]"
related: ["[[concepts/training-stability]]", "[[concepts/loss-spikes]]", "[[concepts/llm-pretraining]]"]
last_compiled: 2026-04-05
summary: "ArXiv paper identifying two root causes of loss spikes (shortcut-based and layer normalization gradient explosion), proposing Embed LN and Scaled Embed fixes that eliminate spikes and enable 2x larger learning rates."
---

## Key Points

- Loss spikes stem from two sources of gradient explosion: shortcut-based and LN-based
- Standard initialization causes shortcut explosion; scaled initialization prevents it but enables LN explosion
- Embed LN (normalizing embeddings) and Scaled Embed (multiplying by sqrt(d)) eliminate spikes
- Stabilized training enables 2x larger learning rates
- Benefits scale with model size (tested on 350M and 1.7B)

## Detailed Summary

The paper provides a rigorous theoretical framework for understanding [[concepts/loss-spikes]] during LLM pretraining.

**Shortcut explosion**: Residual connections amplify gradient norms exponentially. Standard He initialization causes FFN output standard deviations to grow unbounded.

**LN explosion**: When inputs to LayerNorm have very small standard deviations (common with scaled initialization), the LN gradient becomes inversely proportional to input magnitude, causing explosion in shallow layers.

The critical insight is that scaled initialization (which prevents shortcut explosion) actually *enables* LN explosion — previous work missed this interaction.

**Solutions**: Apply LayerNorm to embeddings (Embed LN) or multiply embeddings by sqrt(d) (Scaled Embed) to ensure appropriate input magnitudes to LN layers.

## Related Concepts

- [[concepts/training-stability]] — the broader topic
- [[concepts/loss-spikes]] — the specific failure mode
- [[concepts/learning-rate-schedules]] — interacts with stability
- [[concepts/llm-pretraining]] — the process being stabilized

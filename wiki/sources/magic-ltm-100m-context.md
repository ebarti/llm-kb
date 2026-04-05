---
title: "Source: Magic LTM-2-Mini — 100M Token Context Windows"
type: source-summary
source: "[[raw/magic-ltm-100m-context]]"
related: ["[[concepts/long-context-models]]", "[[concepts/context-windows]]", "[[entities/magic-ltm]]"]
last_compiled: 2026-04-05
summary: "Magic's LTM-2-Mini achieves 100M token context (10M lines of code) using a sequence-dimension algorithm 1,000x cheaper than standard attention, requiring a fraction of one H100 vs 638 for Llama 405B."
---

## Key Points

- 100 million token context window = 10 million lines of code or 750 novels
- Sequence-dimension algorithm is **1,000x cheaper** than Llama 3.1 405B attention for 100M tokens
- Memory: Llama 405B needs **638 H100s** for 100M token KV cache vs **fraction of one H100** for LTM
- Introduced **HashHop** benchmark using incompressible hash pairs (harder than Needle-in-a-Haystack)
- Custom training/inference stack from scratch (no torch autograd, custom CUDA)

## Detailed Summary

Magic's LTM-2-Mini represents the most radical departure from standard transformer architecture in the long-context space. While most models scale context by engineering around attention's O(n^2) complexity, Magic replaced the attention mechanism entirely with their "sequence-dimension algorithm," achieving three orders of magnitude better efficiency.

The practical implications are striking: serving a 100M-token context with standard transformers requires hundreds of high-end GPUs per user just for the KV cache. LTM achieves this on a fraction of a single GPU. This suggests an alternative future where entire codebases, documentation libraries, and project histories live permanently in context.

Magic also contributed HashHop, a more rigorous long-context benchmark that addresses criticisms of [[concepts/needle-in-a-haystack]] being too easy. HashHop uses incompressible random hash pairs, forcing the model to truly store and retrieve information rather than relying on patterns.

## Related Concepts

- [[concepts/long-context-models]] — represents the extreme end of the context-length spectrum
- [[concepts/context-windows]] — demonstrates radically different approaches to scaling context
- [[concepts/needle-in-a-haystack]] — HashHop is a harder alternative benchmark
- [[entities/magic-ltm]] — the model and company

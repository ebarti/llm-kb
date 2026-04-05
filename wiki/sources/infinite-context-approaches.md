---
title: "Source: Infinite Context Approaches — StreamingLLM, Infini-attention, Ring Attention"
type: source-summary
source: "[[raw/infinite-context-approaches]]"
related: ["[[concepts/infinite-context]]", "[[concepts/context-windows]]", "[[concepts/long-context-models]]"]
last_compiled: 2026-04-05
summary: "Four architectural approaches to infinite/unbounded context: StreamingLLM (attention sinks), Infini-attention (compressive memory), Ring Attention (multi-device distribution), InfLLM (external memory lookup)."
---

## Key Points

- **StreamingLLM**: Attention sinks + rolling window. No fine-tuning needed. But no long-range retrieval.
- **Infini-attention**: Compressive memory in vanilla attention. Bounded memory for infinite context. Tested on 1M-token passkey retrieval.
- **Ring Attention**: Distributes across devices with zero communication overhead. Full accuracy, no approximations.
- **InfLLM**: Training-free external memory with efficient token-relevant lookup.

## Detailed Summary

These four approaches represent fundamentally different strategies for pushing beyond fixed context windows:

**StreamingLLM** (MIT Han Lab, ICLR 2024) discovered that initial tokens serve as "attention sinks" regardless of their content. By keeping these sink tokens plus a rolling window of recent tokens, models maintain stable perplexity over unlimited sequence lengths. The limitation is that it cannot attend to tokens outside the current window — useful for streaming but not for retrieval over long histories.

**Infini-attention** (Google, 2024) is the most elegant approach, adding compressive memory directly into the attention mechanism. Each transformer block maintains both local masked attention and a long-term linear attention mechanism with bounded memory. This enables infinite-length processing with bounded compute — tested successfully on 1M-token passkey retrieval and 500K-token book summarization.

**Ring Attention** (UC Berkeley, 2023) takes a hardware-distribution approach, splitting sequences across multiple devices and overlapping communication with computation. This maintains full accuracy with zero overhead, scaling linearly with device count.

**InfLLM** takes the pragmatic training-free route, storing distant context in external memory units and using efficient lookup for attention computation.

## Related Concepts

- [[concepts/infinite-context]] — the goal all four approaches pursue
- [[concepts/context-windows]] — the fundamental limitation they address
- [[concepts/long-context-models]] — these enable long-context capabilities at the architecture level
- [[concepts/virtual-context-management]] — InfLLM and Infini-attention are forms of virtual context

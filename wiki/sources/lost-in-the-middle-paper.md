---
title: "Source: Lost in the Middle — Liu et al. (TACL 2023)"
type: source-summary
source: "[[raw/lost-in-the-middle-paper]]"
related: ["[[concepts/lost-in-the-middle]]", "[[concepts/context-windows]]", "[[concepts/needle-in-a-haystack]]"]
last_compiled: 2026-04-05
summary: "Landmark paper documenting the U-shaped performance curve: LLMs perform best on information at beginning/end of context, with >30% degradation for middle-positioned content."
---

## Key Points

- Language models exhibit a **U-shaped performance curve**: best performance on information at the beginning (primacy bias) and end (recency bias), worst in the middle
- Performance can degrade by **more than 30%** when relevant information shifts from start/end to middle positions
- Even models designed for long-context processing show this vulnerability
- Attention accumulation explains the effect: early tokens receive more attention weight because they are visible to all subsequent tokens

## Detailed Summary

This Stanford/UC Berkeley paper (Liu et al., TACL 2023) is the foundational work on positional bias in long-context LLMs. Using multi-document QA and key-value retrieval tasks, the authors demonstrated that all tested models struggled with information placed in the middle of their context windows.

The mechanism is rooted in transformer attention: Token #1 is visible to every subsequent token, accumulating substantial attention weight. Token #500 in the middle is only visible from #501 onward, receiving systematically less attention. The result is that models treat context positions unequally, with the beginning and end serving as strong task-framing signals while the middle becomes "noise."

This work directly motivated several practical solutions: strategic document ordering in RAG pipelines, Multi-scale Positional Encoding (Ms-PoE), and reranking models that position critical content optimally.

## Related Concepts

- [[concepts/lost-in-the-middle]] — the phenomenon this paper names and characterizes
- [[concepts/context-windows]] — demonstrates that having a large window is insufficient without effective utilization
- [[concepts/needle-in-a-haystack]] — related evaluation paradigm for long-context retrieval
- [[concepts/rag-vs-index-based-retrieval]] — motivates strategic document ordering in RAG systems

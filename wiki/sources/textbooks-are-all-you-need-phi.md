---
title: "Source: Textbooks Are All You Need — Microsoft Phi Models"
type: source-summary
source: "[[raw/textbooks-are-all-you-need-phi]]"
related: ["[[concepts/synthetic-data-generation]]", "[[concepts/data-quality-bottleneck]]", "[[entities/microsoft-phi]]"]
last_compiled: 2026-04-05
summary: "Microsoft Research demonstrates that 1.3B-parameter phi-1 trained on 'textbook quality' synthetic data matches models 10x larger — data quality decisively outperforms scale."
reading_time: "2 min"
---

## Key Points

- Phi-1 (1.3B params) achieves 50.6% HumanEval with only 7B tokens (6B web + 1B synthetic from GPT-3.5)
- Trained in 4 days on 8 A100 GPUs — fraction of typical LLM training cost
- "Textbook quality" filtering: curate web data + generate synthetic textbooks and exercises
- Phi-2 (2.7B) matches or outperforms models up to 25x larger
- Phi-4 surpasses its teacher model (GPT-4) on STEM QA — going beyond mere distillation
- Iterative filtering loop: generate synthetic content → filter → feed back to LLM → synthesize more
- Key finding: "efficient training data selection outperforms scale"

## Detailed Summary

The Phi model series is the strongest empirical evidence that data quality dominates model scale. Starting with phi-1 for code generation, Microsoft showed that carefully curated "textbook quality" data — a mix of filtered web content and GPT-3.5-generated synthetic textbooks — enables a 1.3B model to rival much larger competitors. The approach was extended to general knowledge (phi-1.5), then scaled to phi-2, phi-3, and phi-4.

The most striking result is phi-4: by strategically incorporating synthetic data throughout training, it surpasses GPT-4 (its own teacher) on STEM benchmarks. This demonstrates that synthetic data generation combined with rigorous filtering goes beyond simple knowledge distillation — it can create novel capabilities.

## Related Concepts

- [[concepts/synthetic-data-generation]] — textbook-quality synthetic data is the core innovation
- [[concepts/data-quality-bottleneck]] — phi proves data quality > model scale
- [[concepts/knowledge-distillation]] — phi-4 goes beyond distillation to surpass its teacher
- [[entities/microsoft-phi]] — the model family

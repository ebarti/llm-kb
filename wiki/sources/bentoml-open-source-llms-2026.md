---
title: "Source: The Best Open-Source LLMs in 2026"
type: source-summary
source: "[[raw/bentoml-open-source-llms-2026]]"
related: ["[[concepts/open-source-llms]]", "[[concepts/mixture-of-experts]]", "[[entities/deepseek]]", "[[entities/qwen]]", "[[entities/meta-llama]]"]
last_compiled: 2026-04-05
summary: "Comprehensive ranking of S-tier open-source LLMs in 2026: Qwen3.5, DeepSeek V3.2, GLM-5, Kimi-K2.5, MiniMax-M2.5, and OpenAI's gpt-oss-120b — all using MoE architectures."
---

## Key Points
- Open-weight models trail SOTA proprietary models by only ~3 months on average
- All top models use [[concepts/mixture-of-experts]] architecture for compute efficiency
- [[entities/deepseek]] V3.2 (671B total, MIT license) and [[entities/qwen]] 3.5 (397B total) dominate general reasoning
- [[entities/meta-llama]] 4 introduced MoE to the Llama line with 10M token context (Scout)
- OpenAI released gpt-oss-120b under Apache 2.0, running on a single 80GB GPU
- Chinese labs (DeepSeek, Qwen, GLM, Kimi, MiMo, MiniMax) produce the majority of frontier open models

## Detailed Summary

BentoML's 2026 survey ranks the best open-source LLMs across multiple dimensions. The landscape has shifted dramatically: five independent open model families simultaneously reached frontier quality, making the competitive open-source ecosystem structural rather than a one-off.

The top tier is dominated by [[concepts/mixture-of-experts]] models that activate only a fraction of total parameters per token. Qwen3.5-397B-A17B activates 17B of 397B parameters; DeepSeek V3.2 uses 671B total; Kimi-K2.5 reaches 1 trillion total with 32B active. This architecture enables frontier performance with manageable inference costs.

Key use-case recommendations: [[entities/deepseek]] V3.2-Speciale for reasoning, GLM-5 and MiniMax-M2.5 for coding, MiMo-V2-Flash and Kimi-K2.5 for agentic workflows, and Qwen3.5 or DeepSeek V3.2 for general chat.

## Notable Quotes
> "Open-weight models now trail the SOTA proprietary models by only about three months on average."

## Related Concepts
- [[concepts/open-source-llms]] — the core topic; maps the 2026 landscape
- [[concepts/mixture-of-experts]] — dominant architecture across all top models
- [[concepts/local-llm-inference]] — these models can be self-hosted with appropriate hardware
- [[comparisons/open-source-vs-closed-llms]] — performance gap analysis

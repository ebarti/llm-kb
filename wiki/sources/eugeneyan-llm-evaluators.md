---
title: "Source: Evaluating the Effectiveness of LLM-Evaluators"
type: source-summary
source: "[[raw/eugeneyan-llm-evaluators]]"
related: ["[[concepts/llm-as-judge]]", "[[concepts/evaluation-bias]]", "[[entities/mt-bench]]", "[[entities/chatbot-arena]]", "[[entities/prometheus]]"]
last_compiled: 2026-04-05
summary: "Data-rich analysis of LLM-as-Judge effectiveness: GPT-4 achieves 85% agreement with humans on MT-Bench, but exhibits position bias (50-70%), verbosity bias (>90%), and self-enhancement bias (10-25%); includes mitigation strategies and alternative frameworks."
---

## Key Points

- GPT-4 achieved 85% agreement with human experts on [[entities/mt-bench]] (exceeding human-human agreement of 81%)
- Position bias: GPT-3.5 biased 50% of the time, Claude-v1 biased 70% toward first-position responses
- Verbosity bias: both Claude-v1 and GPT-3.5 preferred longer responses >90% of the time
- Self-enhancement bias: GPT-4 favored itself +10%, Claude-v1 favored itself +25%
- Panel of diverse LLMs (PoLL) achieves better correlation than single larger models at 1/7th cost
- For factuality detection, best models achieved only 58.5% accuracy distinguishing factual vs hallucinated summaries
- Binary classification outputs over Likert scales enable better metric interpretation

## Detailed Summary

Eugene Yan's analysis is the most data-rich examination of [[concepts/llm-as-judge]] effectiveness. The core finding is nuanced: LLM evaluators approach human-level agreement in aggregate but exhibit systematic biases that must be actively mitigated.

**Agreement data** varies dramatically by task. General preference judgments show 83-87% agreement with humans, but complex tasks like [[concepts/faithfulness-and-groundedness]] evaluation drop to 0.55 Spearman's rho. [[entities/prometheus]] (fine-tuned on 100K GPT-4 examples) achieved 0.897 Pearson correlation, suggesting specialized evaluators outperform general-purpose ones.

**Bias mitigation** is critical. The PoLL approach (ensemble of smaller models with max voting) achieves better correlation than single larger models at dramatically lower cost. Chain-of-thought prompting consistently improves accuracy. Using Cohen's kappa instead of percentage agreement provides more precise measurement of true alignment.

**Key frameworks**: EvalLM enables iterative prompt refinement (91.4% logical explanations). CriticGPT achieves 80-85% bug detection vs 65-70% for humans. LM vs LM Cross-Examination reveals inconsistencies through multi-turn interaction.

## Notable Quotes

> "LLM-evaluators aligned better with non-expert annotators, suggesting results may be inflated when annotation quality varies."

## Related Concepts

- [[concepts/llm-as-judge]] — the paradigm under evaluation
- [[concepts/evaluation-bias]] — the central challenge identified
- [[concepts/hallucination-detection]] — where LLM judges struggle most
- [[entities/mt-bench]] — primary benchmark used for evaluation

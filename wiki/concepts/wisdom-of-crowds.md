---
title: "Wisdom of Crowds"
type: concept
sources: ["[[sources/wisdom-of-the-crowd]]", "[[sources/cip-whitepaper-collective-intelligence]]", "[[sources/brookings-ai-collective-intelligence]]"]
related: ["[[concepts/collective-intelligence]]", "[[concepts/wikipedia-knowledge-model]]", "[[concepts/ai-alignment-democratic]]"]
last_compiled: 2026-04-05
summary: "Aggregated independent judgments from diverse groups outperform individual experts — mathematically formalized by Page's Diversity Prediction Theorem — but requiring conditions (diversity, independence, decentralization, aggregation) that AI both enables and threatens."
---

## Overview

The wisdom of crowds is the empirical finding that the aggregated judgment of a large, diverse, independent group typically outperforms any individual member — including experts. First documented by Aristotle, famously demonstrated by Francis Galton's 1906 ox-weighing experiment (800 guesses, median within 1% of true weight), and popularized by James Surowiecki's 2004 book.

Wisdom of crowds is the **statistical foundation** beneath [[concepts/collective-intelligence]]: where CI is the broader capacity of groups, WoC is the specific mechanism by which independent errors cancel while shared information reinforces.

## Key Ideas

### The Diversity Prediction Theorem

Scott E. Page formalized the mathematics: **collective squared error = average individual squared error minus predictive diversity**. This has a profound implication: diversity is not a nice-to-have — it is *mathematically necessary* for crowd accuracy. A homogeneous crowd, no matter how expert, cannot achieve WoC effects because there is no diversity to subtract.

### Four Conditions (Surowiecki)

1. **Diversity** of opinion — each person holds private information or interpretation
2. **Independence** — opinions are not determined by those around them
3. **Decentralization** — people can specialize and draw on local knowledge
4. **Aggregation** — a mechanism exists for combining individual judgments

These conditions map directly onto the design requirements for [[concepts/collaborative-knowledge-building]] systems. [[concepts/wikipedia-knowledge-model]] satisfies all four.

### Advanced Aggregation Methods

- **Surprisingly Popular Algorithm** (MIT): Asks what people believe AND what they think others believe; selects answers more popular than expected. Reduces errors 21.3% vs. simple majority.
- **Dialectical Bootstrapping**: Individuals make second estimates using "consider-the-opposite" thinking, improving personal accuracy.
- **WICRO Algorithm**: Gauges expertise by measuring relative "distance" between individuals.
- **Geometric mean and median**: More robust to social influence than arithmetic mean.

## Failure Modes

- **Systematic biases**: Averaging eliminates random errors but not shared biases
- **Social influence**: Communication between participants destroys independence (information cascades)
- **Strategic voting**: People misrepresent beliefs for strategic advantage
- **Digital distortions**: Demographic biases, power-law activity distributions, bot influence

## AI and Crowd Wisdom

AI transforms WoC in two directions:

**Enhancement**: AI can aggregate at unprecedented scale, weight by detected expertise, identify and correct for biases, and implement sophisticated methods like the surprisingly popular algorithm automatically. The [[entities/collective-intelligence-project]] uses AI-assisted tools to summarize consensus across viewpoints in citizens' assemblies.

**Degradation**: AI-generated content creates correlated errors (violating independence), content homogenization reduces diversity, and AI summaries may replace the diverse contributions that crowds depend on. When AI models trained on crowd outputs are used to generate new "contributions," the effective crowd size shrinks even as apparent participation grows.

## Sources

- [[sources/wisdom-of-the-crowd]] — comprehensive overview and mathematical foundations
- [[sources/cip-whitepaper-collective-intelligence]] — WoC mechanisms for AI alignment
- [[sources/brookings-ai-collective-intelligence]] — AI bridging crowd deliberation and modeling

## Related Concepts

- [[concepts/collective-intelligence]] — the broader framework WoC supports
- [[concepts/wikipedia-knowledge-model]] — WoC applied to knowledge creation at scale
- [[concepts/ai-alignment-democratic]] — using aggregated values to align AI
- [[concepts/collaborative-knowledge-building]] — structured group knowledge creation

---
title: "Copyright and Training Data"
type: concept
sources: ["[[sources/copyright-ai-training-data-2025]]", "[[sources/nebius-llm-data-preparation]]"]
related: ["[[concepts/training-data-curation]]", "[[concepts/multilingual-training-data]]"]
last_compiled: 2026-04-05
summary: "The evolving legal landscape around using copyrighted works for AI training — emerging US consensus that general-purpose training is 'highly transformative' (fair use), but significant uncertainty remains with cases involving OpenAI and Google expected in 2026."
---

## Overview

Whether training LLMs on copyrighted works constitutes fair use is one of the most consequential legal questions in AI. The answer directly determines what data sources are available for training, and therefore constrains the [[concepts/training-data-curation]] pipeline.

## Current Legal State (as of early 2026)

### US Copyright Office (May 2025)

Released a 108-page report concluding that "some uses of copyrighted works for generative AI training will qualify as fair use, and some will not." Deliberately avoided a blanket rule — fair use is inherently fact-specific.

### Key Court Decisions

**In favor of AI training (fair use found):**
- **Bartz v. Anthropic** (June 2025, N.D. Cal.): training deemed "highly transformative"
- **Kadrey v. Meta** (June 2025, N.D. Cal.): same finding, two days later

**Against AI training (fair use denied):**
- **Thomson Reuters v. ROSS Intelligence** (Feb 2025, D. Del.): headnotes were protectable; ROSS's fair use defense failed

### Emerging Consensus

A judicial consensus is developing that training a general-purpose AI model is "highly transformative" — the strongest factor favoring fair use under the four-factor test. However, rulings remain narrow and fact-specific.

## Four-Factor Fair Use Analysis

US copyright fair use analysis considers:
1. **Purpose and character of use**: transformative use favors fair use; commercial use weighs against
2. **Nature of the copyrighted work**: creative works get more protection than factual ones
3. **Amount used**: using the whole work weighs against fair use
4. **Effect on the market**: if AI competes with the original, weighs against fair use

For general-purpose AI training, factor 1 (transformative) tends to strongly favor fair use, but factors 2-4 create fact-specific uncertainty.

## 2026 Outlook

- Cases involving OpenAI and Google expected
- Total AI copyright cases may peak in 2026
- Litigation focus shifting from training data to AI outputs
- Expected: aggressive discovery into proprietary training data, class certification battles

## Impact on Data Curation

Legal uncertainty affects curation in several ways:
- Labs increasingly invest in licensing deals with publishers
- Open datasets like [[entities/fineweb]] and [[entities/dclm]] use publicly available web data, relying on fair use
- Some data categories (textbooks, scientific papers) face higher legal risk
- [[sources/nebius-llm-data-preparation]] identifies copyright restrictions as one of three emerging challenges for data curation

## International Variation

Different jurisdictions have different copyright frameworks for AI training:
- **EU**: the AI Act and existing database rights add constraints
- **Japan**: notably permissive toward AI training use
- **UK**: proposed but withdrew a broad training exemption

## Sources

- [[sources/copyright-ai-training-data-2025]] — legal landscape overview
- [[sources/nebius-llm-data-preparation]] — copyright as a practical constraint

## Related Concepts

- [[concepts/training-data-curation]] — legal constraints shape data sourcing
- [[concepts/multilingual-training-data]] — copyright law varies by jurisdiction

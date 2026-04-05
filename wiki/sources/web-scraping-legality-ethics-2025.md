---
title: "Source: Web Scraping Legality, Ethics, and Compliance (2025)"
type: source-summary
source: "[[raw/web-scraping-legality-ethics-2025]]"
related: ["[[concepts/web-scraping-ethics-and-law]]", "[[concepts/web-scraping-at-scale]]"]
tags: [web-scraping, legal, ethics, robots-txt, gdpr, compliance]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Web scraping legality analysis: hiQ v. LinkedIn confirms public data access is legal in US; GDPR imposes EUR 20M fines for personal data; EU AI Act requires training data provenance; robots.txt is non-binding but legally relevant."
---

## Key Points

- hiQ Labs v. LinkedIn (2022): accessing publicly available data is not unauthorized access under CFAA
- GDPR: fines up to EUR 20M/4% revenue for scraping personal data without legal basis
- EU AI Act (2025): new transparency requirements for AI training data provenance
- robots.txt is not legally binding but CNIL (France) treats compliance as factor in Legitimate Interest test
- Terms of Service violations don't trigger criminal liability but serve as evidence in disputes
- Six ethical practices: respect robots.txt, rate-limit, real user-agents, avoid PII, skip auth content, document practices

## Detailed Summary

This Browserless article provides the clearest 2025 legal framework for web scraping. The key insight is that legality depends on three factors: **data type** (public vs. personal vs. protected), **access method** (open vs. authenticated vs. bypassed), and **jurisdiction** (US CFAA vs. EU GDPR vs. Canada PIPEDA).

For knowledge base builders, the most relevant finding is that scraping publicly available content for research and knowledge compilation carries minimal legal risk in most jurisdictions. The risk increases dramatically when: (1) personal data is involved, (2) access controls are bypassed, or (3) the EU AI Act's training data provenance requirements apply.

The robots.txt analysis is nuanced: while not legally binding, respecting it is increasingly treated as a legal signal. France's CNIL explicitly considers robots.txt compliance in its Legitimate Interest balancing test, meaning ignoring Disallow directives creates legal exposure in the EU.

## Concepts Introduced or Discussed

- [[concepts/web-scraping-ethics-and-law]] — the core topic
- [[concepts/web-scraping-at-scale]] — legal constraints affect architecture choices

## Quotes & Evidence

> "Scraping legality isn't one-size-fits-all."
> "Ignoring [robots.txt] can undermine claims of acting in good faith."

## Metadata

- **Author**: Browserless
- **Date Published**: 2025-03
- **Format**: article
- **URL**: https://www.browserless.io/blog/is-web-scraping-legal

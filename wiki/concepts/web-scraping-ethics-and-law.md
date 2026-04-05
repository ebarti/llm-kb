---
title: "Web Scraping Ethics and Law"
type: concept
sources: ["[[sources/web-scraping-legality-ethics-2025]]", "[[sources/web-scraping-best-practices-2026]]"]
related: ["[[concepts/web-scraping-at-scale]]", "[[concepts/content-extraction]]", "[[concepts/data-quality-bottleneck]]"]
tags: [web-scraping, ethics, legal, robots-txt, gdpr, compliance]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Legal framework for web scraping: public data is generally legal (hiQ v. LinkedIn); GDPR imposes EUR 20M fines for personal data; EU AI Act requires training data provenance; robots.txt compliance is legally relevant though not binding."
---

## Overview

Web scraping operates in a complex legal and ethical landscape that knowledge base builders must navigate carefully. The core principle is that **scraping publicly available data for non-commercial research and knowledge compilation is generally low-risk**, but the specifics depend on data type, access method, and jurisdiction.

For LLM knowledge bases that ingest web content (like this one), the legal and ethical dimensions are not abstract — they directly constrain what content can be ingested and how.

## Legal Framework

### United States: CFAA
The Computer Fraud and Abuse Act governs unauthorized computer access. The landmark **hiQ Labs v. LinkedIn (2022)** ruling established that accessing publicly available data doesn't constitute unauthorized access. However, bypassing technical access controls (login walls, CAPTCHAs) can still violate CFAA.

### European Union: GDPR + AI Act
- **GDPR**: Scraping personal data (names, emails, behavioral data) without legal basis risks fines up to EUR 20 million or 4% of global revenue
- **EU AI Act (2025)**: New transparency requirements for AI training data — organizations scraping to train AI must document data provenance
- **CNIL (France)**: Explicitly considers robots.txt compliance in Legitimate Interest balancing test

### Canada: PIPEDA
Personal data collection and use governed by standards comparable to GDPR.

## robots.txt

The robots.txt protocol (at `example.com/robots.txt`) is the primary mechanism for websites to communicate crawling preferences.

**Legal status**: Not legally binding in itself, but:
- Compliance is treated as good faith signal by regulators
- Non-compliance is treated as negative signal in legal disputes
- CNIL considers it in Legitimate Interest balancing

**Best practice**: Always check and respect robots.txt before scraping, even for knowledge base construction.

## Ethical Principles for Knowledge Base Builders

1. **Prefer public APIs** — always check if the site offers an API before scraping
2. **Respect robots.txt** — honor Disallow directives
3. **Rate-limit requests** — align with human browsing speeds, never overload servers
4. **Attribute sources** — always record source URLs and authors in raw/ frontmatter
5. **Avoid PII** — don't scrape personal data without legal basis
6. **Skip authenticated content** — never bypass login walls
7. **Document practices** — maintain logs of what was scraped and when
8. **Check for CC/open licenses** — prefer openly licensed content

## Risk Matrix

| Content Type | Access Method | Jurisdiction | Risk Level |
|-------------|--------------|-------------|------------|
| Public article | Open web | US | Very Low |
| Public article | Open web | EU (no PII) | Low |
| Content with PII | Open web | EU | **High** |
| Behind login | Bypassed | Any | **Very High** |
| Public data for AI training | Open web | EU (AI Act) | Medium |
| robots.txt Disallowed | Scraped anyway | EU | Medium-High |

## Sources

- [[sources/web-scraping-legality-ethics-2025]] — comprehensive legal analysis
- [[sources/web-scraping-best-practices-2026]] — ethical best practices

## Related Concepts

- [[concepts/web-scraping-at-scale]] — legal constraints affect architecture
- [[concepts/content-extraction]] — what gets extracted matters legally

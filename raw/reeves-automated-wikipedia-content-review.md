---
title: "Machines in the Margins: A Systematic Review of Automated Content Generation for Wikipedia"
source: "https://arxiv.org/html/2509.22443"
author: "Neal Reeves, Elena Simperl"
date_published: 2025-09-01
date_ingested: 2026-04-05
tags: [Wikipedia, automated-content, AI-generation, systematic-review, CSCW]
type: paper
status: raw
discovered_via: search
---

# Machines in the Margins: Automated Content Generation for Wikipedia

**Authors:** Neal Reeves and Elena Simperl (King's College London; TU Munich)

## Methodology

Systematic literature review across five databases (ACM Digital Library, IEEE Explore, Sage, Scopus, Web of Science). Screened 4,909 initial results, selecting 51 peer-reviewed papers (2014 onward) describing implemented content generation approaches.

## Key Findings

### Content Types Generated

Nine categories identified: article sections, summaries, section headings, images/captions, links, infoboxes, navboxes, references, and categories. No study generated comprehensive articles with all content elements; most focused on single content types.

### Technical Approaches

Five methodological groups:
1. **Template/rule-based systems** — strong control but poor scalability
2. **Topic modeling** — requires less training data
3. **Graph-based methods** — leverages Wikipedia's relational structure
4. **Sequence-to-sequence models** — neural approaches
5. **Transformer-based approaches** — increasingly dominant in recent research

### Data Sources

Four primary sources: individual articles, existing Wikipedia content, Wikidata, and web content. Using Wikipedia as a source for generating "new" content raises verifiability concerns — "Wikipedia content cannot and should not be used as reference material" for Wikipedia articles.

### Evaluation Gaps

- 44 studies used computational metrics alone
- Only 4 directly engaged Wikipedia editors
- 7 studies deployed content to Wikipedia, monitoring subsequent edits
- "There is no guarantee that deployed content will receive edits" even when published

## Critical Implications

### For Wikipedia Communities

Automated generation risks replacing creative work, particularly affecting minority-language communities. Questions persist about whether tools should complement rather than substitute human contribution.

### For CSCW Generally

The review surfaces epistemic justice concerns — how automated systems might render certain contributors invisible — and questions about balancing technological support against opportunities for human learning and creative struggle.

## Conclusion

While diverse automated approaches exist, deployment remains limited. Significant gaps exist between research proposals and Wikipedia's practical policies, particularly regarding attribution, verifiability, and community acceptance.

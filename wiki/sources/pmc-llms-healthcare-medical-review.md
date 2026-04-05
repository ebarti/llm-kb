---
title: "Source: Large Language Models in Healthcare and Medical Applications"
type: source-summary
source: "[[raw/pmc-llms-healthcare-medical-review]]"
related: ["[[concepts/llm-healthcare-applications]]", "[[concepts/llm-applications-beyond-code]]", "[[concepts/ai-scientific-discovery]]"]
tags: [healthcare, medical-AI, clinical-decision-support, drug-discovery]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Comprehensive review covering 7 healthcare LLM domains — clinical decision support, education, patient care, literature analysis, drug discovery, radiology, and documentation — with GPT-4 at 93.1% on USMLE and Med-PaLM 2 +19% on MultiMedQA."
---

## Key Points

- Seven major application domains: clinical decision support, medical education, patient care, literature analysis, drug discovery, radiology, clinical documentation
- GPT-4 achieved 93.1% accuracy on MedQA (USMLE benchmark)
- Med-PaLM 2 exceeded baseline models by 19% on MultiMedQA suite
- RWE-LLM processed over 300,000 clinical interactions with robust error detection
- Specialized models: Med-PaLM, GatorTron, BioGPT, Meditron, Med-Flamingo, LLaVA-Med
- Drug discovery models: MolGPT, ChemLLM, AlphaFold, ESMFold
- Less than a third of studies address ethical, regulatory, and patient safety implications

## Detailed Summary

This PMC review provides the most comprehensive taxonomy of LLM applications in healthcare. The seven domains span the full clinical workflow from diagnosis through treatment and administration.

**Clinical decision support** is the most advanced domain: LLMs analyze patient symptoms and medical records to suggest diagnoses and recommend treatments. Stanford researchers employed LLMs for cardiac conditions, while NIH's [[entities/gatortron]] examines EHRs for drug interactions.

**Drug discovery** represents the most transformative potential: specialized chemical language models achieve notable results in de novo drug design. Models like MolGPT and ChemLLM predict compound behaviors in biological systems, while [[entities/alphafold]] and ESMFold handle protein structure prediction.

**Radiology and medical imaging** showcases multimodal capabilities: Med-Flamingo and [[entities/llava-med]] analyze radiological images alongside clinical data, while ChatCAD automates diagnostic report generation.

The review is notably candid about **challenges**: hallucinations producing plausible but wrong medical information, bias perpetuation from historical data affecting underrepresented populations, and the critical gap where less than a third of studies address ethical and regulatory implications. The authors recommend "maintaining a balance between innovation and caution."

## Concepts Introduced or Discussed

- [[concepts/llm-healthcare-applications]] -- seven-domain taxonomy
- [[concepts/ai-scientific-discovery]] -- drug discovery applications
- [[concepts/hallucination-contamination]] -- medical hallucination risks
- [[concepts/multimodal-ai]] -- radiology and imaging applications

## Metadata

- **Author**: Multiple (PMC)
- **Date Published**: 2025
- **Format**: paper (review)
- **URL**: https://pmc.ncbi.nlm.nih.gov/articles/PMC12189880/

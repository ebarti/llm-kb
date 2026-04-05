---
title: "Audio Generation"
type: concept
sources: ["[[sources/ai-music-generation-2026]]"]
related: ["[[concepts/diffusion-models]]", "[[concepts/audio-visual-generation]]", "[[concepts/video-generation]]", "[[entities/suno]]", "[[entities/udio]]", "[[entities/elevenlabs]]"]
tags: [audio-generation, music-ai, generative-ai, creative-tools]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "AI music and sound synthesis -- dominated in 2026 by Suno v5 (~100M users, 44.1kHz, 12-track stems) and Udio, with major label settlements legitimizing the space and ElevenLabs bringing voice synthesis expertise to music."
---

## Overview

Audio generation encompasses AI systems that synthesize music, sound effects, speech, and ambient audio from text descriptions, reference audio, or other inputs. The music generation segment has matured rapidly, with [[entities/suno]] achieving ~100 million users and a $2.4B+ valuation. Unlike [[concepts/image-generation]] which is dominated by open-source models, audio generation remains primarily a closed-source, platform-driven market.

## Key Ideas

### Music Generation Platforms

**[[entities/suno]] v5** is the market leader, offering:
- Output at 44.1kHz with up to 12 individual stem tracks
- Suno Studio: timeline-based editor with stem separation and MIDI export for DAW integration
- Natural vocal synthesis excelling in pop, rock, R&B with complex lyrical phrasing
- Free tier (10 songs/day) to Premier ($30/mo, 2000 songs)

**[[entities/udio]]** (ex-DeepMind engineers) prioritizes audio fidelity:
- Rated "almost indistinguishable from real recordings" for instrumental quality
- Inpainting tool for selective regeneration of specific song sections
- Licensing settled with UMG and Warner Music Group (2025)

**[[entities/elevenlabs]] Music** (launched August 2025) leverages the $11B company's voice synthesis technology:
- Vocals described as "unsettlingly realistic" with superior breath, vibrato, emotional inflection
- Songs up to 4 minutes, multiple languages
- Fewer editing tools than competitors

### Specialized and Open-Source

- **AIVA**: Orchestral/cinematic composition with MIDI editor. First AI recognized as composer by France's SACEM.
- **Soundraw**: Trains exclusively on in-house productions -- zero copyright risk. Instrumental only.
- **Meta MusicGen**: Fully open-source, self-hosted. Instrumental only.
- **Google MusicFX**: Free, 70-second limit, real-time DJ mode co-developed with Jacob Collier.

### Legal Transformation

The legal landscape shifted dramatically in 2025. Warner settled with Suno, and UMG settled with Udio. Both companies now form partnerships with major labels, transforming AI music from a litigation target to a licensed creative tool. This mirrors the trajectory of sampling technology decades earlier.

### Audio in Video Generation

A major 2026 trend is [[concepts/audio-visual-generation]]: [[entities/veo]] 3 generates synchronized sound effects, dialogue, and ambient audio alongside video from a single text prompt. [[entities/kling]] 3.0 produces native audio with character dialogue and lip synchronization. This convergence is eliminating entire post-production workflows.

## Technical Architecture

Music generation models generally use:
- **Neural audio codecs**: Compressing audio into discrete or continuous tokens (similar to [[concepts/visual-tokenization]] for images)
- **Autoregressive transformers**: Predicting audio tokens sequentially, conditioned on text
- **Diffusion-based refinement**: Some models use diffusion decoders for final waveform generation
- **Voice modeling**: Specialized attention to vocal characteristics, breath patterns, vibrato

## How It Connects

Audio generation shares architectural foundations with [[concepts/image-generation]] (diffusion and autoregressive approaches) and increasingly converges with [[concepts/video-generation]] through [[concepts/audio-visual-generation]]. The same neural codec + transformer architecture used for music applies to sound effects, speech, and ambient audio.

## Open Questions

- Will open-source music models catch up to commercial platforms?
- How will label partnerships shape the creative freedom of AI music tools?
- Can AI music models achieve the fine-grained control professional musicians need?
- When will real-time AI-assisted live performance become practical?

## Sources

- [[sources/ai-music-generation-2026]] -- 2026 market landscape

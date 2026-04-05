---
title: "Anti-Bot Evasion"
type: concept
sources: ["[[sources/web-scraping-best-practices-2026]]", "[[sources/python-scraping-tools-comparison]]", "[[sources/crawl4ai-llm-web-crawler]]"]
related: ["[[concepts/web-scraping-at-scale]]", "[[concepts/web-scraping-ethics-and-law]]", "[[concepts/content-extraction]]"]
tags: [anti-bot, web-scraping, proxy-rotation, stealth]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Techniques for avoiding web scraping detection: IP rotation, header randomization, behavior mimicry, session persistence, and headless browser stealth — balanced against ethical obligations to respect site owners."
---

## Overview

Anti-bot evasion is the set of techniques scrapers use to avoid detection and blocking by website protection systems. Modern websites deploy increasingly sophisticated defenses: Web Application Firewalls (WAFs), browser fingerprinting, behavioral analysis, CAPTCHAs, and rate limiting. Scrapers must navigate these without crossing ethical or legal boundaries (see [[concepts/web-scraping-ethics-and-law]]).

For knowledge base construction, the tension is real: some high-value content sources have aggressive anti-bot measures, but respecting those measures is both ethically correct and legally prudent. The goal is not "bypassing security" but "appearing as a legitimate, well-behaved user."

## Detection Mechanisms

### Request-Level
- **Rate analysis**: Too many requests too fast from one IP
- **Header inspection**: Missing or incorrect User-Agent, Referer, Accept headers
- **Cookie analysis**: Missing session cookies, inconsistent cookie behavior
- **TLS fingerprinting**: JA3/JA4 fingerprints of the TLS handshake reveal scraping libraries

### Browser-Level
- **Canvas fingerprinting**: Drawing operations reveal headless browser signatures
- **WebRTC analysis**: Reveals real IP behind proxies
- **Navigator properties**: headless Chrome has detectable properties (`navigator.webdriver = true`)
- **Plugin enumeration**: Real browsers have plugins; headless ones often don't

### Behavioral
- **Mouse/scroll patterns**: Bots don't move mice or scroll naturally
- **Click timing**: Bots click instantly; humans have variable delays
- **Session patterns**: Bots visit pages in systematic order; humans browse non-linearly

## Evasion Techniques

### IP Rotation
- **Residential proxies**: IPs from real ISPs, most expensive, hardest to detect
- **Datacenter proxies**: Cheaper but more easily identified
- **Mobile proxies**: IPs from mobile carriers, high trust level
- **Rotation frequency**: Per-request for aggressive scraping, per-session for stealth

### Header Management
- Rotate User-Agent strings across real browser versions
- Include realistic Accept, Accept-Language, Accept-Encoding headers
- Set appropriate Referer headers (e.g., Google search for new visits)
- Avoid Python library identifiers ("Python-urllib", "python-requests")

### Headless Browser Stealth
- [[entities/playwright]] stealth mode: patches navigator properties, canvas rendering, WebGL
- Puppeteer stealth plugin: community-maintained patches for Chrome detection evasion
- [[entities/crawl4ai]]: 3-tier anti-bot detection with automatic proxy escalation

### Behavior Mimicry
- Randomized delays between actions (not fixed intervals)
- Natural mouse movement trajectories
- Variable scrolling speeds
- Realistic viewport sizes

## Ethical Boundary

Anti-bot evasion exists on a spectrum:
- **Acceptable**: Rotating User-Agents, adding delays, using residential proxies
- **Gray area**: Stealth browser patches, session manipulation
- **Unacceptable**: Bypassing CAPTCHAs, breaking authentication, overwhelming servers

For knowledge base builders, the principle is: if the site is actively trying to prevent automated access, consider whether scraping it is appropriate, and whether there's an API or alternative source.

## Sources

- [[sources/web-scraping-best-practices-2026]] — proxy rotation, headers, behavior mimicry
- [[sources/python-scraping-tools-comparison]] — Playwright stealth capabilities
- [[sources/crawl4ai-llm-web-crawler]] — 3-tier anti-bot with proxy escalation

## Related Concepts

- [[concepts/web-scraping-at-scale]] — evasion enables scale
- [[concepts/web-scraping-ethics-and-law]] — ethical boundaries on evasion

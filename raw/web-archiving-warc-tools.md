---
title: "Web Archiving: WARC Format and Preservation Tools"
source: "https://github.com/iipc/awesome-web-archiving"
author: "International Internet Preservation Consortium (IIPC)"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [web-archiving, warc, preservation, internet-archive, digital-preservation]
type: repo
status: raw
discovered_via: search
---

# Web Archiving: WARC Format and Preservation Tools

Comprehensive overview of web archiving tools, formats, and resources curated by the International Internet Preservation Consortium.

## WARC Format

WARC (Web ARChive) is the ISO 28500:2017 standard for combining multiple digital resources into aggregate archive files. Used by Library of Congress, British Library, BnF, National Library of Australia, and Internet Archive.

## Acquisition Tools

### Browser-Based & Desktop Crawlers
- **ArchiveBox**: Maintains additive archive from RSS feeds, bookmarks, links using wget and Chrome headless
- **Browsertrix Crawler**: High-fidelity crawling in Docker with Chromium
- **Brozzler**: Distributed crawler using real Chrome/Chromium browser
- **HTTrack**: Website copying utility for offline browsing
- **Heritrix**: Internet Archive's open-source archival-quality web crawler
- **SingleFile**: Browser extension + CLI for single-file HTML archives
- **Wpull**: Wget-compatible downloader and crawler

### Specialized Capture
- **ArchiveWeb.Page**: Chrome plugin for interactive archiving with WARC/WACZ export
- **Auto Archiver**: Python script for social media preservation
- **crocoite**: Headless Chrome crawler outputting WARC
- **grab-site**: Archivist's web crawler with dashboard
- **Social Feed Manager**: Archives Twitter, Tumblr, Flickr, Weibo
- **twarc**: CLI for Twitter JSON data archiving

## Replay & Access

- **OpenWayback**: Open-source Wayback Machine implementation
- **PYWB**: Python 3 web archival replay tool
- **ReplayWeb.page**: Client-side WARC/WACZ replay engine
- **InterPlanetary Wayback (ipwb)**: WARC indexing using IPFS

## WARC I/O Libraries

- **Python**: warcio (streaming), FastWARC (high-performance), Warcat
- **Java**: jwarc (type-safe), Jwat (validation)
- **Go**: webarchive
- **Rust**: warc

## Analysis Frameworks

- **Archives Unleashed Toolkit (AUT)**: Apache Spark-based analysis
- **Common Crawl Jupyter notebooks**: Analysis of Common Crawl datasets

## Public Data Resources

- **Common Crawl**: Petabytes of web data in WARC format, freely available
- **Internet Archive Wayback Machine**: 800B+ archived pages
- **End of Term Archive**: Government web preservation

## Relevance to LLM Knowledge Bases

Web archiving provides:
1. **Permanence**: Raw source preservation when URLs disappear
2. **Provenance**: Full HTTP metadata (headers, timestamps, redirects)
3. **Completeness**: Full page snapshots including JS-rendered content
4. **Standards compliance**: ISO format with wide tool support

For knowledge base construction, archiving source pages in WARC format ensures raw sources remain accessible even if the original URL goes offline — a significant advantage over storing only extracted text.

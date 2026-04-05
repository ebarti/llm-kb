---
title: "Beautiful Soup"
type: entity
entity_type: tool
url: "https://www.crummy.com/software/BeautifulSoup/"
related: ["[[concepts/content-extraction]]", "[[entities/scrapy]]", "[[entities/playwright]]"]
tags: [beautiful-soup, python, html-parsing, web-scraping]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Python's most popular HTML/XML parsing library — lightweight, handles malformed markup gracefully, often used with requests for simple scraping or with Playwright for hybrid JS+parsing workflows."
---

## Overview

Beautiful Soup is a Python library for parsing HTML and XML documents. It creates a parse tree that allows navigation, searching, and modification of the document structure.

## Key Facts

- **Type**: Python library
- **URL**: https://www.crummy.com/software/BeautifulSoup/
- **Version**: 4.14.3
- **Notable for**: Graceful handling of malformed/broken HTML; simplest API for HTML parsing

## Features

- Multiple parser backends: html.parser, lxml (50% faster), html5lib (most lenient)
- Handles broken and malformed markup automatically
- Simple, Pythonic API (find, find_all, select)
- Lightweight with minimal dependencies

## Common Usage Pattern

```python
import requests
from bs4 import BeautifulSoup

response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
content = soup.find('article').get_text()
```

## Hybrid Pattern

Beautiful Soup is commonly combined with [[entities/playwright]] for JavaScript-rendered pages:
1. Playwright renders the page (handles JS)
2. Beautiful Soup parses the rendered HTML (efficient navigation)

## Mentions

- [[sources/python-scraping-tools-comparison]] — compared with Scrapy and Playwright
- [[concepts/content-extraction]] — as lightweight parsing tool

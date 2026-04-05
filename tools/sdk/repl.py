#!/usr/bin/env python3
"""
Interactive Python REPL with the Knowledge Base pre-loaded.

Opens a Python interactive shell with the KB class imported and an
instance created, ready for exploration.

Usage:
    python3 tools/sdk/repl.py
    python3 tools/sdk/repl.py --kb-path /path/to/kb
"""

import sys
import os
import code
import argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb import KnowledgeBase


INTRO = """
========================================
  LLM Knowledge Base - Interactive REPL
========================================

The KB is loaded as `kb`. Try:

  kb.get_stats()                                  # overall statistics
  kb.search("knowledge graph")                    # full-text search
  kb.get_article("concepts/llm-knowledge-base")   # read an article
  kb.get_articles(type="concept")                 # list all concepts
  kb.get_summaries()                              # one-line summaries
  kb.get_links("concepts/llm-knowledge-base")     # outgoing + incoming links
  kb.get_backlinks("concepts/llm-knowledge-base") # who links here?
  kb.get_related("concepts/llm-knowledge-base")   # related articles (1 hop)
  kb.get_orphans()                                # articles with no backlinks
  kb.get_hubs()                                   # most-connected articles
  kb.get_tag_cloud()                              # tag frequencies
  kb.get_log()                                    # recent activity
  kb.get_word_count()                             # total word count
  kb.get_word_count("concepts/llm-knowledge-base")# single article words
  kb.export_all()                                 # full JSON export dict

Type help(kb) for full API docs. Ctrl+D to exit.
"""


def main():
    parser = argparse.ArgumentParser(description="KB Interactive REPL")
    parser.add_argument("--kb-path", default="/Users/eloibarti/Desktop/agentic-ai",
                        help="Path to the knowledge base root")
    args = parser.parse_args()

    kb = KnowledgeBase(path=args.kb_path)

    # Pre-import useful modules into the REPL namespace
    import json
    from pprint import pprint

    namespace = {
        "kb": kb,
        "KnowledgeBase": KnowledgeBase,
        "json": json,
        "pprint": pprint,
    }

    console = code.InteractiveConsole(locals=namespace)
    console.interact(banner=INTRO, exitmsg="Goodbye!")


if __name__ == "__main__":
    main()

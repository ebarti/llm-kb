"""
Knowledge Base SDK — Python package for interacting with the LLM knowledge base.

Usage:
    from tools.sdk.kb import KnowledgeBase
    kb = KnowledgeBase()
    print(kb.get_stats())
"""

import sys
from pathlib import Path

# Ensure the SDK directory is on sys.path so 'kb' can be found
# whether this is imported as a package or run directly.
_sdk_dir = str(Path(__file__).resolve().parent)
if _sdk_dir not in sys.path:
    sys.path.insert(0, _sdk_dir)

try:
    from .kb import KnowledgeBase
except ImportError:
    from kb import KnowledgeBase

__all__ = ["KnowledgeBase"]
__version__ = "1.0.0"

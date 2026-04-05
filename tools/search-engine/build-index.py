#!/usr/bin/env python3
"""
Build (or rebuild) the search index for the wiki.
Usage: python build-index.py [--force]
"""

import argparse
import sys
import time
from pathlib import Path

# Import from search module
sys.path.insert(0, str(Path(__file__).resolve().parent))
from search import scan_documents, build_index, save_index, INDEX_FILE


def main():
    parser = argparse.ArgumentParser(description="Build the wiki search index")
    parser.add_argument("--force", action="store_true", help="Force full rebuild")
    args = parser.parse_args()

    print("Scanning wiki documents...")
    t0 = time.time()
    docs = scan_documents()
    print(f"  Found {len(docs)} documents")

    print("Building index...")
    index = build_index(docs)

    print("Saving index...")
    save_index(index)

    elapsed = time.time() - t0
    print(f"Index built in {elapsed:.2f}s")
    print(f"  Documents: {index['num_docs']}")
    print(f"  Vocabulary: {len(index['vocab'])} terms")
    print(f"  Avg doc length: {index['avg_dl']:.0f} tokens")
    print(f"  Saved to: {INDEX_FILE}")


if __name__ == "__main__":
    main()

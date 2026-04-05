# PRD-02: LLM Knowledge Base — Advanced Features

## Q&A System
- User asks questions via `./kb "question"`
- Claude reads `wiki/_meta/summaries.md` to find relevant articles
- Reads full articles as needed to construct answers
- Answers are optionally saved to `output/` or filed back into wiki
- Supports follow-up questions in interactive mode: `./kb -i`

## Output Rendering
- **Markdown reports**: saved to `output/reports/`
- **Marp slides**: saved to `output/slides/` — viewable via Obsidian Marp plugin
- **Python visualizations**: Claude writes matplotlib/plotly scripts, executes them, saves images to `output/images/`
- **Filing back**: user can say "file this into the wiki" to promote an output into a wiki article

## Wiki Linting
Triggered by `./kb "lint"` or `./kb "health check"`. Checks for:
- **Broken links**: wikilinks pointing to non-existent files
- **Orphan articles**: articles with no incoming links
- **Missing summaries**: articles without summary in frontmatter
- **Stale content**: raw files not yet reflected in wiki
- **Inconsistencies**: contradictory claims across articles
- **Gaps**: suggests new articles based on concept clustering
- **Missing data**: uses web search to fill gaps

Results saved to `output/lint-report.md`.

## Search Engine (`tools/search.sh`)
- Full-text search over all wiki content
- Returns ranked results with snippets
- Used by Claude as a tool for large queries
- Simple grep-based implementation (no external deps)

## Interactive Mode
- `./kb -i` opens an interactive session
- Claude maintains conversation context
- Can chain operations: "ingest this, then update the wiki, then tell me what's new"

## Incremental Compilation
- `wiki/_meta/manifest.json` tracks file hashes
- On compile, only processes changed/new files
- Existing wiki articles updated rather than rewritten
- Link graph recomputed incrementally

## Success Criteria
- Q&A answers cite specific wiki articles
- Lint catches real issues and suggests actionable fixes
- Search returns relevant results in under 1 second
- Interactive mode feels like a conversation with a research assistant

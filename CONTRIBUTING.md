# Contributing

## Development Workflow — worktrees only

**All development MUST happen in git worktrees.** The primary checkout at `~/Github/llm-kb` stays on `main` and is only used to launch worktrees.

### First-time setup

```bash
git clone git@github.com:ebarti/llm-kb.git ~/Github/llm-kb
cd ~/Github/llm-kb

# The search index is gitignored — rebuild locally
python3 tools/search-engine/build-index.py
```

### Per-task workflow

```bash
# Pick an open issue, then:
cd ~/Github/llm-kb
git fetch origin
BRANCH=feat/42-typed-graph-store
git worktree add ../llm-kb-$BRANCH -b $BRANCH origin/main

cd ../llm-kb-$BRANCH
# ... make changes, commit normally ...
bash tools/tests/run-all.sh         # before opening non-draft PR
git push -u origin $BRANCH

gh pr create --draft \
    --title "feat: typed graph store" \
    --body "Fixes #42 ..." \
    --base main
```

After the PR is merged:

```bash
cd ~/Github/llm-kb
git worktree remove ../llm-kb-$BRANCH
git branch -d $BRANCH
```

### Naming

- **Worktree directory**: `~/Github/llm-kb-<branch>`
- **Branch**: `<type>/<issue-number>-<short-slug>` where `<type>` ∈ `feat`, `fix`, `chore`, `docs`, `refactor`, `perf`, `test`
- **Commit subject**: `<type>: <imperative subject>` lowercase, no trailing period (matches existing `kb:` and `chore:` history)

### Parallel agents

When multiple Claude Code agents work in parallel, each uses its own worktree. The Agent tool's `isolation: "worktree"` parameter creates one automatically. Agents should:

1. Claim an issue in a GitHub comment (`@me working on this`).
2. Work in their isolated worktree.
3. Push their branch and open a **draft** PR.
4. Link the PR to the issue with `Fixes #N` in the body.
5. Mark the PR ready-for-review only after `tools/tests/run-all.sh` passes.

### Hard rules

- No direct pushes to `main`. Period.
- PRs open as **draft** until local tests pass.
- One issue per PR; one PR per branch; one branch per worktree.
- Do not commit `tools/search-engine/.index/`, `.idea/`, or `.obsidian/workspace*.json`.
- Do not hardcode absolute paths. Use `$KB_PATH` or compute from `__file__`.
- Rebuild the search index after wiki changes (local only, do not commit).

## Repository Layout

See [CLAUDE.md](CLAUDE.md) for the authoritative layout and operations manual.

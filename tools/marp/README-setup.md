---
title: "Marp Setup Instructions"
type: tool-docs
---

# Marp Slides -- Setup Instructions

This knowledge base includes a custom Marp theme and slide templates for generating professional presentations from wiki content.

## What is Marp?

Marp (Markdown Presentation Ecosystem) converts markdown files into slide presentations (HTML, PDF, PPTX). Each `---` separator creates a new slide. Frontmatter controls theme, pagination, and branding.

## Option 1: Obsidian Marp Slides Plugin (Recommended)

The easiest way to view and present slides directly in Obsidian.

### Installation

1. Open Obsidian Settings (Cmd+, or Ctrl+,)
2. Go to **Community Plugins** > **Browse**
3. Search for **"Marp Slides"**
4. Click **Install**, then **Enable**

### Using the Custom Theme

1. Open Marp Slides plugin settings in Obsidian
2. Under **Theme CSS**, add the path to the custom theme:
   ```
   tools/marp/kb-theme.css
   ```
   Or paste the full contents of `tools/marp/kb-theme.css` into the custom CSS field.
3. Slides using `theme: kb-theme` in their frontmatter will now render with the custom theme.

### Viewing Slides

- Open any `.md` file with `marp: true` in the frontmatter
- Use the Marp Slides command: **Marp: Toggle Marp Preview**
- Or right-click the file and select **Preview Marp Slides**

## Option 2: VS Code + Marp Extension

1. Install the **Marp for VS Code** extension from the marketplace
2. Open any slide `.md` file
3. Click the preview icon in the top-right corner
4. To use the custom theme, add to VS Code settings:
   ```json
   {
     "markdown.marp.themes": [
       "./tools/marp/kb-theme.css"
     ]
   }
   ```

## Option 3: marp-cli (Command Line)

For batch building slides to HTML or PDF.

### Installation

```bash
# Via npm (recommended)
npm install -g @marp-team/marp-cli

# Verify installation
marp --version
```

### Building Slides

```bash
# Build all slides in a directory to HTML
./tools/marp/build.sh output/slides/

# Build a single file
./tools/marp/build.sh output/slides/llm-knowledge-bases-overview.md

# Build as PDF (requires Chrome or Chromium)
./tools/marp/build.sh output/slides/ --pdf

# Watch mode -- rebuilds on file save
./tools/marp/build.sh --watch output/slides/llm-knowledge-bases-overview.md
```

### Direct marp-cli Usage

```bash
# HTML output with custom theme
marp --theme tools/marp/kb-theme.css --allow-local-files output/slides/topic.md

# PDF output
marp --theme tools/marp/kb-theme.css --pdf --allow-local-files output/slides/topic.md

# PPTX output
marp --theme tools/marp/kb-theme.css --pptx --allow-local-files output/slides/topic.md

# Watch mode
marp --theme tools/marp/kb-theme.css --watch output/slides/topic.md
```

## Using the Custom Theme

### Theme Features

The `kb-theme` theme includes:

- **Dark variant** (default): Deep blue background with green/blue accent colors
- **Light variant**: Add `<!-- _class: light -->` to any slide
- **Title slide**: Add `<!-- _class: title -->` for centered hero layout
- **Section divider**: Add `<!-- _class: divider -->` for section breaks
- **End slide**: Add `<!-- _class: end -->` for closing slides

### Slide Classes

```markdown
<!-- _class: title -->    Title/hero slide with gradient heading
<!-- _class: divider -->  Section divider with radial glow
<!-- _class: light -->    Light background variant
<!-- _class: end -->      Closing slide
```

### Two-Column Layouts

```html
<div class="columns">
<div>

Left column content (markdown works here)

</div>
<div>

Right column content

</div>
</div>
```

Variants: `columns` (50/50), `columns-wide-left` (66/33), `columns-wide-right` (33/66), `columns-3` (three equal columns).

### Stat Callouts

```html
<div class="stat">
<div class="number">42</div>
<div class="label">Articles</div>
</div>
```

### Badges

```html
<span class="badge">Default</span>
<span class="badge blue">Info</span>
<span class="badge orange">Warning</span>
<span class="badge red">Critical</span>
```

### Callout Boxes

```html
<div class="callout">Default callout</div>
<div class="callout info">Info callout</div>
<div class="callout warning">Warning callout</div>
<div class="callout danger">Danger callout</div>
```

## Slide Templates

Templates are available in `templates/slides/`:

| Template | Purpose |
|----------|---------|
| `topic-overview.md` | Present a single concept from the wiki |
| `comparison.md` | Compare two approaches (X vs. Y) |
| `research-briefing.md` | Summarize a research session |
| `wiki-status.md` | Report on wiki health and statistics |
| `entity-profile.md` | Profile a tool, person, or organization |

## Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Deep Blue | `#1a1b26` | Background |
| Surface | `#24283b` | Cards, code blocks |
| Accent Green | `#9ece6a` | Headings, emphasis, markers |
| Accent Blue | `#7aa2f7` | H2 headings, links |
| Accent Cyan | `#7dcfff` | H3 headings, operators |
| Accent Orange | `#ff9e64` | Inline code |
| Accent Magenta | `#bb9af7` | Italics, blockquote borders |
| Text Primary | `#c0caf5` | Body text |
| Text Secondary | `#565f89` | Muted text, captions |

This palette is inspired by the Tokyo Night color scheme used in many code editors, chosen for readability and visual consistency with Obsidian's dark mode.

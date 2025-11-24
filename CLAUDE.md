# Claude Context for tmy.se

This document provides context for AI assistants working on this Pelican blog.

## Project Overview

Personal blog at https://www.tmy.se built with Pelican static site generator. ~2,342 articles dating back to 2007, primarily in German, about Sweden, technology, and various topics.

## Recent Modernization (Nov 2025)

### Dependency Management
- Migrated to **uv** for Python package management
- `pyproject.toml` defines dependencies (pelican, pillow, markdown, piexif, pelican-photos, wand)
- Makefile updated: `PY?=uv run python`, `PELICAN?=uv run pelican`
- No need to manually activate virtualenvs - `uv run` handles it

### Plugin Migration
- Removed local `plugins/` directory (contained old photos and representative_image plugins)
- Now using official `pelican-photos` package from PyPI
- Fixed Pillow 10+ compatibility (`Image.ANTIALIAS` → `Image.LANCZOS`) was already done in local plugin

### Helper Scripts
- `post.py` - Create draft blog posts
- `picpost.py` - Create photo posts (grabs latest from ~/Downloads)
- Both modernized: use `pathlib`, respect `$EDITOR`, auto-increment slugs, date-only format (no time)
- Handle Swedish characters (ä→a, ö→o, å→a)

### Deployment Setup
- Git hook at `.git/hooks/pre-push` runs `make html` then `make rsync_upload` before push
- Deploys to `tmy@bestbo.se:/home/tmy/tmy.se` via rsync+ssh
- SSH key auth required (note: server rejects key auth if home directory has g+w permissions)
- Can bypass with `git push --no-verify`

### Categories → Tags Migration
- Disabled category system entirely (`CATEGORY_SAVE_AS = ''`)
- Migrated 2,017 posts from `Category: Schweden` to `Tags: Schweden`
- Script: `migrate_schweden_category.py` (adds tag, removes Category line)
- All other Category lines removed with `sed -i '/^Category:/d' content/*.md`
- Tags are the primary taxonomy now (1000+ tag pages)

### Configuration Notes

**pelicanconf.py (development):**
- Feeds disabled (all `FEED_*` set to None)
- `DELETE_OUTPUT_DIRECTORY = False` (preserves cache)
- `CACHE_CONTENT = True`, `LOAD_CONTENT_CACHE = True`
- Custom URL scheme: `/{slug}` for articles, no dates in URLs
- `DEFAULT_PAGINATION = 10`
- `DEFAULT_CATEGORY = 'uncategorized'` (required even though categories disabled)

**publishconf.py (production):**
- `SITEURL = 'https://www.tmy.se'`
- Feeds: `FEED_ATOM = 'atom'`, `FEED_RSS = 'feed'`, `FEED_MAX_ITEMS = 100`
- `CATEGORY_FEED_ATOM = None` (disabled)
- `DELETE_OUTPUT_DIRECTORY = True`

**robots.txt:**
```
Disallow: /index*     # Pagination pages
Disallow: /tag/       # Tag archive pages
Disallow: /drafts/    # Draft posts
```

### Content Structure
- Articles: `content/*.md` → `output/{slug}`
- Drafts: `Status: draft` → `output/drafts/{slug}`
- Static files: Listed in `STATIC_PATHS` (pic/, robots.txt, favicon.ico, etc.)
- Photos: `content/pic/` processed by pelican-photos plugin

### Post Metadata Format
```markdown
Title: Post Title
Slug: post-slug
Date: 2025-11-23
Status: published
Tags: tag1, tag2

Content here.
```

**Important:**
- Date is YYYY-MM-DD only (no time) - sufficient for infrequent posting
- Status defaults to 'draft' via `DEFAULT_METADATA`
- No Category field - categories disabled
- Summary marker: `<!-- more -->` to show excerpt on index/feeds

### Common Commands
```bash
make html              # Build site
make serve             # Build and serve at localhost:8000
make devserver         # Build, serve, auto-reload on changes
make drafts            # List all draft posts
make publish           # Build with production settings
make rsync_upload      # Build and deploy to server
git push               # Triggers pre-push hook (builds + deploys + pushes)

./post.py "Title"      # Create draft post
./picpost.py "Title"   # Create photo post
```

### Theme
- Custom theme: `theme/chunk/`
- Comment code (isso/disqus) still in templates but disabled (comments.tmy.se is offline)
- Consider removing comment blocks from `theme/chunk/templates/article.html` if touching templates

### Known Issues/Quirks
- RSS feeds show `<category>uncategorized</category>` for posts - Pelican requirement, can't be fully removed without template override
- Photos plugin needs ImageMagick installed (required by wand package)
- Cache directory speeds up rebuilds significantly
- `t/` and `tmp/` directories preserved during rsync (see Makefile excludes)

### File Locations
- Content: `content/*.md`
- Config: `pelicanconf.py`, `publishconf.py`
- Theme: `theme/chunk/`
- Output: `output/` (git-ignored)
- Cache: `cache/` (git-ignored)
- Photos: `content/pic/`
- Static: As defined in `STATIC_PATHS`

### Migration Scripts
- `migrate_schweden_category.py` - Category→Tag migration (can be deleted after use)

### Dependencies Note
The `wand` package requires ImageMagick to be installed on the system:
```bash
# Debian/Ubuntu
sudo apt install imagemagick libmagickwand-dev

# If ImageMagick not available, images in picpost.py won't resize
```

## SEO/Performance
- 234 pagination pages (index, index2...index234) - excluded from search engines
- 1000+ tag pages - excluded from search engines via robots.txt
- Focus search engines on ~2,342 actual article pages
- No tracking/analytics/cookies (isso comments disabled)
- Feeds at `/atom` and `/feed` (RSS)

## Maintenance Tips
- Run `make drafts` to see unpublished posts
- Use `<!-- more -->` marker to show excerpts instead of full posts on index
- Keep `pyproject.toml` dependencies updated via `uv`
- Cache directory can be deleted if builds act strange
- Test builds with `make html` before deploying

## Last Updated
November 2025 - Major modernization and cleanup

# tmy.se

Source files for my blog at https://www.tmy.se - built with Pelican.

## Setup

Dependencies are managed with `uv` via `pyproject.toml`:
```bash
uv sync          # Install/update dependencies
```

**Dependencies:**
- pelican - static site generator
- pelican-photos - photo gallery plugin
- pillow - image processing
- markdown - markdown support
- piexif - EXIF metadata handling

## Development

```bash
make html        # Build site to output/
make serve       # Build and serve at http://localhost:8000
make devserver   # Build, serve, and auto-reload on changes
make clean       # Remove generated files
```

## Publishing

### Automated (recommended)
```bash
git commit -am "New post"
git push
```

The pre-push hook automatically:
1. Runs `make html` (aborts if build fails)
2. Runs `make rsync_upload` (deploys to bestbo.se)
3. Pushes to GitHub

### Manual
```bash
make rsync_upload    # Build + rsync to bestbo.se:/home/tmy/tmy.se
```

To skip the hook:
```bash
git push --no-verify
```

## Configuration

- `pelicanconf.py` - Development settings
- `publishconf.py` - Production settings (SITEURL, feeds)
- `theme/chunk/` - Custom theme
- `content/` - Blog posts and pages

## SSH Deploy

Deploys via rsync+ssh to:
- Host: `bestbo.se`
- User: `tmy`
- Path: `/home/tmy/tmy.se`

SSH key auth required (already configured).

## Notes

- Draft posts: Set `status: draft` in metadata → published to `/drafts/{slug}`
- Photos: Place in `content/pic/` → processed by photos plugin
- Cache enabled for faster rebuilds
- Directories `t/` and `tmp/` are preserved during deployment

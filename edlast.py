#!/usr/bin/env -S uv run

import os
from subprocess import call
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
CONT = ROOT / 'content'

# Find all markdown files in content/
md_files = list(CONT.glob('*.md'))

if not md_files:
    print('No files found in content/')
    exit(1)

# Get the most recently modified file
latest = max(md_files, key=lambda f: f.stat().st_mtime)

print(f'Opening: {latest.name}')

editor = os.environ.get('EDITOR', 'vim')
call([editor, str(latest)])

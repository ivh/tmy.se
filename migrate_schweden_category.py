#!/usr/bin/env python3
"""
Migrate Category: Schweden to Tags: schweden and remove Category line
"""

import re
from pathlib import Path

CONTENT_DIR = Path(__file__).parent / 'content'

def migrate_post(filepath):
    """Add schweden tag and remove Category line if Category contains Schweden"""
    content = filepath.read_text()

    # Check if this post has Category line with Schweden anywhere
    has_schweden_category = re.search(r'^Category:.*Schweden', content, re.MULTILINE)
    if not has_schweden_category:
        return False

    modified = False
    lines = content.split('\n')
    new_lines = []

    for i, line in enumerate(lines):
        # Remove any Category line that contains Schweden
        if line.startswith('Category:') and 'Schweden' in line:
            modified = True
            continue

        # Add Schweden to Tags if Tags line exists
        if line.startswith('Tags:'):
            tags = line[5:].strip()
            if tags:
                # Has existing tags
                if 'schweden' not in tags.lower():
                    line = f'Tags: {tags}, Schweden'
                    modified = True
            else:
                # Empty tags line
                line = 'Tags: Schweden'
                modified = True

        new_lines.append(line)

    # If there was no Tags line, add one after the metadata section
    if modified and not any(l.startswith('Tags:') for l in new_lines):
        # Find where to insert (after Date, Status, or Slug line)
        insert_pos = 0
        for i, line in enumerate(new_lines):
            if line.startswith(('Date:', 'Status:', 'Slug:')):
                insert_pos = i + 1
        new_lines.insert(insert_pos, 'Tags: Schweden')

    if modified:
        filepath.write_text('\n'.join(new_lines))
        return True

    return False

if __name__ == '__main__':
    count = 0
    for md_file in CONTENT_DIR.glob('*.md'):
        if migrate_post(md_file):
            print(f'✓ {md_file.name}')
            count += 1

    print(f'\nMigrated {count} posts from Category: Schweden to Tags: Schweden')

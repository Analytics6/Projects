#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / 'project_markdowns'
TEMPLATE_FILE = MD_DIR / '_detailed_er_template.md'
BACKUP_DIR = ROOT / 'backups_er'

if not TEMPLATE_FILE.exists():
    print(f"Template not found: {TEMPLATE_FILE}")
    raise SystemExit(1)

BACKUP_DIR.mkdir(exist_ok=True)

template = TEMPLATE_FILE.read_text()

md_files = sorted([p for p in MD_DIR.glob('*.md') if p.name not in ('_expanded_template.md','_detailed_er_template.md')])
updated = []
skipped = []

for md in md_files:
    text = md.read_text()
    if '## Detailed ER Diagram' in text:
        skipped.append(md.name)
        continue

    # create a safe backup copy in backups_er
    bak = BACKUP_DIR / (md.name + '.pre_er.bak')
    bak.write_text(text)

    stem = md.stem
    prefix = re.sub(r'[^a-z0-9]', '_', stem.lower())
    expansion = template.replace('{{PREFIX}}', prefix).replace('{{FILENAME}}', md.name)

    new_text = text.rstrip() + '\n\n## Detailed ER Diagram\n\n' + expansion + '\n'
    md.write_text(new_text)
    updated.append(md.name)

print(f"Processed {len(md_files)} files: updated={len(updated)}, skipped={len(skipped)}")
if updated:
    print('Updated files:')
    for f in updated:
        print(' -', f)
if skipped:
    print('Skipped (already had detailed ER):')
    for f in skipped:
        print(' -', f)

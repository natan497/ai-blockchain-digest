#!/usr/bin/env python3
"""Rebuild index.html post list from files in posts/."""
import re
from pathlib import Path

MONTHS = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

posts = sorted(Path('posts').glob('*.md'), reverse=True)

items = []
for f in posts:
    m = re.match(r'^(\d{4})-(\d{2})-(\d{2})-', f.name)
    if not m:
        continue
    year, month, day = int(m.group(1)), int(m.group(2)), int(m.group(3))
    date_str = f'{MONTHS[month - 1]} {day}, {year}'
    items.append(
        f'      <li>\n'
        f'        <a href="post.html?post=posts/{f.name}">'
        f'AI &amp; Blockchain Digest &mdash; {date_str}</a>\n'
        f'        <div class="post-date">{date_str}</div>\n'
        f'      </li>'
    )

post_list_html = '\n'.join(items)

index_path = Path('index.html')
content = index_path.read_text()

new_content = re.sub(
    r'(<ul class="post-list">).*?(</ul>)',
    f'\\1\n{post_list_html}\n    \\2',
    content,
    flags=re.DOTALL
)

index_path.write_text(new_content)
print(f'Built index.html with {len(items)} post(s)')

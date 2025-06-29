#!/usr/bin/env uv
"""
Check all links in Jekyll posts for validity using uv (ultra-fast Python runner).
- Scans all .md files in _posts/
- Finds all http(s):// links
- Checks each link for HTTP 200 OK
- Prints a report of broken links
"""
import re
import sys
import os
import httpx
from pathlib import Path
import asyncio

POSTS_DIR = Path('_posts')
LINK_RE = re.compile(r'https?://[^\s)>"]+')
TIMEOUT = 10

async def check_link(session, url):
    try:
        r = await session.get(url, timeout=TIMEOUT, follow_redirects=True)
        return url, r.status_code
    except Exception as e:
        return url, str(e)

async def main():
    all_links = {}
    for post in POSTS_DIR.glob('*.md'):
        with open(post, encoding='utf-8') as f:
            content = f.read()
        links = LINK_RE.findall(content)
        if links:
            all_links[post] = links
    if not all_links:
        print('No links found.')
        return
    print(f'Checking {sum(len(v) for v in all_links.values())} links...')
    async with httpx.AsyncClient() as session:
        tasks = []
        for post, links in all_links.items():
            for link in links:
                tasks.append(check_link(session, link))
        results = await asyncio.gather(*tasks)
    # Map url to status
    status_map = dict(results)
    broken = []
    for post, links in all_links.items():
        for link in links:
            status = status_map.get(link)
            if status != 200:
                broken.append((post, link, status))
    if broken:
        print('\nBroken links:')
        for post, link, status in broken:
            print(f'{post}: {link} -> {status}')
    else:
        print('All links OK!')

if __name__ == '__main__':
    asyncio.run(main())

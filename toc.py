#!/usr/bin/env python3
"""
Replace [TOC] in a markdown file with a generated table of contents.
Only headings appearing after [TOC] are included.

Usage:
    python toc.py <file.md> [options]

Options:
    --mindepth INT   Heading level to start from (default: 2, meaning ##)
    --maxdepth INT   Heading level to end at   (default: 3, meaning ###)
    --numbered       Use numbered TOC (1., 1.1, 1.2, 2., ...) instead of bullets
    --inplace        Overwrite the file in place (default: print to stdout)
"""

import re
import sys
import argparse
from pathlib import Path


def slugify(title: str) -> str:
    """Generate a GitHub-compatible anchor from a heading title."""
    anchor = title.lower()
    anchor = re.sub(r'[^\w\s-]', '', anchor)
    anchor = re.sub(r'\s+', '-', anchor)
    anchor = re.sub(r'-+', '-', anchor)
    return anchor.strip('-')


def parse_headings(text: str, mindepth: int, maxdepth: int) -> list[dict]:
    """Extract headings after [TOC] within the given depth range."""
    headings = []
    in_fence = False
    after_toc = False

    for line in text.splitlines():
        if re.match(r'^```', line):
            in_fence = not in_fence
        if in_fence:
            continue
        if '[TOC]' in line:
            after_toc = True
            continue
        if not after_toc:
            continue
        m = re.match(r'^(#{1,6})\s+(.+)', line)
        if m:
            level = len(m.group(1))
            if mindepth <= level <= maxdepth:
                headings.append({'level': level, 'title': m.group(2).strip()})

    return headings


def build_bullet_toc(headings: list[dict], mindepth: int) -> str:
    lines = []
    for h in headings:
        indent = '  ' * (h['level'] - mindepth)
        anchor = slugify(h['title'])
        lines.append(f"{indent}- [{h['title']}](#{anchor})")
    return '\n'.join(lines)


def build_numbered_toc(headings: list[dict], mindepth: int, maxdepth: int) -> str:
    depth = maxdepth - mindepth + 1
    counters = [0] * depth
    lines = []

    for h in headings:
        idx = h['level'] - mindepth
        counters[idx] += 1
        for i in range(idx + 1, depth):
            counters[i] = 0

        number = '.'.join(str(c) for c in counters[:idx + 1])
        indent = '  ' * idx
        anchor = slugify(h['title'])
        lines.append(f"{indent}- {number}. [{h['title']}](#{anchor})")

    return '\n'.join(lines)


def generate_toc(text: str, mindepth: int, maxdepth: int, numbered: bool) -> str:
    headings = parse_headings(text, mindepth, maxdepth)
    if not headings:
        return ''
    if numbered:
        return build_numbered_toc(headings, mindepth, maxdepth)
    else:
        return build_bullet_toc(headings, mindepth)


def main():
    parser = argparse.ArgumentParser(
        description='Replace [TOC] in a markdown file with a generated table of contents.'
    )
    parser.add_argument('file', help='Markdown file to process')
    parser.add_argument('--mindepth', type=int, default=2,
                        help='Heading level to start from (default: 2 = ##)')
    parser.add_argument('--maxdepth', type=int, default=3,
                        help='Heading level to end at (default: 3 = ###)')
    parser.add_argument('--numbered', action='store_true',
                        help='Use numbered TOC (1., 1.1, ...) instead of bullets')
    parser.add_argument('--inplace', action='store_true',
                        help='Overwrite the file in place')
    args = parser.parse_args()

    if args.mindepth < 1 or args.maxdepth > 6 or args.mindepth > args.maxdepth:
        print("Error: mindepth must be >= 1, maxdepth <= 6, and mindepth <= maxdepth.", file=sys.stderr)
        sys.exit(1)

    path = Path(args.file)
    if not path.exists():
        print(f"Error: file not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    text = path.read_text(encoding='utf-8')

    if '[TOC]' not in text:
        print("Warning: [TOC] marker not found in file.", file=sys.stderr)
        sys.exit(1)

    toc = generate_toc(text, args.mindepth, args.maxdepth, args.numbered)
    result = text.replace('[TOC]', toc)

    if args.inplace:
        path.write_text(result, encoding='utf-8')
        print(f"✓ TOC written to {args.file}")
    else:
        print(result)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Batch-crawl arXiv search results for the awesome list curation pass."""

from __future__ import annotations

import argparse
import html
import json
import re
import urllib.parse
import urllib.request


def clean(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def crawl(query: str, size: int = 200, start: int = 0) -> list[dict[str, str]]:
    params = {
        "query": query,
        "searchtype": "all",
        "abstracts": "show",
        "order": "-announced_date_first",
        "size": str(size),
        "start": str(start),
    }
    url = "https://arxiv.org/search/?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "awesome-dexterous-hand/1.0 (metadata curation)"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        page = response.read().decode("utf-8", "replace")

    records = []
    for block in re.findall(r'<li class="arxiv-result">(.*?)</li>', page, re.S):
        match = re.search(r'<p class="list-title.*?<a href="([^"]+/abs/([^"]+))"', block, re.S)
        title = re.search(r'<p class="title[^>]*>(.*?)</p>', block, re.S)
        abstract = re.search(r'<span class="abstract-full[^>]*>(.*?)</span>', block, re.S)
        date = re.search(r'<p class="is-size-7[^>]*>(Submitted .*?)</p>', block, re.S)
        if not match or not title:
            continue
        records.append(
            {
                "id": match.group(2),
                "url": "https://arxiv.org/abs/" + match.group(2),
                "title": clean(title.group(1)),
                "abstract": clean(abstract.group(1)) if abstract else "",
                "date": clean(date.group(1)) if date else "",
                "query": query,
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", action="append", required=True)
    parser.add_argument("--size", type=int, default=200)
    parser.add_argument("--output", default="arxiv_results.json")
    args = parser.parse_args()

    merged: dict[str, dict[str, str]] = {}
    for query in args.query:
        for record in crawl(query, size=args.size):
            merged.setdefault(record["id"], record)
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(list(merged.values()), handle, ensure_ascii=False, indent=2)
    print(f"crawled {len(merged)} unique arXiv records -> {args.output}")


if __name__ == "__main__":
    main()

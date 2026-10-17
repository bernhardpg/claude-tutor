# [claude]
"""Download missing paper PDFs into papers/<topic>/pdfs/ (gitignored).

Reads the reading-list table in each papers/<topic>/README.md: the first link in a table row
is the paper. arXiv abs/pdf links and direct .pdf links are downloaded; rows without one are
skipped. Files are named <year>_<first author>_<link text>.pdf, e.g. 2025_Ze_TWIST.pdf; for
arXiv papers the year and author come from the arXiv API, otherwise from the Year column.

    uv run papers/fetch.py              # all topics
    uv run papers/fetch.py humanoid-wbc # one topic
"""

import re
import subprocess
import sys
import time
import unicodedata
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

PAPERS = Path(__file__).parent
FIRST_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
ARXIV = re.compile(r"arxiv\.org/(?:abs|pdf)/([\w.\-/]+?)(?:v\d+)?(?:\.pdf)?$")


def pdf_url(url: str) -> str | None:
    if m := ARXIV.search(url):
        return f"https://arxiv.org/pdf/{m.group(1)}"
    if url.lower().endswith(".pdf") and url.startswith("http"):
        return url
    return None


def slug(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^\w.\-]+", "-", text).strip("-")


def papers(readme: Path):
    """Yield (name, year from the table, pdf url, arXiv id or None) per paper row."""
    for line in readme.read_text().splitlines():
        if not line.startswith("|") or not (m := FIRST_LINK.search(line)):
            continue
        name, url = m.groups()
        if src := pdf_url(url):
            year = next((c.strip() for c in line.split("|")[2:] if re.fullmatch(r"\s*\d{4}\s*", c)), "")
            arxiv_id = m2.group(1) if (m2 := ARXIV.search(url)) else None
            yield slug(name), year, src, arxiv_id


def arxiv_meta(ids: list[str]) -> dict[str, tuple[str, str]]:
    """arXiv id -> (year of first version, first author's last name)."""
    if not ids:
        return {}
    url = f"https://export.arxiv.org/api/query?id_list={','.join(ids)}&max_results={len(ids)}"
    with urllib.request.urlopen(url, timeout=60) as r:
        root = ET.fromstring(r.read())
    ns = {"a": "http://www.w3.org/2005/Atom"}
    meta = {}
    for e in root.findall("a:entry", ns):
        entry_id = re.sub(r"v\d+$", "", e.findtext("a:id", "", ns).rsplit("/abs/", 1)[-1])
        author = e.find("a:author/a:name", ns).text.split()[-1]
        meta[entry_id] = (e.findtext("a:published", "", ns)[:4], slug(author))
    return meta


def main():
    topics = sys.argv[1:] or sorted(p.parent.name for p in PAPERS.glob("*/README.md"))
    for topic in topics:
        out = PAPERS / topic / "pdfs"
        rows = list(papers(PAPERS / topic / "README.md"))
        meta = arxiv_meta([a for *_, a in rows if a])
        for name, year, src, arxiv_id in rows:
            year, author = meta.get(arxiv_id, (year, ""))
            dest = out / ("_".join(filter(None, [year, author, name])) + ".pdf")
            if dest.exists():
                continue
            out.mkdir(exist_ok=True)
            print(f"{topic}/{name}  <-  {src}")
            download(src, dest)
            time.sleep(1)  # be polite to arXiv


def download(src: str, dest: Path):
    # curl, not urllib: urllib reliably truncates some large arXiv PDFs mid-stream
    part = dest.with_suffix(".part")  # never leave a truncated file under the final name
    ok = subprocess.run(["curl", "-fsSL", "--retry", "3", "-o", part, src]).returncode == 0
    if ok:
        part.rename(dest)
    else:
        part.unlink(missing_ok=True)
        print("  FAILED")


if __name__ == "__main__":
    main()

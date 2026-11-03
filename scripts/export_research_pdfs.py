#!/usr/bin/env python3
"""Export the Cascade November 3, 2026 cited research packet to PDF.

The input Markdown files are the authoritative editable sources. The output
is generated during each GitHub Pages deployment and included in the static
site. Links and Chicago-style superscript footnotes are preserved.

Run from the repository root:
  python scripts/export_research_pdfs.py --root . --out docs/downloads
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import quote, urlsplit
from html import escape

import markdown
from bs4 import BeautifulSoup
from pypdf import PdfReader, PdfWriter
from weasyprint import HTML


SOURCES = [
    (
        "Cascade proposed M-2 industrial ordinance",
        "proposals/DRAFT-ORDINANCE-M2-DATA-CENTER-PERFORMANCE-STANDARDS-2026-11-03.md",
        "cascade-m2-ordinance-2026-11-03.pdf",
        False,
    ),
    (
        "Cascade proposed Chapter 165 definitions ordinance",
        "proposals/DRAFT-ORDINANCE-CH165-DEFINITIONS-2026-11-03.md",
        "cascade-definitions-ordinance-2026-11-03.pdf",
        False,
    ),
    (
        "Iowa law and dictionary definitions - 86 terms",
        "dataset/policy/38_IOWA_STATE_AND_M2_DEFINITIONS_2026-11-03.md",
        "cascade-definitions-reference-2026-11-03.pdf",
        True,
    ),
    (
        "Data center litigation - 27 case abstracts",
        "dataset/policy/40_DATA_CENTER_CASE_ABSTRACTS_2026-11-03.md",
        "cascade-case-abstracts-2026-11-03.pdf",
        False,
    ),
]
COMBINED_NAME = "cascade-complete-research-packet-2026-11-03.pdf"
SITE_BASE = "https://ttbakiatwoam.github.io/cascade-data-center"
REPO_BASE = "https://github.com/ttbakiatwoam/cascade-data-center/blob/master"
CSS = r"""
@page {
  size: letter;
  margin: 0.75in 0.77in 0.76in 0.77in;
  @top-right {
    content: "CASCADE, IOWA  |  DISCUSSION DRAFT";
    font: 7.6pt "DejaVu Sans", sans-serif;
    color: #536273;
  }
  @bottom-left {
    content: "Independent research  |  3 November 2026";
    font: 7.2pt "DejaVu Sans", sans-serif;
    color: #687481;
  }
  @bottom-right {
    content: "Page " counter(page);
    font: 7.2pt "DejaVu Sans", sans-serif;
    color: #687481;
  }
}
html { color: #172333; }
body { font: 9.5pt/1.43 "DejaVu Serif", "Liberation Serif", serif; }
h1, h2, h3, h4 { font-family: "DejaVu Sans", "Liberation Sans", sans-serif; line-height: 1.26; color: #192d46; break-after: avoid; }
h1 { font-size: 17pt; margin: 0.11in 0 0.20in; border-bottom: 1.5pt solid #344b69; padding-bottom: 0.12in; }
h2 { font-size: 12.4pt; margin: 0.28in 0 0.11in; border-bottom: 0.35pt solid #cbd3db; padding-bottom: 0.05in; }
h3 { font-size: 10.5pt; margin: 0.22in 0 0.07in; }
h4 { font-size: 9.6pt; margin: 0.1in 0 0.06in; }
p { margin: 0 0 0.115in; orphans: 2; widows: 2; }
strong { color: #162b44; }
blockquote { border-left: 2pt solid #7b8a9a; padding-left: 0.14in; margin: 0.15in 0 0.22in; color: #39475a; }
ul, ol { padding-left: 0.26in; margin: 0.09in 0 0.17in; }
li { margin-bottom: 0.04in; }
a { color: #1f527f; text-decoration: none; overflow-wrap: anywhere; }
sup, .footnote-ref { font-size: 70%; line-height: 0; vertical-align: super; }
hr { border: none; border-top: 0.5pt solid #cbd3db; margin: 0.26in 0; }
table { border-collapse: collapse; table-layout: fixed; width: 100%; font-size: 8.5pt; margin: 0.12in 0 0.22in; }
thead { display: table-header-group; }
tr { break-inside: avoid; }
th, td { border-bottom: 0.4pt solid #c7d1dc; padding: 6pt 7pt; text-align: left; vertical-align: top; overflow-wrap: anywhere; }
th { color: #192d46; font-family: "DejaVu Sans", sans-serif; background: #eef2f7; }
section.glossary-term { margin: 0.17in 0 0.19in; padding-bottom: 0.075in; border-bottom: 0.4pt solid #d7e0e7; break-inside: avoid; }
.glossary-term h3 { font-size: 10pt; margin: 0 0 0.10in; }
.glossary-term p { font-size: 9pt; margin-bottom: 0.055in; line-height: 1.34; }
.glossary-term .field-label { font-family: "DejaVu Sans", sans-serif; font-weight: bold; color: #364d69; }
.footnote { border-top: 0.75pt solid #c5ced8; margin-top: 0.26in; padding-top: 0.12in; font-size: 8pt; }
.footnote ol, .footnote li, .footnote p { font-size: 8pt; overflow-wrap: anywhere; }
.footnote li { margin-bottom: 0.07in; }
.codehilite, code { overflow-wrap: anywhere; font-size: 8pt; }
.meta { font: 8pt "DejaVu Sans", sans-serif; color: #566675; margin-bottom: 0.16in; }
"""


def local_link_to_public(href: str, source_path: Path, root: Path) -> str:
    if href.startswith(("http://", "https://", "#", "mailto:", "tel:")):
        return href
    if "{{" in href or "{%" in href:
        return SITE_BASE + "/"
    if href.startswith("/downloads/"):
        return SITE_BASE + href
    # Preserve GitHub blob links for references to other project files.
    try:
        target = (source_path.parent / href.split("#", 1)[0]).resolve()
        rel = target.relative_to(root.resolve())
        suffix = "#" + href.split("#", 1)[1] if "#" in href else ""
        if rel.parts and rel.parts[0] == "docs":
            return SITE_BASE + "/" + quote(str(rel.relative_to("docs")).replace("\\", "/")) + suffix
        return REPO_BASE + "/" + quote(rel.as_posix()) + suffix
    except (ValueError, OSError):
        return href


def simplify_reference_tables(soup: BeautifulSoup) -> None:
    """Reflow seven-column dictionaries into accessible printable entries."""
    tables = list(soup.find_all("table"))
    # A stray blank line or closing </div> can terminate the first Markdown
    # table early. Without strict row counts, the remaining definition rows
    # appear as raw pipe-delimited text in the PDF instead of glossary entries.
    expected_rows = (55, 5, 26)
    if len(tables) != len(expected_rows):
        raise RuntimeError(
            f"Expected {len(expected_rows)} glossary tables, found {len(tables)}"
        )
    for index, table in enumerate(tables):
        thead = table.find("thead")
        heads = [cell.get_text(" ", strip=True) for cell in thead.find_all("th")] if thead else []
        if len(heads) < 6:
            raise RuntimeError("Dictionary table has fewer than six columns")
        new = soup.new_tag("div")
        new["class"] = ["glossary-entries"]
        tbody = table.find("tbody")
        entries = tbody.find_all("tr", recursive=False) if tbody else []
        if len(entries) != expected_rows[index]:
            raise RuntimeError(
                f"Glossary table {index+1} has {len(entries)} rows; "
                f"expected {expected_rows[index]}. Check for a broken "
                "Markdown table boundary or prematurely closed wrapper."
            )
        for tr in entries:
            cells = tr.find_all("td", recursive=False)
            if len(cells) != len(heads):
                raise RuntimeError("Dictionary row does not match header width")
            sec = soup.new_tag("section")
            sec["class"] = ["glossary-term"]
            heading = soup.new_tag("h3")
            for child in list(cells[0].contents):
                heading.append(child.extract())
            sec.append(heading)
            for idx in range(1, len(cells)):
                p = soup.new_tag("p")
                lab = soup.new_tag("span")
                lab["class"] = ["field-label"]
                lab.string = heads[idx] + ": "
                p.append(lab)
                for child in list(cells[idx].contents):
                    p.append(child.extract())
                sec.append(p)
            new.append(sec)
        table.replace_with(new)


def document_html(source_path: Path, root: Path, title: str, glossary: bool) -> str:
    raw = source_path.read_text(encoding="utf-8")
    if raw.startswith("---\n"):
        raw = re.sub(r"\A---\n.*?\n---\n", "", raw, flags=re.S)
    raw = raw.replace("{{ '/draft-ordinance/' | relative_url }}", SITE_BASE + "/draft-ordinance/")
    raw = raw.replace("{{ '/definitions/' | relative_url }}", SITE_BASE + "/definitions/")
    raw = raw.replace("{{ '/data-center-litigation/' | relative_url }}", SITE_BASE + "/data-center-litigation/")
    html = markdown.markdown(raw, extensions=["tables", "footnotes", "sane_lists", "attr_list"], output_format="html5")
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(["style", "script"]):
        tag.decompose()
    for a in soup.find_all("a", href=True):
        a["href"] = local_link_to_public(a["href"], source_path, root)
    if glossary:
        simplify_reference_tables(soup)
    html_body = str(soup)
    return '<!doctype html><html lang="en"><head><meta charset="utf-8">' + (
        f"<title>{escape(title)}</title><style>{CSS}</style></head><body>"
        + f'<div class="meta">CASCADE, IOWA - November 3, 2026 - Source-linked research edition - Not adopted law</div>'
        + html_body + "</body></html>"
    )


def build(root: Path, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    completed = []
    for title, rel, name, glossary in SOURCES:
        path = root / rel
        if not path.is_file():
            raise FileNotFoundError(str(path))
        dest = output / name
        html = document_html(path, root, title, glossary)
        HTML(string=html, base_url=root.as_uri() + "/").write_pdf(str(dest))
        reader = PdfReader(str(dest))
        if not reader.pages:
            raise RuntimeError(f"Empty PDF: {name}")
        text_sample = "".join((page.extract_text() or "") for page in reader.pages[:2])
        if not text_sample.strip():
            raise RuntimeError(f"No selectable text in PDF: {name}")
        print(f"{name}: {len(reader.pages)} pages; {dest.stat().st_size} bytes", flush=True)
        completed.append((title, dest))
    writer = PdfWriter()
    for title, dest in completed:
        writer.append(str(dest), outline_item=title)
    writer.add_metadata({"/Title": "Cascade Iowa M-2 Zoning, Definitions, and Case Abstracts - November 3, 2026",
                         "/Subject": "Chicago-note cited independent working research - not adopted law",
                         "/Author": "Cascade Data Center Research Project"})
    combined = output / COMBINED_NAME
    with combined.open("wb") as stream:
        writer.write(stream)
    print(f"{COMBINED_NAME}: {len(PdfReader(str(combined)).pages)} pages", flush=True)
    found = sorted(x.name for x in output.glob("*.pdf"))
    expected = sorted([item[2] for item in SOURCES] + [COMBINED_NAME])
    if found != expected:
        raise RuntimeError(f"Unexpected PDF files: {found}; expected {expected}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--out", type=Path, default=Path("docs/downloads"))
    args = parser.parse_args()
    build(args.root.resolve(), args.out.resolve())

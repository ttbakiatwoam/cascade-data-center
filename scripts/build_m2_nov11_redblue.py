#!/usr/bin/env python3
"""Publish the November 11, 2026 Cascade M-2 black/red/blue ordinance draft.

The source is the entire source-grounded November 11 legislative redline,
NOT the historical November 5 PDF.  Only four definitions received reported
committee approval.  Other independent proposals remain clearly identified
as unapproved.  No original zoning scan, 86-term glossary, or annotated
sidebar packet is appended.

Usage: python scripts/build_m2_nov11_redblue.py --root . --out docs/downloads
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import fitz
import markdown
from bs4 import BeautifulSoup
from weasyprint import HTML

SOURCE = "proposals/COMPLETE-M2-COLOR-CODED-REDLINE-2026-11-11.md"
PDF_NAME = "cascade-m2-red-blue-draft-ordinance-2026-11-11.pdf"
APPROVED = (
    "Data Center",
    "Data Center Business",
    "Sustainable Design",
    "Hyperscale Data Center",
)

CSS = r"""
@page {
  size: letter;
  margin: 0.69in 0.71in 0.70in;
  @top-left {
    content: "CASCADE, IOWA | M-2 ORDINANCE REDLINE";
    color: #5d6872;
    font: 7pt "DejaVu Sans", sans-serif;
  }
  @bottom-left {
    content: "Meeting record: 11 Nov 2026 | Working draft - NOT adopted law";
    color: #596674;
    font: 7pt "DejaVu Sans", sans-serif;
  }
  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);
    color: #596674;
    font: 7pt "DejaVu Sans", sans-serif;
  }
}
html, body { color: #171b20; }
body { font: 9.0pt/1.47 "DejaVu Serif", serif; }
h1,h2,h3,h4 { font-family:"DejaVu Sans",sans-serif; line-height:1.28; break-after:avoid; color:#24374a; }
h1 { font-size:17pt; margin:0.12in 0 0.16in; border-bottom:1.5pt solid #36485b; padding-bottom:0.085in; }
h2 { font-size:12pt; margin:0.22in 0 0.11in; border-bottom:0.6pt solid #d2d9e1; padding-bottom:0.04in; }
h3 { font-size:10.4pt; margin:0.19in 0 0.08in; }
h4 { font-size:9.5pt; margin:0.15in 0 0.07in; }
p { margin:0.045in 0 0.105in; }
a { color:#245780; text-decoration:none; overflow-wrap:anywhere; }
em { font-style:italic; }
li { margin:0.025in 0 0.052in; }
ul,ol { padding-left:0.25in; margin:0.05in 0 0.10in; }
hr { border:0; border-top:0.7pt solid #c4ccd4; margin:0.19in 0; }
table { border-collapse:collapse; table-layout:fixed; width:100%; font-size:7.8pt; margin:0.10in 0 0.17in; }
thead { display:table-header-group; }
tr { break-inside:avoid; }
td,th { border-bottom:0.6pt solid #d1d9e1; padding:5.5pt 6pt; vertical-align:top; overflow-wrap:anywhere; }
th { font:bold 7.6pt "DejaVu Sans",sans-serif; text-align:left; background:#edf1f5; }
blockquote { border-left:2pt solid #aeb5bd; padding:0.045in 0 0.048in 0.14in; margin:0.07in 0 0.16in; }
blockquote p:first-child { margin-top:0.0in; }
blockquote p:last-child { margin-bottom:0.0in; }
blockquote.m2-proposed { border-left:3pt solid #a8232c; background:#fff8f8; padding:0.065in 0.08in 0.07in 0.12in; }
blockquote.m2-proposed, blockquote.m2-proposed p,
blockquote.m2-proposed li, blockquote.m2-proposed strong,
blockquote.m2-proposed em, blockquote.m2-proposed span,
blockquote.m2-proposed a { color:#a5232e !important; }
blockquote.m2-proposed p:first-child { font-family:"DejaVu Sans",sans-serif; font-size:7.8pt; }
.m2-add, .m2-add strong, .m2-redline-tag { color:#a5232e !important; }
.m2-edit, .m2-edit strong, .m2-blue-note, .m2-blue-note strong { color:#1c59a3 !important; }
.m2-blue-note { border-left:2pt solid #1c59a3; padding-left:7pt; }
.footnote { font-size:7.6pt; line-height:1.32; }
.footnote ol { padding-left:0.22in; }
.footnote li { margin-bottom:0.07in; overflow-wrap:anywhere; }
.footnote-ref { vertical-align:super; font-size:0.76em; }
code { font-size:7.7pt; }
.cover { break-after:page; }
.cover h1 { font-size:21pt; color:#243447; margin-top:0.23in; }
.cover .date { color:#203d5a; font:bold 11pt "DejaVu Sans", sans-serif; letter-spacing:0.02em; }
.cover .subtitle { color:#4b5b6c; font:10.2pt/1.4 "DejaVu Sans",sans-serif; }
.cover .status { font:bold 8.2pt "DejaVu Sans",sans-serif; background:#f0f3f6; padding:0.14in; margin:0.17in 0; }
.cover h2 { margin-top:0.19in; }
.cover table td:first-child { width:34%; font-weight:bold; }
.cover table td:nth-child(2) { width:66%; }
.cover .note { font-size:8.3pt; line-height:1.43; }
"""

COVER = """
<section class="cover">
  <p class="date">NOVEMBER 11, 2026 | COMMITTEE MEETING UPDATE</p>
  <h1>City of Cascade, Iowa<br>M-2 &amp; Citywide Zoning<br>Draft Ordinance Redline</h1>
  <p class="subtitle">Existing text in black / proposed ordinance text in red /
     transcription and formatting corrections in blue</p>
  <p class="status">INDEPENDENT WORKING DRAFT — NOT CITY-ADOPTED LAW.
     The November 11 advisory-committee vote approved definitions for draft
     consideration only. The City Council has not enacted this document.</p>
  <h2>Four definitions approved for the committee draft</h2>
  <table>
    <thead><tr><th>Definition</th><th>November 11 reported action</th></tr></thead>
    <tbody>
      <tr><td>Data Center</td><td>Approved; exact 5–3 or 6–2 tally not independently confirmed.</td></tr>
      <tr><td>Data Center Business</td><td>Approved; exact 5–3 or 6–2 tally not independently confirmed.</td></tr>
      <tr><td>Sustainable Design</td><td>Approved unanimously; numerical tally not independently confirmed.</td></tr>
      <tr><td>Hyperscale Data Center</td><td>Approved 5–3: 100,000 square feet or larger
          <strong>AND</strong> electrical demand <strong>exceeding 60 megawatts</strong>.
          No calendar-year or “annually” test was approved.</td></tr>
    </tbody>
  </table>
  <p class="note"><strong>Scope:</strong> The full integrated comparison follows.
     The source redline lists 28 independently proposed §165.41 additions, of
     which only the four named above were reported approved at the November 11
     meeting. The remaining definitions and all separate proposed performance
     standards — including a citywide hyperscale prohibition — are
     <strong>not represented as committee-approved</strong>.</p>
  <p class="note"><strong>Authority:</strong> Based on the repository's
     contemporaneous November 11 participant-reported record, not certified City
     minutes. The underlying existing-code baseline remains subject to City
     Clerk/Attorney confirmation of later enactments and numbering.</p>
  <p class="note"><strong>Reading guide:</strong> RED indicates text a future City
     ordinance would need to enact; BLUE indicates only spelling, layout, or
     transcription repair to existing text. Source links and legal notes are
     preserved in the redline. Historical original scans and the 86-term
     research glossary are intentionally excluded from this dated PDF.</p>
</section>
"""


def validate_source(s: str) -> None:
    if "Draft proposals for November 18, 2026" not in s:
        raise RuntimeError("Expected the November 11 source for November 18 review")
    for term in APPROVED:
        if "**" + term + ":**" not in s:
            raise RuntimeError("November 11 approved definition missing: " + term)
    for exact in (
        "100,000 square feet or larger.",
        "Electrical demand exceeding 60 megawatts.",
        "An entity whose business among other businesses, is to operate or lease a data center in the city of cascade.",
        "Construction design that reduces negative environmental effects and improves occupant health and comfort through resource conservation, waste minimization, and healthier environments.",
        "A structure or building rehabilitated or constructed to house a group of networked server computers",
        "The remaining definitions in this redline are additional",
        "## BLUE COPYEDIT REGISTER",
        "## EXISTING §165.12",
        "## EXISTING §165.41",
        "### B. Permitted Principal Uses and Structures",
        "### G(19).",
    ):
        if exact not in s:
            raise RuntimeError("Incomplete or inconsistent November 11 source: " + exact[:95])
    definition_labels = re.findall(r"RED — NEW §165\.41 DEFINITION \((\d+) OF 28\)", s)
    if definition_labels != [str(i) for i in range(1, 29)]:
        raise RuntimeError("Expected 28 ordered independently proposed §165.41 definitions")
    g_sections = [int(n) for n in re.findall(r"^### G\((\d+)\)\.", s, re.M)]
    if g_sections != list(range(2,20)):
        raise RuntimeError("Missing or unordered new §165.11(G) clauses")
    citations = set(re.findall(r"\[\^(\d+)\](?!:)",s))
    notes = set(re.findall(r"^\[\^(\d+)\]:",s,re.M))
    if citations - notes:
        raise RuntimeError("Unresolved source footnotes: " + str(sorted(citations-notes)))


def build_html(raw: str) -> tuple[str,int,int]:
    # Remove decorative emoji only; preserve legislative wording and red/blue labels.
    raw = raw.replace("🟥 ", "").replace("🟦 ", "")
    converted = markdown.markdown(raw, extensions=[
        "tables", "footnotes", "sane_lists", "attr_list", "md_in_html"
    ])
    soup = BeautifulSoup(converted, "html.parser")
    red_count = 0
    for quote in soup.find_all("blockquote"):
        if quote.select_one(".m2-redline-tag"):
            quote["class"] = list(quote.get("class", [])) + ["m2-proposed"]
            red_count += 1
    blue_count = len(soup.select(".m2-edit"))
    for node in soup.find_all(["p","h2","h3","h4"]):
        line = node.get_text(" ",strip=True)
        if line.startswith("BLUE ") or line.startswith("BLUE —"):
            node["class"] = list(node.get("class",[])) + ["m2-blue-note"]
            blue_count += 1
    if red_count < 45 or blue_count < 8:
        raise RuntimeError("Red/blue source markup was lost: red blocks = %s; blue = %s" %
                           (red_count, blue_count))
    if len(soup.select("table")) < 3:
        raise RuntimeError("Ordinance comparison tables were not rendered")
    html = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<title>November 11 Cascade M-2 red and blue ordinance draft</title>'
        '<style>' + CSS + '</style></head><body>'
        + COVER + '<main>' + str(soup) + '</main></body></html>'
    )
    return html, red_count, blue_count


def check_output(dest: Path, red_blocks: int, blue_items: int) -> None:
    with fitz.open(str(dest)) as check:
        if len(check) < 12 or check.page_count > 150:
            raise RuntimeError("PDF page-count sanity failed: %d" % len(check))
        alltext = "\n".join(page.get_text() for page in check)
        for fragment in (
            "NOVEMBER 11, 2026",
            "Data Center Business",
            "Hyperscale Data Center",
            "100,000 square feet or larger",
            "Electrical demand exceeding 60 megawatts",
            "Sustainable Design",
            "BLUE COPYEDIT REGISTER",
            "Decommissioning",
        ):
            if fragment not in alltext:
                raise RuntimeError("Missing PDF text: " + fragment)
        red_chars = blue_chars = 0
        bounds_issues = []
        for i,page in enumerate(check):
            for block in page.get_text("dict")["blocks"]:
                if block.get("type") != 0:
                    continue
                for line in block.get("lines",[]):
                    for span in line.get("spans",[]):
                        c = span.get("color", 0)
                        r,g,b = (c>>16)&255,(c>>8)&255,c&255
                        n = len(span.get("text", ""))
                        if r > 100 and g < 95 and b < 120:
                            red_chars += n
                        if r < 80 and 55 < g < 145 and b > 130:
                            blue_chars += n
                x0,y0,x1,y1 = block["bbox"]
                if x0 < -1 or y0 < -1 or x1 > page.rect.width+1 or y1 > page.rect.height+1:
                    bounds_issues.append((i+1,tuple(round(x,1) for x in block["bbox"])))
        if red_chars < 3500 or blue_chars < 60:
            raise RuntimeError("Text coloring QA failed: red=%d blue=%d" % (red_chars,blue_chars))
        if bounds_issues:
            raise RuntimeError("Detected page-edge text clipping: %s" % bounds_issues[:5])
        print("%s: %s pages, %s bytes; red blocks=%s, blue items=%s; red text=%s chars, blue text=%s chars" %
              (dest, len(check), dest.stat().st_size, red_blocks,blue_items,red_chars,blue_chars))
        print("Verified voted-definition wording, legal notes, source citations, and pagination")


def save_pdf(root: Path, outdir: Path) -> Path:
    src = root / SOURCE
    if not src.is_file():
        raise FileNotFoundError(src)
    raw = src.read_text(encoding="utf-8")
    validate_source(raw)
    html, red_blocks, blue_items = build_html(raw)
    data = HTML(string=html, base_url=root.as_uri()+"/").write_pdf()
    with fitz.open(stream=data, filetype="pdf") as pdf:
        pdf.set_metadata({
            "title": "Cascade M-2 Red/Blue Draft Ordinance - November 11, 2026",
            "subject": "Nov 11 reported definition votes; black existing, red proposals, blue copyedits",
            "author": "Cascade Data Center Research (independent)",
            "keywords": "Cascade Iowa, zoning, M-2, ordinance, redline, November 11 2026"
        })
        pdf.set_toc([
            [1, "November 11 committee definition record and draft status",1],
            [1, "Integrated M-2 and citywide zoning red/blue text",2],
        ])
        outdir.mkdir(parents=True, exist_ok=True)
        dest = outdir / PDF_NAME
        pdf.save(str(dest), garbage=3, deflate=True)
    check_output(dest,red_blocks,blue_items)
    return dest


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--out", type=Path, default=Path("docs/downloads"))
    args = parser.parse_args()
    save_pdf(args.root.resolve(), args.out.resolve())

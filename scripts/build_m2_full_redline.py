#!/usr/bin/env python3
"""Render the complete section 165.11 redline with explicit red/blue legend.

The source is proposals/COMPLETE-M2-COLOR-CODED-REDLINE-2026-11-05.md.
It contains every original M-2 A-G(1) provision, existing 2022 B(18),
and new red B(19), D(8), G(2)-G(19), and local definitions.
Five unmodified original scanned source pages are appended to the PDF.

Usage: python scripts/build_m2_full_redline.py --root . --out docs/downloads
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import fitz
import markdown
from bs4 import BeautifulSoup
from weasyprint import HTML

SOURCE = "proposals/COMPLETE-M2-COLOR-CODED-REDLINE-2026-11-05.md"
SCAN = "sources/cascade-zoning/Entire zoning code-1.pdf"
PDF_NAME = "cascade-m2-full-color-redline-2026-11-05.pdf"

STYLE = r"""
@page {
 size: letter;
 margin: 0.72in 0.70in 0.73in 0.70in;
 @top-left {
  content:"CASCADE, IOWA  |  M-2 SECTION 165.11";
  color:#556272; font: 7.1pt "DejaVu Sans";
 }
 @bottom-left {
  content:"Independent discussion draft | 05 Nov 2026 | Not adopted law";
  color:#647386; font: 7pt "DejaVu Sans";
 }
 @bottom-right {
  content:"Page " counter(page);
  color:#647386; font: 7pt "DejaVu Sans";
 }
}
html,body { color:#172536; }
body { font: 9pt/1.43 "DejaVu Serif",serif; }
h1,h2,h3,h4 { font-family:"DejaVu Sans",sans-serif; color:#1b344b; break-after:avoid; line-height:1.26; }
h1 { font-size:16pt; border-bottom:2pt solid #244463; padding-bottom:0.10in; margin:0 0 0.16in; }
h2 { font-size:12pt; border-bottom:0.6pt solid #cad4df; margin:0.25in 0 0.12in; padding-bottom:0.06in; }
h3 { font-size:10.5pt; margin:0.22in 0 0.09in; }
h4 { font-size:10pt; margin:0.17in 0 0.08in; }
p { margin: 0.04in 0 0.105in; }
a { color:#215687; text-decoration:none; overflow-wrap:anywhere; }
strong { font-weight:bold; }
ul,ol { padding-left:0.27in; }
li { margin-bottom:0.035in; }
hr { border:0; border-top:0.7pt solid #bcc8d6; margin:0.24in 0; }
table { border-collapse:collapse; width:100%; table-layout:fixed; font-size:8.0pt; margin:0.08in 0 0.18in; }
thead { display:table-header-group; }
tr { break-inside:avoid; }
td,th { border-bottom:0.5pt solid #ccd5df; padding:5pt 7pt; vertical-align:top; overflow-wrap:anywhere; }
td:first-child,th:first-child { width:13%; }
td:nth-child(2),th:nth-child(2) { width:48%; }
td:nth-child(3),th:nth-child(3) { width:39%; }
th { color:#1b344b; background:#edf2f7; font: bold 7.9pt "DejaVu Sans",sans-serif; }
.m2-edit { color:#225ca3; font-weight:650; }
.m2-add { color:#a31b25; font-weight:bold; }
.m2-addblock { color:#9e1f28; border-left:2.8pt solid #b72e38; padding:0.02in 0 0.02in 0.14in; margin:0.15in 0 0.20in; break-inside:auto; }
.m2-addblock h2, .m2-addblock h3, .m2-addblock strong { color:#951d26; }
.m2-addblock a { color:#941c26; text-decoration:underline; }
.footnote { font-size:7.6pt; line-height:1.32; }
.footnote ol { padding-left:0.25in; }
.footnote li { margin-bottom:0.085in; overflow-wrap:anywhere; }
.footnote-ref { vertical-align:super; font-size:0.72em; }
code { font-size:8pt; }
"""


def assert_complete(s: str) -> None:
    if not s.count('<div class="m2-addblock" markdown="1">') == 4:
        raise RuntimeError("Expected exactly four red proposed-addition blocks")
    for marker in [
        "### A. Statement of Intent",
        "### B. Permitted Principal Uses and Structures",
        "### C. Permitted Accessory Uses and Structures",
        "### D. Special Exception Uses and Structures",
        "### E. Minimum Lot Area",
        "### F. Permitted Signs",
        "### G. Special Requirements",
        "**18. Fitness Center",
        "**19. Data Center or High-Density Computing Facility.",
        "**8. Major Industrial Facility.",
        "## BLUE COPYEDIT REGISTER",
        "§165.11(G)(17)",
    ]:
        if marker not in s:
            raise RuntimeError("Missing source section: " + marker)
    g = [int(x) for x in re.findall(r"^### G\((\d+)\)\.", s, re.M)]
    if g != list(range(2, 20)):
        raise RuntimeError(f"Expected G(2)-G(19) in source, found {g}")
    definitions = re.findall(r"^\*\*[^*\n]+:\*\*", s, re.M)
    if len(definitions) != 26:
        raise RuntimeError(f"Expected 26 proposed new definitions, got {len(definitions)}")
    table = s.split("### B. Permitted Principal Uses and Structures",1)[1].split("### C. Permitted Accessory Uses and Structures",1)[0]
    old_rows = re.findall(r"^\| \*\*(\d+)\.\*\* \|", table, re.M)
    if old_rows != [str(i) for i in range(1,18)]:
        raise RuntimeError("Original B(1)-B(17) source rows missing or reordered")
    d = s.split("### D. Special Exception Uses and Structures",1)[1].split("### E. Minimum Lot Area",1)[0]
    for i in range(1,8):
        if f"**{i}.**" not in d:
            raise RuntimeError("Original D("+str(i)+") missing")
    if "handwritten" not in d.lower():
        raise RuntimeError("Required source-scan handwritten-marks caveat missing")
    refs = set(re.findall(r"\[\^(\d+)\](?!:)", s))
    notes = set(re.findall(r"^\[\^(\d+)\]:", s, flags=re.M))
    if refs - notes:
        raise RuntimeError("Unresolved source references: "+str(sorted(refs-notes)))


def document_html(text: str) -> str:
    converted = markdown.markdown(text, extensions=[
        "tables","footnotes","sane_lists","attr_list","md_in_html"
    ])
    soup = BeautifulSoup(converted,"html.parser")
    add_blocks = soup.select("div.m2-addblock")
    if len(add_blocks) != 4:
        raise RuntimeError("Markdown red-block rendering failed; got "+str(len(add_blocks)))
    # Readable, real HTML paragraphs/headings must exist inside the red blocks.
    if len(add_blocks[2].select("h3")) != 18:
        raise RuntimeError("G performance requirements were not parsed inside red block")
    if len(add_blocks[3].select("p")) < 26:
        raise RuntimeError("Proposed definitions were not parsed inside red block")
    if len(soup.select("table")) < 3:
        raise RuntimeError("Original use table, legend, and copyedit register missing")
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Cascade M-2 complete color redline</title><style>'+STYLE+'</style></head><body>'+str(soup)+'</body></html>'


def save_pdf(root: Path, outdir: Path) -> Path:
    source = root / SOURCE
    original = root / SCAN
    if not source.exists() or not original.exists():
        raise FileNotFoundError(f"Missing original source or redline source: {source}; {original}")
    s = source.read_text("utf-8")
    assert_complete(s)
    html = document_html(s)
    # Render in-memory first to inspect before appending the original scanned pages.
    rendered = fitz.open(stream=HTML(string=html,base_url=root.as_uri()+"/").write_pdf(),filetype="pdf")
    original_scan = fitz.open(str(original))
    if len(original_scan)<49:
        raise RuntimeError("Original scan has fewer than 49 pages")
    output = fitz.open()
    output.insert_pdf(rendered)
    start_scan = len(output) + 1
    cover = output.new_page(width=612,height=792)
    cover.draw_rect(cover.rect,color=None,fill=(0.975,0.98,0.99))
    cover.insert_textbox(fitz.Rect(58,185,548,285),"UNALTERED ORIGINAL M-2 SCAN",fontname="hebo",fontsize=21,color=(0.12,0.26,0.40))
    cover.insert_textbox(fitz.Rect(58,305,546,500),
         "The following five pages are exact images of the archived municipal M-2 text (original PDF pages 45-49, printed code pages 34-38). This reproduction is supplied to verify the black, blue and red integrated reprint. Handwritten marks visible in source page 47 are preserved, not interpreted as adopted legislation.",
         fontname="helv",fontsize=11.6,lineheight=1.55,color=(0.18,0.26,0.34))
    cover.insert_text((58,730),"SOURCE REPRODUCTION - NEVER AN ADOPTED COLOR REDLINE",fontname="hebo",fontsize=8,color=(0.35,0.42,0.50))
    output.insert_pdf(original_scan,from_page=44,to_page=48)
    output.set_toc([
      [1,"Full reprint - color legend, original M-2 and red additions",1],
      [1,"Unmodified original M-2 facsimile (five pages)",start_scan],
    ])
    output.set_metadata({
      "title":"Cascade M-2 Full Original Text and Color-Coded November 5, 2026 Redline",
      "subject":"Black existing / Red substantive additions / Blue formatting and grammar only",
      "author":"Cascade Data Center independent research",
    })
    outdir.mkdir(parents=True,exist_ok=True)
    dest = outdir / PDF_NAME
    output.save(str(dest),garbage=3,deflate=True)
    total_pages = len(output)
    source_pages = len(rendered)
    output.close()
    rendered.close()
    original_scan.close()
    # Confirm color, text, source appendices and completeness.
    check = fitz.open(str(dest))
    if len(check)!=total_pages or len(check.get_toc())!=2 or total_pages < 15:
        raise RuntimeError("PDF length, bookmarks or integrity failed")
    alltext = "".join(p.get_text() for p in check[:source_pages])
    if "BLUE COPYEDIT REGISTER" not in alltext or "RED - PROPOSED NEW" not in alltext:
        raise RuntimeError("Legend or editing register not found in PDF text")
    colors = {}
    for page in check[:source_pages]:
        for block in page.get_text("dict")["blocks"]:
            if block.get("type")!=0:
                continue
            for line in block.get("lines",[]):
                for span in line.get("spans",[]):
                    colors[span.get("color",0)]=colors.get(span.get("color",0),0)+len(span.get("text",""))
    redish = sum(n for c,n in colors.items() if ((c>>16)&255)>95 and ((c>>8)&255)<95 and (c&255)<105)
    blueish = sum(n for c,n in colors.items() if ((c>>16)&255)<90 and ((c>>8)&255)>45 and (c&255)>105)
    if redish < 4000 or blueish < 70:
        raise RuntimeError(f"Missing red/blue vector text colors: red={redish} blue={blueish}")
    print(f"{dest}: {total_pages} pages (reprint {source_pages}; untouched scan 5), {dest.stat().st_size} bytes")
    print(f"Text colors: RED {redish} chars / BLUE {blueish} chars; source terms and sections validated")
    check.close()
    return dest


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--root",type=Path,default=Path("."))
    parser.add_argument("--out",type=Path,default=Path("docs/downloads"))
    args=parser.parse_args()
    save_pdf(args.root.resolve(),args.out.resolve())

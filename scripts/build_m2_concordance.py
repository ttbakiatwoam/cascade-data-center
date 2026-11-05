#!/usr/bin/env python3
"""Create a source-faithful, annotated Cascade M-2 zoning comparison PDF.

Canonical sources:
  sources/cascade-zoning/Entire zoning code-1.pdf  (original as preserved)
  dataset/policy/41_M2_ORIGINAL_SCAN_CONCORDANCE_2026-11-03.md
  proposals/DRAFT-ORDINANCE-M2-DATA-CENTER-PERFORMANCE-STANDARDS-2026-11-03.md

No source pages are overwritten. The five original M-2 pages appear unaltered
after a separate annotated facsimile. The 2009 draft remains clearly labeled.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import fitz
from weasyprint import HTML

from export_research_pdfs import document_html
from build_m2_full_redline import document_html as colored_redline_html, assert_complete as check_colored_redline_source, SOURCE as COLOR_REDLINE_SOURCE


OUTPUT_FILE = "cascade-m2-original-scan-highlighted-comparison-2026-11-03.pdf"
SOURCE_SCAN = "sources/cascade-zoning/Entire zoning code-1.pdf"
COMPARISON = "dataset/policy/41_M2_ORIGINAL_SCAN_CONCORDANCE_2026-11-03.md"
DRAFT = "proposals/DRAFT-ORDINANCE-M2-DATA-CENTER-PERFORMANCE-STANDARDS-2026-11-03.md"


COMMENTS = [
    (
        "SCAN PAGE 45 | Code p. 34",
        "A - INTENT / B - PERMITTED USES",
        [
            ("RETAIN", "A. The existing M-2 purpose and heavy industrial use language remains."),
            ("RETAIN", "B(1) through the uses visible on this page continue to apply."),
            ("ADDITION LATER", "The 2022 fitness amendment and new data-center use are addressed after B(17) on page 46."),
        ],
    ),
    (
        "SCAN PAGE 46 | Code p. 35",
        "B - END OF LIST / C - ACCESSORY",
        [
            ("RETAIN", "Existing B(10)-B(17), ending with mini-warehouses, remain unchanged."),
            ("ENACTED 2022", "Ordinance 05-22 added permitted B(18): fitness centers, with parking at 1 space/200 sq ft."),
            ("ADD B(19)", "Our new draft adds data centers and high-density computing as a principal use, after the existing B(18)."),
            ("RETAIN", "C(1)-C(4) existing accessory provisions remain."),
        ],
    ),
    (
        "SCAN PAGE 47 | Code p. 36",
        "D - SPECIAL EXCEPTIONS",
        [
            ("RETAIN", "Existing D(1)-D(3) include livestock, bulk storage, and certain higher-impact industry."),
            ("RETAIN", "Existing special-exception procedure under Section 165.34(2) remains."),
            ("ADD AFTER D(7)", "The new Major Industrial Facility item D(8) follows the seven existing exceptions; see next scan page."),
        ],
    ),
    (
        "SCAN PAGE 48 | Code p. 37",
        "D - END OF SPECIAL EXCEPTIONS",
        [
            ("RETAIN", "Existing D(4)-D(7), including wrecking yards, towers, signs, and adult-oriented uses, remain."),
            ("ADD D(8)", "Major Industrial Facility threshold: 5 MW power, 25,000 gallons/day water, 2 MW generation, or 5 MWh storage."),
            ("CAUTION", "No new permitted use is granted merely because an application qualifies for special-exception review."),
        ],
    ),
    (
        "SCAN PAGE 49 | Code p. 38",
        "E / F / G - KEY CORRECTION",
        [
            ("RETAIN", "E general yards: front 25 ft, rear 25 ft, side 20 ft, corner street-side 20 ft; 60 ft height."),
            ("RETAIN", "F sign rules remain. G(1) already refers to supplementary Section 165.12."),
            ("ADD G(2)-G(19)", "Eighteen new M-2 performance standards now begin AFTER G(1), not at G(1)."),
            ("ENACTED 2024", "Section 165.12(12) separately governs M-2 fence heights and maintenance."),
            ("VERIFY 2009", "The zero-lot-line source page is stamped DRAFT; adoption cannot be inferred from the scan."),
        ],
    ),
]


def separator(document: fitz.Document, title: str, text: str, subtext: str = "") -> None:
    p = document.new_page(width=612, height=792)
    p.draw_rect(fitz.Rect(0, 0, 612, 792), fill=(0.97, 0.98, 0.99), color=None)
    p.draw_line((62, 228), (550, 228), color=(0.22, 0.36, 0.51), width=2)
    p.insert_textbox(fitz.Rect(62, 254, 550, 364), title, fontsize=22,
                     lineheight=1.25, fontname="hebo", color=(0.10, 0.22, 0.37))
    p.insert_textbox(fitz.Rect(64, 390, 544, 540), text, fontsize=11.3,
                     lineheight=1.48, fontname="helv", color=(0.24, 0.31, 0.40))
    p.insert_textbox(fitz.Rect(64, 632, 545, 727), subtext, fontsize=9.1,
                     lineheight=1.32, fontname="helv", color=(0.34, 0.40, 0.48))
    p.insert_text((64, 754), "NOVEMBER 3, 2026  |  INDEPENDENT DISCUSSION DRAFT",
                  fontname="hebo", fontsize=7.5, color=(0.37, 0.43, 0.50))


def annotated_scan(document: fitz.Document, source: fitz.Document) -> None:
    for j, comments in enumerate(COMMENTS):
        pidx = j + 44
        src = source.load_page(pidx)
        p = document.new_page(width=940, height=792)
        p.draw_rect(p.rect, color=None, fill=(1, 1, 1))
        # Preserve the source's physical layout and aspect ratio on the left.
        scan_dest = fitz.Rect(14, 12, 615, 779)
        p.show_pdf_page(scan_dest, source, pidx, keep_proportion=True)
        # A vertical divider leaves the full scan visible without marks.
        p.draw_line((624, 20), (624, 771), color=(0.75, 0.81, 0.86), width=1.1)
        side = fitz.Rect(638, 18, 924, 772)
        p.draw_rect(side, fill=(0.96, 0.975, 0.988), color=(0.84, 0.88, 0.92), width=0.8)
        label, title, entries = comments
        p.insert_textbox(fitz.Rect(651, 34, 909, 67), label, fontsize=10.2,
                         fontname="hebo", color=(0.21, 0.35, 0.49))
        p.insert_textbox(fitz.Rect(651, 74, 910, 129), title, fontsize=14,
                         lineheight=1.25, fontname="hebo", color=(0.10, 0.22, 0.37))
        y = 145
        for badge, detail in entries:
            typ = badge.split(" ")[0]
            if typ == "ADD":
                border, bg = (0.59, 0.31, 0.06), (1.0, 0.95, 0.84)
            elif typ == "ENACTED":
                border, bg = (0.08, 0.37, 0.24), (0.90, 0.97, 0.93)
            elif typ == "VERIFY" or typ == "CAUTION":
                border, bg = (0.48, 0.26, 0.37), (0.98, 0.94, 0.96)
            else:
                border, bg = (0.24, 0.39, 0.52), (0.92, 0.96, 0.99)
            # Rule blocks are self-contained: original scan is never overwritten.
            estimated = min(120, 57 + max(0, len(detail)-70)*0.38)
            rect = fitz.Rect(649, y, 913, y+estimated)
            p.draw_rect(rect, color=border, fill=bg, width=0.65)
            p.insert_textbox(fitz.Rect(660, y+7, 905, y+25), badge,
                             fontname="hebo", fontsize=9.6, color=border)
            remain = p.insert_textbox(fitz.Rect(659, y+27, 904, y+estimated-5),
                                      detail, fontname="helv", fontsize=9.05,
                                      lineheight=1.18, color=(0.12, 0.22, 0.33))
            if remain < 0:
                raise RuntimeError(f"Annotation overflow on page {pidx+1}: {badge}")
            y += estimated+11
        if y > 740:
            raise RuntimeError(f"Annotation blocks exceed page on {pidx+1}")
        p.insert_text((651, 754), "Source scan shown at left; annotations at right",
                      fontsize=8, fontname="heit", color=(0.37, 0.45, 0.52))


def source_pdf_to_document(path: Path, root: Path, title: str) -> fitz.Document:
    html = document_html(path, root, title, False)
    pdf = HTML(string=html, base_url=root.as_uri()+"/").write_pdf()
    return fitz.open(stream=pdf, filetype="pdf")


def build(root: Path, destination: Path) -> Path:
    original = root / SOURCE_SCAN
    if not original.is_file():
        raise FileNotFoundError(f"Original Cascade scan not available: {original}")
    source = fitz.open(str(original))
    if source.page_count < 49:
        raise RuntimeError(f"Zoning scan should contain at least 49 pages, found {source.page_count}")
    # Assert the source PDF page metadata is plausible. This does not OCR the image.
    for num in range(44, 49):
        if source.load_page(num).rect.width < 350:
            raise RuntimeError(f"Source page {num+1} unexpectedly narrow")
    report = source_pdf_to_document(root / COMPARISON, root, "Original Cascade M-2 scan and amendment concordance")
    draft = source_pdf_to_document(root / DRAFT, root, "November 3 proposed M-2 zoning ordinance")
    colored_source = (root / COLOR_REDLINE_SOURCE).read_text("utf-8")
    check_colored_redline_source(colored_source)
    colored = fitz.open(stream=HTML(string=colored_redline_html(colored_source), base_url=root.as_uri()+"/").write_pdf(),filetype="pdf")

    doc = fitz.open()
    report_first = 1
    doc.insert_pdf(report)
    anno_first = doc.page_count + 2
    separator(doc, "ANNOTATED ORIGINAL M-2", "Original City scan, PDF pp. 45-49, reproduced with a separate right-side commentary panel. The scan itself is never modified. ADD marks identify insertion points, not text already adopted by the City.")
    annotated_scan(doc, source)
    original_first = doc.page_count + 2
    separator(doc, "UNALTERED SOURCE M-2", "The next five pages are direct copies of the actual City zoning scan's pages 45-49, exactly as preserved in the original file. They show M-2 Section 165.11, printed pages 34-38.")
    doc.insert_pdf(source, from_page=44, to_page=48)
    colored_first = doc.page_count + 2
    separator(doc, "COMPLETE COLOR-CODED M-2 REDLINE", "BLACK: existing language. RED: substantive proposed additions. BLUE: grammar, spelling and formatting only. Every original M-2 A through G(1) provision is reprinted with B(18) and proposed insertions at B(19), D(8), and G(2)-G(19). Refer to the original unchanged scans immediately before this section.")
    doc.insert_pdf(colored)
    draft_first = doc.page_count + 2
    separator(doc, "FULL REVISED DRAFT ORDINANCE", "The following document contains all of the proposed new text and its source notes. Section G(1) remains unchanged; new M-2 G requirements are G(2) through G(19). This proposal is NOT enacted law.")
    doc.insert_pdf(draft)
    draft2009_first = doc.page_count + 2
    separator(doc, "HISTORICAL 2009 DRAFT", "The scan's PDF page 6 is explicitly titled DRAFT ORDINANCE 117-09. Its interior zero-lot-line proposal is not established as adopted by the available copy. Obtain the enacted ordinance, if any, before asserting a zero-lot-line exception.")
    doc.insert_pdf(source, from_page=5, to_page=5)

    # Produce a navigable PDF with section bookmarks.
    doc.set_toc([
        [1, "Section 1 - M-2 historical and proposal comparison", report_first],
        [1, "Section 2 - Annotated original M-2 scan", anno_first],
        [1, "Section 3 - Original M-2 scan, unaltered pages 45-49", original_first],
        [1, "Section 4 - Integrated full M-2 reprint, red additions and blue copyedits", colored_first],
        [1, "Section 5 - Full November 3 proposed amended ordinance", draft_first],
        [1, "Section 6 - 2009 zero-lot-line draft (not enacted proof)", draft2009_first],
    ])
    doc.set_metadata({
        "title": "Cascade M-2: Original Scan, Fully Integrated Red/Blue Redline, and Working Amendment",
        "author": "Cascade Data Center independent research",
        "subject": "Chicago-noted comparison; original scan pp. 45-49; 2022/2024 amendments; not adopted law",
    })
    destination.mkdir(parents=True, exist_ok=True)
    out = destination / OUTPUT_FILE
    doc.save(str(out), garbage=3, deflate=True)
    page_count = doc.page_count
    doc.close()
    report.close()
    draft.close()
    colored.close()
    source.close()
    test = fitz.open(str(out))
    if test.page_count != page_count or len(test.get_toc()) != 6:
        raise RuntimeError("PDF integrity/bookmark verification failed")
    fulltext = "".join(p.get_text() for p in test)
    for required in ("G(2)", "G(19)", "B(19)", "Ordinance 05-22", "2009", "BLUE COPYEDIT REGISTER", "RED - PROPOSED"):
        if required not in fulltext:
            raise RuntimeError(f"Missing expected comparison content: {required}")
    print(f"CREATED {out} ({test.page_count} pages; {out.stat().st_size} bytes)")
    print(f"TOC: {test.get_toc()}")
    test.close()
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--out", default="m2-build")
    args = ap.parse_args()
    build(Path(args.root).resolve(), Path(args.out).resolve())

#!/usr/bin/env python3
"""Build the dated Cascade M-2 November 9, 2026 committee submission.

Runs AFTER the source PDFs are built by the GitHub Pages workflow. It preserves
source PDF pages verbatim and places two transmittal/verification pages before
the compiled sources, plus one distinct November 4 legal-research source note.
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path
import fitz

SOURCES = (
    ("A. Original M-2, annotated comparison and full proposed ordinance",
     "cascade-m2-original-scan-highlighted-comparison-2026-11-03.pdf", 63),
    ("B. Updated 86-term Iowa statutory and legal-dictionary reference",
     "cascade-definitions-reference-2026-11-03.pdf", 36),
    ("C. National data-center litigation: 27 case abstracts",
     "cascade-case-abstracts-2026-11-03.pdf", 11),
    ("D. Optional Chapter 165.41 definitions ordinance",
     "cascade-definitions-ordinance-2026-11-03.pdf", 5),
)
OUTPUT = "Cascade_M2_Complete_Committee_Submission_2026-11-09.pdf"
REPO = "https://github.com/ttbakiatwoam/cascade-data-center"
INK = (0.11, 0.19, 0.29)
MUTED = (0.36, 0.43, 0.50)
ACCENT = (0.17, 0.32, 0.48)
BG = (0.97, 0.98, 0.99)

def txt(p, text, x, y, w, h, size=10, bold=False, color=INK, lineheight=1.28):
    room = p.insert_textbox(
        fitz.Rect(x, y, x+w, y+h), text,
        fontsize=size, fontname="hebo" if bold else "helv",
        color=color, lineheight=lineheight,
    )
    if room < -1:
        raise RuntimeError(f"Text does not fit on {p.number+1}: {text[:80]!r}")

def begin(doc, number, tag):
    p = doc.new_page(width=612, height=792)
    p.draw_rect(fitz.Rect(0, 0, 9, 792), color=None, fill=ACCENT)
    p.draw_rect(fitz.Rect(9, 0, 612, 92), color=None, fill=BG)
    txt(p, "INDEPENDENT RESEARCH   |   CASCADE M-2   |   09 NOV 2026",
        42, 41, 500, 22, size=9.0, bold=True, color=ACCENT)
    p.draw_line((42, 744), (564, 744), color=(0.82, 0.86, 0.89), width=0.7)
    txt(p, tag, 44, 758, 465, 16, size=8.2, color=MUTED)
    txt(p, str(number), 531, 758, 32, 16, size=8.2, color=MUTED)
    return p

def first_page(doc, page_ranges):
    p = begin(doc, 1, "Independent discussion draft - not adopted City law")
    txt(p, "CASCADE, IOWA", 48, 113, 500, 30, size=16, bold=True, color=ACCENT)
    txt(p, "M-2 ordinance comparison and\nsupporting research",
        48, 153, 520, 92, size=23, bold=True)
    txt(p, "Data Center Advisory Committee review packet | 9 November 2026",
        48, 268, 520, 28, size=10.3, color=MUTED)
    txt(p, "INDEPENDENT RESEARCH ONLY. Not adopted law, a certified codification, a legal opinion, or a project approval.",
        48, 309, 508, 47, size=10)
    p.draw_line((48, 380), (560, 380), color=(0.72, 0.78, 0.83), width=1.1)
    txt(p, "CONTENTS", 48, 393, 480, 21, size=11, bold=True, color=ACCENT)
    ys = (430, 481, 532, 583)
    names = (
        "Original City M-2 scan, annotated revisions, redline and full draft",
        "86-term Iowa-law / Oxford / Merriam-Webster / Wex / FindLaw glossary",
        "27 litigation case abstracts and numbered source notes",
        "Optional standalone Chapter 165.41 definitions ordinance",
    )
    for i, (start, end) in enumerate(page_ranges):
        y = ys[i]
        p.draw_rect(fitz.Rect(48, y, 88, y+30), fill=BG, color=None)
        txt(p, chr(65+i), 60, y+5, 24, 22, size=13, bold=True, color=ACCENT)
        txt(p, names[i], 101, y+1, 397, 40, size=9.45, bold=True)
        txt(p, f"{start}-{end}", 511, y+6, 45, 18, size=8.6, color=MUTED)
    txt(p, "E. November 4 LexisNexis Assist Iowa-law source-check note (final page)",
        48, 650, 506, 40, size=9.6, bold=True)
    txt(p, "Proposed ordinance language remains subject to committee review, City Attorney review, and lawful enactment.",
        48, 697, 502, 38, size=8.6, color=MUTED)

def second_page(doc):
    p = begin(doc, 2, "Source version and evidence boundaries")
    txt(p, "CONTENT AND VERSION VERIFICATION", 48, 122, 510, 38,
        size=17, bold=True, color=ACCENT)
    items = (
        ("Original M-2 source", "The five source scan pages 45-49 and separately annotated facsimiles appear in Part A. Existing subsection G(1) is retained."),
        ("Color-coded proposal", "Black is historical existing language, red denotes new substantive language, and blue denotes editorial or formatting adjustments."),
        ("Noise protocol", "Includes 65 dBA / 75 dBC M-2 property-line standards; sensitive-receptor provisions; owner-consented indoor baselines; closed windows and doors; and HVAC fan ON at 65-75 F where practicable."),
        ("Generators, emissions and aesthetics", "Includes generator schedules, applicable emissions permits or exemption determinations, screening, exterior lighting, and related performance provisions."),
        ("Latest full definitions appendix", "Part B uses the November 4 Cornell Wex and FindLaw legal-dictionary update in addition to Iowa statutory, Oxford and Merriam-Webster comparison material."),
        ("Litigation evidence cutoff", "Part C reports 27 selected cases with status research through October 28, 2026. Subsequent dispositions require fresh docket verification."),
    )
    y=178
    for title, body in items:
        txt(p, title.upper(), 48, y, 512, 21, size=9.45, bold=True, color=ACCENT)
        txt(p, body, 48, y+23, 510, 50, size=9.25)
        y += 85
    txt(p, "Not included: unreleased CMU/MVEC utility records, new construction evidence, or case updates after the research cutoff.",
        48, 697, 514, 41, size=8.6, color=MUTED)

def add_note(doc):
    p = begin(doc, len(doc)+1, "Supplemental legal research - 4 November 2026")
    txt(p, "LEXISNEXIS ASSIST: IOWA-LAW SOURCE CHECK", 48, 120, 510, 59,
        size=17, bold=True, color=ACCENT)
    txt(p, "Research annotation only; not controlling law and not a revision to the November 3 proposed ordinance.",
        48, 185, 507, 42, size=9.9)
    checks = (
        ("State data-center definition", "Iowa Code section 423.3(95)(f), rather than section 423.4, supplies the quoted data-center definition for the sales-tax program. Investment/refund criteria are not zoning definitions."),
        ("Zoning uniformity", "Section 414.2 requires district-wise uniformity for classes or kinds of buildings. The draft uses objectively measurable impacts across M-2 users, subject to legal review."),
        ("Municipal franchise fees", "Section 364.2(4)(f) is a specific source to analyze separately from the general limits on new municipal taxes. This packet does not establish a fee."),
        ("Air permits and other oversight", "The draft seeks information about applicable emissions permits or exemption determinations; it does not replace state or federal environmental authorization."),
        ("Unverified AI case summaries", "Some case descriptions in the Assist output require direct opinion and docket review before being cited as judicial holdings."),
        ("Drafting effect", "The November 4 memo explicitly made no change to the November 3 proposed ordinance. Existing highlighted changes are not silently revised."),
    )
    y = 247
    for title, body in checks:
        txt(p, title.upper(), 48, y, 514, 19, size=9.1, bold=True, color=ACCENT)
        txt(p, body, 48, y+21, 510, 47, size=8.8)
        y += 72
    p.draw_line((48, 681), (559, 681), color=(0.72,0.78,0.83), width=0.7)
    txt(p, "Complete source review and verbatim prompt/output transcript are retained in the GitHub repository under dataset/policy and sources/legal-research.",
        48, 691, 510, 46, size=8.5, color=MUTED)
    p.insert_link({"kind":fitz.LINK_URI, "from":fitz.Rect(48, 689, 559, 737),
                   "uri":REPO+"/blob/master/dataset/policy/46_LEXISNEXIS_ASSIST_DEFINITION_AND_IOWA_AUTHORITY_REVIEW_2026-11-04.md"})

def build(outdir):
    source_docs=[]
    ranges=[]
    current=3
    for title, fname, minimum in SOURCES:
        path=outdir/fname
        if not path.is_file():
            raise FileNotFoundError(f"Missing source PDF: {path}")
        src=fitz.open(path)
        if len(src)<minimum:
            raise RuntimeError(f"Unexpectedly short {fname}: {len(src)} pages")
        source_docs.append((title, src))
        ranges.append((current,current+len(src)-1))
        current += len(src)
    output=fitz.open()
    first_page(output,ranges)
    second_page(output)
    toc=[[1,"Transmittal, contents and verification",1]]
    for (title, src), (start,end) in zip(source_docs,ranges):
        output.insert_pdf(src,links=True,annots=True)
        toc.append([1,title,start])
    add_note(output)
    toc.append([1,"E. November 4 LexisNexis Assist research note",len(output)])
    output.set_toc(toc)
    output.set_metadata({
        "title":"Cascade M-2: 9 November 2026 complete advisory committee submission",
        "subject":"Original zoning, annotated comparison, full proposed ordinance, updated glossary, case abstracts and source cross-check",
        "author":"Independent Cascade data center ordinance research",
        "keywords":"Cascade, Iowa, zoning, M-2, redline, definitions, legal research, 2026-11-09",
    })
    target=outdir/OUTPUT
    output.save(target,garbage=4,deflate=True)
    output.close()
    for title, src in source_docs:
        src.close()
    shutil.copyfile(outdir/SOURCES[0][1],outdir/"Cascade_M2_Original_Proposed_Annotated_Corrected_2026-11-05.pdf")
    shutil.copyfile(outdir/SOURCES[1][1],outdir/"Cascade_M2_Updated_86_Term_Definitions_2026-11-05.pdf")
    check=fitz.open(target)
    expected=3+sum(end-start+1 for start,end in ranges)
    assert len(check)==expected, (len(check),expected)
    assert len(check.get_toc())==6
    assert "proposed" in check[2].get_text().lower()
    assert "dictionary" in check[ranges[1][0]-1].get_text().lower()
    assert "LEXISNEXIS" in check[-1].get_text().upper()
    print(f"Verified {target}: {len(check)} pages, {len(check.get_toc())} bookmarks, {target.stat().st_size} bytes")
    print("Part ranges:",ranges)
    check.close()

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",type=Path,default=Path("docs/downloads"))
    args=ap.parse_args()
    args.out.mkdir(parents=True,exist_ok=True)
    build(args.out)

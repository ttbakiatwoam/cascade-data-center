#!/usr/bin/env python3
"""Generate a source-controlled, printable November 18 Cascade committee packet.

A source-grounded compilation, not official adopted zoning or certified minutes.
The original City red/blue PDF is embedded unchanged. Government legal facsimiles
are inserted with editorial search highlights; their underlying text is unedited.
"""
import argparse
import html
import re
from pathlib import Path
from datetime import date
from urllib.parse import quote

import fitz
import markdown
import requests
from bs4 import BeautifulSoup
from weasyprint import HTML

BASE = "https://github.com/ttbakiatwoam/cascade-data-center/blob/master/"
OUT_NAME = "cascade-advisory-committee-meeting-packet-2026-11-18.pdf"
SOURCE_REDLINE = "docs/downloads/cascade-m2-red-blue-draft-ordinance-2026-11-11.pdf"
SOURCE_MD = "proposals/COMPLETE-M2-COLOR-CODED-REDLINE-2026-11-11.md"
STATE_GLOSSARY = "dataset/policy/38_IOWA_STATE_AND_M2_DEFINITIONS_2026-11-03.md"
MEMO = "proposals/NOVEMBER-18-2026-GENERATORS-AIR-AND-IOWA-CITY-COMPARATORS.md"

CFR_ROOT = "https://www.govinfo.gov/content/pkg/CFR-2025-title40-vol8/pdf/"
CFR_SECTIONS = ["60-4201","60-4202","60-4204","60-4205","60-4207","60-4209","60-4211","60-4214"]
IAC22_URL = "https://www.legis.iowa.gov/docs/iac/chapter/06-10-2026.567.22.pdf"
IAC23_URLS = [
    "https://www.legis.iowa.gov/docs/iac/chapter/06-10-2026.567.23.pdf",
    "https://www.legis.iowa.gov/docs/iac/chapter/10-15-2025.567.23.pdf",
]
CENTRAL_URL = "https://www.centralcityia.gov/vertical/sites/%7BE92EF555-E1B5-4E87-8D0F-7EE113321960%7D/uploads/Zoning_Code_Amendment.pdf"
PALO_URL = "https://cityofpalo.com/vertical/sites/%7B434D4528-2EBA-41FD-BB30-AF0F1451A315%7D/uploads/93-2026_Zoning_Regulations-_EU-1_Data_Center_Exclusive_Use_District.pdf"
FUEL_PART_URL = "https://www.govinfo.gov/content/pkg/CFR-2024-title40-vol37/pdf/CFR-2024-title40-vol37-part1090.pdf"

STYLE = """
@page {size:letter; margin: .72in .7in .7in;
 @top-left{content:"CASCADE  |  NOVEMBER 18 COMMITTEE PACKET";font:7.5pt "DejaVu Sans";color:#536274}
 @bottom-left{content:"Independent working research - not adopted law";font:7pt "DejaVu Sans";color:#637180}
 @bottom-right{content:"Page " counter(page);font:7pt "DejaVu Sans";color:#637180}}
body{font:9pt/1.48 "DejaVu Serif",serif;color:#1a2530;}
h1,h2,h3,h4{font-family:"DejaVu Sans";color:#213c53;line-height:1.26;break-after:avoid}
h1{font-size:18pt;margin:0.18in 0 0.13in;border-bottom:1.5pt solid #234e6b;padding-bottom:.06in}
h2{font-size:12pt;margin:.22in 0 .10in;border-bottom:.5pt solid #d8e0e8}
h3{font-size:10pt;margin:.16in 0 .07in}
p{margin:.06in 0 .105in} a{color:#19548b;overflow-wrap:anywhere;text-decoration:none}
ul,ol{margin:.06in 0 .1in;padding-left:.28in}li{margin:0 0 .05in}
table{border-collapse:collapse;width:100%;font-size:7.6pt;table-layout:fixed;margin:.12in 0 .18in}
thead{display:table-header-group}tr{break-inside:avoid}
td,th{border-bottom:.5pt solid #c8d2db;padding:5.5pt 6pt;text-align:left;vertical-align:top;overflow-wrap:anywhere}
th{font:7.4pt "DejaVu Sans";font-weight:bold;background:#eaf0f5}
blockquote{border-left:3pt solid #bd302f;padding-left:.12in;margin:.12in 0}
.definition{break-inside:avoid;border-left:2.5pt solid #b12d38;padding:.03in .11in;margin:.16in 0;background:#fffafa}
.definition .status{font:7.3pt "DejaVu Sans";color:#6b4a4a}
.definition h3{color:#9a2431}.definition p{font-size:8.5pt}
.section-break{break-before:page;}
.cover{break-after:page}
.cover h1{font-size:23pt;border:0;margin:.45in 0 .1in}
.cover .eyebrow{font: bold 10pt "DejaVu Sans";color:#355b78;letter-spacing:.7pt}
.cover .sub{font:11pt "DejaVu Sans";color:#516575}
.notice{background:#f0f3f6;padding:.11in .15in;break-inside:avoid;border-left:3pt solid #455f76}
.warn{background:#fff8e9;padding:.09in .14in;break-inside:avoid;border-left:3pt solid #ad7f21}
.small{font-size:8pt;color:#5b6874}
p.source{font:7.5pt/1.4 "DejaVu Sans";color:#466078}
code{font-size:7pt}
"""
INTRO = """<section class="cover">
<p class="eyebrow">CASCADE DATA CENTER ADVISORY COMMITTEE</p>
<h1>November 18, 2026<br>Meeting Research Packet</h1>
<p class="sub">M-2 red/blue draft | 28 local definitions | diesel generators and air emissions | Iowa municipal zoning</p>
<p>Prepared November 16, 2026 • City of Cascade, Iowa • Independent research compilation</p>
<div class="notice"><b>Status:</b> Neither the attached independent zoning proposal nor this research brief has been adopted by the City Council. Four definitions were reported approved for the committee's working draft November 11; the remaining 24 definitions and the proposed performance rules were not.</div>
<h2>Included in order</h2>
<ol>
<li><b>Cover and action questions</b> — assumptions, source caveats, legislative status</li>
<li><b>November 11 red/blue full ordinance</b> — rebuilt from current source with November 16 independent draft corrections; existing zoning baseline preserved, not adopted law</li>
<li><b>28 proposed Section 165.41 definitions</b> — complete wording and source footnotes; approved versus proposed clearly separated</li>
<li><b>Definitions omitted from the 86-term research glossary</b> — terms already treated in Iowa law or Cascade code, with source references</li>
<li><b>EPA / Iowa diesel-generator research</b> — federal operating rules, Tier classifications, 15/1,000 ppm fuel sulfur, ambient concentrations, permit questions</li>
<li><b>Verbatim official federal/Iowa sources</b> — reproduced government PDF pages with transparent highlights; source edition noted</li>
<li><b>Iowa municipal comparisons</b> — Central City working draft and relevant city-law links; Central City original pages where obtainable</li>
</ol>
<h2>Non-negotiable distinctions</h2>
<p><b>Generator count is not engine tier.</b> The reported 15 units and 40 MW electrical project load do not independently establish a diesel-generator equipment schedule, Tier 4 certification, use category, permit thresholds or the installed generating capacity.</p>
<p><b>PPM is not a single emissions standard.</b> Fuel sulfur limits are in ppm; ambient NO2, SO2, CO and ozone may be in ppm/ppb. Engine NOx, CO and particulate certification is usually in g/kW-hr. A fuel-sulfur ppm number is not an exhaust NOx ppm limit.</p>
<p><b>Government originals versus editorial work.</b> Reproduced PDF facsimiles preserve original statutory text; transparent yellow highlights are editorial. The dated print editions are cited separately from links to current official regulations.</p>
<p class="small">Full source repository: https://github.com/ttbakiatwoam/cascade-data-center<br>
Sources checked through November 16, 2026; obtain certified city minutes and final generator inventory before final legal conclusions.</p>
</section>
<h1>Meeting decision/questions checklist</h1>
<div class="warn"><b>Do not assume Tier 4 from 15 generators or 40 MW.</b> Ask Simple Mining for exact engine inventory, model year, per-cylinder displacement, emergency/nonemergency status, EPA emissions certification, permitted run hours, air-pollutant mass emissions, sulfur specification and concurrent-operation scenario.</div>
<ol>
<li>Confirm which of the <b>four committee definitions</b> were approved at November 11 and certified roll calls. No separate adoption of the Hyperscale ban has been shown.</li>
<li>Review the remaining <b>24 local proposals</b> individually, distinguishing definitional necessity from operational requirements.</li>
<li>Confirm Iowa DNR construction and operating permit applicability, NSPS Subpart IIII, RICE NESHAP Subpart ZZZZ, and cumulative emissions from all proposed engines.</li>
<li>Decide whether to request additional City zoning operating conditions after reviewing EPA/Iowa preemption and uniformity; avoid inventing unsupported ppm thresholds.</li>
<li>Compare <b>Central City (draft)</b>, <b>Palo (enacted EU-1)</b>, <b>Dubuque (temporary moratorium)</b> and other Iowa municipalities by actual legal status, not generic "Iowa data center law".</li>
</ol>"""


def read(root, rel):
    return (root / rel).read_text(encoding="utf-8")


def render_html(markup, root):
    data = "<!doctype html><html><head><meta charset='utf-8'><style>" + STYLE + "</style></head><body>" + markup + "</body></html>"
    return fitz.open(stream=HTML(string=data, base_url=str(root)).write_pdf(), filetype="pdf")


def md(text):
    return markdown.markdown(text, extensions=["tables","sane_lists","footnotes"])


def scrub_links(text):
    """Make relative citations absolute, keep public legal links."""
    return re.sub(r"\]\((\.\./[^)]+)\)", lambda m: "](" + BASE + m.group(1).replace("../","") + ")", text)


def create_definitions(root):
    source = read(root, SOURCE_MD)
    glossary = read(root, STATE_GLOSSARY)
    footnotes = {n:t for n,t in re.findall(r"^\[\^(\d+)\]:\s*(.+)$", source, re.M)}
    blocks = re.findall(
        r"^> 🟥 \*\*RED — NEW §165\.41 DEFINITION \((\d+) OF 28\).*?$(.*?)(?=^> 🟥 \*\*RED — NEW §165\.41 DEFINITION|\n## |\Z)",
        source, flags=re.M|re.S
    )
    if len(blocks) != 28 or [int(n) for n,_ in blocks] != list(range(1,29)):
        raise RuntimeError("Expected 28 ordered §165.41 local definitions, got %d" % len(blocks))
    body = ['<h1>28 proposed §165.41 terms — full text and sources</h1>']
    body.append("""<div class="notice"><b>Omitted-definition notice (for the November 18 meeting):</b> The earlier 86-term research glossary is <b>not</b> a proposal to enact 86 new local definitions. Terms already defined in Cascade §165.41 or in Iowa statutory/administrative programs were removed from the <i>local amendment proposal</i> to avoid inconsistent duplications. <b>They are enumerated after the 28 terms.</b> These existing rules are scattered across Iowa Code Chapters <b>103A, 414, 423, 455B, 657</b> and 567 IAC environmental rules — <b>not all in Chapter 414</b>. Three terms (Data Center, Data Center Business and Sustainable Design) were nonetheless expressly approved for draft local wording on November 11; this does not incorporate state tax/building-code eligibility automatically.</div>""")
    body.append("<p class='small'><b>Vote status:</b> 1-4 approved for advisory working draft only (participant-reported); numbers 5-28 are independently drafted options and require separate committee action. “Approved” does not mean City Council adopted law.</p>")
    collected=[]
    for ordinal,chunk in blocks:
        lines = chunk.splitlines()
        lines=[line[2:] if line.startswith("> ") else "" for line in lines if line.startswith(">")]
        lines=[line for line in lines if not "RED — NEW" in line]
        bodytext="\n".join(lines).strip()
        m=re.search(r"\*\*(.+?):\*\*",bodytext)
        if not m:
            raise RuntimeError("Missing definition heading %s" % ordinal)
        title=m.group(1)
        citations=list(dict.fromkeys(re.findall(r"\[\^(\d+)\]", bodytext)))
        bodytext=re.sub(r"\[\^(\d+)\]",r" [source \1]", bodytext)
        if int(ordinal)==1 and "structure or building" not in bodytext:
            raise RuntimeError("Canonical Data Center changed")
        if int(ordinal)==2 and not ("100,000 square feet or larger" in bodytext and "Electrical demand exceeding 60 megawatts" in bodytext):
            raise RuntimeError("Canonical Hyperscale thresholds changed")
        sources=[]
        for n in citations:
            note = footnotes.get(n,"Source note in dated complete redline")
            sources.append("<p class='source'><b>Source %s:</b> %s</p>"%(html.escape(n),md(scrub_links(note))))
        if not sources:
            sources.append("<p class='source'><b>Source:</b> independent Cascade M-2 technical/operational proposal, supported by draft §165.11 and technical research. No claim of an already codified Iowa zoning definition. <a href='"+BASE+SOURCE_MD+"'>Full source redline</a>.</p>")
        collected.append(title)
        status="PARTICIPANT-REPORTED COMMITTEE-APPROVED DRAFT TERM" if int(ordinal)<=4 else "INDEPENDENT PROPOSED TERM — NOT COMMITTEE-APPROVED"
        body.append("<section class='definition'><h3>%s. %s</h3><p class='status'>%s</p>%s%s</section>" % (ordinal,html.escape(title),status,md(bodytext),"\n".join(sources)))
    rows=[]
    state_section=glossary.split("## A. Definitions actually found in Iowa statutes and current administrative rules",1)[1].split("## B.",1)[0]
    for line in state_section.splitlines():
        m=re.match(r"^\| \*\*(.+?)\*\* \| (.*?) \| (.*?) \|",line)
        if not m:continue
        name,description,reference=m.groups()
        if name.casefold() in ["data center","data center business","sustainable design"]:
            continue
        match=re.search(r"https?://[^)]+",reference)
        url=match.group(0) if match else BASE+STATE_GLOSSARY
        if url[-1] in ",.;": url=url[:-1]
        rows.append((name,url))
    if len(rows)!=52:raise RuntimeError("Expected 52 state-law glossary terms not carried into local ordinance, got "+str(len(rows)))
    body.append("<div class='section-break'><h1>Omitted or nonproposed glossary terms</h1></div>")
    body.append("<div class='notice'><b>Important distinction:</b> “Removed” means <i>not proposed as a new local definition</i>; it does not repeal or delete state laws or existing Cascade definitions. The 52 items below are Iowa statutory/administrative reference terms remaining outside the 28 proposed local entries. Their legal scope ranges from <b>building regulation, state tax, air pollution, hazardous waste and water allocation</b> to general land use. They are <b>not all statewide zoning definitions</b>. The prior 86-term collection additionally contained five legal-principle explanations, not freestanding Iowa statutory definitions.</div>")
    body.append("<h2>Already in Cascade zoning (do not redefine without an identified reason)</h2>")
    body.append(md("""| Existing local term | Already enacted location |
| --- | --- |
| Accessory Use | Cascade §165.41(1) |
| Building (Structure) | Cascade §165.41(8) |
| Dwelling Unit | Cascade §165.41(12) |
| Lot | Cascade §165.41(30) |
| Structure (Building) | Cascade §165.41(51) |
"""))
    body.append("<h2>52 state-law terms omitted from the proposed 28</h2>")
    body.append("<p>Each term links to the source used in the 86-term research glossary. Verify each statute's limited legal context before applying it to land-use zoning.</p>")
    body.append("<table><thead><tr><th style='width:46%'>Iowa term not reproposed</th><th>Primary Iowa-law or rule reference</th></tr></thead><tbody>")
    for name,url in rows:
        body.append("<tr><td>"+html.escape(name)+"</td><td><a href='"+html.escape(url,quote=True)+"'>"+html.escape(url.split("/")[-1])+"</a></td></tr>")
    body.append("</tbody></table>")
    body.append("<h2>Five additional zoning-law concepts retained as research, not local definitions</h2>")
    body.append("<p><b>Special exception; Variance; Public welfare / general welfare; Zoning uniformity; Stormwater controls.</b> These are concepts whose meaning and legal authority derive from applicable state and local procedures, not five newly proposed §165.41 terms. [Source table]("+BASE+STATE_GLOSSARY+").</p>")
    body.append("<p class='source'>Master research sources: <a href='"+BASE+STATE_GLOSSARY+"'>86-term research register</a> and <a href='"+BASE+SOURCE_MD+"'>November 11 complete redline</a>. Reported draft votes: <a href='"+BASE+"dataset/updates/50_COMMITTEE_APPROVED_DEFINITIONS_CANONICAL_2026-11-11.md'>four canonical definitions</a>.</p>")
    return render_html("\n".join(body),root),collected


def fetch_pdf(session,url,mandatory=False):
    try:
        r=session.get(url,timeout=75,headers={"User-Agent":"Cascade-Committee-Research/1.0 (public records compilation); Mozilla/5.0","Accept":"application/pdf,*/*"})
        r.raise_for_status()
        if not r.content.startswith(b"%PDF") or len(r.content)<900:
            raise ValueError("not a usable PDF")
        d=fitz.open(stream=r.content,filetype="pdf")
        print("SOURCE",url,"pages",len(d),"bytes",len(r.content))
        return d
    except Exception as ex:
        print("MISSING SOURCE",url,type(ex).__name__,str(ex)[:200])
        if mandatory:raise RuntimeError("Required official facsimile unavailable: "+url) from ex
        return None


def highlight(doc,patterns):
    colors=(.97,.82,.20)
    count=0
    for page in doc:
        for pattern in patterns:
            for rect in page.search_for(pattern)[:35]:
                try:
                    mark=page.add_highlight_annot(rect)
                    mark.set_colors(stroke=colors)
                    mark.set_opacity(.35)
                    mark.update()
                    count+=1
                except Exception:
                    pass
    return count


def insert_source(dest,src,title,toc,sections,color_terms=()):
    start=len(dest)+1
    if color_terms:highlight(src,color_terms)
    dest.insert_pdf(src,annots=True)
    toc.append([1,title,start])
    sections.append((title,start,len(src)))


def select_pages(doc,needles,neighbors=0,max_pages=18):
    found=[]
    for i,p in enumerate(doc):
        txt=p.get_text()
        if any(q.lower() in txt.lower() for q in needles):
            for k in range(max(0,i-neighbors),min(len(doc),i+neighbors+1)):
                found.append(k)
    pages=list(dict.fromkeys(found))
    if not pages: raise RuntimeError("Required legal text not found in official publication: "+str(needles))
    if len(pages)>max_pages:pages=pages[:max_pages]
    result=fitz.open()
    for page in pages: result.insert_pdf(doc,from_page=page,to_page=page)
    return result,pages


def make(root,out):
    root=root.resolve();out=out.resolve()
    origin=root/SOURCE_REDLINE
    if not origin.exists(): raise RuntimeError("Missing source November 11 red/blue PDF")
    definitions,titles=create_definitions(root)
    memo=read(root,MEMO)
    research=render_html("<div class='section-break'><h1>Generator and Iowa zoning research</h1></div>"+md(memo),root)
    with fitz.open(origin) as ordinance:
        if len(ordinance)!=24:raise RuntimeError("Unexpected Nov 11 ordinance pages "+str(len(ordinance)))
        doc=fitz.open()
        toc=[]
        sections=[]
        introduction=render_html(INTRO,root)
        insert_source(doc,introduction,"November 18 cover and committee questions",toc,sections)
        insert_source(doc,ordinance,"November 11 original black/red/blue M-2 draft (unchanged)",toc,sections)
        insert_source(doc,definitions,"28 definitions, 52 omitted Iowa statutory terms, existing Cascade terms",toc,sections)
        insert_source(doc,research,"EPA / Iowa diesel and municipal zoning research",toc,sections)

        session=requests.Session()
        for label in CFR_SECTIONS:
            sec=label.replace("-",".")
            url=CFR_ROOT+"CFR-2025-title40-vol8-sec"+label+".pdf"
            src=fetch_pdf(session,url,mandatory=True)
            patterns={
                "60-4202":["Tier 2","Tier 3","2,237 KW","3,700 KW"],
                "60-4205":["g/KW-hr","Tier 2","Tier 3"],
                "60-4207":["1,000 parts per million","30 liters per cylinder","1090.305"],
                "60-4211":["100 hours per calendar year","50 hours","peak shaving"],
            }.get(label,["emission standards","emergency"])
            insert_source(doc,src,"Official federal CFR 2025: 40 CFR §"+sec,toc,sections,patterns)

        # The government publishes Part 1090 as a full facsimile.
        # Extract the unchanged printed page containing the ULSD sulfur rule.
        part=fetch_pdf(session,FUEL_PART_URL,mandatory=True)
        fuel,pages=select_pages(part,["§ 1090.305", "Maximum sulfur content of 15 ppm"],neighbors=0,max_pages=3)
        if "15 ppm" not in " ".join(p.get_text() for p in fuel):raise RuntimeError("ULSD 15 ppm rule not present")
        insert_source(doc,fuel,"Official printed EPA 40 CFR §1090.305 (2024 ed; revised 2026)",toc,sections,["Maximum sulfur content of 15 ppm","15 ppm"])
        print("FUEL PAGE INDICES",pages)
        # 2026 official Iowa Chapter 22 source: actual compiled internal IAC page header is 1/7/26
        # on the June 10 archive; do not describe it as an Oct 28 edition.
        iac=fetch_pdf(session,IAC22_URL,mandatory=True)
        state,spages=select_pages(iac,["Emergency generator","potential to emit for emergency generators","567—22.11","22.11(455B)"],neighbors=1,max_pages=15)
        insert_source(doc,state,"Official Iowa 567 IAC Ch. 22 excerpts (June 10 2026 archive)",toc,sections,[
            "Emergency generator","500 hours of operation annually","8,760 hours","Ambient air quality standards"
        ])
        print("IOWA CHAPTER22 PAGE INDICES",spages)

        # The city user provided the Central City draft. Attach original City source when accessible.
        central=fetch_pdf(session,CENTRAL_URL,mandatory=False)
        if central is not None and len(central)>=8:
            insert_source(doc,central,"Central City Iowa: original proposed 10-page zoning/water draft",toc,sections,[
                "Tier 1 Data Center","Tier 2 Data Center","Tier 3 Data Center",
                "65 dBA","Generator operation and testing","Monday through Friday",
                "Council final review","Acoustical studies","Cooling and water disclosure"
            ])
        else:
            print("WARNING: Central City original unavailable; source paragraphs and link in research memo only")
        palo=fetch_pdf(session,PALO_URL,mandatory=False)
        if palo is not None:
            insert_source(doc,palo,"City of Palo enacted Ordinance 93-2026 EU-1 comparison",toc,sections,["EU-1","Data Centers","backup power generation","Major Site Plan"])

        # Validate source contents.
        alltext="\n".join(page.get_text() for page in doc)
        must=["November 18, 2026","Data Center Business","Hyperscale Data Center",
              "100,000 square feet or larger","Electrical demand exceeding 60 megawatts",
              "15 ppm","Central City","Air"]
        for t in must:
            if t not in alltext: raise RuntimeError("Missing packet text: "+t)
        if len(titles)!=28 or len(doc)<55:raise RuntimeError("Incomplete packet: definitions="+str(len(titles))+", pages="+str(len(doc)))
        doc.set_toc(toc)
        doc.set_metadata({
          "title":"Cascade November 18 2026 Advisory Committee Research Packet",
          "subject":"M-2 red/blue draft; 28 definitions; federal and Iowa diesel emissions; city zoning comparators",
          "author":"Cascade Data Center Independent Research",
          "keywords":"Cascade Iowa M-2 2026-11-18 EPA diesel air zoning Central City"
        })
        out.parent.mkdir(parents=True,exist_ok=True)
        doc.save(out,garbage=3,deflate=True)
        print("PACKET",out,"pages",len(doc),"bytes",out.stat().st_size)
        for name,start,count in sections:print("SECTION",start,count,name)
        print("NOTE: Official PDF source pages are exact source text with editorial transparent highlights.")
        if central is None: print("WARNING: No Central City full original document; brief linked to supplied original.")
    return out


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--root",default=".")
    p.add_argument("--out",default="docs/downloads/"+OUT_NAME)
    a=p.parse_args()
    make(Path(a.root),Path(a.out))

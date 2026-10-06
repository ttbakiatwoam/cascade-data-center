#!/usr/bin/env python3
"""Offline checks for navigation, preserved evidence, and the question bank."""

import csv
import hashlib
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def visible_markdown(text):
    """Ignore fenced code and HTML comments when finding navigation."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return re.sub(r"^(`{3,}|~{3,}).*?^\1[^\n]*$", "", text, flags=re.M | re.S)


def heading_ids(text):
    counts = {}
    anchors = set()
    for match in re.finditer(r"^#{1,6}\s+(.+?)\s*#*\s*$", visible_markdown(text), re.M):
        heading = re.sub(r"<[^>]*>", "", match[1]).lower()
        heading = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", heading)
        slug = re.sub(r"[^\w\- ]", "", heading).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        anchors.add(slug + (f"-{count}" if count else ""))
    return anchors


def main():
    errors = []
    link_count = 0
    documents = sorted(ROOT.rglob("*.md"))
    for path in documents:
        if ".git" in path.relative_to(ROOT).parts:
            continue
        text = visible_markdown(path.read_text(encoding="utf-8"))
        for match in re.finditer(r"\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)", text):
            url = urlsplit(match[1].strip("<>"))
            if url.scheme or url.netloc:
                continue
            link_count += 1
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            location = f"{path.relative_to(ROOT)}: {match[1]}"
            if not target.is_relative_to(ROOT):
                errors.append(f"Link escapes repository: {location}")
            elif not target.exists():
                errors.append(f"Missing link target: {location}")
            elif url.fragment and target.suffix == ".md":
                if unquote(url.fragment) not in heading_ids(target.read_text(encoding="utf-8")):
                    errors.append(f"Missing heading: {location}")

    manifest = ROOT / "sources/SHA256SUMS"
    source_count = 0
    listed = set()
    for line in manifest.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (sources/.+)", line)
        if not match:
            errors.append(f"Invalid source manifest line: {line}")
            continue
        digest, name = match.groups()
        target = ROOT / name
        source_count += 1
        if name in listed:
            errors.append(f"Duplicate source manifest entry: {name}")
        listed.add(name)
        if not target.resolve().is_relative_to(ROOT / "sources"):
            errors.append(f"Source path escapes sources directory: {name}")
        elif not target.is_file():
            errors.append(f"Missing preserved source: {name}")
        elif hashlib.sha256(target.read_bytes()).hexdigest() != digest:
            errors.append(f"Preserved source hash mismatch: {name}")
    source_files = {str(p.relative_to(ROOT)) for p in (ROOT / "sources").rglob("*")
                    if p.is_file() and p.name not in {"README.md", "SHA256SUMS", ".DS_Store"}}
    for name in sorted(source_files - listed):
        errors.append(f"Preserved source missing from manifest: {name}")

    with (ROOT / "dataset/community/questions.csv").open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        rows = list(reader)
        if reader.fieldnames != ["Topic", "Question"]:
            errors.append("Question-bank schema must be Topic,Question")
        if len(rows) != 76:
            errors.append(f"Expected the original 76 questions; found {len(rows)}")
        if any(None in row or not (row.get("Topic") or "").strip() or
               not (row.get("Question") or "").strip() for row in rows):
            errors.append("Question bank contains incomplete or malformed rows")

    result = subprocess.run(["bash", "-n", str(ROOT / "scripts/submit-questions.sh")],
                            capture_output=True, text=True)
    if result.returncode:
        errors.append(f"Submission helper syntax: {result.stderr.strip()}")

    if errors:
        print("Repository checks failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Passed: {link_count} local links, {source_count} preserved source hashes, "
          f"{len(rows)} questions, and Bash syntax. No network requests or submissions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

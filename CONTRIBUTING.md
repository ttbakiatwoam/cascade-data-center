# Maintaining the research collection

Start with the [research methodology, evidence labels, and privacy rules](dataset/00_INDEX.md). The [research scope](docs/research-scope.md) preserves the project's purpose and policy stance.

## Adding or updating evidence

1. Add the public citation and provenance to the [source index](dataset/evidence/22_SOURCE_INDEX.md). Identify the publisher, document date, URL, and source status.
2. Put preserved files in the relevant `sources/` subfolder. Keep original bytes and filenames; label OCR and automated captions as derivatives. Add the new file's SHA-256 to `sources/SHA256SUMS` without regenerating hashes for existing files.
3. Update the relevant topic note and record when the evidence was reviewed. Keep company/utility representations distinct from independent verification and preliminary estimates distinct from final commitments.
4. Update the [open questions tracker](dataset/project/21_OPEN_QUESTIONS_AND_EVIDENCE_GAPS.md) when a project's evidence status changes. Preserve material corrections and the dated history.
5. Keep project-generated draft ordinance text in `proposals/` with its draft label. Historical or external draft records keep their own status labels in the zoning/comparator collections.
6. Add new notes to the [research index](dataset/00_INDEX.md) and the relevant folder README. Keep existing numbered filenames stable; use an unused number for a new note.
7. Run the local checks before proposing the change:

```sh
python3 scripts/check-repository.py
```

The checks validate local Markdown file/heading links, preserved source hashes, the question-bank format, and submission-helper syntax. They do not contact external websites, verify legal status, or submit questions.

## Placement and privacy

See the [layout guide](docs/repository-layout.md) for folder responsibilities and previous paths. Do not add private correspondence, personal identifiers, private social-media discussions, or local dispute material. Public institutional records remain identified where necessary for source traceability.

The question-submission helper is optional and manually operated. Repository validation does not run it or contact the form.

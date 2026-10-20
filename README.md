# dai — decentralized AI × deep learning × cryptography reservoir

A living reference tracking how new research in decentralized AI, deep
learning, and cryptography relates to systems that already ship in
production. Built to answer one question on demand: **"what's changed
since I last checked, and does it actually affect anything real?"**

## AI-generated content notice

The research, analysis, and "does this affect system X" judgments in this
repository are produced primarily by an AI (Claude) with a human
(maintainer) directing scope and spot-checking output. This is **not**
peer-reviewed material and carries no claim of novel authorship over the
analysis itself. Treat every claim here as a starting point for your own
verification, not a citable source. See each entry's `confidence` field.

## Structure

```
/systems/      One file per tracked production system: what it does,
               what it's built on, current known limitations, and the
               matrix of properties that incoming research gets checked
               against.

/foundations/  One foundational paper per field — chosen because a
               tracked system's own docs/whitepaper demonstrably cites
               it, not because it's subjectively "important."

/watch/        checkpoint.json tracks the last-checked timestamp per
               source so a manual trigger only reports deltas.
               log/ holds one dated entry per trigger run.

index.json     Generated, not hand-edited. Structured mirror of every
               systems/ and foundations/ file (frontmatter, prose
               sections, and property matrices parsed into tables) for
               anything — a dashboard, a script — that wants to consume
               this content without parsing markdown. Source of truth is
               always the .md files; index.json just reflects them.

scripts/build_index.py  Regenerates index.json from the current state of
               systems/ and foundations/. Stdlib only, no dependencies.
```

## Update process

The markdown files are the source of truth. Any time one of them changes
— a manual edit, or a watch-trigger run writing a new finding — the
process is:

1. Edit/add the relevant `systems/*.md` or `foundations/*.md` file,
   including bumping its `last_updated` frontmatter field.
2. Run `python3 scripts/build_index.py` to regenerate `index.json`.
3. Commit the markdown change and the regenerated `index.json` together
   in the same commit — they should never drift apart. If a watch run
   produced the change, its `watch/log/` entry documents why.

`index.json` is never hand-edited. If its shape needs to change (a new
field, a new section type), that happens by changing
`scripts/build_index.py` and regenerating, not by patching the JSON
directly.

## How the watch loop works

This is **pull, not push** — no cron, no schedule. You trigger a check
whenever you want (e.g. "catch me up"). The run:

1. Pulls new items since the last checkpoint from a fixed, narrow set of
   sources (IACR ePrint + relevant arXiv categories) — not the entire
   literature.
2. Filters for relevance against the tracked systems/fields list below.
3. For anything touching a tracked system: reads it properly (no time
   limit — optimized for accuracy, not speed) and checks it against
   that system's property matrix. A companion note gets written **only
   if something in the matrix actually changes.**
4. For anything field-relevant but not tied to a tracked system: filed
   as "related, unverified relevance" — a visibly lower confidence tier,
   no full write-up.
5. Checkpoint updates; you get a short report: N new, M matrix-impacting,
   rest filed.

Most runs will resolve in minutes with "nothing new." The occasional run
that finds something real will take as long as it takes to read properly.

## Tracked systems and fields

| System | Field |
|---|---|
| EZKL | ZKML / verifiable inference |
| Gensyn | Decentralized / distributed training |
| Zama (Concrete-ML) | FHE for ML |
| Nillion | Secure MPC for ML |
| Bittensor | Decentralized incentive / consensus mechanisms for ML networks |

This list is deliberately small. Scope grows only when a new system
earns a row, not by default.

## Deployment plan (decided, not yet executed)

This repo is meant to end up publicly hosted on GitHub Pages — a static
page reading `index.json` directly (not the default Jekyll markdown
render, which can't do the filterable/interactive view that's the
actual goal).

A separate project, **misbar-platform** (`../misbar-platform`), will
reference the deployed site rather than host this content itself:

- misbar-platform is Dockerized and deployed independently, so it
  cannot read `../dai` as a live relative path at build/runtime —
  whatever it needs has to be either a public URL or a copy committed
  into its own repo. A publicly hosted Pages site solves this cleanly:
  no file-copying, no sync step, no drift.
- misbar-platform's design system (`src/design-system/`) encodes
  product-specific meanings — `StatusChip`'s VERIFIED/PENDING/FAILED is
  a cryptographic check outcome, `EvidenceRecord`'s disclosed/withheld
  is a commitment-scheme claim, `SeverityBadge`/`FindingsLog` are
  red-teaming severity. None of these map onto this repo's "grounded vs.
  inferred" citation-confidence framing without a category error —
  claiming a research citation is "VERIFIED" would overstate what it
  means by misbar-platform's own rules. Hosting separately avoids that
  mismatch entirely rather than forcing a fit.
- Reference method decided: a **custom subdomain via CNAME**
  (e.g. `research.misbar.xyz` pointed at the GitHub Pages site) —
  reads as integrated/on-brand, one DNS record, no code changes needed
  on the misbar-platform side, and no live coupling between the two
  repos' deploy pipelines.

**Not yet done:** no GitHub remote exists for this repo yet, nothing is
pushed, Pages isn't enabled, and the static dashboard page itself isn't
built. Revisit once the dashboard page is further along.

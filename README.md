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
```

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

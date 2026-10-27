---
name: Story Protocol
field: On-chain IP and training-data licensing
category: ownership
foundation:
last_updated: 2026-10-27
confidence: inferred (press-release level only)
website: "https://www.story.foundation"
---

# Story Protocol

## What it does

An on-chain registry for IP: ownership, licensing terms, derivative
permissions and economic rights in machine-readable form.

## Architecture summary

- On 2026-01-29 Story and OpenLedger announced a joint standard for
  licensed AI training: AI systems train on licensed IP, prove how it was
  used, enforce license terms at runtime, and distribute royalties
  automatically (see `/systems/openledger.md`).
- Story's role is the canonical IP registry. This is a press release, not
  independent validation; the protocol's own docs were not read.

## Built on (foundational lineage)

None found. Foundation intentionally empty.

## Property matrix

| Property | Current value | Source |
|---|---|---|
| Function | IP registry + licensing terms | Joint announcement |

## Comparison axes

| Axis | Class | Detail | Source |
|---|---|---|---|
| Correctness | OPEN QUESTION | Proving how licensed IP was used in training is unsolved; no mechanism described | Joint announcement, inferred |
| Trust rests on | NOT COVERED | Registering IP on-chain doesn't establish the registrant owns it | Not addressed in this file's sources |
| Confidentiality | NOT COVERED | — | Not addressed in this file's sources |
| Lineage | NONE FOUND | — | File's lineage note, inferred |
| Maturity | NOT COVERED | — | Not addressed in this file's sources |
| On-chain | NOT COVERED | An on-chain IP registry; which chain isn't stated | Not addressed in this file's sources |

## Known limitations

- "Cryptographically proving how IP is used" in training is the hard,
  unsolved part (see `/foundations/zk-proof-of-training.md`: proofs of
  training do not establish what data overlapped); no mechanism was
  described in the sources.
- Registering IP on-chain does not establish that the registrant owns it.

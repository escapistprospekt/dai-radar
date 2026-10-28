---
name: Atoma Network
field: Confidential computing (TEE) for AI inference
category: private-compute
foundation: foundations/tee-remote-attestation.md
last_updated: 2026-10-27
confidence: grounded (2024 sources); current status unverified
website: "https://atoma.network"
---

# Atoma Network

## What it does

A decentralized, privacy-preserving inference layer on Sui. Announced May
2024 as a verifiable inference network serving Sui; reported live on Sui
mainnet in December 2024 (alpha, with a demo chat app "Utopia").

## Architecture summary

- AI processing runs in TEEs so inputs and outputs are isolated from the
  operators (press release).
- OpenAI-compatible API endpoints.
- Atoma's team paper, "Privacy-Preserving Decentralized AI with
  Confidential Computing" (Lee, Antonio, Khan; arXiv 2410.13752, Oct 2024),
  argues TEEs protect model parameters and user data on untrusted
  machines at lower cost than zkML ("prohibitive computational
  overhead"), says TEEs "face a few limitations", and outlines how they
  fit Atoma's framework. Only the abstract was read.

## Built on (foundational lineage)

The arXiv paper is Atoma's own framing, not a cited foundation of the
mechanism. Link to `foundations/tee-remote-attestation.md` is **inferred**.
It also positions itself against `/foundations/zkml.md`.

## Property matrix

| Property | Current value | Source |
|---|---|---|
| Chain | Sui | Decrypt / Chainwire |
| Verification | TEE-based (vs zkML) | arXiv 2410.13752 abstract |

## Comparison axes

| Axis | Class | Detail | Source |
|---|---|---|---|
| Correctness | ATTESTATION | TEE-based verification, positioned as a practical alternative to zkML | arXiv 2410.13752 abstract |
| Trust rests on | HARDWARE VENDOR | TEE hardware isolates inputs and outputs from operators | Decrypt / Chainwire press release |
| Confidentiality | HARDWARE ENCLAVE | Inputs and outputs isolated from node operators inside TEEs | Decrypt / Chainwire press release |
| Lineage | NONE FOUND | Team paper (arXiv 2410.13752) is framing, not a cited foundation; TEE link inferred | File's lineage note, inferred |
| Maturity | OPEN QUESTION | Reported alpha on Sui mainnet in Dec 2024; nothing newer found | 2024 sources only, inferred |
| On-chain | EXISTING CHAINS | Sui | Decrypt / Chainwire |

## Known limitations

- All sources are 2024; the current state of the network was not found.
  Treat as stale until checked against the project's repo and docs
  (docs.atoma.network was unreachable this pass).

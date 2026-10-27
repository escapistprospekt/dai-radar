---
name: Secret Network
field: Confidential computing (TEE) for AI inference
category: private-compute
foundation: foundations/tee-remote-attestation.md
last_updated: 2026-10-27
confidence: grounded (docs structure, partnership post); inferred (details beyond that)
website: "https://scrt.network"
---

# Secret Network

## What it does

A Cosmos-based blockchain for confidential smart contracts: data is
encrypted at rest, in transit and during computation inside TEEs. It now
also offers "Secret AI" and SecretVM confidential virtual machines.

## Architecture summary

- Docs sections reviewed: Intel SGX privacy technology (remote
  attestation, sealing, trusted/untrusted core), encryption key
  management (consensus seed rotation), Secret AI (SubscriptionManager,
  WorkerManager, RewardsManager contracts), and SecretVM.
- **Morpheus integration (2026-08-07):** Morpheus built a TEE Provider so
  Secret's confidential AI models are available through its decentralized
  inference marketplace.

## Built on (foundational lineage)

None cited in the pages reviewed. **Inferred** link to
`foundations/tee-remote-attestation.md` (SGX origin).

## Property matrix

| Property | Current value | Source |
|---|---|---|
| TEE | Intel SGX (L1 contracts); SecretVM for VMs | Secret docs index |
| AI economics | On-chain subscription / worker / rewards contracts | Secret docs index |

## Comparison axes

| Axis | Class | Detail | Source |
|---|---|---|---|
| Correctness | ATTESTATION | Intel SGX remote attestation (doc index only; architecture pages unread) | Secret docs index, inferred |
| Trust rests on | HARDWARE VENDOR | Intel SGX, which has a record of published side-channel attacks | Secret docs index, inferred |
| Confidentiality | HARDWARE ENCLAVE | Data encrypted at rest, in transit and during computation inside TEEs; SecretVM for VMs | Secret docs index |
| Lineage | NONE FOUND | No paper cited; the link to Intel SGX Explained is inferred from the shared TEE-attestation mechanism | Secret docs index, inferred link |
| Maturity | LIVE | Running chain; Secret AI models offered via Morpheus since 2026-08-07 | Partnership post; classification inferred |
| On-chain | OWN CHAIN | Cosmos-based chain for confidential smart contracts | Secret docs index |

## Known limitations

- The architecture pages themselves were not read in this pass; only the
  doc index and the partnership post were. Deepen before relying on detail.
- The partnership post calls the stack "unhackable" with no audit or
  benchmark evidence; treat as marketing.
- SGX has a record of published side-channel attacks; check Secret's own
  post-mortems before concluding anything about current exposure.

---
field: ZK proof of training / verifiable training
paper: "Falafel: Modular Zero-Knowledge Proofs of Training in the Federated Setting"
authors: Tariq Bontekoe, Sven Bootsma, Vincent Dunning, Thom Sijpesteijn, Thomas Attema
year: 2026
venue: IACR ePrint 2026/1335
link: https://eprint.iacr.org/2026/1335
---

# ZK proofs of training (research cluster)

## Why this is here

**Research, not a shipping system.** No tracked system cites these papers
yet; they sit in the foundations as the leading edge of extending
`/foundations/zkml.md` from proving *inference* to proving *training*.
Seeded with Falafel; two other 2026 papers are grouped with it. All three
abstracts were read; none of the full papers were. Peer-review status was
not checked.

## Papers

- **Falafel** (ePrint 2026/1335, received 2026-06-29): zkPoT for federated
  learning covering local training steps and the central weight update.
  Claims ~70 kB proof for one LeNet round, ~150 s to generate, 10-15x
  smaller than prior zkPoT work, and avoids Fiat-Shamir with arithmetic
  hashes.
- **ZKBoost** (ePrint 2026/202; Melissaris, Polychroniadou, Takahashi,
  Weng, Xu): first zkPoT for XGBoost; VOLE-based; fixed-point XGBoost
  within 1% of standard accuracy.
- **Verifiable Fine-Tuning** (arXiv 2510.16830; Akgul et al., v3 Dec 2025):
  proofs that a released model was fine-tuned from a public base under a
  declared program and committed dataset, using recursive aggregation. No
  code link; the abstract gives no proof-size or prover-cost numbers.

## Open problems (from search results, secondary)

- Proving training correct does not prove anything about training-data
  overlap with private records.
- Governance analyses call ZK for frontier-scale verification promising but
  currently impractical.

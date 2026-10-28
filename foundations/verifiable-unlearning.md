---
field: Verifiable machine unlearning
paper: "Verifiable and Provably Secure Machine Unlearning"
authors: Thorsten Eisenhofer, Doreen Riepel, Varun Chandrasekaran, Esha Ghosh, Olga Ohrimenko, Nicolas Papernot
year: 2025
venue: IEEE SaTML 2025
link: https://arxiv.org/abs/2210.09126
---

# Verifiable and Provably Secure Machine Unlearning

## Why this is here

**Research, not a shipping system.** No tracked system cites it. It extends
the ZK-for-ML cluster (`/foundations/zk-proof-of-training.md`,
`/foundations/zkml.md`) to proving that data was *removed* from a model.
Author names and venue are from search results plus background knowledge
and should be checked; only listings and abstracts were seen.

## Core contribution

A cryptographic definition of verifiable unlearning, plus a protocol using
SNARKs and hash chains: proofs cover correct execution of the unlearning
step and that the deleted point is absent from the new training set.
Tested on linear regression, logistic regression and neural networks.

## Related 2026 work (listings only)

- **ZK-APEX** (MLSys 2026): personalized unlearning on edge devices; a ViT
  proof in ~2 hours, claimed >10^7x faster than retraining-based
  verification.
- **VeriForgot** (March 2026 preprint, not peer reviewed): combines
  membership-inference tests, blockchain unlearning certificates and a ZK
  proof of parameter shift; its authors argue no cryptographically
  verifiable mechanism yet proves unlearning occurred.
- A separate paper titled "Verification of Machine Unlearning is Fragile"
  exists; its findings were not read.

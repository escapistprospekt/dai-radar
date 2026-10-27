---
field: Formal verification of neural networks
paper: "Efficient Neural Network Robustness Certification with General Activation Functions"
authors: Huan Zhang, Tsui-Wei Weng, Pin-Yu Chen, Cho-Jui Hsieh, Luca Daniel
year: 2018
venue: NeurIPS 2018
link: https://arxiv.org/abs/1811.00866
---

# CROWN: Efficient Neural Network Robustness Certification

## Why this is the seed for this field

Grounded for α,β-CROWN: its README lists CROWN (2018) first among the
papers users should cite, then auto_LiRPA, α-CROWN, β-CROWN and later
extensions, so the lineage is a documented citation chain. The venue and
author list above are from background knowledge, not from the README, and
should be checked against the arXiv page.

## Core contribution

Linear bound propagation: derive linear lower and upper bounds on each
neuron's output over an input region, for general activations, giving a
sound (possibly loose) certificate that no input in the region violates
a property. Later work adds branch-and-bound (β-CROWN) to make this
complete for ReLU networks and runs it on GPUs.

## Link to tracked systems

`/systems/alpha-beta-crown.md` (grounded). `/systems/marabou.md` is a
different approach (SMT/LP based) and links here only as an inferred peer.
Both address *behavioural properties of a model*, a different problem
than the cryptographic proofs of correct execution in `/foundations/zkml.md`.

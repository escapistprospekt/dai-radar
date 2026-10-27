---
field: Differential privacy for ML training
paper: "Deep Learning with Differential Privacy"
authors: Martin Abadi, Andy Chu, Ian Goodfellow, H. Brendan McMahan, Ilya Mironov, Kunal Talwar, Li Zhang
year: 2016
venue: ACM CCS 2016
link: https://arxiv.org/abs/1607.00133
---

# Deep Learning with Differential Privacy

## Why this is the seed for this field

**Inferred, not grounded.** The Opacus README reviewed does not cite this
paper (it cites its own technical report, arXiv:2109.12298, plus clipping
papers). It is used here as the standard origin of DP-SGD, the algorithm
that Opacus's `noise_multiplier` / `max_grad_norm` parameters implement.
Flower's docs also list DP strategies and accountants (see
`/systems/flower.md`), but Flower's authoritative foundation is secure
aggregation, since DP there is a second, separate feature.

## Core contribution

DP-SGD: clip each example's gradient to a norm bound, add calibrated
Gaussian noise, and track cumulative privacy loss with a "moments
accountant," so a model can be trained with a quantified (epsilon, delta)
guarantee on what it leaks about any single training example.

## Link to tracked systems

`/systems/opacus.md`. Distinct from the cryptographic foundations in this
repo (MPC, FHE, secure aggregation): DP bounds what the *output* reveals;
it does not hide data during computation.

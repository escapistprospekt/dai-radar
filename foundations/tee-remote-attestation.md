---
field: Confidential computing (TEE) for AI inference
paper: "Intel SGX Explained"
authors: Victor Costan, Srinivas Devadas
year: 2016
venue: IACR ePrint 2016/086
link: https://eprint.iacr.org/2016/086
---

# Intel SGX Explained

## Why this is the seed for this field

**Inferred, not grounded.** None of the TEE-based inference systems filed
under this foundation (Phala/dstack, Tinfoil, Chutes, NEAR AI Cloud,
Secret Network, Oasis ROFL, Atoma, Venice) cites this paper in the docs
reviewed. It is used here as the standard academic reference for the shared
mechanism they all rely on: hardware-enforced isolation plus *remote
attestation*, where the hardware signs a measurement of the code and
configuration so a remote client can decide whether to trust it. Contrast
`/foundations/ccf-confidential-computing.md`, where Azure's docs name CCF
directly.

## Core contribution

A systematization of how SGX-style enclaves provide isolation, sealing and
attestation, and of the attack surface around them. Newer designs the
tracked systems use (Intel TDX confidential VMs, NVIDIA GPU confidential
computing, AMD SEV-SNP) differ in granularity (VM instead of enclave) but
keep the same trust shape: the hardware vendor's attestation signature is
the root of trust.

## Link to tracked systems

See `/systems/phala-dstack.md`, `/systems/tinfoil.md`,
`/systems/chutes.md`, `/systems/near-ai-cloud.md`,
`/systems/secret-network.md`, `/systems/oasis-sapphire-rofl.md`,
`/systems/atoma-network.md`, `/systems/venice-ai.md`. A recurring
caveat across all of them: attestation is evidence of what is running,
not a guarantee it is secure, and side-channel attacks on TEEs are an open
research area.

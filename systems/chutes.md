---
name: Chutes
field: Confidential computing (TEE) for AI inference
category: private-compute
foundation: foundations/tee-remote-attestation.md
last_updated: 2026-10-27
confidence: grounded (TEE mode, per Chutes' own post); unverified (Bittensor relationship)
website: "https://chutes.ai"
---

# Chutes

## What it does

A serverless AI inference platform that added a TEE serving mode (public
announcement dated 2026-05-07) for confidential LLM inference.

## Architecture summary

- **Hardware:** Intel TDX for CPU isolation plus NVIDIA confidential
  computing for the GPU.
- **Attestation:** measured boot (RTMR measurements); a hardware-signed TD
  Quote is checked by validators against a known-good configuration; NVIDIA
  GPU attestation is verified; the LUKS-encrypted root filesystem unlocks
  only after attestation; Kubernetes admission allows only cosign-signed
  images.
- **Optional E2EE:** on eligible TEE-backed instances, prompts are
  encrypted client-side and decrypted only inside a verified TEE.

## Built on (foundational lineage)

No paper cited. Lineage to `foundations/tee-remote-attestation.md` is
**inferred**. The announcement page does not mention Bittensor; the
common description of Chutes as a Bittensor subnet comes from outside this
pass and is **unverified here**.

## Property matrix

| Property | Current value | Source |
|---|---|---|
| Isolation | Intel TDX + NVIDIA CC | Chutes post |
| E2EE | Optional, eligible instances only | Chutes post |
| Image policy | cosign-signed images only | Chutes post |

## Comparison axes

| Axis | Class | Detail | Source |
|---|---|---|---|
| Correctness | ATTESTATION | Validators check a hardware-signed TDX quote and NVIDIA GPU attestation against a known-good configuration | Chutes post, grounded |
| Trust rests on | HARDWARE VENDOR | Intel TDX and NVIDIA confidential computing; only cosign-signed images admitted | Chutes post, grounded |
| Confidentiality | HARDWARE ENCLAVE | TEE serving mode; optional client-side E2EE on eligible instances, not the default | Chutes post, grounded |
| Lineage | NONE FOUND | No paper cited; the link to Intel SGX Explained is inferred from the shared TEE-attestation mechanism | Chutes post, inferred link |
| Maturity | LIVE | TEE serving mode announced 2026-05-07 on a running inference platform | Chutes post, grounded |
| On-chain | NOT COVERED | Commonly described as a Bittensor subnet; unverified in this pass | Not addressed in this file's sources |

## Known limitations

- E2EE is not the default for all inference.
- Narrower runtime paths and more complexity than standard inference.
- The post itself says "We do not present TEEs as a silver bullet" and
  notes TEEs still need software validation and auditability.

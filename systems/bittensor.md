---
name: Bittensor
field: Decentralized incentive / consensus mechanisms for ML networks
last_updated: 2026-10-20
confidence: grounded
---

# Bittensor

## What it does

Bittensor is a decentralized network in which independent operators ("miners")
run machine-learning models and are paid in the TAO token based on how
useful their outputs are judged to be by other network participants
("validators"). Instead of a central benchmark deciding what's useful, peers
rank each other, and rewards flow from that peer-ranking.

## Architecture summary

- **Subtensor**: the layer-0 blockchain (built on Polkadot Substrate) that
  records peer identity, stake, and the consensus/incentive state.
- **Subnets**: independently defined competitions, each specifying its own
  task (e.g. text generation, image generation) and its own validator
  scoring logic. As of 2026 the network has scaled to roughly 64-128 active
  subnets (sources disagree on the exact figure at time of writing; mainnet
  slot cap is 128, with an expansion to 256 planned). [[FalconX: State of
  Bittensor]](https://www.falconx.io/newsroom/state-of-bittensor-subnet-adoption-trends-network-mechanics-and-covenants-departure)
- **Dynamic TAO (dTAO)**: deployed to mainnet ~Feb 13, 2025. Replaced a
  single global emission pool with per-subnet "alpha" tokens and AMM pools,
  letting TAO holders stake directly into specific subnets rather than the
  network as a whole. [[CryptoBriefing]](https://cryptobriefing.com/bittensor-dynamic-tao-emission-model/)
- **Yuma Consensus (YC)**: the mechanism that turns validator rankings into
  miner payouts (see below).

## Built on (foundational lineage)

**Shapley (1952), "A Value for n-Person Games"** — explicitly cited in
Bittensor's own academic paper, *"Incentivizing Intelligence: The Bittensor
Approach"* (Steeves, Shaabana, Hu, Luus, Liu, Tasker-Steeves et al.), hosted
at [bittensor.com/academia](https://www.bittensor.com/academia), as the
theoretical basis for the peer-ranking mechanism: Shapley values are used to
fairly attribute each peer's contribution to the network's informational
output across permutations of participants.

The whitepaper (*"Bittensor: A Peer-to-Peer Intelligence Market,"* Yuma Rao,
[bittensor.com/whitepaper](https://www.bittensor.com/whitepaper)) separately
cites Fisher Information pruning (LeCun et al. 1989; Yu et al. 2017) as the
theoretical ideal behind how peer-significance weights are ranked, and cites
a cluster of standard deep-learning papers (Hinton et al. 2015 on
distillation/general intelligence, Devlin et al. 2019, Radford et al. 2019,
Shazeer et al. 2017) as background for why peer-to-peer intelligence markets
are plausible — these are context, not the mechanism's core theoretical
grounding.

**Note on naming**: the official academic paper describes the
Shapley-value-based ranking and trust-weighted consensus mechanism but does
not use the name "Yuma Consensus" anywhere in that document. "Yuma
Consensus" as a named, specific algorithm (stake-weighted median + outlier
clipping) appears in community/ecosystem documentation and later working
papers rather than in the cited academic source itself — flagged here as a
naming gap between the academic grounding and the term actually used in
practice.

## Property matrix

| Property | Current value | Source |
|---|---|---|
| Consensus/incentive mechanism | Yuma Consensus — stake-weighted median of validator rankings with outlier clipping; rewards require >50% stake-trust to avoid exponential penalty | [hoge.gg explainer](https://hoge.gg/yuma-consensus-2026-how-bittensor-decides-who-gets-paid/) (community source, not primary) |
| Theoretical basis for ranking | Shapley value attribution | [bittensor.com/academia](https://www.bittensor.com/academia) |
| Base chain | Subtensor (Polkadot Substrate) | docs.bittensor.com |
| Tokenomics model | Dynamic TAO — per-subnet alpha tokens + AMM pools, live since Feb 2025 | [CryptoBriefing](https://cryptobriefing.com/bittensor-dynamic-tao-emission-model/) |
| Subnet count | ~64-128 active, cap 128 (256 planned) | [FalconX](https://www.falconx.io/newsroom/state-of-bittensor-subnet-adoption-trends-network-mechanics-and-covenants-departure) |
| Maturity | Mainnet live, first emission halving Dec 2025 (7200 → 3600 TAO/day) | search aggregation, not independently verified against chain data |
| Collusion assumption | Honest nodes assumed to hold >50% of stake | bittensor.com/whitepaper |

## Known limitations

- **Weight copying**: validators can copy other validators' submitted
  weights to earn rewards without doing the underlying evaluation work,
  free-riding on honest validators. Acknowledged as a known issue — a
  working paper titled *"Weight Copying in Bittensor"* (Opentensor, May
  2024) exists specifically addressing it, though the document's full
  content could not be retrieved directly for this entry (link redirected
  to a generic docs page: https://docs.learnbittensor.org/papers/BT_Weight_Copier-29May2024.pdf).
  Flagged as inferred-exists, content-unverified.
- **Governance centralization tension**: validator/stake concentration has
  drawn scrutiny over how decentralized the network actually is in
  practice. [Yellow.com research](https://yellow.com/research/bittensor-decentralized-ai-market-control-2026)
  raises this; not independently verified here.
- **Naming/documentation gap**: as noted above, the specific "Yuma
  Consensus" algorithm described in secondary sources isn't the same
  document as the academic paper citing Shapley values — the primary
  academic source and the commonly-cited mechanism name don't fully line up,
  which makes precise grounding harder than for the other tracked systems.

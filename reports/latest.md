# Solana Ecosystem Pulse

_Generated 2026-10-04T21:33:36Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 4,243.2 / 1,724.9 |
| Recent slot time | 265.5 ms |
| Epoch progress | 48.7% |
| Active / delinquent validators | 671 / 15 |
| Delinquent stake | 0.027% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | $121.44 (1.55%) |
| DeFi TVL | $6.73B |
| Stablecoin supply | $16.53B |
| DEX volume, 24h | $1.55B |

## Anomalies

- **WARNING: dex_volume_24h_usd:** dex_volume_24h_usd is unusually below its recent baseline. (robust z=-3.60, median=2.57e+09, n=48)
- **INFO: dex_volume_change_24h_pct:** DEX volume changed at least 35% day over day. (fixed threshold)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,935,562 SOL | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,927,649 SOL | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,346,574 SOL | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,305,935 SOL | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,136,537 SOL | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,254,655 SOL | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,241,331 SOL | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,616,097 SOL | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,061,519 SOL | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3cMHJRjJMUk9yVZtmYTYeFrXf` | 6,686,111 SOL | 0% |

## Ecosystem updates

### Official Solana news

- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) (Fri, 02 Oct 2026 19:30:00 GMT)
- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) (Wed, 30 Sep 2026 19:17:00 GMT)
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) (Mon, 28 Sep 2026 15:00:00 GMT)
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) (Thu, 24 Sep 2026 13:20:00 GMT)
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) (Wed, 23 Sep 2026 14:06:00 GMT)
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) (Sat, 19 Sep 2026 11:28:00 GMT)

### Agave releases

- [Release v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) (2026-10-03T06:50:48Z)
- [Release v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) (2026-09-28T15:10:04Z)
- [Release v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) (2026-09-18T15:32:23Z)
- [Release v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) (2026-09-18T12:15:17Z)
- [Release v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) (2026-09-11T14:39:49Z)

## Source health

| Source | Status | Latency | Checked |
|---|---|---:|---|
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | ok | 522 ms | 2026-10-04T21:33:28Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | ok | 275 ms | 2026-10-04T21:33:28Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 219 ms | 2026-10-04T21:33:28Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 247 ms | 2026-10-04T21:33:28Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 222 ms | 2026-10-04T21:33:28Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | ok | 360 ms | 2026-10-04T21:33:28Z |
| [solana_news](https://solana.com/rss.xml) | ok | 322 ms | 2026-10-04T21:33:28Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 8064 ms | 2026-10-04T21:33:28Z |

## Coverage and interpretation

Included:

- network performance and epoch state
- validator delinquency and stake concentration
- SOL price and market capitalization
- DeFi TVL, stablecoin supply, and DEX volume
- official Solana news, Agave releases, and SIMD repository updates

Not yet included (reported explicitly instead of approximated):

- Dune dashboards requiring credentials or fragile scraping
- X/Twitter sentiment requiring an API key
- daily active addresses and tokenized-equity volume without a stable keyless API
- median transaction fees until a bounded direct-RPC sampler is added

> Public RPC and free market-data endpoints can rate-limit or disagree. This report preserves source-level health and never replaces a missing metric with fabricated data. It is operational telemetry, not financial advice.

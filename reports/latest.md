# Solana Ecosystem Pulse

_Generated 2026-11-24T22:31:00Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 1,526.2 / 1,526.2 |
| Recent slot time | 216.6 ms |
| Epoch progress | 9.4% |
| Active / delinquent validators | 660 / 27 |
| Delinquent stake | 0.019% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | $69.63 (-3.49%) |
| DeFi TVL | $4.54B |
| Stablecoin supply | $13.14B |
| DEX volume, 24h | $1.81B |

## Anomalies

- **WARNING: source.solana_news:** solana_news failed; output is partial. (HTTPError: HTTP Error 429: Too Many Requests)
- **INFO: dex_volume_change_24h_pct:** DEX volume changed at least 35% day over day. (fixed threshold)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,003,542 SOL | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 15,962,658 SOL | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,418,812 SOL | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,242,949 SOL | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,885,209 SOL | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,615,268 SOL | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,283,847 SOL | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,016,085 SOL | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,968,432 SOL | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,779,378 SOL | 5% |

## Ecosystem updates

### Official Solana news


### Agave releases

- [Release v5.0.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) (2026-11-19T20:57:32Z)
- [Release v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) (2026-11-06T08:17:22Z)
- [Release v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) (2026-11-05T18:33:50Z)
- [Release v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) (2026-10-28T20:35:10Z)
- [Release v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) (2026-10-26T20:06:18Z)

## Source health

| Source | Status | Latency | Checked |
|---|---|---:|---|
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | ok | 532 ms | 2026-11-24T22:30:54Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | ok | 125 ms | 2026-11-24T22:30:54Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 533 ms | 2026-11-24T22:30:54Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 555 ms | 2026-11-24T22:30:54Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 284 ms | 2026-11-24T22:30:54Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | ok | 389 ms | 2026-11-24T22:30:54Z |
| [solana_news](https://solana.com/rss.xml) | error | 148 ms | 2026-11-24T22:30:54Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 5595 ms | 2026-11-24T22:30:54Z |

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

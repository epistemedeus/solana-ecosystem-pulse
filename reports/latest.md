# Solana Ecosystem Pulse

_Generated 2026-11-23T23:58:35Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 1,634.1 / 1,634.1 |
| Recent slot time | 212.0 ms |
| Epoch progress | 22.0% |
| Active / delinquent validators | 660 / 26 |
| Delinquent stake | 0.036% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | $72.00 (2.03%) |
| DeFi TVL | $4.68B |
| Stablecoin supply | $13.60B |
| DEX volume, 24h | $975.74M |

## Anomalies

- **WARNING: source.solana_news:** solana_news failed; output is partial. (HTTPError: HTTP Error 429: Too Many Requests)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 17,028,046 SOL | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,091,420 SOL | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,412,158 SOL | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,240,508 SOL | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,856,366 SOL | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,634,022 SOL | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,276,354 SOL | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 8,005,660 SOL | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,776 SOL | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,778,434 SOL | 5% |

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
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | ok | 419 ms | 2026-11-23T23:58:29Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | ok | 132 ms | 2026-11-23T23:58:29Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 231 ms | 2026-11-23T23:58:29Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 1094 ms | 2026-11-23T23:58:29Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 210 ms | 2026-11-23T23:58:29Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | ok | 288 ms | 2026-11-23T23:58:29Z |
| [solana_news](https://solana.com/rss.xml) | error | 176 ms | 2026-11-23T23:58:29Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 5570 ms | 2026-11-23T23:58:29Z |

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

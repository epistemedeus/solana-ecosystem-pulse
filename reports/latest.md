# Solana Ecosystem Pulse

_Generated 2026-11-08T22:12:21Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 2,403.5 / 2,403.5 |
| Recent slot time | 218.2 ms |
| Epoch progress | 20.0% |
| Active / delinquent validators | 661 / 36 |
| Delinquent stake | 0.144% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | $86.37 (-3.03%) |
| DeFi TVL | $5.22B |
| Stablecoin supply | $14.77B |
| DEX volume, 24h | $917.44M |

## Anomalies

- **WARNING: source.solana_news:** solana_news failed; output is partial. (HTTPError: HTTP Error 429: Too Many Requests)
- **INFO: dex_volume_change_24h_pct:** DEX volume changed at least 35% day over day. (fixed threshold)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,050,553 SOL | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,720,131 SOL | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 13,021,912 SOL | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,279,070 SOL | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,553,388 SOL | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,550,278 SOL | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,222,876 SOL | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,775,137 SOL | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,980,319 SOL | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,711,284 SOL | 5% |

## Ecosystem updates

### Official Solana news


### Agave releases

- [Release v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) (2026-11-06T08:17:22Z)
- [Release v4.4.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.1) (2026-11-05T18:33:50Z)
- [Release v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) (2026-10-28T20:35:10Z)
- [Release v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) (2026-10-26T20:06:18Z)
- [Release v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) (2026-10-26T21:15:55Z)

## Source health

| Source | Status | Latency | Checked |
|---|---|---:|---|
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | ok | 454 ms | 2026-11-08T22:12:15Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | ok | 213 ms | 2026-11-08T22:12:15Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 202 ms | 2026-11-08T22:12:15Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 174 ms | 2026-11-08T22:12:15Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 403 ms | 2026-11-08T22:12:15Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | ok | 316 ms | 2026-11-08T22:12:15Z |
| [solana_news](https://solana.com/rss.xml) | error | 186 ms | 2026-11-08T22:12:15Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 5719 ms | 2026-11-08T22:12:15Z |

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

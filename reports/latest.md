# Solana Ecosystem Pulse

_Generated 2026-11-16T22:13:00Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 2,628.1 / 2,628.1 |
| Recent slot time | 214.3 ms |
| Epoch progress | 64.5% |
| Active / delinquent validators | 662 / 37 |
| Delinquent stake | 0.035% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | $72.08 (-0.16%) |
| DeFi TVL | $4.73B |
| Stablecoin supply | $13.94B |
| DEX volume, 24h | $1.35B |

## Anomalies

- **WARNING: source.solana_news:** solana_news failed; output is partial. (HTTPError: HTTP Error 429: Too Many Requests)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,936,855 SOL | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,432,361 SOL | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,486,687 SOL | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,142,842 SOL | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,787,748 SOL | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,620,150 SOL | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,212,350 SOL | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,959,108 SOL | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,992,227 SOL | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,709,566 SOL | 5% |

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
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | ok | 510 ms | 2026-11-16T22:12:54Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | ok | 200 ms | 2026-11-16T22:12:54Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 100 ms | 2026-11-16T22:12:54Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 122 ms | 2026-11-16T22:12:54Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 283 ms | 2026-11-16T22:12:54Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | ok | 376 ms | 2026-11-16T22:12:54Z |
| [solana_news](https://solana.com/rss.xml) | error | 163 ms | 2026-11-16T22:12:54Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 5581 ms | 2026-11-16T22:12:54Z |

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

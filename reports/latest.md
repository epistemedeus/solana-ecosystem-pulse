# Solana Ecosystem Pulse

_Generated 2026-10-29T13:10:38Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 1,690.9 / 1,690.9 |
| Recent slot time | 212.0 ms |
| Epoch progress | 51.1% |
| Active / delinquent validators | 663 / 26 |
| Delinquent stake | 0.857% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | $100.53 (-0.83%) |
| DeFi TVL | $5.65B |
| Stablecoin supply | $15.35B |
| DEX volume, 24h | $1.73B |

## Anomalies

- **WARNING: delinquent_stake_pct:** delinquent_stake_pct is unusually above its recent baseline. (robust z=12.11, median=0.0491, n=48)
- **WARNING: source.solana_news:** solana_news failed; output is partial. (HTTPError: HTTP Error 429: Too Many Requests)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,028,574 SOL | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,665,444 SOL | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,878,826 SOL | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,762,073 SOL | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,705,356 SOL | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,466,646 SOL | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,218,110 SOL | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,761,555 SOL | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,998,037 SOL | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,646,428 SOL | 5% |

## Ecosystem updates

### Official Solana news


### Agave releases

- [Release v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) (2026-10-28T20:35:10Z)
- [Release v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) (2026-10-26T20:06:18Z)
- [Release v4.4.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.1) (2026-10-26T21:15:55Z)
- [Release v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) (2026-10-15T22:20:41Z)
- [Release v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) (2026-10-13T06:35:48Z)

## Source health

| Source | Status | Latency | Checked |
|---|---|---:|---|
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | ok | 420 ms | 2026-10-29T13:10:31Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | ok | 141 ms | 2026-10-29T13:10:31Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 156 ms | 2026-10-29T13:10:31Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 572 ms | 2026-10-29T13:10:31Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 238 ms | 2026-10-29T13:10:31Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | ok | 305 ms | 2026-10-29T13:10:31Z |
| [solana_news](https://solana.com/rss.xml) | error | 108 ms | 2026-10-29T13:10:31Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 6968 ms | 2026-10-29T13:10:31Z |

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

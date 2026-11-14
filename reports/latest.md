# Solana Ecosystem Pulse

_Generated 2026-11-14T22:30:25Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 2,162.1 / 2,162.1 |
| Recent slot time | 216.6 ms |
| Epoch progress | 79.6% |
| Active / delinquent validators | 663 / 36 |
| Delinquent stake | 0.092% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | $69.68 (-11.22%) |
| DeFi TVL | $4.72B |
| Stablecoin supply | $13.80B |
| DEX volume, 24h | $1.56B |

## Anomalies

- **WARNING: sol_price_change_24h_pct:** SOL moved at least 10% over 24 hours. (fixed threshold)
- **WARNING: sol_price_usd:** sol_price_usd is unusually below its recent baseline. (robust z=-3.53, median=93.07, n=48)
- **WARNING: source.agave_releases:** agave_releases failed; output is partial. (HTTPError: HTTP Error 403: rate limit exceeded)
- **WARNING: source.simd_updates:** simd_updates failed; output is partial. (HTTPError: HTTP Error 403: rate limit exceeded)
- **WARNING: source.solana_news:** solana_news failed; output is partial. (HTTPError: HTTP Error 429: Too Many Requests)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,955,905 SOL | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,374,909 SOL | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,611,498 SOL | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,140,468 SOL | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,736,890 SOL | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,574,439 SOL | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,199,377 SOL | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,914,792 SOL | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,990,062 SOL | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,707,745 SOL | 5% |

## Ecosystem updates

### Official Solana news


### Agave releases


## Source health

| Source | Status | Latency | Checked |
|---|---|---:|---|
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | error | 31 ms | 2026-11-14T22:30:19Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | ok | 48 ms | 2026-11-14T22:30:19Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 154 ms | 2026-11-14T22:30:19Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 160 ms | 2026-11-14T22:30:19Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 157 ms | 2026-11-14T22:30:19Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | error | 20 ms | 2026-11-14T22:30:19Z |
| [solana_news](https://solana.com/rss.xml) | error | 83 ms | 2026-11-14T22:30:19Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 6607 ms | 2026-11-14T22:30:19Z |

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

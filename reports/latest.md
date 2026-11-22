# Solana Ecosystem Pulse

_Generated 2026-11-22T19:46:08Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 2,864.9 / 2,864.9 |
| Recent slot time | 215.8 ms |
| Epoch progress | 12.7% |
| Active / delinquent validators | 662 / 23 |
| Delinquent stake | 0.012% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | $70.22 (-0.61%) |
| DeFi TVL | $4.64B |
| Stablecoin supply | $13.04B |
| DEX volume, 24h | $1.35B |

## Anomalies

- **WARNING: source.agave_releases:** agave_releases failed; output is partial. (HTTPError: HTTP Error 403: rate limit exceeded)
- **WARNING: source.simd_updates:** simd_updates failed; output is partial. (HTTPError: HTTP Error 403: rate limit exceeded)
- **WARNING: source.solana_news:** solana_news failed; output is partial. (HTTPError: HTTP Error 429: Too Many Requests)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,918,440 SOL | 0% |
| 2 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,346,959 SOL | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,401,889 SOL | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,243,005 SOL | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,842,253 SOL | 10% |
| 6 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,612,896 SOL | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,269,555 SOL | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,998,895 SOL | 7% |
| 9 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,987,495 SOL | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,775,083 SOL | 5% |

## Ecosystem updates

### Official Solana news


### Agave releases


## Source health

| Source | Status | Latency | Checked |
|---|---|---:|---|
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | error | 84 ms | 2026-11-22T19:46:01Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | ok | 110 ms | 2026-11-22T19:46:01Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 111 ms | 2026-11-22T19:46:01Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 826 ms | 2026-11-22T19:46:01Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 113 ms | 2026-11-22T19:46:01Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | error | 83 ms | 2026-11-22T19:46:01Z |
| [solana_news](https://solana.com/rss.xml) | error | 107 ms | 2026-11-22T19:46:01Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 6416 ms | 2026-11-22T19:46:01Z |

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

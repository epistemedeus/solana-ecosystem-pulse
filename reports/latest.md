# Solana Ecosystem Pulse

_Generated 2026-08-26T07:11:15Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 3,092.2 / 1,213.0 |
| Recent slot time | 363.6 ms |
| Epoch progress | 71.9% |
| Active / delinquent validators | 685 / 10 |
| Delinquent stake | 0.044% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | $96.83 (-4.59%) |
| DeFi TVL | $5.60B |
| Stablecoin supply | $15.88B |
| DEX volume, 24h | $2.95B |

## Anomalies

- **WARNING: slot_time_ms:** slot_time_ms is unusually below its recent baseline. (robust z=-3.62, median=409.6, n=48)
- **WARNING: source.agave_releases:** agave_releases failed; output is partial. (HTTPError: HTTP Error 403: rate limit exceeded)
- **WARNING: source.simd_updates:** simd_updates failed; output is partial. (HTTPError: HTTP Error 403: rate limit exceeded)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,066,966 SOL | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,035,907 SOL | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,268,330 SOL | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,739,871 SOL | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,202,562 SOL | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,924,729 SOL | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,579,462 SOL | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,953,722 SOL | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,300,009 SOL | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,574,676 SOL | 0% |

## Ecosystem updates

### Official Solana news

- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) (Mon, 24 Aug 2026 14:19:00 GMT)
- [Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic) (Wed, 19 Aug 2026 10:00:00 GMT)
- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) (Mon, 17 Aug 2026 00:00:00 GMT)
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) (Thu, 13 Aug 2026 15:03:00 GMT)
- [How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi) (Thu, 13 Aug 2026 02:06:00 GMT)
- [Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap) (Wed, 12 Aug 2026 12:57:00 GMT)

### Agave releases


## Source health

| Source | Status | Latency | Checked |
|---|---|---:|---|
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | error | 104 ms | 2026-08-26T07:11:07Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | ok | 217 ms | 2026-08-26T07:11:07Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 154 ms | 2026-08-26T07:11:07Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 1135 ms | 2026-08-26T07:11:07Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 286 ms | 2026-08-26T07:11:07Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | error | 103 ms | 2026-08-26T07:11:07Z |
| [solana_news](https://solana.com/rss.xml) | ok | 344 ms | 2026-08-26T07:11:07Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 7981 ms | 2026-08-26T07:11:07Z |

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

# Solana Ecosystem Pulse

_Generated 2026-08-23T02:01:49Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 3,934.4 / 2,065.8 |
| Recent slot time | 365.9 ms |
| Epoch progress | 96.0% |
| Active / delinquent validators | 687 / 8 |
| Delinquent stake | 0.014% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | $96.00 (2.40%) |
| DeFi TVL | $5.50B |
| Stablecoin supply | $15.82B |
| DEX volume, 24h | $3.65B |

## Anomalies

- **WARNING: defi_tvl_usd:** defi_tvl_usd is unusually above its recent baseline. (robust z=13.80, median=4.843e+09, n=48)
- **WARNING: dex_volume_24h_usd:** dex_volume_24h_usd is unusually above its recent baseline. (robust z=5.17, median=1.668e+09, n=48)
- **WARNING: slot_time_ms:** slot_time_ms is unusually below its recent baseline. (robust z=-7.60, median=413.8, n=48)
- **WARNING: sol_price_usd:** sol_price_usd is unusually above its recent baseline. (robust z=19.13, median=76, n=48)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,066,372 SOL | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,054,078 SOL | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,175,413 SOL | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,782,032 SOL | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,178,661 SOL | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,917,577 SOL | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,402,660 SOL | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,964,352 SOL | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,357,821 SOL | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,547,243 SOL | 0% |

## Ecosystem updates

### Official Solana news

- [Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic) (Wed, 19 Aug 2026 10:00:00 GMT)
- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) (Mon, 17 Aug 2026 00:00:00 GMT)
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) (Thu, 13 Aug 2026 15:03:00 GMT)
- [How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi) (Thu, 13 Aug 2026 02:06:00 GMT)
- [Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap) (Wed, 12 Aug 2026 12:57:00 GMT)
- [MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps) (Tue, 11 Aug 2026 10:00:00 GMT)

### Agave releases

- [Release v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) (2026-08-21T14:34:51Z)
- [Release v4.3.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) (2026-08-21T12:47:32Z)
- [Release v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) (2026-08-13T18:49:41Z)
- [Release v4.3.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.0) (2026-08-14T18:34:44Z)
- [Release v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) (2026-08-07T20:29:04Z)

## Source health

| Source | Status | Latency | Checked |
|---|---|---:|---|
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | ok | 3233 ms | 2026-08-23T02:01:41Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | ok | 180 ms | 2026-08-23T02:01:41Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 158 ms | 2026-08-23T02:01:41Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 179 ms | 2026-08-23T02:01:41Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 315 ms | 2026-08-23T02:01:41Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | ok | 5530 ms | 2026-08-23T02:01:41Z |
| [solana_news](https://solana.com/rss.xml) | ok | 195 ms | 2026-08-23T02:01:41Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 7658 ms | 2026-08-23T02:01:41Z |

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

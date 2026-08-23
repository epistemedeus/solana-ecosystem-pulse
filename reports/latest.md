# Solana Ecosystem Pulse

_Generated 2026-08-23T13:04:35Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 3,447.0 / 1,576.3 |
| Recent slot time | 361.4 ms |
| Epoch progress | 21.2% |
| Active / delinquent validators | 681 / 14 |
| Delinquent stake | 1.006% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | $94.61 (1.09%) |
| DeFi TVL | $5.54B |
| Stablecoin supply | $15.83B |
| DEX volume, 24h | $3.73B |

## Anomalies

- **WARNING: defi_tvl_usd:** defi_tvl_usd is unusually above its recent baseline. (robust z=11.83, median=4.846e+09, n=48)
- **WARNING: delinquent_stake_pct:** More than 1% of observed stake is delinquent. (fixed threshold)
- **WARNING: delinquent_stake_pct:** delinquent_stake_pct is unusually above its recent baseline. (robust z=80.11, median=0.0199, n=48)
- **WARNING: dex_volume_24h_usd:** dex_volume_24h_usd is unusually above its recent baseline. (robust z=4.94, median=1.705e+09, n=48)
- **WARNING: slot_time_ms:** slot_time_ms is unusually below its recent baseline. (robust z=-8.00, median=412.4, n=48)
- **WARNING: sol_price_usd:** sol_price_usd is unusually above its recent baseline. (robust z=15.41, median=76.11, n=48)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 16,984,006 SOL | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,032,941 SOL | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,211,671 SOL | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,728,738 SOL | 5% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,165,202 SOL | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,876,408 SOL | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,480,578 SOL | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,930,731 SOL | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,359,446 SOL | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,568,551 SOL | 0% |

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
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | ok | 354 ms | 2026-08-23T13:04:27Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | ok | 151 ms | 2026-08-23T13:04:27Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 94 ms | 2026-08-23T13:04:27Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 108 ms | 2026-08-23T13:04:27Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 302 ms | 2026-08-23T13:04:27Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | ok | 299 ms | 2026-08-23T13:04:27Z |
| [solana_news](https://solana.com/rss.xml) | ok | 321 ms | 2026-08-23T13:04:27Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 7754 ms | 2026-08-23T13:04:27Z |

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

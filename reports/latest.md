# Solana Ecosystem Pulse

_Generated 2026-08-20T07:09:02Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 2,965.4 / 1,310.6 |
| Recent slot time | 411.0 ms |
| Epoch progress | 50.6% |
| Active / delinquent validators | 688 / 8 |
| Delinquent stake | 0.023% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | $85.91 (11.71%) |
| DeFi TVL | $5.20B |
| Stablecoin supply | $15.76B |
| DEX volume, 24h | $2.79B |

## Anomalies

- **WARNING: defi_tvl_usd:** defi_tvl_usd is unusually above its recent baseline. (robust z=13.84, median=4.826e+09, n=48)
- **WARNING: dex_volume_24h_usd:** dex_volume_24h_usd is unusually above its recent baseline. (robust z=4.62, median=1.564e+09, n=48)
- **WARNING: sol_price_change_24h_pct:** SOL moved at least 10% over 24 hours. (fixed threshold)
- **WARNING: sol_price_usd:** sol_price_usd is unusually above its recent baseline. (robust z=12.59, median=75.93, n=48)
- **INFO: dex_volume_change_24h_pct:** DEX volume changed at least 35% day over day. (fixed threshold)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,101,527 SOL | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,011,570 SOL | 0% |
| 3 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 12,410,378 SOL | 5% |
| 4 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,198,972 SOL | 0% |
| 5 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,188,631 SOL | 7% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 8,991,290 SOL | 10% |
| 7 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 8,308,413 SOL | 0% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,991,430 SOL | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,344,654 SOL | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,546,146 SOL | 0% |

## Ecosystem updates

### Official Solana news

- [Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic) (Wed, 19 Aug 2026 10:00:00 GMT)
- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) (Mon, 17 Aug 2026 00:00:00 GMT)
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) (Thu, 13 Aug 2026 15:03:00 GMT)
- [How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi) (Thu, 13 Aug 2026 02:06:00 GMT)
- [Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap) (Wed, 12 Aug 2026 12:57:00 GMT)
- [MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps) (Tue, 11 Aug 2026 10:00:00 GMT)

### Agave releases

- [Release v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) (2026-08-13T18:49:41Z)
- [Release v4.3.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.0) (2026-08-14T18:34:44Z)
- [Release v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) (2026-08-07T20:29:04Z)
- [Release v4.3.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.3) (2026-08-05T19:35:39Z)
- [Release v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1) (2026-07-31T15:02:44Z)

## Source health

| Source | Status | Latency | Checked |
|---|---|---:|---|
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | ok | 457 ms | 2026-08-20T07:08:54Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | ok | 177 ms | 2026-08-20T07:08:54Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 227 ms | 2026-08-20T07:08:54Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 1006 ms | 2026-08-20T07:08:54Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 336 ms | 2026-08-20T07:08:54Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | ok | 420 ms | 2026-08-20T07:08:54Z |
| [solana_news](https://solana.com/rss.xml) | ok | 344 ms | 2026-08-20T07:08:54Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 7493 ms | 2026-08-20T07:08:54Z |

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

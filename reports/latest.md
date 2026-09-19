# Solana Ecosystem Pulse

_Generated 2026-09-19T11:06:27Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 3,788.4 / 1,210.9 |
| Recent slot time | 259.7 ms |
| Epoch progress | 93.8% |
| Active / delinquent validators | 677 / 11 |
| Delinquent stake | 0.036% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | $111.88 (5.80%) |
| DeFi TVL | $6.26B |
| Stablecoin supply | $15.49B |
| DEX volume, 24h | $3.54B |

## Anomalies

- **WARNING: defi_tvl_usd:** defi_tvl_usd is unusually above its recent baseline. (robust z=6.43, median=5.877e+09, n=48)
- **WARNING: slot_time_ms:** slot_time_ms is unusually below its recent baseline. (robust z=-11.37, median=315.8, n=48)
- **WARNING: sol_price_usd:** sol_price_usd is unusually above its recent baseline. (robust z=3.71, median=101.7, n=47)
- **INFO: dex_volume_change_24h_pct:** DEX volume changed at least 35% day over day. (fixed threshold)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,815,472 SOL | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,816,148 SOL | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,510,308 SOL | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,398,202 SOL | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,784,908 SOL | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,254,526 SOL | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,077,527 SOL | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,397,869 SOL | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,085,578 SOL | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,557,940 SOL | 0% |

## Ecosystem updates

### Official Solana news

- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) (Wed, 16 Sep 2026 00:56:00 GMT)
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) (Mon, 14 Sep 2026 11:00:00 GMT)
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) (Thu, 10 Sep 2026 20:16:00 GMT)
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026) (Thu, 10 Sep 2026 20:16:00 GMT)
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) (Tue, 08 Sep 2026 13:14:00 GMT)
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) (Mon, 07 Sep 2026 07:00:00 GMT)

### Agave releases

- [Release v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) (2026-09-18T15:32:23Z)
- [Release v4.3.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0) (2026-09-18T12:15:17Z)
- [Release v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) (2026-09-11T14:39:49Z)
- [Release v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) (2026-09-10T19:19:58Z)
- [Release v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) (2026-09-04T15:46:13Z)

## Source health

| Source | Status | Latency | Checked |
|---|---|---:|---|
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | ok | 473 ms | 2026-09-19T11:06:21Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | ok | 218 ms | 2026-09-19T11:06:21Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 285 ms | 2026-09-19T11:06:21Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 1017 ms | 2026-09-19T11:06:21Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 319 ms | 2026-09-19T11:06:21Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | ok | 354 ms | 2026-09-19T11:06:21Z |
| [solana_news](https://solana.com/rss.xml) | ok | 299 ms | 2026-09-19T11:06:21Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 5940 ms | 2026-09-19T11:06:21Z |

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

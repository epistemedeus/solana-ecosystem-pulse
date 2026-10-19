# Solana Ecosystem Pulse

_Generated 2026-10-19T13:27:32Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 4,626.4 / 1,682.9 |
| Recent slot time | 222.2 ms |
| Epoch progress | 15.2% |
| Active / delinquent validators | 666 / 13 |
| Delinquent stake | 0.366% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | $105.29 (2.07%) |
| DeFi TVL | $5.90B |
| Stablecoin supply | $15.45B |
| DEX volume, 24h | $1.70B |

## Anomalies

- **WARNING: delinquent_stake_pct:** delinquent_stake_pct is unusually above its recent baseline. (robust z=41.00, median=0.0073, n=48)
- **INFO: dex_volume_change_24h_pct:** DEX volume changed at least 35% day over day. (fixed threshold)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,095,415 SOL | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,730,365 SOL | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,524,168 SOL | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 10,975,836 SOL | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 9,717,890 SOL | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,481,609 SOL | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,252,107 SOL | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,785,119 SOL | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,993,888 SOL | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,731,556 SOL | 0% |

## Ecosystem updates

### Official Solana news

- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) (Wed, 14 Oct 2026 15:05:00 GMT)
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) (Mon, 12 Oct 2026 04:41:00 GMT)
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) (Fri, 09 Oct 2026 12:46:00 GMT)
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) (Thu, 08 Oct 2026 18:18:00 GMT)
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026) (Thu, 08 Oct 2026 08:33:00 GMT)
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet) (Wed, 07 Oct 2026 23:30:00 GMT)

### Agave releases

- [Release v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) (2026-10-15T22:20:41Z)
- [Release v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) (2026-10-13T06:35:48Z)
- [Release v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) (2026-10-08T20:27:41Z)
- [Release v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) (2026-10-03T06:50:48Z)
- [Release v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) (2026-09-28T15:10:04Z)

## Source health

| Source | Status | Latency | Checked |
|---|---|---:|---|
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | ok | 349 ms | 2026-10-19T13:27:24Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | ok | 209 ms | 2026-10-19T13:27:24Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 253 ms | 2026-10-19T13:27:24Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 280 ms | 2026-10-19T13:27:24Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 182 ms | 2026-10-19T13:27:24Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | ok | 299 ms | 2026-10-19T13:27:24Z |
| [solana_news](https://solana.com/rss.xml) | ok | 195 ms | 2026-10-19T13:27:24Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 7789 ms | 2026-10-19T13:27:24Z |

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

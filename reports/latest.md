# Solana Ecosystem Pulse

_Generated 2026-08-30T21:11:08Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 3,766.1 / 1,637.2 |
| Recent slot time | 317.5 ms |
| Epoch progress | 41.2% |
| Active / delinquent validators | 680 / 17 |
| Delinquent stake | 0.005% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | $103.99 (-1.16%) |
| DeFi TVL | $5.94B |
| Stablecoin supply | $15.77B |
| DEX volume, 24h | $1.67B |

## Anomalies

- **WARNING: slot_time_ms:** slot_time_ms is unusually below its recent baseline. (robust z=-3.75, median=365.9, n=48)
- **INFO: dex_volume_change_24h_pct:** DEX volume changed at least 35% day over day. (fixed threshold)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,203,741 SOL | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 16,085,807 SOL | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,389,824 SOL | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,479,512 SOL | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,452,658 SOL | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,293,056 SOL | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,023,631 SOL | 10% |
| 8 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,295,972 SOL | 5% |
| 9 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,201,762 SOL | 7% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,589,845 SOL | 0% |

## Ecosystem updates

### Official Solana news

- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) (Thu, 27 Aug 2026 04:15:00 GMT)
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) (Mon, 24 Aug 2026 14:19:00 GMT)
- [Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic) (Wed, 19 Aug 2026 10:00:00 GMT)
- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) (Mon, 17 Aug 2026 00:00:00 GMT)
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) (Thu, 13 Aug 2026 15:03:00 GMT)
- [How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi) (Thu, 13 Aug 2026 02:06:00 GMT)

### Agave releases

- [Release v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) (2026-08-28T06:07:28Z)
- [Release v4.3.0-beta.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.3) (2026-08-28T18:53:56Z)
- [Release v4.2.2](https://github.com/anza-xyz/agave/releases/tag/v4.2.2) (2026-08-28T18:47:41Z)
- [Release v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) (2026-08-21T14:34:51Z)
- [Release v4.3.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.1) (2026-08-21T12:47:32Z)

## Source health

| Source | Status | Latency | Checked |
|---|---|---:|---|
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | ok | 409 ms | 2026-08-30T21:11:01Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | ok | 204 ms | 2026-08-30T21:11:01Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 218 ms | 2026-08-30T21:11:01Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 1039 ms | 2026-08-30T21:11:01Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 254 ms | 2026-08-30T21:11:01Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | ok | 371 ms | 2026-08-30T21:11:01Z |
| [solana_news](https://solana.com/rss.xml) | ok | 393 ms | 2026-08-30T21:11:01Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 6275 ms | 2026-08-30T21:11:01Z |

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

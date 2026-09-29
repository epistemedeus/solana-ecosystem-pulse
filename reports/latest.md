# Solana Ecosystem Pulse

_Generated 2026-09-29T12:59:57Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 4,051.9 / 1,528.3 |
| Recent slot time | 264.3 ms |
| Epoch progress | 48.4% |
| Active / delinquent validators | 670 / 12 |
| Delinquent stake | 0.108% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | n/a (n/a%) |
| DeFi TVL | $6.51B |
| Stablecoin supply | $16.11B |
| DEX volume, 24h | $2.66B |

## Anomalies

- **WARNING: source.agave_releases:** agave_releases failed; output is partial. (HTTPError: HTTP Error 403: rate limit exceeded)
- **WARNING: source.coingecko:** coingecko failed; output is partial. (HTTPError: HTTP Error 403: Forbidden)
- **WARNING: source.simd_updates:** simd_updates failed; output is partial. (HTTPError: HTTP Error 403: rate limit exceeded)
- **INFO: dex_volume_change_24h_pct:** DEX volume changed at least 35% day over day. (fixed threshold)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,824,525 SOL | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,886,038 SOL | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,338,577 SOL | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 11,300,554 SOL | 0% |
| 5 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,209,855 SOL | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,243,744 SOL | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,224,466 SOL | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,637,468 SOL | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 6,700,083 SOL | 5% |
| 10 | `DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a` | 6,518,407 SOL | 0% |

## Ecosystem updates

### Official Solana news

- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) (Mon, 28 Sep 2026 15:00:00 GMT)
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) (Thu, 24 Sep 2026 13:20:00 GMT)
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) (Wed, 23 Sep 2026 14:06:00 GMT)
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) (Sat, 19 Sep 2026 11:28:00 GMT)
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) (Sat, 19 Sep 2026 10:00:00 GMT)
- [Breakpoint 2026: A guide to getting oriented (Part 1)](https://solana.com/news/breakpoint-guide-part1) (Fri, 18 Sep 2026 10:00:00 GMT)

### Agave releases


## Source health

| Source | Status | Latency | Checked |
|---|---|---:|---|
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | error | 155 ms | 2026-09-29T12:59:51Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | error | 119 ms | 2026-09-29T12:59:51Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 311 ms | 2026-09-29T12:59:51Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 1195 ms | 2026-09-29T12:59:51Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 267 ms | 2026-09-29T12:59:51Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | error | 135 ms | 2026-09-29T12:59:51Z |
| [solana_news](https://solana.com/rss.xml) | ok | 257 ms | 2026-09-29T12:59:51Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 5758 ms | 2026-09-29T12:59:51Z |

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

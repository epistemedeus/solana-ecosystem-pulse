# Solana Ecosystem Pulse

_Generated 2026-09-20T11:31:07Z · schema `solana.ecosystem.pulse.v1` · status **watch**_

## Executive snapshot

| Metric | Value |
|---|---:|
| Network health | ok |
| Recent TPS / non-vote TPS | 3,731.4 / 1,173.8 |
| Recent slot time | 264.3 ms |
| Epoch progress | 70.1% |
| Active / delinquent validators | 678 / 12 |
| Delinquent stake | 0.007% |
| Nakamoto coefficient (33%) | 18 |
| SOL price (24h) | $108.11 (-3.33%) |
| DeFi TVL | $6.12B |
| Stablecoin supply | $16.45B |
| DEX volume, 24h | $2.88B |

## Anomalies

- **WARNING: defi_tvl_usd:** defi_tvl_usd is unusually above its recent baseline. (robust z=3.89, median=5.877e+09, n=48)
- **WARNING: slot_time_ms:** slot_time_ms is unusually below its recent baseline. (robust z=-7.07, median=315.8, n=48)
- **WARNING: source.agave_releases:** agave_releases failed; output is partial. (HTTPError: HTTP Error 403: rate limit exceeded)
- **WARNING: source.simd_updates:** simd_updates failed; output is partial. (HTTPError: HTTP Error 403: rate limit exceeded)

## Validator concentration

| Rank | Vote account | Stake | Commission |
|---:|---|---:|---:|
| 1 | `CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1` | 17,849,776 SOL | 7% |
| 2 | `he1iusunGwqrNtafDtLdhsUQDFvo13z9sUa36PauBtk` | 15,819,247 SOL | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5GNHyqc89KduzMP7423eWiD5g` | 12,500,805 SOL | 0% |
| 4 | `CatzoSMUkTRidT5DwBxAC2pEtnwMBTpkCepHkFgZDiqb` | 11,362,749 SOL | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxbHXMrjyQx2aKkoBR5H1GJF8iD` | 9,786,807 SOL | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4td8tdoUFPTng8Fb8gPyc53dJx` | 9,252,843 SOL | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKgp4WoZerQcSqWC7BitBzgUNAm` | 9,116,740 SOL | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2FpczXjpK3VYrvRudywSZaM29mF` | 7,434,776 SOL | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJnX5SYH4hCfQ9VuGnqrKaKwycB` | 7,086,871 SOL | 5% |
| 10 | `HZKopZYvv8v6un2H6KUNVQCnK5zM9emKKezvqhTBSpEc` | 6,627,951 SOL | 100% |

## Ecosystem updates

### Official Solana news

- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) (Sat, 19 Sep 2026 11:28:00 GMT)
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) (Sat, 19 Sep 2026 10:00:00 GMT)
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) (Wed, 16 Sep 2026 00:56:00 GMT)
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) (Mon, 14 Sep 2026 11:00:00 GMT)
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) (Thu, 10 Sep 2026 20:16:00 GMT)
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026) (Thu, 10 Sep 2026 20:16:00 GMT)

### Agave releases


## Source health

| Source | Status | Latency | Checked |
|---|---|---:|---|
| [agave_releases](https://api.github.com/repos/anza-xyz/agave/releases?per_page=5) | error | 122 ms | 2026-09-20T11:31:01Z |
| [coingecko](https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true) | ok | 153 ms | 2026-09-20T11:31:01Z |
| [defillama_chains](https://api.llama.fi/v2/chains) | ok | 152 ms | 2026-09-20T11:31:01Z |
| [defillama_dex](https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume) | ok | 160 ms | 2026-09-20T11:31:01Z |
| [defillama_stables](https://stablecoins.llama.fi/stablecoinchains) | ok | 310 ms | 2026-09-20T11:31:01Z |
| [simd_updates](https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5) | error | 110 ms | 2026-09-20T11:31:01Z |
| [solana_news](https://solana.com/rss.xml) | ok | 177 ms | 2026-09-20T11:31:01Z |
| [solana_rpc](https://api.mainnet-beta.solana.com) | ok | 6249 ms | 2026-09-20T11:31:01Z |

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

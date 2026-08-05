# Solana Ecosystem Pulse

A keyless, automatically updating view of Solana's network health, validator set, economic activity, ecosystem updates, and anomaly signals.

**Live dashboard:** [epistemedeus.github.io/solana-ecosystem-pulse/dashboard/](https://epistemedeus.github.io/solana-ecosystem-pulse/dashboard/)  
**Current machine-readable report:** [`data/latest.json`](./data/latest.json)  
**Current human-readable report:** [`reports/latest.md`](./reports/latest.md)

## Why this is useful

Most ecosystem dashboards either depend on a vendor key, hide source failures, or mix metrics with incompatible definitions. Pulse makes a smaller but stronger promise:

- every default data source is public and needs no credential;
- one failed off-chain source produces a partial report, not fabricated replacement data;
- source health and collection latency are first-class output;
- raw JSON, Markdown, and an interactive dark-theme dashboard are generated together;
- anomalies combine explicit safety thresholds with a robust median/MAD baseline built from prior refreshes;
- all output is reproducible with Python's standard library.

## Coverage

| Area | Metrics / updates | Source |
|---|---|---|
| Network | health, finalized slot, block height, epoch progress, TPS, non-vote TPS, slot time, transaction count, core version | [Solana JSON-RPC](https://solana.com/docs/rpc) |
| Validators | active/delinquent count, delinquent stake, top-10 concentration, 33% Nakamoto coefficient, top validators and commission | `getVoteAccounts` |
| Supply | circulating and total SOL | `getSupply` |
| Economy | SOL price/change/market cap | [CoinGecko public API](https://www.coingecko.com/en/api) |
| DeFi | chain TVL and 24h/7d/30d DEX volume | [DefiLlama API](https://defillama.com/docs/api) |
| Stablecoins | USD-pegged circulating supply on Solana | DefiLlama stablecoin API |
| News | latest official posts | [Solana RSS](https://solana.com/rss.xml) |
| Upgrades | Agave releases and recent SIMD repository changes | GitHub public API |

The report explicitly marks four requested areas as not yet covered rather than guessing: Dune dashboards that require credentials or fragile scraping, X sentiment that requires an API key, daily active addresses/tokenized-equity volume without a stable keyless endpoint, and median fees until a bounded direct-RPC sampler is added.

## Run locally

Requirements: Python 3.10+ and internet access. There is no install step.

```bash
python3 pulse.py
python3 -m unittest -v
python3 -m http.server 8000
```

Open `http://localhost:8000/dashboard/`.

To use a different public or private RPC:

```bash
SOLANA_RPC_URL=https://your-rpc.example python3 pulse.py
```

Generated files are written atomically:

```text
data/latest.json       full structured snapshot + source health + chart history
data/history.jsonl     compact rolling baseline (180 refreshes)
reports/latest.md      human-readable report
dashboard/index.html   self-contained interactive dashboard
```

## Automation strategy

`.github/workflows/update.yml` runs every six hours and on manual dispatch. It:

1. collects all sources concurrently;
2. validates the snapshot and runs the test suite;
3. commits only changed generated artifacts;
4. deploys the repository as a static GitHub Pages site.

The workflow needs no repository secrets. `contents: write`, `pages: write`, and `id-token: write` are scoped to the workflow itself.

Six hours is deliberately conservative: public RPCs and no-key APIs have shared rate limits, while ecosystem-health decisions rarely benefit from noisy minute-level polling. The CLI supports more frequent execution when the operator supplies a dedicated RPC.

## Anomaly detection

Rules currently flag:

- RPC health not `ok`;
- recent slot time above 600 ms (warning) or 800 ms (critical);
- delinquent stake above 1% (warning) or 5% (critical);
- absolute SOL 24h move of at least 10%;
- absolute DEX volume day-over-day change of at least 35%.

After eight stored samples, each core numeric metric also receives a robust z-score against the most recent 48 snapshots:

```text
robust_z = 0.6745 × (current − median) / MAD
```

An absolute robust z-score of 3.5 or more is flagged. Median absolute deviation is used instead of mean/standard deviation so a real incident does not immediately erase its own baseline.

## Metric interpretation

- RPC `numTransactions` includes vote transactions; Pulse reports both total and non-vote TPS.
- The 33% Nakamoto coefficient is calculated from current activated stake: the smallest number of validators whose cumulative active stake reaches one third.
- `stablecoin_supply_usd` currently includes USD-pegged circulation only, not conversion of EUR/JPY/other pegs.
- DeFiLlama and CoinGecko can revise methodology or rate-limit no-key requests. Their source rows expose the outcome of every refresh.
- Public RPC is suitable for a reproducible demo, not a latency SLA.

This is operational telemetry, not financial advice.

## Originality

The collector, normalization schema, robust anomaly engine, report renderer, and dashboard are original code written for this project. No SolPulse or other dashboard code was copied.

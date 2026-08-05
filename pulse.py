#!/usr/bin/env python3
"""Solana Ecosystem Pulse: keyless collection, anomaly detection, and reports.

Uses only the Python standard library. All default sources are public and need
no API key. Outputs are written atomically so a failed refresh cannot corrupt
the last known-good dashboard.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import html
import json
import math
import os
import statistics
import sys
import tempfile
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Callable


SCHEMA_VERSION = "solana.ecosystem.pulse.v1"
DEFAULT_RPC = "https://api.mainnet-beta.solana.com"
USER_AGENT = "solana-ecosystem-pulse/1.0 (+https://github.com/epistemedeus/solana-ecosystem-pulse)"
LAMPORTS_PER_SOL = 1_000_000_000

SOURCES = {
    "defillama_chains": "https://api.llama.fi/v2/chains",
    "defillama_stables": "https://stablecoins.llama.fi/stablecoinchains",
    "defillama_dex": (
        "https://api.llama.fi/overview/dexs/Solana"
        "?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume"
    ),
    "coingecko": (
        "https://api.coingecko.com/api/v3/simple/price"
        "?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true"
    ),
    "solana_news": "https://solana.com/rss.xml",
    "agave_releases": "https://api.github.com/repos/anza-xyz/agave/releases?per_page=5",
    "simd_updates": (
        "https://api.github.com/repos/solana-foundation/solana-improvement-documents/commits?per_page=5"
    ),
}


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def iso_time(value: dt.datetime | None = None) -> str:
    return (value or utc_now()).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def http_bytes(url: str, *, data: bytes | None = None, timeout: float = 25.0) -> bytes:
    headers = {
        "Accept": "application/json, application/rss+xml, application/xml;q=0.9, */*;q=0.5",
        "Content-Type": "application/json",
        "User-Agent": USER_AGENT,
    }
    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read()


def http_json(url: str, *, data: bytes | None = None, timeout: float = 25.0) -> Any:
    return json.loads(http_bytes(url, data=data, timeout=timeout))


def run_source(name: str, url: str, loader: Callable[[], Any]) -> tuple[str, Any, dict[str, Any]]:
    started = time.perf_counter()
    checked_at = iso_time()
    try:
        payload = loader()
        source = {
            "name": name,
            "url": url,
            "status": "ok",
            "checked_at": checked_at,
            "latency_ms": round((time.perf_counter() - started) * 1000),
            "error": None,
        }
        return name, payload, source
    except Exception as exc:  # Preserve partial output when one public source is degraded.
        source = {
            "name": name,
            "url": url,
            "status": "error",
            "checked_at": checked_at,
            "latency_ms": round((time.perf_counter() - started) * 1000),
            "error": f"{type(exc).__name__}: {str(exc)[:240]}",
        }
        return name, None, source


def rpc_payload() -> bytes:
    calls = [
        ("health", "getHealth", []),
        ("slot", "getSlot", [{"commitment": "finalized"}]),
        ("block_height", "getBlockHeight", [{"commitment": "finalized"}]),
        ("epoch", "getEpochInfo", [{"commitment": "finalized"}]),
        ("performance", "getRecentPerformanceSamples", [60]),
        ("votes", "getVoteAccounts", [{"commitment": "finalized"}]),
        ("supply", "getSupply", [{"commitment": "finalized"}]),
        ("transaction_count", "getTransactionCount", [{"commitment": "finalized"}]),
        ("version", "getVersion", []),
    ]
    return json.dumps(
        [
            {"jsonrpc": "2.0", "id": call_id, "method": method, "params": params}
            for call_id, method, params in calls
        ],
        separators=(",", ":"),
    ).encode()


def load_rpc(rpc_url: str) -> dict[str, Any]:
    raw = http_json(rpc_url, data=rpc_payload(), timeout=35)
    if not isinstance(raw, list):
        raise ValueError("RPC batch response was not a list")
    results: dict[str, Any] = {}
    errors: dict[str, Any] = {}
    for item in raw:
        call_id = str(item.get("id"))
        if "error" in item:
            errors[call_id] = item["error"]
        else:
            results[call_id] = item.get("result")
    required = {"health", "slot", "epoch", "performance", "votes", "supply"}
    missing = sorted(required.difference(results))
    if missing:
        raise ValueError(f"RPC response missing required calls: {', '.join(missing)}; errors={errors}")
    results["partial_errors"] = errors
    return results


def load_rss() -> list[dict[str, str]]:
    root = ET.fromstring(http_bytes(SOURCES["solana_news"]))
    items: list[dict[str, str]] = []
    for item in root.findall("./channel/item")[:8]:
        items.append(
            {
                "title": (item.findtext("title") or "Untitled").strip(),
                "url": (item.findtext("link") or "").strip(),
                "published_at": (item.findtext("pubDate") or "").strip(),
            }
        )
    return items


def fetch_all(rpc_url: str) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    specs: list[tuple[str, str, Callable[[], Any]]] = [
        ("solana_rpc", rpc_url, lambda: load_rpc(rpc_url)),
        ("defillama_chains", SOURCES["defillama_chains"], lambda: http_json(SOURCES["defillama_chains"])),
        (
            "defillama_stables",
            SOURCES["defillama_stables"],
            lambda: http_json(SOURCES["defillama_stables"]),
        ),
        ("defillama_dex", SOURCES["defillama_dex"], lambda: http_json(SOURCES["defillama_dex"])),
        ("coingecko", SOURCES["coingecko"], lambda: http_json(SOURCES["coingecko"])),
        ("solana_news", SOURCES["solana_news"], load_rss),
        (
            "agave_releases",
            SOURCES["agave_releases"],
            lambda: http_json(SOURCES["agave_releases"]),
        ),
        ("simd_updates", SOURCES["simd_updates"], lambda: http_json(SOURCES["simd_updates"])),
    ]
    data: dict[str, Any] = {}
    source_rows: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(specs)) as executor:
        futures = [executor.submit(run_source, *spec) for spec in specs]
        for future in concurrent.futures.as_completed(futures):
            name, payload, source = future.result()
            data[name] = payload
            source_rows.append(source)
    source_rows.sort(key=lambda row: row["name"])
    return data, source_rows


def as_float(value: Any, default: float | None = None) -> float | None:
    try:
        number = float(value)
        return number if math.isfinite(number) else default
    except (TypeError, ValueError):
        return default


def find_named(rows: Any, name: str) -> dict[str, Any]:
    if not isinstance(rows, list):
        return {}
    return next((row for row in rows if isinstance(row, dict) and row.get("name") == name), {})


def validator_metrics(votes: dict[str, Any]) -> dict[str, Any]:
    current = list(votes.get("current") or [])
    delinquent = list(votes.get("delinquent") or [])
    all_validators = current + delinquent
    active_stake = sum(int(v.get("activatedStake") or 0) for v in current)
    delinquent_stake = sum(int(v.get("activatedStake") or 0) for v in delinquent)
    total_stake = active_stake + delinquent_stake
    ordered = sorted(current, key=lambda row: int(row.get("activatedStake") or 0), reverse=True)
    threshold = active_stake / 3 if active_stake else 0
    running = 0
    nakamoto = 0
    for validator in ordered:
        running += int(validator.get("activatedStake") or 0)
        nakamoto += 1
        if running >= threshold:
            break
    top = [
        {
            "vote_account": v.get("votePubkey"),
            "node_identity": v.get("nodePubkey"),
            "stake_sol": round(int(v.get("activatedStake") or 0) / LAMPORTS_PER_SOL, 2),
            "commission_pct": v.get("commission"),
        }
        for v in ordered[:10]
    ]
    top10_stake = sum(int(v.get("activatedStake") or 0) for v in ordered[:10])
    return {
        "active_count": len(current),
        "delinquent_count": len(delinquent),
        "active_stake_sol": round(active_stake / LAMPORTS_PER_SOL, 2),
        "delinquent_stake_sol": round(delinquent_stake / LAMPORTS_PER_SOL, 2),
        "delinquent_stake_pct": round(delinquent_stake / total_stake * 100, 4) if total_stake else None,
        "top_10_stake_pct": round(top10_stake / active_stake * 100, 2) if active_stake else None,
        "nakamoto_33_coefficient": nakamoto or None,
        "top_validators": top,
    }


def performance_metrics(samples: list[dict[str, Any]]) -> dict[str, Any]:
    normalized = [sample for sample in samples if (sample.get("samplePeriodSecs") or 0) > 0]
    if not normalized:
        return {}
    recent = normalized[0]

    def sample_tps(sample: dict[str, Any], key: str = "numTransactions") -> float:
        return float(sample.get(key) or 0) / float(sample.get("samplePeriodSecs") or 1)

    recent_tps = sample_tps(recent)
    recent_non_vote = sample_tps(recent, "numNonVoteTransactions")
    weighted_seconds = sum(float(s.get("samplePeriodSecs") or 0) for s in normalized)
    weighted_txs = sum(float(s.get("numTransactions") or 0) for s in normalized)
    weighted_non_vote = sum(float(s.get("numNonVoteTransactions") or 0) for s in normalized)
    slot_time_ms = (
        float(recent.get("samplePeriodSecs") or 0) / float(recent.get("numSlots") or 1) * 1000
    )
    return {
        "tps_recent": round(recent_tps, 2),
        "non_vote_tps_recent": round(recent_non_vote, 2),
        "tps_rolling": round(weighted_txs / weighted_seconds, 2) if weighted_seconds else None,
        "non_vote_tps_rolling": round(weighted_non_vote / weighted_seconds, 2) if weighted_seconds else None,
        "slot_time_ms_recent": round(slot_time_ms, 2),
        "sample_count": len(normalized),
        "sample_window_seconds": round(weighted_seconds),
    }


def normalize_snapshot(raw: dict[str, Any], sources: list[dict[str, Any]]) -> dict[str, Any]:
    rpc = raw.get("solana_rpc") or {}
    epoch = rpc.get("epoch") or {}
    perf = performance_metrics(rpc.get("performance") or [])
    validators = validator_metrics(rpc.get("votes") or {})
    supply = ((rpc.get("supply") or {}).get("value") or {})
    chain = find_named(raw.get("defillama_chains"), "Solana")
    stables = find_named(raw.get("defillama_stables"), "Solana")
    stable_by_currency = stables.get("totalCirculatingUSD") or {}
    dex = raw.get("defillama_dex") or {}
    coin = (raw.get("coingecko") or {}).get("solana") or {}

    epoch_slots = int(epoch.get("slotsInEpoch") or 0)
    epoch_index = int(epoch.get("slotIndex") or 0)
    network = {
        "health": rpc.get("health"),
        "slot": rpc.get("slot"),
        "block_height": rpc.get("block_height") or epoch.get("blockHeight"),
        "transaction_count": rpc.get("transaction_count") or epoch.get("transactionCount"),
        "epoch": epoch.get("epoch"),
        "epoch_progress_pct": round(epoch_index / epoch_slots * 100, 2) if epoch_slots else None,
        "epoch_slot_index": epoch_index,
        "epoch_slots": epoch_slots,
        "solana_core_version": (rpc.get("version") or {}).get("solana-core"),
        **perf,
    }
    economy = {
        "sol_price_usd": as_float(coin.get("usd")),
        "sol_price_change_24h_pct": as_float(coin.get("usd_24h_change")),
        "sol_market_cap_usd": as_float(coin.get("usd_market_cap")),
        "defi_tvl_usd": as_float(chain.get("tvl")),
        "stablecoin_supply_usd": as_float(stable_by_currency.get("peggedUSD")),
        "dex_volume_24h_usd": as_float(dex.get("total24h")),
        "dex_volume_7d_usd": as_float(dex.get("total7d")),
        "dex_volume_30d_usd": as_float(dex.get("total30d")),
        "dex_volume_change_24h_pct": as_float(dex.get("change_1d")),
        "circulating_supply_sol": round(float(supply.get("circulating") or 0) / LAMPORTS_PER_SOL, 2),
        "total_supply_sol": round(float(supply.get("total") or 0) / LAMPORTS_PER_SOL, 2),
    }
    releases = [
        {
            "name": item.get("name") or item.get("tag_name"),
            "tag": item.get("tag_name"),
            "published_at": item.get("published_at"),
            "url": item.get("html_url"),
            "prerelease": bool(item.get("prerelease")),
        }
        for item in (raw.get("agave_releases") or [])[:5]
    ]
    simd_updates = [
        {
            "sha": str(item.get("sha") or "")[:12],
            "message": (((item.get("commit") or {}).get("message") or "").splitlines() or [""])[0],
            "updated_at": ((item.get("commit") or {}).get("author") or {}).get("date"),
            "url": item.get("html_url"),
        }
        for item in (raw.get("simd_updates") or [])[:5]
    ]
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": iso_time(),
        "status": "healthy" if rpc.get("health") == "ok" else "degraded",
        "network": network,
        "validators": validators,
        "economy": economy,
        "ecosystem": {
            "news": (raw.get("solana_news") or [])[:6],
            "agave_releases": releases,
            "simd_updates": simd_updates,
        },
        "coverage": {
            "included": [
                "network performance and epoch state",
                "validator delinquency and stake concentration",
                "SOL price and market capitalization",
                "DeFi TVL, stablecoin supply, and DEX volume",
                "official Solana news, Agave releases, and SIMD repository updates",
            ],
            "not_included": [
                "Dune dashboards requiring credentials or fragile scraping",
                "X/Twitter sentiment requiring an API key",
                "daily active addresses and tokenized-equity volume without a stable keyless API",
                "median transaction fees until a bounded direct-RPC sampler is added",
            ],
        },
        "sources": sources,
        "anomalies": [],
        "history": [],
    }


def metric_values(snapshot: dict[str, Any]) -> dict[str, float]:
    paths = {
        "tps": ("network", "tps_recent"),
        "non_vote_tps": ("network", "non_vote_tps_recent"),
        "slot_time_ms": ("network", "slot_time_ms_recent"),
        "delinquent_stake_pct": ("validators", "delinquent_stake_pct"),
        "defi_tvl_usd": ("economy", "defi_tvl_usd"),
        "stablecoin_supply_usd": ("economy", "stablecoin_supply_usd"),
        "dex_volume_24h_usd": ("economy", "dex_volume_24h_usd"),
        "sol_price_usd": ("economy", "sol_price_usd"),
    }
    result: dict[str, float] = {}
    for name, path in paths.items():
        value = as_float(snapshot.get(path[0], {}).get(path[1]))
        if value is not None:
            result[name] = value
    return result


def read_history(path: Path, limit: int = 180) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            row = json.loads(line)
            if isinstance(row, dict) and isinstance(row.get("metrics"), dict):
                rows.append(row)
        except json.JSONDecodeError:
            continue
    return rows[-limit:]


def robust_z(current: float, historic: list[float]) -> tuple[float | None, float | None]:
    if len(historic) < 8:
        return None, None
    median = statistics.median(historic)
    deviations = [abs(value - median) for value in historic]
    mad = statistics.median(deviations)
    if mad == 0:
        return None, median
    return 0.6745 * (current - median) / mad, median


def detect_anomalies(snapshot: dict[str, Any], history: list[dict[str, Any]]) -> list[dict[str, Any]]:
    anomalies: list[dict[str, Any]] = []

    def add(severity: str, metric: str, value: Any, message: str, basis: str) -> None:
        anomalies.append(
            {"severity": severity, "metric": metric, "value": value, "message": message, "basis": basis}
        )

    network = snapshot["network"]
    validators = snapshot["validators"]
    economy = snapshot["economy"]
    if network.get("health") != "ok":
        add("critical", "network.health", network.get("health"), "RPC health is not OK.", "direct RPC")
    slot_time = as_float(network.get("slot_time_ms_recent"))
    if slot_time is not None and slot_time > 800:
        add("critical", "slot_time_ms", slot_time, "Recent slot time is above 800 ms.", "fixed threshold")
    elif slot_time is not None and slot_time > 600:
        add("warning", "slot_time_ms", slot_time, "Recent slot time is above 600 ms.", "fixed threshold")
    delinquent = as_float(validators.get("delinquent_stake_pct"))
    if delinquent is not None and delinquent > 5:
        add("critical", "delinquent_stake_pct", delinquent, "More than 5% of observed stake is delinquent.", "fixed threshold")
    elif delinquent is not None and delinquent > 1:
        add("warning", "delinquent_stake_pct", delinquent, "More than 1% of observed stake is delinquent.", "fixed threshold")
    price_change = as_float(economy.get("sol_price_change_24h_pct"))
    if price_change is not None and abs(price_change) >= 10:
        add("warning", "sol_price_change_24h_pct", price_change, "SOL moved at least 10% over 24 hours.", "fixed threshold")
    dex_change = as_float(economy.get("dex_volume_change_24h_pct"))
    if dex_change is not None and abs(dex_change) >= 35:
        add("info", "dex_volume_change_24h_pct", dex_change, "DEX volume changed at least 35% day over day.", "fixed threshold")

    current_metrics = metric_values(snapshot)
    for metric, current in current_metrics.items():
        historic = [
            float(row["metrics"][metric])
            for row in history[-48:]
            if metric in row.get("metrics", {}) and as_float(row["metrics"][metric]) is not None
        ]
        score, median = robust_z(current, historic)
        if score is not None and abs(score) >= 3.5:
            direction = "above" if score > 0 else "below"
            add(
                "warning",
                metric,
                round(current, 4),
                f"{metric} is unusually {direction} its recent baseline.",
                f"robust z={score:.2f}, median={median:.4g}, n={len(historic)}",
            )
    for source in snapshot["sources"]:
        if source["status"] != "ok":
            add("warning", f"source.{source['name']}", None, f"{source['name']} failed; output is partial.", source.get("error") or "source error")
    order = {"critical": 0, "warning": 1, "info": 2}
    anomalies.sort(key=lambda item: (order.get(item["severity"], 9), item["metric"]))
    return anomalies


def compact_history(history: list[dict[str, Any]], current: dict[str, Any]) -> list[dict[str, Any]]:
    rows = history[-47:] + [{"generated_at": current["generated_at"], "metrics": metric_values(current)}]
    return rows


def append_history(path: Path, row: dict[str, Any], retain: int = 180) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    history = read_history(path, limit=retain - 1)
    history.append(row)
    atomic_write(path, "\n".join(json.dumps(item, separators=(",", ":"), sort_keys=True) for item in history) + "\n")


def fmt_number(value: Any, digits: int = 0) -> str:
    number = as_float(value)
    if number is None:
        return "n/a"
    return f"{number:,.{digits}f}"


def fmt_usd(value: Any) -> str:
    number = as_float(value)
    if number is None:
        return "n/a"
    for threshold, suffix in ((1e12, "T"), (1e9, "B"), (1e6, "M"), (1e3, "K")):
        if abs(number) >= threshold:
            return f"${number / threshold:,.2f}{suffix}"
    return f"${number:,.2f}"


def markdown_report(snapshot: dict[str, Any]) -> str:
    n = snapshot["network"]
    v = snapshot["validators"]
    e = snapshot["economy"]
    anomalies = snapshot["anomalies"]
    lines = [
        "# Solana Ecosystem Pulse",
        "",
        f"_Generated {snapshot['generated_at']} · schema `{snapshot['schema_version']}` · status **{snapshot['status']}**_",
        "",
        "## Executive snapshot",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Network health | {n.get('health') or 'n/a'} |",
        f"| Recent TPS / non-vote TPS | {fmt_number(n.get('tps_recent'), 1)} / {fmt_number(n.get('non_vote_tps_recent'), 1)} |",
        f"| Recent slot time | {fmt_number(n.get('slot_time_ms_recent'), 1)} ms |",
        f"| Epoch progress | {fmt_number(n.get('epoch_progress_pct'), 1)}% |",
        f"| Active / delinquent validators | {fmt_number(v.get('active_count'))} / {fmt_number(v.get('delinquent_count'))} |",
        f"| Delinquent stake | {fmt_number(v.get('delinquent_stake_pct'), 3)}% |",
        f"| Nakamoto coefficient (33%) | {fmt_number(v.get('nakamoto_33_coefficient'))} |",
        f"| SOL price (24h) | {fmt_usd(e.get('sol_price_usd'))} ({fmt_number(e.get('sol_price_change_24h_pct'), 2)}%) |",
        f"| DeFi TVL | {fmt_usd(e.get('defi_tvl_usd'))} |",
        f"| Stablecoin supply | {fmt_usd(e.get('stablecoin_supply_usd'))} |",
        f"| DEX volume, 24h | {fmt_usd(e.get('dex_volume_24h_usd'))} |",
        "",
        "## Anomalies",
        "",
    ]
    if anomalies:
        lines.extend(
            f"- **{item['severity'].upper()}: {item['metric']}:** {item['message']} ({item['basis']})"
            for item in anomalies
        )
    else:
        lines.append("- No rule-based or robust-baseline anomalies detected with available data.")
    lines.extend(["", "## Validator concentration", "", "| Rank | Vote account | Stake | Commission |", "|---:|---|---:|---:|"])
    for index, validator in enumerate(v.get("top_validators") or [], start=1):
        vote = validator.get("vote_account") or "n/a"
        lines.append(f"| {index} | `{vote}` | {fmt_number(validator.get('stake_sol'), 0)} SOL | {fmt_number(validator.get('commission_pct'), 0)}% |")
    lines.extend(["", "## Ecosystem updates", "", "### Official Solana news", ""])
    for item in snapshot["ecosystem"]["news"]:
        lines.append(f"- [{item['title']}]({item['url']}) ({item['published_at']})")
    lines.extend(["", "### Agave releases", ""])
    for item in snapshot["ecosystem"]["agave_releases"]:
        lines.append(f"- [{item['name']}]({item['url']}) ({item['published_at']})")
    lines.extend(["", "## Source health", "", "| Source | Status | Latency | Checked |", "|---|---|---:|---|"])
    for source in snapshot["sources"]:
        lines.append(f"| [{source['name']}]({source['url']}) | {source['status']} | {source['latency_ms']} ms | {source['checked_at']} |")
    lines.extend(
        [
            "",
            "## Coverage and interpretation",
            "",
            "Included:",
            "",
            *[f"- {item}" for item in snapshot["coverage"]["included"]],
            "",
            "Not yet included (reported explicitly instead of approximated):",
            "",
            *[f"- {item}" for item in snapshot["coverage"]["not_included"]],
            "",
            "> Public RPC and free market-data endpoints can rate-limit or disagree. This report preserves source-level health and never replaces a missing metric with fabricated data. It is operational telemetry, not financial advice.",
            "",
        ]
    )
    return "\n".join(lines)


def dashboard_html(snapshot: dict[str, Any]) -> str:
    data_json = json.dumps(snapshot, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="A keyless, automatically updating Solana network and ecosystem dashboard.">
<title>Solana Ecosystem Pulse</title>
<style>
:root{{--bg:#060912;--panel:#0d1220;--panel2:#11182a;--text:#f5f7fb;--muted:#8f9bb3;--line:#222c42;--green:#14f195;--cyan:#42d9ff;--violet:#8b5cf6;--red:#ff5d73;--amber:#ffbd59}}
*{{box-sizing:border-box}} body{{margin:0;background:radial-gradient(circle at 82% -10%,#20204b 0,transparent 34%),radial-gradient(circle at -10% 40%,#063d37 0,transparent 30%),var(--bg);color:var(--text);font:15px/1.5 Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;min-height:100vh}}
a{{color:var(--cyan);text-decoration:none}} a:hover{{text-decoration:underline}} .wrap{{max-width:1240px;margin:auto;padding:38px 24px 70px}} header{{display:flex;justify-content:space-between;gap:24px;align-items:flex-start;margin-bottom:28px}} .eyebrow{{font:700 11px ui-monospace,SFMono-Regular,monospace;letter-spacing:.18em;color:var(--green);text-transform:uppercase}} h1{{font-size:clamp(35px,6vw,66px);line-height:.98;letter-spacing:-.055em;margin:10px 0 14px}} .sub{{max-width:700px;color:var(--muted);font-size:17px}} .stamp{{background:#0d1220cc;border:1px solid var(--line);border-radius:18px;padding:14px 16px;min-width:230px}} .badge{{display:inline-flex;gap:8px;align-items:center;font-weight:750;text-transform:uppercase;font-size:11px;letter-spacing:.1em}} .dot{{width:8px;height:8px;border-radius:50%;background:var(--green);box-shadow:0 0 15px var(--green)}} .muted{{color:var(--muted)}} .grid{{display:grid;grid-template-columns:repeat(12,1fr);gap:14px}} .card{{grid-column:span 3;background:linear-gradient(145deg,#11182ae8,#0b101de8);border:1px solid var(--line);border-radius:22px;padding:20px;min-height:145px;box-shadow:0 14px 44px #0004}} .wide{{grid-column:span 6}} .full{{grid-column:1/-1}} .label{{font:700 11px ui-monospace,SFMono-Regular,monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}} .value{{font-size:31px;font-weight:780;letter-spacing:-.04em;margin:9px 0 4px}} .detail{{font-size:13px;color:var(--muted)}} .accent{{height:3px;border-radius:5px;background:linear-gradient(90deg,var(--green),var(--cyan),var(--violet));margin-top:16px}} h2{{font-size:22px;margin:42px 0 14px;letter-spacing:-.025em}} .alert{{padding:14px 16px;border:1px solid var(--line);border-left:3px solid var(--amber);border-radius:12px;margin:9px 0;background:#151421}} .alert.critical{{border-left-color:var(--red)}} .alert.info{{border-left-color:var(--cyan)}} .alert strong{{font-size:13px;text-transform:uppercase;letter-spacing:.08em}} table{{width:100%;border-collapse:collapse}} th,td{{padding:12px 10px;text-align:left;border-bottom:1px solid var(--line)}} th{{font:700 11px ui-monospace,SFMono-Regular,monospace;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}} td{{font-size:13px}} code{{color:#cbd4e8}} .bar{{height:7px;background:#202941;border-radius:8px;overflow:hidden;margin-top:12px}} .bar>i{{height:100%;display:block;background:linear-gradient(90deg,var(--green),var(--cyan));border-radius:inherit}} .spark{{width:100%;height:76px;margin-top:10px;overflow:visible}} .updates{{display:grid;grid-template-columns:1fr 1fr;gap:14px}} .update{{padding:13px 0;border-bottom:1px solid var(--line)}} .update:last-child{{border:0}} .source-ok{{color:var(--green)}} .source-error{{color:var(--red)}} footer{{margin-top:44px;padding-top:18px;border-top:1px solid var(--line);display:flex;justify-content:space-between;gap:20px;color:var(--muted);font-size:12px}}
@media(max-width:900px){{.card{{grid-column:span 6}}.wide{{grid-column:1/-1}}header{{display:block}}.stamp{{margin-top:18px}}}} @media(max-width:560px){{.wrap{{padding:24px 14px 50px}}.card{{grid-column:1/-1}}.updates{{grid-template-columns:1fr}}footer{{display:block}}}}
</style>
</head>
<body><main class="wrap">
<header><div><div class="eyebrow">Keyless · verifiable · auto-updating</div><h1>Solana<br>Ecosystem Pulse</h1><div class="sub">Network health, validator concentration, economic activity, upgrades and anomaly signals, collected from direct RPC and public sources without credentials.</div></div><div class="stamp"><div class="badge"><span class="dot"></span><span id="status"></span></div><div class="detail" style="margin-top:8px">Last refresh<br><strong id="generated"></strong></div></div></header>
<section class="grid" id="metrics"></section>
<h2>Signal desk</h2><section id="alerts"></section>
<section class="grid" style="margin-top:14px"><article class="card wide"><div class="label">TPS · recent samples</div><div id="tpsChart"></div></article><article class="card wide"><div class="label">DeFi TVL · recent snapshots</div><div id="tvlChart"></div></article></section>
<h2>Validator set</h2><section class="grid"><article class="card wide"><div class="label">Epoch progress</div><div class="value" id="epoch"></div><div class="bar"><i id="epochBar"></i></div><div class="detail" id="epochDetail"></div></article><article class="card wide"><div class="label">Stake decentralization</div><div class="value" id="nakamoto"></div><div class="detail" id="stakeDetail"></div></article><article class="card full" style="overflow:auto"><table><thead><tr><th>#</th><th>Vote account</th><th>Stake</th><th>Commission</th></tr></thead><tbody id="validators"></tbody></table></article></section>
<h2>Ecosystem updates</h2><section class="updates"><article class="card wide"><div class="label">Official Solana news</div><div id="news"></div></article><article class="card wide"><div class="label">Agave releases</div><div id="releases"></div></article></section>
<h2>Source health</h2><article class="card full" style="overflow:auto"><table><thead><tr><th>Source</th><th>Status</th><th>Latency</th><th>Checked</th></tr></thead><tbody id="sources"></tbody></table></article>
<footer><span>Schema <code>{SCHEMA_VERSION}</code> · operational telemetry, not financial advice.</span><span><a href="../data/latest.json">JSON</a> · <a href="../reports/latest.md">Markdown</a> · <a href="https://github.com/epistemedeus/solana-ecosystem-pulse">Source</a></span></footer>
</main>
<script>const D={data_json};
const $=id=>document.getElementById(id), esc=s=>String(s??'n/a').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]));
const num=(v,d=0)=>v==null?'n/a':Number(v).toLocaleString(undefined,{{maximumFractionDigits:d,minimumFractionDigits:d}}); const usd=v=>{{if(v==null)return'n/a';for(const [n,s] of [[1e12,'T'],[1e9,'B'],[1e6,'M'],[1e3,'K']])if(Math.abs(v)>=n)return'$'+(v/n).toFixed(2)+s;return'$'+Number(v).toFixed(2)}};
$('status').textContent=D.status; $('generated').textContent=new Date(D.generated_at).toLocaleString(); if(D.status!=='healthy')document.querySelector('.dot').style.background='var(--red)';
const n=D.network,v=D.validators,e=D.economy;
const cards=[['Network TPS',num(n.tps_recent,1),num(n.non_vote_tps_recent,1)+' non-vote TPS'],['Slot time',num(n.slot_time_ms_recent,1)+' ms',num(n.sample_window_seconds)+' sec sample window'],['Active validators',num(v.active_count),num(v.delinquent_count)+' delinquent'],['Delinquent stake',num(v.delinquent_stake_pct,3)+'%',num(v.delinquent_stake_sol,0)+' SOL equivalent'],['SOL price',usd(e.sol_price_usd),(e.sol_price_change_24h_pct>=0?'+':'')+num(e.sol_price_change_24h_pct,2)+'% · 24h'],['DeFi TVL',usd(e.defi_tvl_usd),'DeFiLlama chain TVL'],['Stablecoin supply',usd(e.stablecoin_supply_usd),'USD-pegged circulation'],['DEX volume · 24h',usd(e.dex_volume_24h_usd),(e.dex_volume_change_24h_pct>=0?'+':'')+num(e.dex_volume_change_24h_pct,2)+'% day over day']];
$('metrics').innerHTML=cards.map((c,i)=>`<article class="card"><div class="label">${{esc(c[0])}}</div><div class="value">${{esc(c[1])}}</div><div class="detail">${{esc(c[2])}}</div>${{i===0?'<div class="accent"></div>':''}}</article>`).join('');
$('alerts').innerHTML=D.anomalies.length?D.anomalies.map(a=>`<div class="alert ${{esc(a.severity)}}"><strong>${{esc(a.severity)}} · ${{esc(a.metric)}}</strong><div>${{esc(a.message)}}</div><div class="detail">${{esc(a.basis)}}</div></div>`).join(''):'<div class="alert info"><strong>Clear</strong><div>No rule-based or baseline anomalies detected with available data.</div></div>';
function spark(metric,format){{const pts=D.history.map(x=>x.metrics?.[metric]).filter(x=>Number.isFinite(x));if(pts.length<2)return'<div class="detail" style="margin-top:20px">History builds automatically after each scheduled refresh.</div>';const lo=Math.min(...pts),hi=Math.max(...pts),span=hi-lo||1,path=pts.map((x,i)=>`${{i?'L':'M'}} ${{(i/(pts.length-1)*100).toFixed(2)}} ${{(68-(x-lo)/span*58).toFixed(2)}}`).join(' ');return`<svg class="spark" viewBox="0 0 100 76" preserveAspectRatio="none"><defs><linearGradient id="g${{metric}}"><stop stop-color="#14f195"/><stop offset="1" stop-color="#8b5cf6"/></linearGradient></defs><path d="${{path}}" fill="none" stroke="url(#g${{metric}})" stroke-width="2" vector-effect="non-scaling-stroke"/></svg><div class="detail">${{format(pts.at(-1))}} now · range ${{format(lo)}} to ${{format(hi)}}</div>`}};
$('tpsChart').innerHTML=spark('tps',x=>num(x,1)); $('tvlChart').innerHTML=spark('defi_tvl_usd',usd);
$('epoch').textContent='Epoch '+num(n.epoch); $('epochBar').style.width=Math.max(0,Math.min(100,n.epoch_progress_pct||0))+'%'; $('epochDetail').textContent=num(n.epoch_progress_pct,2)+'% · slot '+num(n.epoch_slot_index)+' of '+num(n.epoch_slots);
$('nakamoto').textContent=num(v.nakamoto_33_coefficient)+' validators'; $('stakeDetail').textContent='to exceed 33% of active stake · top 10 hold '+num(v.top_10_stake_pct,2)+'%';
$('validators').innerHTML=(v.top_validators||[]).map((x,i)=>`<tr><td>${{i+1}}</td><td><code title="${{esc(x.vote_account)}}">${{esc((x.vote_account||'').slice(0,9))}}…${{esc((x.vote_account||'').slice(-7))}}</code></td><td>${{num(x.stake_sol)}} SOL</td><td>${{num(x.commission_pct)}}%</td></tr>`).join('');
const updates=(id,rows,label)=>$(id).innerHTML=(rows||[]).map(x=>`<div class="update"><a href="${{esc(x.url)}}" target="_blank" rel="noopener">${{esc(x.title||x.name)}}</a><div class="detail">${{esc(x[label])}}</div></div>`).join('')||'<div class="detail">Source unavailable.</div>';
updates('news',D.ecosystem.news,'published_at'); updates('releases',D.ecosystem.agave_releases,'published_at');
$('sources').innerHTML=D.sources.map(s=>`<tr><td><a href="${{esc(s.url)}}" target="_blank" rel="noopener">${{esc(s.name)}}</a></td><td class="source-${{esc(s.status)}}">${{esc(s.status)}}</td><td>${{num(s.latency_ms)}} ms</td><td>${{esc(s.checked_at)}}</td></tr>`).join('');
</script></body></html>"""


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def validate_snapshot(snapshot: dict[str, Any]) -> None:
    if snapshot.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("unexpected schema version")
    if not snapshot.get("generated_at"):
        raise ValueError("generated_at is missing")
    if not isinstance(snapshot.get("network"), dict) or not isinstance(snapshot.get("sources"), list):
        raise ValueError("required sections are missing")
    if snapshot["network"].get("slot") is None:
        raise ValueError("finalized slot is missing")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rpc-url", default=os.environ.get("SOLANA_RPC_URL", DEFAULT_RPC))
    parser.add_argument("--output-dir", type=Path, default=Path("."))
    parser.add_argument("--history-file", type=Path)
    parser.add_argument("--stdout", action="store_true", help="also print the compact JSON snapshot")
    args = parser.parse_args(argv)
    root = args.output_dir.resolve()
    history_path = (args.history_file or root / "data" / "history.jsonl").resolve()

    raw, sources = fetch_all(args.rpc_url)
    snapshot = normalize_snapshot(raw, sources)
    history = read_history(history_path)
    snapshot["anomalies"] = detect_anomalies(snapshot, history)
    snapshot["history"] = compact_history(history, snapshot)
    if snapshot["anomalies"] and any(item["severity"] == "critical" for item in snapshot["anomalies"]):
        snapshot["status"] = "critical"
    elif snapshot["anomalies"] and snapshot["status"] == "healthy":
        snapshot["status"] = "watch"
    validate_snapshot(snapshot)

    atomic_write(root / "data" / "latest.json", json.dumps(snapshot, indent=2, ensure_ascii=False, sort_keys=True) + "\n")
    atomic_write(root / "reports" / "latest.md", markdown_report(snapshot))
    atomic_write(root / "dashboard" / "index.html", dashboard_html(snapshot))
    append_history(history_path, {"generated_at": snapshot["generated_at"], "metrics": metric_values(snapshot)})
    if args.stdout:
        print(json.dumps(snapshot, ensure_ascii=False, separators=(",", ":")))
    else:
        ok_sources = sum(source["status"] == "ok" for source in sources)
        print(f"Generated {snapshot['generated_at']} · {ok_sources}/{len(sources)} sources · {len(snapshot['anomalies'])} anomalies")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (urllib.error.URLError, TimeoutError, ValueError, json.JSONDecodeError) as exc:
        print(f"pulse generation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)

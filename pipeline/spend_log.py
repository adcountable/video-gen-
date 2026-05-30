"""
Tracks per-video API spend to a local JSON log.
Also stores YouTube video IDs so we can pull earnings later.

Log file: logs/spend_log.json
"""

import os
import json
from datetime import datetime
from typing import Optional

LOG_DIR  = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
LOG_FILE = os.path.join(LOG_DIR, "spend_log.json")

# Cost per API call
COST_MINIMAX = 0.15   # MiniMax Music 2.6
COST_FLUX    = 0.04   # FLUX 1.1 Pro image
COST_SLEEP   = 0.00   # Procedural — free


def log_run(
    channel_slug: str,
    run_id: str,
    music_generator: str,
    video_id: Optional[str] = None,
    dry_run: bool = False,
):
    """Record one pipeline run to the spend log."""
    os.makedirs(LOG_DIR, exist_ok=True)

    music_cost = COST_MINIMAX if music_generator == "minimax" else COST_SLEEP
    art_cost   = COST_FLUX
    total_cost = music_cost + art_cost

    entry = {
        "timestamp":       datetime.utcnow().isoformat(),
        "channel_slug":    channel_slug,
        "run_id":          run_id,
        "music_generator": music_generator,
        "music_cost":      music_cost,
        "art_cost":        art_cost,
        "total_cost":      total_cost,
        "video_id":        video_id,      # YouTube video ID if uploaded
        "dry_run":         dry_run,
        "uploaded":        video_id is not None,
    }

    log = _load()
    log.append(entry)
    _save(log)
    return entry


def log_earnings(video_id: str, views: int, revenue_usd: float, date: str):
    """Update a log entry with YouTube earnings data."""
    log = _load()
    for entry in log:
        if entry.get("video_id") == video_id:
            entry["views"]       = views
            entry["revenue_usd"] = revenue_usd
            entry["revenue_date"] = date
            break
    _save(log)


def get_all() -> list:
    return _load()


def get_summary() -> dict:
    log = _load()
    real_runs = [e for e in log if not e.get("dry_run")]
    return {
        "total_runs":     len(real_runs),
        "total_spend":    sum(e["total_cost"] for e in real_runs),
        "music_spend":    sum(e["music_cost"] for e in real_runs),
        "art_spend":      sum(e["art_cost"]   for e in real_runs),
        "total_revenue":  sum(e.get("revenue_usd", 0) for e in real_runs),
        "total_views":    sum(e.get("views", 0)        for e in real_runs),
        "uploaded_count": sum(1 for e in real_runs if e.get("uploaded")),
    }


def _load() -> list:
    if not os.path.exists(LOG_FILE):
        return []
    try:
        with open(LOG_FILE) as f:
            return json.load(f)
    except Exception:
        return []


def _save(log: list):
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)

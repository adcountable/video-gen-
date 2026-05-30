#!/usr/bin/env python3
"""
Daily scheduler — uploads today's channels automatically.

10 channels × 3 uploads/week = 30 videos/week (~$66/mo API costs)

Run manually:    python3 scheduler.py
Run dry-run:     python3 scheduler.py --dry-run
Check schedule:  python3 scheduler.py --show-schedule
Override day:    python3 scheduler.py --day 0   (0=Mon…6=Sun)
"""

import argparse
import datetime
import sys
from channels.registry import ALL_CHANNELS
from pipeline.orchestrator import run

# ── Active channels (top 10 by search volume) ─────────────────────────────────

ACTIVE_CHANNELS = [
    "deep-sleep",        # Sleep — biggest niche on YouTube
    "lofi-study",        # Focus — massive lo-fi audience
    "rain-sleep",        # Sleep — rain sounds, evergreen
    "baby-sleep",        # Sleep — high-intent parents audience
    "coding-music",      # Focus — tech audience, high engagement
    "coffee-shop-beats", # Focus — WFH/study crowd
    "meditation",        # Relax — evergreen, broad appeal
    "nature-sounds",     # Relax — sleep + focus crossover
    "piano-focus",       # Focus — clean, low competition
    "japanese-lofi",     # Mood — trending aesthetic, passionate fans
]

# ── 3x/week schedule (each channel appears exactly 3 times) ───────────────────
# 30 uploads/week spread 4-5 per day across 7 days

DAILY_ROTATION = {
    0: ["deep-sleep",        "lofi-study",        "rain-sleep",   "nature-sounds"],  # Mon (4)
    1: ["baby-sleep",        "coding-music",      "coffee-shop-beats", "piano-focus"], # Tue (4)
    2: ["deep-sleep",        "lofi-study",        "meditation",   "japanese-lofi"],  # Wed (4)
    3: ["rain-sleep",        "baby-sleep",        "coding-music", "nature-sounds"],  # Thu (4)
    4: ["deep-sleep",        "coffee-shop-beats", "meditation",   "piano-focus", "japanese-lofi"], # Fri (5)
    5: ["lofi-study",        "rain-sleep",        "nature-sounds","piano-focus"],    # Sat (4)
    6: ["baby-sleep",        "coding-music",      "coffee-shop-beats", "meditation", "japanese-lofi"], # Sun (5)
}

# Verify: each channel appears exactly 3 times across the week
# deep-sleep:        Mon, Wed, Fri = 3 ✓
# lofi-study:        Mon, Wed, Sat = 3 ✓
# rain-sleep:        Mon, Thu, Sat = 3 ✓
# baby-sleep:        Tue, Thu, Sun = 3 ✓
# coding-music:      Tue, Thu, Sun = 3 ✓
# coffee-shop-beats: Tue, Fri, Sun = 3 ✓
# meditation:        Wed, Fri, Sun = 3 ✓
# nature-sounds:     Mon, Thu, Sat = 3 ✓
# piano-focus:       Tue, Fri, Sat = 3 ✓
# japanese-lofi:     Wed, Fri, Sun = 3 ✓


def get_todays_channels(weekday: int = None) -> list:
    """Return channel slugs scheduled for the given weekday (0=Mon…6=Sun)."""
    if weekday is None:
        weekday = datetime.datetime.now().weekday()
    return list(DAILY_ROTATION.get(weekday, []))


def show_schedule():
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    total = 0
    print("\nWeekly schedule — 10 channels × 3x/week:\n")
    for d in range(7):
        channels = get_todays_channels(d)
        total += len(channels)
        print(f"  {day_names[d]:12s} ({len(channels)})  {', '.join(channels)}")
    print(f"\n  Total uploads/week : {total}")
    print(f"  API cost/week      : ~${total * 0.55:.0f}")
    print(f"  API cost/month     : ~${total * 0.55 * 4:.0f}")
    print(f"  Revenue target     : $8–15k/mo (after 6–12 months)\n")


def main():
    parser = argparse.ArgumentParser(description="Daily YouTube music upload scheduler")
    parser.add_argument("--dry-run",       action="store_true", help="Build videos, skip upload")
    parser.add_argument("--show-schedule", action="store_true", help="Print weekly schedule")
    parser.add_argument("--day", type=int, choices=range(7),    help="Override weekday (0=Mon)")
    args = parser.parse_args()

    if args.show_schedule:
        show_schedule()
        return

    weekday  = args.day if args.day is not None else datetime.datetime.now().weekday()
    day_name = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][weekday]
    channels = get_todays_channels(weekday)

    if not channels:
        print(f"No uploads scheduled for {day_name}.")
        return

    print(f"\n📅 {day_name} — uploading {len(channels)} video(s): {', '.join(channels)}\n")

    failed = []
    for slug in channels:
        try:
            run(ALL_CHANNELS[slug], dry_run=args.dry_run)
        except Exception as e:
            print(f"\n❌ {slug} failed: {e}")
            failed.append(slug)

    print(f"\n{'='*60}")
    success = len(channels) - len(failed)
    print(f"  {success}/{len(channels)} uploaded successfully")
    if failed:
        print(f"  Failed: {', '.join(failed)}")
    print(f"{'='*60}\n")

    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()

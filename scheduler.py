#!/usr/bin/env python3
"""
Daily scheduler — figures out which channels to upload today and runs them.

Rotation: 25 channels spread across 7 days (3-4 per day).
To upload 3x/week per channel, set UPLOADS_PER_WEEK = 3 below.

Run manually:    python3 scheduler.py
Run dry-run:     python3 scheduler.py --dry-run
Check schedule:  python3 scheduler.py --show-schedule
"""

import argparse
import datetime
import sys
from channels.registry import ALL_CHANNELS
from pipeline.orchestrator import run

# ── Schedule config ────────────────────────────────────────────────────────────

# How many times per week each channel uploads (1 = once, 3 = three times)
UPLOADS_PER_WEEK = 1

# Which channels upload on which day (0=Mon … 6=Sun)
# 25 channels spread across 7 days
DAILY_ROTATION = {
    0: ["deep-sleep",     "lofi-study",     "spa-music",    "happy-morning"],   # Mon  (4)
    1: ["baby-sleep",     "deep-work-jazz", "yoga-flow",    "sad-rainy-day"],   # Tue  (4)
    2: ["sleep-meditation","coding-music",  "anxiety-relief","romantic-jazz"],  # Wed  (4)
    3: ["rain-sleep",     "coffee-shop-beats","nature-sounds","christmas-ambient"], # Thu (4)
    4: ["432hz-sleep",    "classical-study","meditation",   "worship-instrumental"], # Fri (4)
    5: ["binaural-sleep", "piano-focus",    "reiki-healing"],                   # Sat  (3)
    6: ["african-meditation", "japanese-lofi"],                                 # Sun  (2)
}

# If UPLOADS_PER_WEEK > 1, additional upload days per channel
EXTRA_DAYS = {
    # channel-slug: [extra_weekday, ...]
    "deep-sleep":          [2, 4],
    "lofi-study":          [2, 5],
    "spa-music":           [3, 6],
    "happy-morning":       [3, 5],
    "baby-sleep":          [3, 5],
    "deep-work-jazz":      [4, 6],
    "yoga-flow":           [0, 4],
    "sad-rainy-day":       [0, 4],
    "sleep-meditation":    [0, 5],
    "coding-music":        [0, 4],
    "anxiety-relief":      [1, 5],
    "romantic-jazz":       [0, 5],
    "rain-sleep":          [1, 5],
    "coffee-shop-beats":   [1, 5],
    "nature-sounds":       [2, 6],
    "christmas-ambient":   [2, 5],
    "432hz-sleep":         [2, 6],
    "classical-study":     [1, 3],
    "meditation":          [1, 3],
    "worship-instrumental":[2, 0],
    "binaural-sleep":      [2, 4],
    "piano-focus":         [2, 4],
    "reiki-healing":       [0, 3],
    "african-meditation":  [1, 4],
    "japanese-lofi":       [0, 3],
}


def get_todays_channels(weekday: int = None) -> list:
    """Return the list of channel slugs scheduled for today."""
    if weekday is None:
        weekday = datetime.datetime.now().weekday()

    channels = list(DAILY_ROTATION.get(weekday, []))

    if UPLOADS_PER_WEEK > 1:
        for slug, extra_days in EXTRA_DAYS.items():
            if weekday in extra_days and slug not in channels:
                channels.append(slug)

    return channels


def show_schedule():
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    total = 0
    print(f"\nWeekly schedule ({UPLOADS_PER_WEEK}x per channel per week):\n")
    for d in range(7):
        channels = get_todays_channels(d)
        total += len(channels)
        print(f"  {day_names[d]:12s} ({len(channels):2d})  {', '.join(channels)}")
    print(f"\n  Total uploads/week: {total}")
    print(f"  Est. API cost/week: ~${total * 0.55:.0f}")
    print(f"  Est. API cost/month: ~${total * 0.55 * 4:.0f}\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Build videos, skip upload")
    parser.add_argument("--show-schedule", action="store_true", help="Print weekly schedule")
    parser.add_argument("--day", type=int, choices=range(7), help="Override weekday (0=Mon)")
    args = parser.parse_args()

    if args.show_schedule:
        show_schedule()
        return

    weekday = args.day if args.day is not None else datetime.datetime.now().weekday()
    day_name = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][weekday]
    channels = get_todays_channels(weekday)

    if not channels:
        print(f"No channels scheduled for {day_name}.")
        return

    print(f"\n📅 {day_name} — {len(channels)} channel(s) scheduled: {', '.join(channels)}\n")

    failed = []
    for slug in channels:
        channel = ALL_CHANNELS[slug]
        try:
            run(channel, dry_run=args.dry_run)
        except Exception as e:
            print(f"\n❌ {slug} failed: {e}")
            failed.append(slug)

    print(f"\n{'='*60}")
    print(f"Done. {len(channels) - len(failed)}/{len(channels)} uploaded successfully.")
    if failed:
        print(f"Failed: {', '.join(failed)}")
    print(f"{'='*60}\n")

    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()

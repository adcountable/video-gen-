#!/usr/bin/env python3
"""
Daily scheduler — 25 channels × 3 uploads/week = 75 videos/week

Run manually:    python3 scheduler.py
Dry run:         python3 scheduler.py --dry-run
Check schedule:  python3 scheduler.py --show-schedule
Override day:    python3 scheduler.py --day 0   (0=Mon…6=Sun)
"""

import argparse
import datetime
import sys
from channels.registry import ALL_CHANNELS
from pipeline.orchestrator import run

# ── 3x/week schedule — 25 channels × 3 = 75 uploads/week ─────────────────────
# Each channel appears exactly 3 times. ~10–11 uploads per day.
#
# Verified counts per channel:
#   deep-sleep, lofi-study, happy-morning     → Mon, Wed, Fri
#   baby-sleep, coffee-shop-beats, worship     → Mon, Thu, Sat
#   sleep-meditation, coding-music, yoga-flow  → Tue, Thu, Sun
#   rain-sleep, spa-music                      → Mon, Wed, Sat
#   432hz-sleep                                → Tue, Fri, Sun
#   binaural-sleep, classical-study, romantic  → Wed, Fri, Sun
#   deep-work-jazz, sad-rainy-day, christmas   → Tue, Thu, Sat
#   piano-focus, reiki-healing                 → Tue, Fri, Sat
#   nature-sounds                              → Wed, Fri, Sat
#   anxiety-relief, japanese-lofi              → Mon, Thu, Sun
#   meditation                                 → Mon, Fri, Sun
#   african-meditation                         → Tue, Wed, Sun

DAILY_ROTATION = {
    0: [  # Monday (11)
        "deep-sleep", "baby-sleep", "rain-sleep",
        "lofi-study", "coffee-shop-beats", "spa-music",
        "anxiety-relief", "meditation", "happy-morning",
        "worship-instrumental", "japanese-lofi",
    ],
    1: [  # Tuesday (10)
        "sleep-meditation", "432hz-sleep",
        "deep-work-jazz", "coding-music", "piano-focus",
        "yoga-flow", "reiki-healing",
        "sad-rainy-day", "christmas-ambient", "african-meditation",
    ],
    2: [  # Wednesday (10)
        "deep-sleep", "rain-sleep", "binaural-sleep",
        "lofi-study", "classical-study", "spa-music",
        "nature-sounds", "happy-morning",
        "romantic-jazz", "african-meditation",
    ],
    3: [  # Thursday (11)
        "baby-sleep", "sleep-meditation",
        "deep-work-jazz", "coding-music", "coffee-shop-beats",
        "yoga-flow", "anxiety-relief",
        "sad-rainy-day", "christmas-ambient",
        "worship-instrumental", "japanese-lofi",
    ],
    4: [  # Friday (11)
        "deep-sleep", "432hz-sleep", "binaural-sleep",
        "lofi-study", "piano-focus", "classical-study",
        "nature-sounds", "reiki-healing", "meditation",
        "happy-morning", "romantic-jazz",
    ],
    5: [  # Saturday (11)
        "baby-sleep", "rain-sleep",
        "deep-work-jazz", "coffee-shop-beats", "piano-focus",
        "spa-music", "nature-sounds", "reiki-healing",
        "sad-rainy-day", "christmas-ambient", "worship-instrumental",
    ],
    6: [  # Sunday (11)
        "sleep-meditation", "432hz-sleep", "binaural-sleep",
        "coding-music", "classical-study",
        "yoga-flow", "anxiety-relief", "meditation",
        "romantic-jazz", "african-meditation", "japanese-lofi",
    ],
}


def get_todays_channels(weekday: int = None) -> list:
    if weekday is None:
        weekday = datetime.datetime.now().weekday()
    return list(DAILY_ROTATION.get(weekday, []))


def show_schedule():
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    total = 0
    print("\nWeekly schedule — 25 channels × 3x/week:\n")
    for d in range(7):
        channels = get_todays_channels(d)
        total += len(channels)
        print(f"  {day_names[d]:12s} ({len(channels):2d})  {', '.join(channels)}")
    print(f"\n  Total uploads/week : {total}")
    print(f"  API cost/week      : ~${total * 0.55:.0f}")
    print(f"  API cost/month     : ~${total * 0.55 * 4:.0f}")
    print(f"  Revenue target     : $15–25k/mo (after 12–18 months)\n")


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
    print(f"  {len(channels) - len(failed)}/{len(channels)} uploaded successfully")
    if failed:
        print(f"  Failed: {', '.join(failed)}")
    print(f"{'='*60}\n")

    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
YouTube Music Bot — entry point.

Usage:
  python run.py work              # upload one work music video
  python run.py sleep             # upload one sleep music video
  python run.py work --dry-run    # build video locally, skip upload
  python run.py sleep --count 3   # upload 3 sleep music videos
"""

import argparse
import channels.work_music as work_music
import channels.sleep_music as sleep_music
from pipeline.orchestrator import run

CHANNELS = {
    "work": (work_music, "work"),
    "sleep": (sleep_music, "sleep"),
}


def main():
    parser = argparse.ArgumentParser(description="Generate and upload YouTube music videos")
    parser.add_argument("channel", choices=["work", "sleep"], help="Which channel to upload to")
    parser.add_argument("--dry-run", action="store_true", help="Build video but skip upload")
    parser.add_argument("--count", type=int, default=1, help="Number of videos to produce (default: 1)")
    args = parser.parse_args()

    module, slug = CHANNELS[args.channel]

    for i in range(args.count):
        if args.count > 1:
            print(f"\n>>> Video {i + 1} of {args.count}")
        run(module, slug, dry_run=args.dry_run)


if __name__ == "__main__":
    main()

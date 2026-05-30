#!/usr/bin/env python3
"""
YouTube Music Bot — entry point.

Usage:
  python3 run.py <channel>                          # generate music + upload
  python3 run.py <channel> --audio track.mp3        # use Suno MP3 + upload
  python3 run.py <channel> --audio track.mp3 --dry-run  # test without uploading
  python3 run.py <channel> --count 3                # upload 3 videos
  python3 run.py --list                             # show all 25 channels

Examples:
  python3 run.py deep-sleep --audio ~/Downloads/suno_sleep.mp3
  python3 run.py lofi-study --dry-run
  python3 run.py japanese-lofi --count 3
"""

import argparse
from channels.registry import ALL_CHANNELS
from pipeline.orchestrator import run


def main():
    parser = argparse.ArgumentParser(description="Generate and upload YouTube music videos")
    parser.add_argument("channel", nargs="?", choices=list(ALL_CHANNELS.keys()),
                        help="Channel slug to upload to")
    parser.add_argument("--audio",   type=str, default=None,
                        help="Path to a local MP3 (e.g. from Suno) — skips music generation")
    parser.add_argument("--dry-run", action="store_true", help="Build video but skip upload")
    parser.add_argument("--count",   type=int, default=1,  help="Number of videos to produce")
    parser.add_argument("--list",    action="store_true",  help="List all available channels")
    args = parser.parse_args()

    if args.list or not args.channel:
        print("\nAvailable channels (25 total):\n")
        groups = {
            "Sleep": ["deep-sleep", "baby-sleep", "sleep-meditation", "rain-sleep",
                      "432hz-sleep", "binaural-sleep"],
            "Focus": ["lofi-study", "deep-work-jazz", "coding-music", "coffee-shop-beats",
                      "classical-study", "piano-focus"],
            "Relax": ["spa-music", "yoga-flow", "anxiety-relief", "nature-sounds",
                      "meditation", "reiki-healing"],
            "Mood":  ["happy-morning", "sad-rainy-day", "romantic-jazz", "christmas-ambient",
                      "worship-instrumental", "african-meditation", "japanese-lofi"],
        }
        for group, slugs in groups.items():
            print(f"  {group}:")
            for slug in slugs:
                print(f"    {slug:30s}  {ALL_CHANNELS[slug].name}")
            print()
        return

    channel = ALL_CHANNELS[args.channel]

    if args.audio and args.count > 1:
        print("Note: --audio with --count will use the same MP3 for all videos.")

    for i in range(args.count):
        if args.count > 1:
            print(f"\n>>> Video {i + 1} of {args.count}")
        run(channel, dry_run=args.dry_run, audio_file=args.audio)


if __name__ == "__main__":
    main()

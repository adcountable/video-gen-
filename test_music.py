"""
Music quality tester — generates one sample per channel archetype and saves
them to tests/music/ so you can listen and decide which model/prompt works best.

Usage:
    python3 test_music.py                    # test all archetypes
    python3 test_music.py --model musicgen   # compare with MusicGen
    python3 test_music.py --slug deep-sleep  # test a specific channel

Cost: ~$0.15 per sample (MiniMax) or ~$0.50 (MusicGen)
"""

import os
import sys
import argparse
import requests
import replicate
from dotenv import load_dotenv

load_dotenv()
os.environ["REPLICATE_API_TOKEN"] = os.environ.get("REPLICATE_API_KEY", "")

OUT_DIR = "tests/music"
os.makedirs(OUT_DIR, exist_ok=True)

# ── Test prompts — one per channel archetype ──────────────────────────────────

TESTS = [
    # (slug, prompt)
    ("deep-sleep",
     "deep sleep music, slow ambient drone, delta waves, low bass hum, "
     "very slow pulse, peaceful void, healing frequencies, no lyrics"),

    ("rain-sleep",
     "rainy night sleep music, soft piano with gentle rain sounds, "
     "cozy indoor feeling, slow tempo, no lyrics"),

    ("binaural-sleep",
     "binaural beats sleep, soft ambient carrier tone, delta 2hz, "
     "deep sleep induction, peaceful, no lyrics"),

    ("lofi-study",
     "lo-fi hip hop study beats, mellow guitar, soft vinyl crackle, "
     "chill and focused, warm Rhodes piano, no lyrics"),

    ("deep-work-jazz",
     "smooth jazz for deep work, warm saxophone, light bass, "
     "brushed drums, coffee shop ambiance, no lyrics"),

    ("coffee-shop-beats",
     "morning cafe music, acoustic guitar, upright bass, "
     "bossa nova inspired, warm and cozy, no lyrics"),

    ("anxiety-relief",
     "anxiety relief music, slow calming piano, grounding bass tones, "
     "60bpm, nervous system regulation, no lyrics"),

    ("happy-morning",
     "happy morning music, upbeat acoustic guitar, cheerful piano, "
     "positive sunrise energy, no lyrics"),

    ("romantic-jazz",
     "romantic jazz, soft saxophone, warm piano, candlelight dinner, "
     "intimate evening, no lyrics"),

    ("japanese-lofi",
     "Japanese lo-fi music, koto and piano, cherry blossom vibes, "
     "slow and serene, wabi-sabi, no lyrics"),
]


def generate_minimax(prompt: str) -> str:
    output = replicate.run(
        "minimax/music-2.6",
        input={
            "prompt": prompt,
            "is_instrumental": True,
            "lyrics_optimizer": False,
            "audio_format": "mp3",
            "bitrate": 256000,
            "sample_rate": 44100,
        },
    )
    return str(output)


def generate_musicgen(prompt: str) -> str:
    MUSICGEN_VERSION = "671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb"
    output = replicate.run(
        f"meta/musicgen:{MUSICGEN_VERSION}",
        input={
            "prompt": prompt,
            "duration": 60,          # 60s for quick test, not 300
            "model_version": "large",
            "output_format": "mp3",
            "normalization_strategy": "loudness",
        },
    )
    return str(output)


def download(url: str, dest: str):
    with requests.get(url, stream=True, timeout=120) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    mb = os.path.getsize(dest) / 1024 / 1024
    print(f"    → {dest} ({mb:.1f} MB)")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", choices=["minimax", "musicgen"], default="minimax")
    parser.add_argument("--slug", help="Test only this channel slug")
    args = parser.parse_args()

    tests = [t for t in TESTS if not args.slug or t[0] == args.slug]
    cost = 0.15 if args.model == "minimax" else 0.08  # musicgen 60s ≈ $0.08

    print(f"\nModel: {args.model} | {len(tests)} samples | ~${cost * len(tests):.2f} total\n")

    for slug, prompt in tests:
        out_path = os.path.join(OUT_DIR, f"{slug}_{args.model}.mp3")

        if os.path.exists(out_path):
            print(f"  [skip] {slug} — already exists")
            continue

        print(f"  [{args.model}] {slug}...")
        print(f"    Prompt: {prompt[:70]}...")

        try:
            if args.model == "minimax":
                url = generate_minimax(prompt)
            else:
                url = generate_musicgen(prompt)
            download(url, out_path)
        except Exception as e:
            print(f"    ✗ Error: {e}")

    print(f"\nDone! Open samples:")
    print(f"  open {OUT_DIR}/")


if __name__ == "__main__":
    main()

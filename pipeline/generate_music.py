"""
Music generation via Replicate + Meta MusicGen.

Suno has no public API — MusicGen is the best drop-in replacement.
Cost: ~$0.06 per 30-second track. We generate 30s and FFmpeg loops it to 1hr.

Get your Replicate API key at: https://replicate.com/account/api-tokens
"""

import os
import requests
import replicate
from config import REPLICATE_API_KEY

# Pin to a specific version for reproducibility
MUSICGEN_VERSION = "671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb"

os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_KEY


def generate_track(prompt: str, duration: int = 30) -> str:
    """
    Generate a music track via MusicGen and return the MP3 download URL.

    duration: 8–30 seconds recommended (Replicate caps at 30s for this model).
    We generate 30s and loop it to full video length in create_video.py.
    """
    print(f"  [musicgen] Generating track ({duration}s): {prompt[:60]}...")

    output = replicate.run(
        f"meta/musicgen:{MUSICGEN_VERSION}",
        input={
            "prompt": prompt,
            "duration": duration,
            "model_version": "large",
            "output_format": "mp3",
            "normalization_strategy": "loudness",
        },
    )

    # Replicate returns the URL directly (or a FileOutput object)
    audio_url = str(output)
    print(f"  [musicgen] Track ready: {audio_url[:80]}...")
    return audio_url


def download_audio(url: str, dest_path: str) -> str:
    """Download the MP3 to dest_path. Returns dest_path."""
    print(f"  [musicgen] Downloading audio → {dest_path}")
    with requests.get(url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with open(dest_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    size = os.path.getsize(dest_path) / (1024 * 1024)
    print(f"  [musicgen] Saved ({size:.1f} MB)")
    return dest_path

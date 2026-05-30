"""
Music generation via Replicate — MiniMax Music 2.6.

~$0.15/video (vs $0.50 for MusicGen). Generates ~3 min of music,
looped by FFmpeg to fill the full hour.

Get your Replicate API key: https://replicate.com/account/api-tokens
"""

import os
import shutil
import tempfile
import requests
import replicate
from config import REPLICATE_API_KEY

MINIMAX_MODEL = "minimax/music-2.6"

os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_KEY


def generate_track(prompt: str) -> str:
    """
    Generate a music clip via MiniMax Music 2.6 and return local MP3 path.
    FFmpeg loops it to fill the hour — free.
    """
    print(f"  [minimax] Generating track: {prompt[:60]}...")

    output = replicate.run(
        MINIMAX_MODEL,
        input={
            "prompt": prompt,
            "is_instrumental": True,
            "lyrics_optimizer": False,
            "audio_format": "mp3",
            "bitrate": 256000,
            "sample_rate": 44100,
        },
    )

    url = str(output)
    print(f"  [minimax] Track ready ✓")

    # Save to a temp file
    tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tmp.close()
    _download(url, tmp.name)
    return tmp.name


def download_audio(url_or_path: str, dest_path: str) -> str:
    """
    Copy local temp file to dest_path, or download if it's a URL.
    Returns dest_path.
    """
    if os.path.exists(url_or_path):
        shutil.copy(url_or_path, dest_path)
        os.remove(url_or_path)
    else:
        _download(url_or_path, dest_path)

    size = os.path.getsize(dest_path) / (1024 * 1024)
    print(f"  [minimax] Audio saved ({size:.1f} MB)")
    return dest_path


def _download(url: str, dest: str):
    print(f"  [minimax] Downloading → {os.path.basename(dest)}")
    with requests.get(url, stream=True, timeout=120) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

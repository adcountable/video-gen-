"""
Music generation via Replicate + Meta MusicGen.

Strategy: generate a 5-minute (300s) clip — ~$0.50/track.
If Replicate caps the duration, we fall back to stitching
multiple 30s clips together using FFmpeg crossfade.

Get your Replicate API key: https://replicate.com/account/api-tokens
"""

import os
import tempfile
import requests
import replicate
from config import REPLICATE_API_KEY, MUSIC_CLIP_SECONDS

# Pin to specific version for reproducibility
MUSICGEN_VERSION = "671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb"
REPLICATE_MAX_DURATION = 300  # seconds — MusicGen large supports up to 300s

os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_KEY


def generate_track(prompt: str) -> str:
    """
    Generate a music clip and return the local MP3 path.

    If MUSIC_CLIP_SECONDS <= 300: single Replicate call (~$0.50 for 5 min).
    If MUSIC_CLIP_SECONDS > 300: generates multiple 30s clips and stitches them.
    """
    if MUSIC_CLIP_SECONDS <= REPLICATE_MAX_DURATION:
        return _generate_single(prompt, MUSIC_CLIP_SECONDS)
    else:
        return _generate_stitched(prompt, MUSIC_CLIP_SECONDS)


def _generate_single(prompt: str, duration: int) -> str:
    """Single MusicGen call — returns MP3 download URL."""
    print(f"  [musicgen] Generating {duration}s track: {prompt[:60]}...")

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

    url = str(output)
    print(f"  [musicgen] Track ready ✓")
    return url


def _generate_stitched(prompt: str, total_seconds: int) -> str:
    """
    Generate multiple 30s clips and crossfade-stitch them into one file.
    Used when total_seconds > 300.
    """
    import math, subprocess, shutil
    from pipeline.create_video import get_ffmpeg_binary

    clip_duration = 30
    n_clips = math.ceil(total_seconds / clip_duration)
    print(f"  [musicgen] Stitching {n_clips} x {clip_duration}s clips → {total_seconds}s total")

    tmp_dir = tempfile.mkdtemp()
    clip_paths = []

    try:
        for i in range(n_clips):
            print(f"  [musicgen] Clip {i+1}/{n_clips}...")
            url = _generate_single(prompt, clip_duration)
            clip_path = os.path.join(tmp_dir, f"clip_{i:02d}.mp3")
            _download(url, clip_path)
            clip_paths.append(clip_path)

        # Crossfade-stitch all clips with 2s overlap
        stitched = os.path.join(tmp_dir, "stitched.mp3")
        _crossfade_stitch(clip_paths, stitched, fade_sec=2)

        # Move to a stable temp file outside tmp_dir
        final = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
        final.close()
        shutil.copy(stitched, final.name)
        return final.name

    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def _crossfade_stitch(clip_paths: list, output: str, fade_sec: int = 2):
    """Stitch MP3 clips with crossfade using FFmpeg."""
    from pipeline.create_video import get_ffmpeg_binary
    import subprocess

    if len(clip_paths) == 1:
        import shutil
        shutil.copy(clip_paths[0], output)
        return

    # Build an ffmpeg filter chain: acrossfade each adjacent pair
    # For N clips: apply acrossfade N-1 times
    ffmpeg = get_ffmpeg_binary()
    inputs = []
    for p in clip_paths:
        inputs += ["-i", p]

    # Build filter_complex for chained acrossfade
    n = len(clip_paths)
    filters = []
    prev = "0:a"
    for i in range(1, n):
        out_label = f"cf{i}" if i < n - 1 else "out"
        filters.append(
            f"[{prev}][{i}:a]acrossfade=d={fade_sec}:c1=tri:c2=tri[{out_label}]"
        )
        prev = f"cf{i}"

    filter_str = ";".join(filters)

    cmd = [ffmpeg, "-y"] + inputs + [
        "-filter_complex", filter_str,
        "-map", "[out]",
        "-c:a", "libmp3lame", "-b:a", "192k",
        output,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"crossfade stitch failed:\n{result.stderr[-1000:]}")


def download_audio(url_or_path: str, dest_path: str) -> str:
    """
    Download URL to dest_path, or copy if already a local file.
    Returns dest_path.
    """
    if os.path.exists(url_or_path):
        import shutil
        shutil.copy(url_or_path, dest_path)
        os.remove(url_or_path)  # clean up the temp file
    else:
        _download(url_or_path, dest_path)

    size = os.path.getsize(dest_path) / (1024 * 1024)
    print(f"  [musicgen] Audio saved ({size:.1f} MB)")
    return dest_path


def _download(url: str, dest: str):
    print(f"  [musicgen] Downloading → {os.path.basename(dest)}")
    with requests.get(url, stream=True, timeout=120) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

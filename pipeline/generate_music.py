"""
Music generation via Replicate + Meta MusicGen.

Strategy: generate 4 x 300s clips using audio continuation, giving 20 min of
unique, seamlessly flowing music. FFmpeg loops that 3x to fill the hour.
Cost: ~$2/video (4 x $0.50) — sounds like a real mix, not a looped clip.

Get your Replicate API key: https://replicate.com/account/api-tokens
"""

import os
import math
import shutil
import tempfile
import requests
import replicate
from config import REPLICATE_API_KEY, MUSIC_CLIP_SECONDS

# Pin to specific version for reproducibility
MUSICGEN_VERSION = "671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb"
CLIP_DURATION = 300       # seconds per clip — MusicGen large max
N_CLIPS       = 4         # 4 x 300s = 20 min unique music, looped 3x = 1hr

os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_KEY


def generate_track(prompt: str) -> str:
    """
    Generate a seamless ~20-minute music piece via 4 continuation clips.
    Returns path to a local MP3 stitched from all clips.
    """
    tmp_dir = tempfile.mkdtemp()
    clip_paths = []

    try:
        # Clip 1 — free generation
        print(f"  [musicgen] Clip 1/{N_CLIPS} — generating seed track...")
        url = _generate_single(prompt, CLIP_DURATION)
        clip_path = os.path.join(tmp_dir, "clip_01.mp3")
        _download(url, clip_path)
        clip_paths.append(clip_path)

        # Clips 2-4 — each continues from the tail of the previous
        for i in range(2, N_CLIPS + 1):
            print(f"  [musicgen] Clip {i}/{N_CLIPS} — continuing from previous...")
            url = _generate_continuation(prompt, clip_paths[-1], CLIP_DURATION)
            clip_path = os.path.join(tmp_dir, f"clip_{i:02d}.mp3")
            _download(url, clip_path)
            clip_paths.append(clip_path)

        # Stitch all clips with crossfade
        print(f"  [musicgen] Stitching {N_CLIPS} clips into seamless mix...")
        stitched = os.path.join(tmp_dir, "mix.mp3")
        _crossfade_stitch(clip_paths, stitched, fade_sec=3)

        # Move to a stable temp file outside tmp_dir
        final = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
        final.close()
        shutil.copy(stitched, final.name)
        return final.name

    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def download_audio(url_or_path: str, dest_path: str) -> str:
    """
    Download URL to dest_path, or move if already a local file.
    Returns dest_path.
    """
    if os.path.exists(url_or_path):
        shutil.copy(url_or_path, dest_path)
        os.remove(url_or_path)  # clean up temp file
    else:
        _download(url_or_path, dest_path)

    size = os.path.getsize(dest_path) / (1024 * 1024)
    print(f"  [musicgen] Mix saved ({size:.1f} MB)")
    return dest_path


# ── Private helpers ────────────────────────────────────────────────────────────

def _generate_single(prompt: str, duration: int) -> str:
    """Single MusicGen call — returns MP3 download URL."""
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
    return str(output)


def _generate_continuation(prompt: str, prev_audio_path: str, duration: int) -> str:
    """
    Generate a MusicGen clip that seamlessly continues from the tail of prev_audio_path.
    Uses the last 10s of the previous clip as the seed.
    """
    with open(prev_audio_path, "rb") as audio_file:
        output = replicate.run(
            f"meta/musicgen:{MUSICGEN_VERSION}",
            input={
                "prompt": prompt,
                "duration": duration,
                "model_version": "large",
                "output_format": "mp3",
                "normalization_strategy": "loudness",
                "continuation": True,
                "input_audio": audio_file,
                "continuation_start": max(0, CLIP_DURATION - 10),  # use last 10s
            },
        )
    return str(output)


def _crossfade_stitch(clip_paths: list, output: str, fade_sec: int = 3):
    """Stitch MP3 clips with crossfade using FFmpeg acrossfade filter."""
    from pipeline.create_video import get_ffmpeg_binary
    import subprocess

    if len(clip_paths) == 1:
        shutil.copy(clip_paths[0], output)
        return

    ffmpeg = get_ffmpeg_binary()
    inputs = []
    for p in clip_paths:
        inputs += ["-i", p]

    # Build chained acrossfade filter
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


def _download(url: str, dest: str):
    print(f"  [musicgen] Downloading → {os.path.basename(dest)}")
    with requests.get(url, stream=True, timeout=120) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

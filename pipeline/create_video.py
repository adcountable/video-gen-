"""
FFmpeg-based video assembly.

Loops a short audio track to fill VIDEO_DURATION_SECONDS, then combines
with a static image (+ slow Ken Burns zoom) to produce a 1920x1080 MP4.

Requires ffmpeg installed: brew install ffmpeg
"""

import os
import subprocess
import tempfile
from config import VIDEO_DURATION_SECONDS, VIDEO_WIDTH, VIDEO_HEIGHT


def build_video(audio_path: str, artwork_path: str, output_path: str) -> str:
    """
    Combine audio (looped to 1 hour) + artwork (with slow zoom) into an MP4.
    Returns output_path.
    """
    print(f"  [ffmpeg] Building {VIDEO_DURATION_SECONDS // 3600}h video...")

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
        looped_audio = tmp.name

    try:
        _loop_audio(audio_path, looped_audio)
        _render_video(artwork_path, looped_audio, output_path)
    finally:
        if os.path.exists(looped_audio):
            os.remove(looped_audio)

    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"  [ffmpeg] Video ready → {output_path} ({size_mb:.0f} MB)")
    return output_path


def _loop_audio(src: str, dest: str):
    """Loop audio file to exactly VIDEO_DURATION_SECONDS."""
    print(f"  [ffmpeg] Looping audio to {VIDEO_DURATION_SECONDS}s...")
    _run([
        "ffmpeg", "-y",
        "-stream_loop", "-1",
        "-i", src,
        "-t", str(VIDEO_DURATION_SECONDS),
        "-c", "copy",
        dest,
    ])


def _render_video(image_path: str, audio_path: str, output_path: str):
    """Combine static image + looped audio with a slow Ken Burns zoom."""
    print(f"  [ffmpeg] Rendering video (this takes a few minutes)...")

    # Ken Burns: very slow zoom from 1.0x → 1.05x over the full duration
    # Using 1fps reduces render time dramatically while looking fine for a static image
    zoom_filter = (
        f"scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}:force_original_aspect_ratio=increase,"
        f"crop={VIDEO_WIDTH}:{VIDEO_HEIGHT},"
        f"zoompan="
        f"z='min(zoom+0.00005,1.05)':"
        f"x='iw/2-(iw/zoom/2)':"
        f"y='ih/2-(ih/zoom/2)':"
        f"d={VIDEO_DURATION_SECONDS}:"  # total frames at fps=1
        f"s={VIDEO_WIDTH}x{VIDEO_HEIGHT}:"
        f"fps=1"
    )

    _run([
        "ffmpeg", "-y",
        "-loop", "1",
        "-framerate", "1",
        "-i", image_path,
        "-i", audio_path,
        "-vf", zoom_filter,
        "-c:v", "libx264",
        "-preset", "faster",
        "-crf", "23",
        "-tune", "stillimage",
        "-pix_fmt", "yuv420p",
        "-r", "1",          # output at 1fps — fine for static content
        "-c:a", "aac",
        "-b:a", "192k",
        "-t", str(VIDEO_DURATION_SECONDS),
        "-movflags", "+faststart",
        output_path,
    ])


def _run(cmd: list[str]):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg error:\n{result.stderr[-2000:]}")

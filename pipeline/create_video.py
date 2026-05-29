"""
FFmpeg-based video assembly.

Loops a short audio track to fill VIDEO_DURATION_SECONDS, then combines
with a static image (+ slow Ken Burns zoom) to produce a 1920x1080 MP4.

get_ffmpeg_binary() + concat approach lifted from MoneyPrinterTurbo:
https://github.com/harry0703/MoneyPrinterTurbo/blob/main/app/services/video.py
"""

import os
import shutil
import subprocess
import tempfile
from config import VIDEO_DURATION_SECONDS, VIDEO_WIDTH, VIDEO_HEIGHT


def get_ffmpeg_binary() -> str:
    """
    Resolve FFmpeg executable — checks in order:
      1. IMAGEIO_FFMPEG_EXE env var (explicit override)
      2. System PATH (brew / apt install)
      3. imageio_ffmpeg bundled binary (pip install imageio-ffmpeg)
      4. Falls back to bare 'ffmpeg' and lets subprocess surface the error
    """
    configured = os.environ.get("IMAGEIO_FFMPEG_EXE")
    if configured:
        return configured

    system_ffmpeg = shutil.which("ffmpeg")
    if system_ffmpeg:
        return system_ffmpeg

    try:
        import imageio_ffmpeg
        bundled = imageio_ffmpeg.get_ffmpeg_exe()
        if bundled:
            return bundled
    except Exception:
        pass

    return "ffmpeg"


def build_video(audio_path: str, artwork_path: str, output_path: str) -> str:
    """
    Combine audio (looped to VIDEO_DURATION_SECONDS) + artwork (Ken Burns zoom)
    into a single MP4. Returns output_path.
    """
    print(f"  [ffmpeg] Building {VIDEO_DURATION_SECONDS // 3600}h video...")
    print(f"  [ffmpeg] Using binary: {get_ffmpeg_binary()}")

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


def concat_clips(clip_files: list, output_path: str, output_dir: str, threads: int = 2):
    """
    Lossless concatenation of multiple MP4 clips using FFmpeg concat demuxer.
    No re-encoding — fast and quality-safe.
    Lifted from MoneyPrinterTurbo concat_video_clips_with_ffmpeg().
    """
    concat_list = os.path.join(output_dir, "ffmpeg-concat-list.txt")
    with open(concat_list, "w", encoding="utf-8") as f:
        for clip in clip_files:
            escaped = os.path.abspath(clip).replace("'", "'\\''")
            f.write(f"file '{escaped}'\n")

    try:
        _run([
            get_ffmpeg_binary(), "-y",
            "-f", "concat", "-safe", "0", "-i", concat_list,
            "-c:v", "libx264", "-threads", str(threads),
            "-pix_fmt", "yuv420p",
            output_path,
        ])
    finally:
        try:
            os.remove(concat_list)
        except Exception:
            pass


# ── Private helpers ────────────────────────────────────────────────────────────

def _loop_audio(src: str, dest: str):
    """Stream-loop audio to exactly VIDEO_DURATION_SECONDS with no re-encode."""
    print(f"  [ffmpeg] Looping audio to {VIDEO_DURATION_SECONDS}s...")
    _run([
        get_ffmpeg_binary(), "-y",
        "-stream_loop", "-1",
        "-i", src,
        "-t", str(VIDEO_DURATION_SECONDS),
        "-c", "copy",
        dest,
    ])


def _render_video(image_path: str, audio_path: str, output_path: str):
    """
    Render static image + audio into an MP4 with a slow Ken Burns zoom.

    Strategy from MoneyPrinterTurbo: scale image to fill frame, then
    apply zoompan from 1.0x → 1.05x over the full duration.
    Encoding at 1fps keeps render time fast — imperceptible on a static image.
    """
    print(f"  [ffmpeg] Rendering video (few minutes)...")

    zoom_filter = (
        f"scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}:force_original_aspect_ratio=increase,"
        f"crop={VIDEO_WIDTH}:{VIDEO_HEIGHT},"
        f"zoompan="
        f"z='min(zoom+0.00005,1.05)':"
        f"x='iw/2-(iw/zoom/2)':"
        f"y='ih/2-(ih/zoom/2)':"
        f"d={VIDEO_DURATION_SECONDS}:"
        f"s={VIDEO_WIDTH}x{VIDEO_HEIGHT}:"
        f"fps=1"
    )

    _run([
        get_ffmpeg_binary(), "-y",
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
        "-r", "1",
        "-c:a", "aac",
        "-b:a", "192k",
        "-t", str(VIDEO_DURATION_SECONDS),
        "-movflags", "+faststart",
        output_path,
    ])


def _run(cmd: list):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg error:\n{result.stderr[-2000:]}")

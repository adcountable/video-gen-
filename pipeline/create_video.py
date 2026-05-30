"""
FFmpeg-based video assembly.

Two formats:
  vinyl  — spinning white vinyl record on black background (@safeplaceinhere style)
  scene  — slow Ken Burns zoom over AI oil painting + channel name overlay (Leisure Dept. style)

get_ffmpeg_binary() + concat lifted from MoneyPrinterTurbo.
"""

import os
import shutil
import subprocess
import tempfile
from config import VIDEO_DURATION_SECONDS, VIDEO_WIDTH, VIDEO_HEIGHT

VINYL_SIZE   = 900   # vinyl diameter in pixels (centered in 1920x1080)
ROTATION_SEC = 20    # seconds per full rotation — slow and hypnotic
FPS          = 24    # smooth playback


def get_ffmpeg_binary() -> str:
    """Resolve FFmpeg — env var → PATH → imageio_ffmpeg bundled."""
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


def build_video(
    audio_path: str,
    art_path: str,
    output_path: str,
    video_format: str = "vinyl",
    channel_name: str = "",
) -> str:
    """
    Combine looped audio + artwork into a 1hr MP4.

    vinyl mode: spinning vinyl record on black background
    scene mode: slow Ken Burns zoom over scene painting with channel name overlay

    Returns output_path.
    """
    print(f"  [ffmpeg] Building {VIDEO_DURATION_SECONDS // 3600}h video ({video_format} format)...")

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
        looped_audio = tmp.name

    try:
        _loop_audio(audio_path, looped_audio)
        if video_format == "scene":
            _render_scene(art_path, looped_audio, output_path, channel_name)
        else:
            _render_spinning_vinyl(art_path, looped_audio, output_path)
    finally:
        if os.path.exists(looped_audio):
            os.remove(looped_audio)

    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"  [ffmpeg] Video ready → {output_path} ({size_mb:.0f} MB)")
    return output_path


def concat_clips(clip_files: list, output_path: str, output_dir: str, threads: int = 2):
    """Lossless multi-clip concat via FFmpeg concat demuxer."""
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
            "-pix_fmt", "yuv420p", output_path,
        ])
    finally:
        try:
            os.remove(concat_list)
        except Exception:
            pass


# ── Private helpers ────────────────────────────────────────────────────────────

def _loop_audio(src: str, dest: str):
    print(f"  [ffmpeg] Looping audio to {VIDEO_DURATION_SECONDS}s...")
    _run([
        get_ffmpeg_binary(), "-y",
        "-stream_loop", "-1", "-i", src,
        "-t", str(VIDEO_DURATION_SECONDS),
        "-c", "copy", dest,
    ])


def _render_spinning_vinyl(vinyl_path: str, audio_path: str, output_path: str):
    """
    Render spinning vinyl on black background.

    Filter chain:
      1. Scale vinyl image to VINYL_SIZE × VINYL_SIZE
      2. Rotate with constant angular velocity (2π / ROTATION_SEC per second)
         — corner fill is black so it blends into background
      3. Overlay centered on a 1920×1080 black background
    """
    print(f"  [ffmpeg] Rendering spinning vinyl ({FPS}fps, {ROTATION_SEC}s/rotation)...")

    x = (VIDEO_WIDTH  - VINYL_SIZE) // 2
    y = (VIDEO_HEIGHT - VINYL_SIZE) // 2

    filter_complex = (
        f"[0:v]scale={VINYL_SIZE}:{VINYL_SIZE}[vinyl_raw];"
        f"[vinyl_raw]rotate=2*PI*t/{ROTATION_SEC}:"
        f"c=black:ow={VINYL_SIZE}:oh={VINYL_SIZE}[vinyl];"
        f"color=black:size={VIDEO_WIDTH}x{VIDEO_HEIGHT}:rate={FPS}[bg];"
        f"[bg][vinyl]overlay={x}:{y}[v]"
    )

    _run([
        get_ffmpeg_binary(), "-y",
        "-loop", "1", "-framerate", str(FPS), "-i", vinyl_path,
        "-i", audio_path,
        "-filter_complex", filter_complex,
        "-map", "[v]",
        "-map", "1:a",
        "-c:v", "libx264",
        "-preset", "faster",
        "-crf", "23",
        "-pix_fmt", "yuv420p",
        "-r", str(FPS),
        "-c:a", "aac",
        "-b:a", "192k",
        "-t", str(VIDEO_DURATION_SECONDS),
        "-movflags", "+faststart",
        output_path,
    ])


def _render_scene(scene_path: str, audio_path: str, output_path: str, channel_name: str = ""):
    """
    Render Leisure Dept-style video:
      - 16:9 oil painting scene fills frame
      - Very slow Ken Burns zoom (1.0x → 1.08x over the full hour) — barely perceptible
      - Channel name in elegant script font overlaid top-center, semi-transparent
    """
    print(f"  [ffmpeg] Rendering scene video with Ken Burns zoom...")

    # Ken Burns: zoom from 1.0 to 1.08 over VIDEO_DURATION_SECONDS
    # zoompan filter: z=zoom expression, x/y keep center, d=total frames
    total_frames = VIDEO_DURATION_SECONDS * FPS
    zoom_end     = 1.08
    zoom_expr    = f"1+({zoom_end}-1)*on/{total_frames}"  # on = output frame number
    cx_expr      = f"iw/2-(iw/zoom/2)"
    cy_expr      = f"ih/2-(ih/zoom/2)"

    # Text overlay — channel name, top-center, script-like font
    font_size = 72
    text_color = "white@0.85"

    # Sanitize channel name for ffmpeg drawtext (escape colons, apostrophes)
    safe_name = channel_name.replace("'", "\\'").replace(":", "\\:") if channel_name else ""

    if safe_name:
        text_filter = (
            f",drawtext=text='{safe_name}'"
            f":fontsize={font_size}"
            f":fontcolor={text_color}"
            f":x=(w-text_w)/2"
            f":y=h*0.08"
            f":shadowcolor=black@0.5:shadowx=2:shadowy=2"
        )
    else:
        text_filter = ""

    filter_complex = (
        f"[0:v]scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}:force_original_aspect_ratio=cover,"
        f"crop={VIDEO_WIDTH}:{VIDEO_HEIGHT},"
        f"zoompan=z='{zoom_expr}':x='{cx_expr}':y='{cy_expr}'"
        f":d={total_frames}:s={VIDEO_WIDTH}x{VIDEO_HEIGHT}:fps={FPS}"
        f"{text_filter}[v]"
    )

    _run([
        get_ffmpeg_binary(), "-y",
        "-loop", "1", "-framerate", str(FPS), "-i", scene_path,
        "-i", audio_path,
        "-filter_complex", filter_complex,
        "-map", "[v]",
        "-map", "1:a",
        "-c:v", "libx264",
        "-preset", "faster",
        "-crf", "23",
        "-pix_fmt", "yuv420p",
        "-r", str(FPS),
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

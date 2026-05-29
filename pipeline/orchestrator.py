"""Runs the full pipeline for one video: music → art → video → upload."""

import os
import time
from config import OUTPUT_DIR
from pipeline.generate_music import generate_track, download_audio
from pipeline.generate_art import generate_artwork
from pipeline.create_video import build_video
from pipeline.upload_youtube import upload_video


def run(channel_module, channel_slug: str, dry_run: bool = False):
    """
    channel_module: imported channels.work_music or channels.sleep_music
    channel_slug:   'work' or 'sleep' (used for OAuth token caching)
    dry_run:        build video locally but skip the YouTube upload
    """
    config = channel_module.get_random_config()
    run_id = str(int(time.time()))
    out = os.path.join(OUTPUT_DIR, run_id)
    os.makedirs(out, exist_ok=True)

    audio_path = os.path.join(out, "track.mp3")
    art_path = os.path.join(out, "artwork.jpg")
    video_path = os.path.join(out, "video.mp4")

    print(f"\n{'='*60}")
    print(f"Channel: {channel_module.CHANNEL_NAME}")
    print(f"Title:   {config['title']}")
    print(f"{'='*60}\n")

    # 1. Generate music (5-min clip, looped to 1hr in build_video)
    audio_url_or_path = generate_track(config["music_prompt"])
    download_audio(audio_url_or_path, audio_path)

    # 2. Generate artwork
    generate_artwork(config["art_prompt"], art_path)

    # 3. Build video
    build_video(audio_path, art_path, video_path)

    if dry_run:
        print(f"\n[dry-run] Video saved to {video_path} — skipping upload.")
        return None

    # 4. Upload to YouTube
    video_id = upload_video(
        video_path=video_path,
        title=config["title"],
        description=config["description"],
        tags=config["tags"],
        category_id=config["category_id"],
        channel_slug=channel_slug,
        thumbnail_path=art_path,
    )

    print(f"\nDone! https://youtu.be/{video_id}\n")
    return video_id

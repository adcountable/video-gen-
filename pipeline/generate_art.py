"""
Artwork generation via Replicate — FLUX 1.1 Pro.

Two formats:
  vinyl  — white vinyl record with hand-drawn doodle on black background (spinning in video)
  scene  — atmospheric oil painting scene (Leisure Dept. style, static with slow Ken Burns)
"""

import os
import requests
import replicate


# ── Vinyl prompt ───────────────────────────────────────────────────────────────

VINYL_BASE_PROMPT = (
    "white vinyl record on pure black background, center hole visible, "
    "hand-drawn doodle in blue ink on the white record surface, "
    "minimalist, simple sketch style, centered, circular record, "
    "no text, clean black background, square composition — doodle: {doodle}"
)

# ── Scene prompt ───────────────────────────────────────────────────────────────

SCENE_BASE_PROMPT = (
    "cinematic oil painting, {scene}, soft warm light, impressionist brushwork, "
    "painterly texture, rich color palette, atmospheric depth, no people, no text, "
    "wide establishing shot, golden hour or soft ambient lighting, "
    "high detail, museum quality, square composition"
)


def generate_artwork(doodle_prompt: str, dest_path: str, video_format: str = "vinyl") -> str:
    """
    Generate artwork and save to dest_path.

    vinyl mode: doodle_prompt is what's drawn on the vinyl (e.g. 'sleeping moon and stars')
    scene mode: doodle_prompt describes the scene (e.g. 'cozy jazz cafe by a rainy window')

    Returns dest_path.
    """
    from config import REPLICATE_API_KEY
    os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_KEY

    if video_format == "scene":
        full_prompt = SCENE_BASE_PROMPT.format(scene=doodle_prompt)
        print(f"  [flux] Generating scene art: {doodle_prompt[:50]}...")
    else:
        full_prompt = VINYL_BASE_PROMPT.format(doodle=doodle_prompt)
        print(f"  [flux] Generating vinyl doodle: {doodle_prompt[:50]}...")

    output = replicate.run(
        "black-forest-labs/flux-1.1-pro",
        input={
            "prompt": full_prompt,
            "aspect_ratio": "16:9" if video_format == "scene" else "1:1",
            "output_format": "jpg",
            "output_quality": 95,
            "safety_tolerance": 2,
        },
    )

    image_url = str(output)
    img_data = requests.get(image_url, timeout=30).content
    with open(dest_path, "wb") as f:
        f.write(img_data)

    print(f"  [flux] Art saved → {dest_path}")
    return dest_path

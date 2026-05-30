"""
Artwork generation via Replicate — FLUX 1.1 Pro.

Uses the same Replicate account as music generation.
No OpenAI account needed.

Cost: ~$0.04/image vs $0.08 for DALL-E 3 HD
Quality: excellent — FLUX produces better images than SDXL
"""

import os
import requests
import replicate


def generate_artwork(prompt: str, dest_path: str) -> str:
    """
    Generate a 16:9 image with FLUX 1.1 Pro and save to dest_path.
    Returns dest_path.
    """
    from config import REPLICATE_API_KEY
    os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_KEY

    print(f"  [flux] Generating artwork: {prompt[:60]}...")

    output = replicate.run(
        "black-forest-labs/flux-1.1-pro",
        input={
            "prompt": prompt,
            "aspect_ratio": "16:9",
            "output_format": "jpg",
            "output_quality": 90,
            "safety_tolerance": 2,
        },
    )

    image_url = str(output)
    print(f"  [flux] Artwork generated — downloading...")

    img_data = requests.get(image_url, timeout=30).content
    with open(dest_path, "wb") as f:
        f.write(img_data)

    print(f"  [flux] Artwork saved → {dest_path}")
    return dest_path

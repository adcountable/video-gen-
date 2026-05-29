"""DALL-E 3 artwork generation via OpenAI API."""

import requests
from openai import OpenAI


def generate_artwork(prompt: str, dest_path: str) -> str:
    """
    Generate a 1792x1024 image with DALL-E 3 and save it to dest_path.
    Returns dest_path.
    """
    from config import OPENAI_API_KEY
    client = OpenAI(api_key=OPENAI_API_KEY)

    print(f"  [dalle] Generating artwork: {prompt[:60]}...")

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1792x1024",
        quality="hd",
        n=1,
        response_format="url",
    )

    image_url = response.data[0].url
    print(f"  [dalle] Artwork generated — downloading...")

    img_data = requests.get(image_url, timeout=30).content
    with open(dest_path, "wb") as f:
        f.write(img_data)

    print(f"  [dalle] Artwork saved → {dest_path}")
    return dest_path

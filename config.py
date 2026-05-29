import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
REPLICATE_API_KEY = os.environ["REPLICATE_API_KEY"]
YOUTUBE_CLIENT_SECRET_FILE = os.getenv("YOUTUBE_CLIENT_SECRET_FILE", "client_secret.json")

MUSIC_CLIP_SECONDS = 300       # 5-min clip (~$0.50) — looped to fill video
VIDEO_DURATION_SECONDS = 3600  # 1 hour
VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080

OUTPUT_DIR = "output"
TOKENS_DIR = "tokens"

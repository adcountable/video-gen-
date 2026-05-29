import os
from dotenv import load_dotenv

load_dotenv()

# API keys — validated at runtime (not import time) so --list works without .env
def _require(key: str) -> str:
    val = os.environ.get(key)
    if not val:
        raise EnvironmentError(f"Missing required env var: {key}  (add it to .env)")
    return val

def get_openai_key():     return _require("OPENAI_API_KEY")
def get_replicate_key():  return _require("REPLICATE_API_KEY")

OPENAI_API_KEY   = os.environ.get("OPENAI_API_KEY", "")
REPLICATE_API_KEY = os.environ.get("REPLICATE_API_KEY", "")

YOUTUBE_CLIENT_SECRET_FILE = os.getenv("YOUTUBE_CLIENT_SECRET_FILE", "client_secret.json")

MUSIC_CLIP_SECONDS    = 300   # 5-min clip (~$0.50) — looped to fill video
VIDEO_DURATION_SECONDS = 3600  # 1 hour
VIDEO_WIDTH  = 1920
VIDEO_HEIGHT = 1080

OUTPUT_DIR = "output"
TOKENS_DIR = "tokens"

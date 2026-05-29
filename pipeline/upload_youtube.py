"""
YouTube Data API v3 uploader with OAuth2.

First run: opens a browser for Google OAuth consent.
Token is cached in tokens/ so subsequent runs are headless.

Setup:
  1. Go to https://console.cloud.google.com
  2. Enable YouTube Data API v3
  3. Create OAuth 2.0 Client ID (Desktop app)
  4. Download as client_secret.json in this directory
"""

import os
import pickle
from typing import Optional
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from config import YOUTUBE_CLIENT_SECRET_FILE, TOKENS_DIR

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]


def _get_credentials(channel_slug: str):
    token_path = os.path.join(TOKENS_DIR, f"{channel_slug}_token.pickle")
    creds = None

    if os.path.exists(token_path):
        with open(token_path, "rb") as f:
            creds = pickle.load(f)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                YOUTUBE_CLIENT_SECRET_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open(token_path, "wb") as f:
            pickle.dump(creds, f)

    return creds


def upload_video(
    video_path: str,
    title: str,
    description: str,
    tags: list[str],
    category_id: str,
    channel_slug: str,
    thumbnail_path: Optional[str] = None,
) -> str:
    """
    Upload video_path to YouTube. Returns the YouTube video ID.
    channel_slug is used to cache the OAuth token (e.g. 'work' or 'sleep').
    """
    print(f"  [youtube] Authenticating for channel '{channel_slug}'...")
    creds = _get_credentials(channel_slug)
    youtube = build("youtube", "v3", credentials=creds)

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id,
        },
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False,
        },
    }

    media = MediaFileUpload(video_path, chunksize=-1, resumable=True, mimetype="video/mp4")

    print(f"  [youtube] Uploading: {title}")
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            pct = int(status.progress() * 100)
            print(f"  [youtube] Upload progress: {pct}%", end="\r")

    video_id = response["id"]
    print(f"\n  [youtube] Upload complete → https://youtu.be/{video_id}")

    if thumbnail_path and os.path.exists(thumbnail_path):
        _set_thumbnail(youtube, video_id, thumbnail_path)

    return video_id


def _set_thumbnail(youtube, video_id: str, thumbnail_path: str):
    print(f"  [youtube] Setting thumbnail...")
    youtube.thumbnails().set(
        videoId=video_id,
        media_body=MediaFileUpload(thumbnail_path),
    ).execute()
    print(f"  [youtube] Thumbnail set.")

"""
Suno API client for generating music tracks.

Suno API docs: https://suno.com/api-docs
You'll need a paid Suno plan with API access.
"""

import time
import requests
from config import SUNO_API_KEY

SUNO_BASE = "https://api.suno.ai/v1"


def _headers():
    return {"Authorization": f"Bearer {SUNO_API_KEY}", "Content-Type": "application/json"}


def generate_track(prompt: str, duration: int = 240) -> str:
    """
    Submit a generation job and poll until the audio file URL is returned.
    Returns the download URL for the MP3.

    duration: target seconds (Suno may cap this — check their docs for max).
    """
    print(f"  [suno] Generating track: {prompt[:60]}...")

    resp = requests.post(
        f"{SUNO_BASE}/generate",
        headers=_headers(),
        json={
            "prompt": prompt,
            "duration": duration,
            "make_instrumental": True,
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()

    # Suno returns a job/task ID — poll for completion
    job_id = data.get("id") or data.get("task_id") or data["data"]["id"]
    print(f"  [suno] Job submitted: {job_id} — polling...")

    return _poll_for_audio(job_id)


def _poll_for_audio(job_id: str, max_wait: int = 300) -> str:
    """Poll the job status endpoint until audio_url is available."""
    deadline = time.time() + max_wait
    while time.time() < deadline:
        resp = requests.get(
            f"{SUNO_BASE}/generate/{job_id}",
            headers=_headers(),
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()

        status = data.get("status") or data.get("state", "")
        audio_url = data.get("audio_url") or data.get("output", {}).get("audio_url")

        if audio_url and status in ("completed", "succeeded", "done", ""):
            print(f"  [suno] Track ready: {audio_url[:60]}...")
            return audio_url

        if status in ("failed", "error"):
            raise RuntimeError(f"Suno generation failed: {data}")

        print(f"  [suno] Status: {status} — waiting 10s...")
        time.sleep(10)

    raise TimeoutError(f"Suno job {job_id} did not complete within {max_wait}s")


def download_audio(url: str, dest_path: str) -> str:
    """Download the audio file to dest_path. Returns dest_path."""
    print(f"  [suno] Downloading audio → {dest_path}")
    with requests.get(url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with open(dest_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"  [suno] Audio saved ({_file_mb(dest_path):.1f} MB)")
    return dest_path


def _file_mb(path: str) -> float:
    import os
    return os.path.getsize(path) / (1024 * 1024)

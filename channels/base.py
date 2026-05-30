"""Base Channel class — all 25 channels are instances of this."""

import random
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Channel:
    slug: str                        # e.g. 'deep-sleep'
    name: str                        # e.g. 'Deep Sleep Music'
    music_prompts: List[str]
    vinyl_doodles: List[str]         # FLUX prompts — vinyl doodle OR scene art depending on format
    title_templates: List[str]
    description_template: str
    tags: List[str]
    chapters: List[str]              # mood names shown as chapter timestamps
    category_id: str = "10"         # YouTube Music category
    video_format: str = "vinyl"      # "vinyl" (spinning record) or "scene" (Leisure Dept-style painting)
    music_generator: str = "minimax" # "minimax" (MusicGen API $0.15) or "sleep" (free procedural)

    def get_random_config(self) -> dict:
        title = random.choice(self.title_templates)
        return {
            "music_prompt": random.choice(self.music_prompts),
            "vinyl_doodle": random.choice(self.vinyl_doodles),
            "title": title,
            "description": self._build_description(title),
            "tags": self.tags,
            "category_id": self.category_id,
            "chapters": self.chapters,
            "video_format": self.video_format,
            "music_generator": self.music_generator,
        }

    def _build_description(self, title: str) -> str:
        # Build chapter timestamps (evenly spaced across 1 hour)
        chapter_lines = []
        interval = 3600 // len(self.chapters)
        for i, name in enumerate(self.chapters):
            secs = i * interval
            m, s = divmod(secs, 60)
            h, m = divmod(m, 60)
            timestamp = f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"
            chapter_lines.append(f"{timestamp} {name}")

        chapters_block = "\n".join(chapter_lines)
        tags_str = " #".join(self.tags)
        return self.description_template.format(title=title, chapters=chapters_block, tags=tags_str)

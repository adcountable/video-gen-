"""Base Channel class — all 25 channels are instances of this."""

import random
from dataclasses import dataclass, field
from typing import List


@dataclass
class Channel:
    slug: str                        # e.g. 'deep-sleep'
    name: str                        # e.g. 'Deep Sleep Music'
    music_prompts: List[str]
    art_prompts: List[str]
    title_templates: List[str]
    description_template: str
    tags: List[str]
    category_id: str = "10"          # YouTube Music category

    def get_random_config(self) -> dict:
        title = random.choice(self.title_templates)
        return {
            "music_prompt": random.choice(self.music_prompts),
            "art_prompt": random.choice(self.art_prompts),
            "title": title,
            "description": self.description_template.format(title=title),
            "tags": self.tags,
            "category_id": self.category_id,
        }

import random

CHANNEL_NAME = "Work Music"

MUSIC_PROMPTS = [
    "ambient lo-fi jazz, soft piano, gentle drums, deep focus, no lyrics, calm and productive",
    "smooth jazz instrumental, warm saxophone, light bass, coffee shop atmosphere, no lyrics",
    "lo-fi hip hop beats, mellow guitar, soft vinyl crackle, study music, no lyrics",
    "ambient electronic, soft synth pads, gentle percussion, focus and concentration, no lyrics",
    "piano jazz, modern, relaxed tempo, background music for work, no lyrics",
    "acoustic guitar instrumental, fingerpicking, calm and steady, focus music, no lyrics",
    "chillout electronic, warm bass, soft melody, deep work, no lyrics",
    "lo-fi jazz fusion, Rhodes piano, light brushed drums, productive atmosphere, no lyrics",
]

ART_PROMPTS = [
    "minimalist workspace illustration, warm desk lamp, coffee cup, soft blues and greens, calm productive atmosphere, digital art",
    "abstract geometric art, cool tones, deep focus, flowing shapes, blues and teals, professional aesthetic",
    "cozy coffee shop interior painting, warm lighting, bookshelves, plants, muted earth tones",
    "minimalist mountain landscape, misty morning, blues and grays, serene and focused, watercolor style",
    "abstract flowing waves, cool blues and greens, calm ocean, meditative, digital painting",
    "modern library interior, soft lighting, books, peaceful study space, warm amber tones",
    "overhead aerial view of city at dusk, cool tones, lights beginning to glow, focus and clarity",
    "minimalist forest path, dappled light, greens and browns, peaceful solitude, watercolor",
]

TITLE_TEMPLATES = [
    "Deep Focus Music – 1 Hour Jazz & Lo-Fi Beats for Work",
    "Smooth Jazz for Concentration – 1 Hour Study Music",
    "Lo-Fi Jazz Beats – 1 Hour Work Music, No Lyrics",
    "Focus Music – 1 Hour Ambient Jazz for Deep Work",
    "Coffee Shop Jazz – 1 Hour Background Music for Work",
    "Chill Lo-Fi Beats – 1 Hour Productive Study Music",
    "Ambient Jazz – 1 Hour Music to Help You Focus",
    "Work Music Mix – 1 Hour Lo-Fi Jazz & Chillout Beats",
]

DESCRIPTION_TEMPLATE = """{title}

Use this music as your background soundtrack for deep work, studying, coding, writing, or any task that needs sustained focus.

♫ 1 hour of continuous music — no interruptions
♫ No lyrics — designed for concentration
♫ Lo-fi jazz & ambient beats

---
🔔 Subscribe for new focus music every week.

#WorkMusic #LoFiJazz #FocusMusic #StudyMusic #DeepWork #AmbientMusic #ChillBeats
"""

TAGS = [
    "work music", "focus music", "lo-fi jazz", "study music", "deep work",
    "ambient music", "background music", "concentration music", "no lyrics",
    "coffee shop music", "chill beats", "productivity music", "1 hour music",
]


def get_random_config():
    idx = random.randint(0, len(TITLE_TEMPLATES) - 1)
    title = TITLE_TEMPLATES[idx]
    return {
        "music_prompt": random.choice(MUSIC_PROMPTS),
        "art_prompt": random.choice(ART_PROMPTS),
        "title": title,
        "description": DESCRIPTION_TEMPLATE.format(title=title),
        "tags": TAGS,
        "category_id": "10",  # YouTube category: Music
    }

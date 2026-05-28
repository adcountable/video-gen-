import random

CHANNEL_NAME = "Sleep Music"

MUSIC_PROMPTS = [
    "deep sleep music, slow ambient piano, soft drones, peaceful and calming, no lyrics, very slow tempo",
    "sleep meditation music, soft synthesizer pads, gentle rain sounds, relaxing, no lyrics",
    "ambient sleep music, deep bass tones, slow breathing rhythm, peaceful night, no lyrics",
    "gentle lullaby ambient, soft bells, slow melodic piano, dreamy and calming, no lyrics",
    "delta wave ambient music, deep resonant tones, slow pulse, sleep induction, no lyrics",
    "peaceful night music, soft orchestral strings, gentle and slow, sleep and relaxation, no lyrics",
    "healing sleep music, soft synthesizer, gentle hum, tranquil atmosphere, no lyrics",
    "deep relaxation music, warm ambient pads, very slow melody, drift to sleep, no lyrics",
]

ART_PROMPTS = [
    "night sky full of stars, milky way, dark deep purples and blues, peaceful and dreamlike, digital painting",
    "moonlit ocean, gentle waves, soft silver light, deep navy and silver tones, serene, watercolor",
    "cozy bedroom at night, warm lamp light, moon visible through window, peaceful, soft illustration",
    "misty forest at night, moonlight through trees, deep purples and teals, dreamlike, digital art",
    "aurora borealis over snowy mountain lake, deep purples and greens, reflections, magical realism",
    "abstract dreamscape, soft clouds, pastel purples and blues, floating, gentle and calm, digital art",
    "cosmic nebula, deep space, purples and blues, stars, vast and peaceful, photorealistic",
    "sleeping cat in moonlight, cozy blanket, window with stars, warm and peaceful, soft illustration",
]

TITLE_TEMPLATES = [
    "Deep Sleep Music – 1 Hour Calm Ambient for Sleeping",
    "Sleep Music – 1 Hour Peaceful Ambient to Fall Asleep Fast",
    "Relaxing Sleep Music – 1 Hour Gentle Ambient Sounds",
    "Calm Sleep Music – 1 Hour Ambient for Deep Rest",
    "Sleep & Relax – 1 Hour Soothing Ambient Music",
    "Night Music – 1 Hour Deep Sleep Ambient",
    "Peaceful Sleep Music – 1 Hour Calming Sounds for Rest",
    "Sleep Deeply – 1 Hour Gentle Ambient Sleep Music",
]

DESCRIPTION_TEMPLATE = """{title}

Let this music carry you gently into a deep, restful sleep. Perfect for bedtime relaxation, meditation, stress relief, or simply winding down after a long day.

♫ 1 hour of continuous sleep music
♫ No lyrics — calm ambient tones
♫ Designed to help you relax and fall asleep

---
🔔 Subscribe for new sleep music every week.

#SleepMusic #AmbientMusic #RelaxingMusic #DeepSleep #MeditationMusic #CalmMusic #SleepingMusic
"""

TAGS = [
    "sleep music", "relaxing music", "ambient music", "deep sleep", "calm music",
    "meditation music", "sleep sounds", "peaceful music", "stress relief",
    "bedtime music", "sleep aid", "1 hour sleep music", "no lyrics",
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

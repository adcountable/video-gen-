"""
All 25 channel definitions.
Each channel has unique music prompts, art style, titles, and tags
so YouTube doesn't fingerprint them as the same source.
"""

from channels.base import Channel

# ── SLEEP (6 channels) ────────────────────────────────────────────────────────

DEEP_SLEEP = Channel(
    slug="deep-sleep",
    name="Deep Sleep Music",
    music_prompts=[
        "deep sleep music, slow ambient piano, soft drones, delta waves, peaceful night, no lyrics, 60 bpm",
        "dark ambient sleep music, low bass hum, slow breathing rhythm, deep rest, no lyrics",
        "sleep induction music, deep resonant tones, slow pulse, healing frequencies, no lyrics",
        "midnight ambient, warm synth pads, very slow melody, drift to unconsciousness, no lyrics",
        "deep sleep soundscape, ocean of sound, slow oscillating bass, peaceful void, no lyrics",
    ],
    art_prompts=[
        "moonlit ocean at midnight, deep navy and black, silver reflections, perfectly still water, cinematic",
        "night sky full of stars over dark mountains, milky way, deep purples and blacks, photorealistic",
        "abstract void of deep space, slow nebula swirl, dark purples and blues, meditative, digital art",
        "lone lighthouse beam on dark ocean, midnight, deep navy, peaceful isolation, oil painting style",
        "underwater bioluminescence, deep ocean, dark blues, soft glowing particles, dreamlike",
    ],
    title_templates=[
        "Deep Sleep Music – 1 Hour Delta Waves for Falling Asleep Fast",
        "Sleep Instantly – 1 Hour Deep Sleep Music, No Ads",
        "Deep Sleep – 1 Hour Calming Music to Fall Asleep",
        "1 Hour Sleep Music – Deep Rest & Relaxation, No Lyrics",
        "Fall Asleep in Minutes – 1 Hour Deep Sleep Ambient",
    ],
    description_template="""{title}

Let this music guide you into a deep, restorative sleep. Designed with slow delta-wave rhythms to calm your nervous system and ease you into rest.

♫ 1 hour of uninterrupted sleep music
♫ No lyrics — pure ambient tones
♫ Delta wave frequencies for deep rest

🔔 New sleep music every week — Subscribe

#DeepSleep #SleepMusic #AmbientMusic #DeltaWaves #FallAsleepFast #RelaxingMusic
""",
    tags=["deep sleep", "sleep music", "delta waves", "fall asleep fast", "ambient music",
          "relaxing music", "1 hour sleep", "no lyrics", "sleep aid", "insomnia relief"],
)

BABY_SLEEP = Channel(
    slug="baby-sleep",
    name="Baby Sleep Music",
    music_prompts=[
        "gentle baby lullaby, soft music box melody, slow and soothing, innocent and peaceful, no lyrics",
        "baby sleep music, soft piano lullaby, gentle harp, slow tempo, nursery ambient, no lyrics",
        "calming baby music, warm music box, slow gentle melody, safe and cozy, no lyrics",
        "infant sleep soundscape, soft white noise blend, gentle lullaby undertones, womb-like warmth, no lyrics",
        "nursery lullaby ambient, soft bells, slow breathing rhythm, gentle and safe, no lyrics",
    ],
    art_prompts=[
        "cozy nursery at night, soft moonlight, stuffed animals, warm pastel colors, gentle illustration",
        "sleeping baby animals in a nest, soft watercolor, pastel pinks and yellows, gentle and safe",
        "moon and stars nursery illustration, pastel blues and whites, soft clouds, children's book style",
        "gentle night sky with sleeping clouds, pastel purples and pinks, soft stars, lullaby illustration",
        "cozy wooden crib with soft blankets, warm amber nightlight, toys, peaceful nursery, watercolor",
    ],
    title_templates=[
        "Baby Sleep Music – 1 Hour Gentle Lullaby for Newborns",
        "Lullaby for Babies – 1 Hour Soft Music to Sleep",
        "Baby Sleep – 1 Hour Calming Music for Infants & Toddlers",
        "Gentle Baby Lullaby – 1 Hour Soothing Sleep Music",
        "1 Hour Baby Sleep Music – Calm & Peaceful for Newborns",
    ],
    description_template="""{title}

Gentle, soothing music designed to help babies and toddlers drift peacefully to sleep. Safe for newborns — no sudden sounds or beats.

♫ 1 hour of continuous gentle lullaby music
♫ No sudden sounds — safe for newborns
♫ Calming and soothing for infants & toddlers

🔔 Subscribe for new baby sleep music weekly

#BabySleep #Lullaby #BabyMusic #InfantSleep #NewbornSleep #ToddlerSleep #GentleMusic
""",
    tags=["baby sleep music", "lullaby", "baby lullaby", "newborn sleep", "infant sleep",
          "toddler sleep", "gentle music", "nursery music", "baby calm", "sleep baby"],
)

SLEEP_MEDITATION = Channel(
    slug="sleep-meditation",
    name="Sleep Meditation Music",
    music_prompts=[
        "sleep meditation music, slow tibetan bowl resonance, soft ambient drone, mindful rest, no lyrics",
        "guided meditation sleep music, soft synthesizer, gentle bells, theta waves, peaceful mind, no lyrics",
        "sleep yoga nidra music, slow ambient, warm low tones, body scan relaxation, no lyrics",
        "healing sleep meditation, 432hz tuning, soft harmonics, deep body relaxation, no lyrics",
        "sleep meditation soundscape, distant chimes, slow breath-like waves, conscious rest, no lyrics",
    ],
    art_prompts=[
        "person meditating on mountain at sunset, silhouette, golden and purple sky, spiritual, digital art",
        "lotus flower floating on still dark water, moonlight, deep purples, spiritual peace, photorealistic",
        "cosmic meditation scene, person floating in space, galaxies, deep blues and golds, surreal art",
        "ancient stone circle at night, stars, soft mist, spiritual energy, cinematic photography style",
        "mandala glowing softly in dark space, purples and golds, sacred geometry, peaceful, digital art",
    ],
    title_templates=[
        "Sleep Meditation Music – 1 Hour Healing Sounds for Deep Rest",
        "Meditation for Sleep – 1 Hour Calming Ambient Music",
        "Sleep Meditation – 1 Hour Tibetan Bowls & Ambient Sounds",
        "1 Hour Sleep Meditation Music – Heal & Restore While You Sleep",
        "Peaceful Sleep Meditation – 1 Hour Deep Relaxation Music",
    ],
    description_template="""{title}

Designed for sleep meditation and yoga nidra practice. These healing sounds guide your mind into a state of conscious rest and deep relaxation.

♫ 1 hour of sleep meditation music
♫ Tibetan bowl harmonics & ambient tones
♫ Supports yoga nidra & body scan practice

🔔 Subscribe for new meditation music weekly

#SleepMeditation #YogaNidra #MeditationMusic #HealingMusic #TibetanBowls #DeepSleep
""",
    tags=["sleep meditation", "meditation music", "yoga nidra", "tibetan bowls", "healing music",
          "deep sleep", "relaxation music", "theta waves", "mindful sleep", "432hz"],
)

RAIN_SLEEP = Channel(
    slug="rain-sleep",
    name="Rain Sleep Sounds",
    music_prompts=[
        "rain sleep music, soft piano with gentle rain sounds, cozy and peaceful, no lyrics, slow tempo",
        "rainy night ambient, light rain on window, slow ambient melody, warm indoor feeling, no lyrics",
        "sleep rain soundscape, steady gentle rain, distant thunder, soft piano undertones, no lyrics",
        "rainy day sleep music, heavy rain on rooftop, slow drone, peaceful and drowsy, no lyrics",
        "forest rain sleep sounds, nature rain, light wind, soft ambient tones, no lyrics",
    ],
    art_prompts=[
        "rainy night window with warm light inside, cozy room visible, rain drops on glass, cinematic",
        "forest in heavy rain, green canopy, water droplets, misty atmosphere, peaceful, photography",
        "cozy cabin in rain, warm lamp glow, rain on roof, forest surroundings, watercolor painting",
        "city street in soft rain at night, reflections on wet pavement, amber streetlights, moody",
        "Japanese zen garden in rain, stone lantern, moss, soft rain ripples in pond, serene photography",
    ],
    title_templates=[
        "Rain Sleep Music – 1 Hour Gentle Rain & Piano for Deep Sleep",
        "Rainy Night Sleep Sounds – 1 Hour Peaceful Rain Ambience",
        "Sleep to the Rain – 1 Hour Relaxing Rain Sounds & Music",
        "1 Hour Rain Sleep – Cozy Rainy Night Ambient for Rest",
        "Rain on Window – 1 Hour Sleep Sounds for Deep Rest",
    ],
    description_template="""{title}

The most natural sleep aid — the gentle sound of rain combined with soft ambient music. Perfect for insomnia, stress relief, and deep relaxation.

♫ 1 hour of gentle rain sounds & ambient music
♫ No lyrics — pure nature + piano tones
♫ Perfect for sleep, study, or relaxation

🔔 New rain sleep sounds every week — Subscribe

#RainSounds #SleepMusic #RainAndPiano #NatureSounds #RainSleep #AmbientRain
""",
    tags=["rain sounds", "rain sleep", "rain and piano", "sleep music", "rain ambience",
          "nature sounds", "rainy night", "cozy rain", "sleep sounds", "rain for sleep"],
)

HZ432_SLEEP = Channel(
    slug="432hz-sleep",
    name="432Hz Sleep Music",
    music_prompts=[
        "432hz tuned sleep music, healing frequency, slow ambient piano, DNA repair vibrations, no lyrics",
        "432hz frequency music, pure tones, slow harmonic drone, cellular healing sleep, no lyrics",
        "432hz solfeggio sleep, warm resonant tones, ancient tuning, deep body healing, no lyrics",
        "432hz sleep induction, pure sine wave harmonics, slow vibration, quantum healing, no lyrics",
        "432hz healing music, tibetan frequencies, slow ambient waves, pineal gland activation, no lyrics",
    ],
    art_prompts=[
        "golden ratio spiral glowing in dark space, sacred geometry, gold and purple, healing energy",
        "sound wave visualization glowing in blues and golds, frequency art, dark background, digital art",
        "DNA helix bathed in golden light, healing frequency waves, dark background, scientific beauty",
        "ancient tuning fork radiating golden sound waves, sacred geometry background, mystical digital art",
        "human silhouette filled with golden healing light, frequency waves, dark space, spiritual art",
    ],
    title_templates=[
        "432Hz Sleep Music – 1 Hour Healing Frequency for Deep Rest",
        "432Hz – 1 Hour Deep Sleep Healing Music, Remove Negativity",
        "432Hz Miracle Tone – 1 Hour Sleep Music & Healing Frequency",
        "1 Hour 432Hz Sleep Music – Full Body Healing While You Sleep",
        "432Hz Deep Sleep – 1 Hour Pure Healing Frequency Music",
    ],
    description_template="""{title}

Tuned to 432Hz — the natural healing frequency. Many believe 432Hz resonates with the universe's natural rhythm, promoting deep cellular healing and restoration during sleep.

♫ 1 hour of 432Hz tuned sleep music
♫ Healing frequency for body & mind restoration
♫ No lyrics — pure frequency tones

🔔 Subscribe for new healing frequency music

#432Hz #HealingFrequency #SleepMusic #432HzMusic #HealingMusic #SolfeggioFrequency
""",
    tags=["432hz", "healing frequency", "432hz music", "sleep music", "solfeggio",
          "healing sleep", "frequency healing", "dna repair", "deep sleep", "432hz sleep"],
)

BINAURAL_SLEEP = Channel(
    slug="binaural-sleep",
    name="Binaural Beats Sleep",
    music_prompts=[
        "binaural beats sleep music, delta 2hz, soft ambient carrier, deep sleep induction, no lyrics",
        "theta binaural beats, 4-8hz, slow ambient music, dream state induction, no lyrics",
        "delta wave binaural, 0.5hz deep sleep, warm carrier tone, unconscious rest, no lyrics",
        "sleep binaural beats, soft drone carrier, 3hz delta, brain entrainment for sleep, no lyrics",
        "deep sleep binaural, 1hz delta waves, peaceful ambient, full sleep cycle support, no lyrics",
    ],
    art_prompts=[
        "brain wave visualization, delta waves glowing blue, dark background, neuroscience art",
        "two hemispheres of brain synchronizing with golden light, dark space, scientific beauty",
        "sound wave interference pattern creating binaural effect, blues and purples, digital art",
        "person sleeping with brainwave visualization overlay, peaceful, blues and greens, digital art",
        "abstract sound frequency landscape, deep blues, slow waves, binaural geometry, digital art",
    ],
    title_templates=[
        "Binaural Beats Sleep – 1 Hour Delta Waves for Deep Sleep",
        "Delta Waves – 1 Hour Binaural Beats Sleep Music",
        "Sleep Binaural Beats – 1 Hour Brain Entrainment for Deep Rest",
        "1 Hour Delta Wave Binaural Beats – Fall Asleep Fast",
        "Binaural Sleep – 1 Hour Deep Delta Waves for Insomnia",
    ],
    description_template="""{title}

⚠️ Use headphones for full binaural effect.

These delta wave binaural beats (0.5–4Hz) are designed to synchronize your brainwaves with deep sleep frequencies, helping you fall asleep faster and sleep more deeply.

♫ 1 hour of delta wave binaural beats
♫ Headphones recommended for best effect
♫ Supports deep sleep & insomnia relief

🔔 Subscribe for new binaural beat music

#BinauralBeats #DeltaWaves #SleepMusic #BrainEntrainment #BinauralSleep #DeepSleep
""",
    tags=["binaural beats", "delta waves", "binaural sleep", "brain entrainment", "sleep music",
          "delta wave sleep", "binaural beats sleep", "insomnia", "deep sleep", "headphones"],
)


# ── FOCUS (6 channels) ────────────────────────────────────────────────────────

LOFI_STUDY = Channel(
    slug="lofi-study",
    name="Lo-Fi Study Music",
    music_prompts=[
        "lo-fi hip hop study beats, mellow guitar, soft vinyl crackle, chill and focused, no lyrics",
        "lo-fi study music, warm Rhodes piano, lazy drums, coffee shop vibe, no lyrics",
        "chill lo-fi beats, dusty samples, slow hip hop groove, productive study session, no lyrics",
        "lo-fi jazz hop, vintage piano, soft bass, rainy day study vibes, no lyrics",
        "lo-fi chill beats, lo-fi guitar, tape hiss, bedroom producer aesthetic, study focus, no lyrics",
    ],
    art_prompts=[
        "anime-style girl studying at desk by rainy window, warm desk lamp, books, cozy lo-fi aesthetic",
        "cozy bedroom study setup, glowing screen, plants, city view at night, lo-fi anime aesthetic",
        "vintage cassette tape with city lights reflection, warm tones, lo-fi aesthetic, illustration",
        "person studying in cozy coffee shop, rain outside, warm amber tones, lo-fi illustration",
        "rooftop study spot at night, city skyline, stars, warm light, lo-fi anime aesthetic",
    ],
    title_templates=[
        "Lo-Fi Study Music – 1 Hour Chill Beats for Focus",
        "Lo-Fi Hip Hop – 1 Hour Study & Relax Beats",
        "Study Lo-Fi – 1 Hour Chill Music for Homework & Focus",
        "1 Hour Lo-Fi Beats – Study, Work, Relax",
        "Chill Lo-Fi Study Music – 1 Hour No Lyrics Focus Beats",
    ],
    description_template="""{title}

The classic lo-fi study session playlist. Chill, mellow beats designed to keep you focused without distracting you from your work.

♫ 1 hour of lo-fi hip hop & jazz beats
♫ No lyrics — pure chill focus music
♫ Perfect for studying, homework & creative work

🔔 Subscribe for new lo-fi beats weekly

#LoFi #StudyMusic #LoFiHipHop #ChillBeats #StudyBeats #FocusMusic
""",
    tags=["lo-fi", "study music", "lo-fi hip hop", "chill beats", "study beats",
          "focus music", "homework music", "lo-fi study", "chill music", "no lyrics"],
)

DEEP_WORK_JAZZ = Channel(
    slug="deep-work-jazz",
    name="Deep Work Jazz",
    music_prompts=[
        "smooth jazz instrumental for deep work, warm saxophone, light bass, focused energy, no lyrics",
        "modern jazz work music, Rhodes piano, brushed drums, coffee shop ambiance, no lyrics",
        "jazz fusion focus music, mellow guitar, upright bass, productive flow state, no lyrics",
        "cool jazz work session, muted trumpet, soft piano, clean rhythm section, no lyrics",
        "ambient jazz for concentration, sparse piano, slow brushed snare, deep focus, no lyrics",
    ],
    art_prompts=[
        "jazz musician silhouette in smoky blue club, moody lighting, deep blues and ambers, cinematic",
        "vintage vinyl record with city rain reflection, warm amber tones, jazz aesthetic, photography",
        "modern office at night, city view, warm lamp, coffee, sophisticated jazz aesthetic",
        "saxophone close-up with bokeh city lights background, golden tones, jazz photography style",
        "minimalist jazz club interior, dim lighting, empty stage, deep blues, sophisticated atmosphere",
    ],
    title_templates=[
        "Deep Work Jazz – 1 Hour Smooth Jazz for Focus & Productivity",
        "Jazz for Deep Work – 1 Hour Concentration Music",
        "Smooth Jazz Work Music – 1 Hour Background Jazz for Office",
        "1 Hour Deep Work Jazz – Flow State Music for Professionals",
        "Focus Jazz – 1 Hour Smooth Background Music for Work",
    ],
    description_template="""{title}

Smooth jazz curated for deep work sessions. The right tempo and energy to keep you in a productive flow state without distraction.

♫ 1 hour of smooth jazz for concentration
♫ No lyrics — pure instrumental jazz
♫ Ideal for office work, writing & creative projects

🔔 Subscribe for weekly jazz work music

#DeepWorkJazz #SmoothJazz #WorkMusic #JazzInstrumental #FocusMusic #ProductivityMusic
""",
    tags=["deep work jazz", "smooth jazz", "work music", "jazz instrumental", "focus music",
          "productivity music", "office music", "jazz focus", "background jazz", "concentration"],
)

CODING_MUSIC = Channel(
    slug="coding-music",
    name="Coding Music",
    music_prompts=[
        "electronic focus music for coding, ambient techno, steady pulse, deep concentration, no lyrics",
        "coding music, minimal electronic, synth arpeggios, hypnotic flow state, no lyrics",
        "programmer music, dark ambient electronic, repetitive patterns, deep focus, no lyrics",
        "coding flow music, driving synth bass, minimal techno, zone-in beats, no lyrics",
        "hacker ambient music, glitch electronic, steady rhythm, deep work concentration, no lyrics",
    ],
    art_prompts=[
        "dark coding setup, multiple monitors with code, blue light, mechanical keyboard, aesthetic photography",
        "neon-lit keyboard and screen with code, cyberpunk aesthetic, blues and purples, digital art",
        "matrix-style code rain in dark room, green glow, programmer aesthetic, digital art",
        "minimalist dark desk with glowing terminal, deep focus atmosphere, blue tones, photography",
        "cyberpunk city at night from programmer window, neon reflections, dark aesthetic, digital art",
    ],
    title_templates=[
        "Coding Music – 1 Hour Electronic Focus Beats for Programming",
        "Music for Coding – 1 Hour Deep Focus Electronic",
        "Programmer Music – 1 Hour Flow State Beats for Coding",
        "1 Hour Coding Music – Electronic Beats for Deep Work",
        "Code in Flow – 1 Hour Focus Music for Developers",
    ],
    description_template="""{title}

Electronic music engineered for deep coding sessions. Repetitive, hypnotic patterns that keep your brain in a focused flow state.

♫ 1 hour of electronic focus music
♫ No lyrics — pure programming fuel
♫ Designed for deep work & flow states

🔔 Subscribe for new coding music weekly

#CodingMusic #ProgrammerMusic #FocusMusic #ElectronicMusic #FlowState #DeepWork
""",
    tags=["coding music", "programmer music", "focus music", "electronic music", "flow state",
          "deep work music", "programming music", "coder music", "music for coding", "techno focus"],
)

COFFEE_SHOP_BEATS = Channel(
    slug="coffee-shop-beats",
    name="Coffee Shop Music",
    music_prompts=[
        "coffee shop jazz, warm acoustic guitar, upright bass, relaxed tempo, morning cafe vibe, no lyrics",
        "cafe background music, bossa nova inspired, light percussion, warm and cozy, no lyrics",
        "coffee shop ambient, acoustic piano, gentle strings, European cafe atmosphere, no lyrics",
        "morning cafe music, light jazz guitar, soft brushed drums, relaxed and productive, no lyrics",
        "coffee shop folk jazz, acoustic instruments, warm recording, cozy independent cafe, no lyrics",
    ],
    art_prompts=[
        "cozy independent coffee shop interior, warm lighting, exposed brick, plants, people working",
        "overhead view of coffee cup and laptop on wooden table, warm morning light, cozy aesthetic",
        "rainy window of coffee shop, people inside with drinks, warm amber glow, watercolor painting",
        "barista pouring latte art, steam, warm cafe colors, golden hour light, photography style",
        "Paris sidewalk cafe, morning light, coffee and croissant, cobblestones, warm illustration",
    ],
    title_templates=[
        "Coffee Shop Music – 1 Hour Cafe Jazz for Work & Study",
        "Coffee Shop Ambience – 1 Hour Cozy Cafe Background Music",
        "Cafe Music – 1 Hour Coffee Shop Jazz & Acoustic Beats",
        "1 Hour Coffee Shop Vibes – Work Music with Cafe Atmosphere",
        "Cozy Coffee Shop – 1 Hour Background Music for Focus",
    ],
    description_template="""{title}

Bring the coffee shop to you. Warm, cozy cafe music perfect for working from home, studying, or just relaxing with a cup of coffee.

♫ 1 hour of coffee shop jazz & acoustic music
♫ No lyrics — warm cafe atmosphere
♫ Perfect for work from home & study sessions

🔔 Subscribe for new cafe music weekly

#CoffeeShopMusic #CafeMusic #CoffeeShopJazz #WorkMusic #StudyMusic #CozyMusic
""",
    tags=["coffee shop music", "cafe music", "coffee shop jazz", "work music", "study music",
          "cozy music", "background music", "cafe ambience", "acoustic music", "morning music"],
)

CLASSICAL_STUDY = Channel(
    slug="classical-study",
    name="Classical Study Music",
    music_prompts=[
        "classical piano study music, Mozart-inspired, gentle and clear, academic focus, no lyrics",
        "baroque study music, harpsichord and strings, orderly and focused, intellectual calm, no lyrics",
        "romantic classical piano, Chopin-inspired, soft and lyrical, deep concentration, no lyrics",
        "classical string quartet, soft chamber music, focused academic mood, no lyrics",
        "contemporary classical piano, minimalist, slow arpeggios, calm study atmosphere, no lyrics",
    ],
    art_prompts=[
        "grand piano in sunlit library, tall windows, books, elegant and classical, photography",
        "ancient university library, arched ceilings, warm candlelight, books everywhere, oil painting",
        "sheet music and quill pen on antique desk, warm light, classical study aesthetic, still life",
        "concert hall empty interior, golden chandeliers, red velvet, classical elegance, photography",
        "Oxford-style reading room, dark wood, green lamps, students studying, classical atmosphere",
    ],
    title_templates=[
        "Classical Music for Studying – 1 Hour Piano & Strings",
        "Study Classical Music – 1 Hour Mozart, Bach & Chopin Inspired",
        "Classical Study – 1 Hour Instrumental Music for Concentration",
        "1 Hour Classical Music – Piano for Focus & Deep Study",
        "Classical Piano Study Music – 1 Hour Academic Focus",
    ],
    description_template="""{title}

Classical and neo-classical instrumental music to sharpen focus and support deep intellectual work. Timeless compositions for timeless studying.

♫ 1 hour of classical instrumental music
♫ Piano, strings & chamber music
♫ Ideal for reading, writing & academic work

🔔 Subscribe for new classical study music

#ClassicalMusic #StudyMusic #ClassicalPiano #FocusMusic #Bach #Mozart #StudyClassical
""",
    tags=["classical music", "study music", "classical piano", "focus music", "Bach",
          "Mozart", "study classical", "instrumental classical", "academic music", "chamber music"],
)

PIANO_FOCUS = Channel(
    slug="piano-focus",
    name="Piano Focus Music",
    music_prompts=[
        "solo piano focus music, modern minimalist, slow arpeggios, deep concentration, no lyrics",
        "contemporary piano work music, sparse and clean, slow melodic phrases, mental clarity, no lyrics",
        "ambient piano for focus, soft sustain pedal, slow exploration, peaceful concentration, no lyrics",
        "cinematic piano focus, emotional but calm, slow development, productive atmosphere, no lyrics",
        "neo-classical piano, Nils Frahm inspired, soft and warm, deep work session, no lyrics",
    ],
    art_prompts=[
        "grand piano keys close-up with morning light, minimalist, black and white, elegant photography",
        "pianist hands on keys with shallow depth of field, warm tones, artistic photography",
        "single upright piano in empty white room, minimalist, soft shadows, contemporary art",
        "piano by large window overlooking misty forest, peaceful and focused, warm tones, photography",
        "abstract piano strings interior, geometric light patterns, black and white, fine art photography",
    ],
    title_templates=[
        "Piano Focus Music – 1 Hour Solo Piano for Deep Work",
        "Relaxing Piano – 1 Hour Focus Music for Study & Work",
        "Piano for Focus – 1 Hour Calm Instrumental Music",
        "1 Hour Piano Music – Deep Focus & Concentration",
        "Solo Piano Work Music – 1 Hour Peaceful Focus",
    ],
    description_template="""{title}

Pure solo piano music for deep focus. Simple, unhurried melodies that create a peaceful mental space for your best work.

♫ 1 hour of solo piano
♫ No lyrics — pure piano focus
♫ Perfect for writing, reading & creative work

🔔 Subscribe for new piano music weekly

#PianoMusic #FocusMusic #SoloPiano #StudyMusic #AmbientPiano #WorkMusic
""",
    tags=["piano music", "focus music", "solo piano", "study music", "ambient piano",
          "work music", "piano focus", "instrumental piano", "relaxing piano", "neo-classical"],
)


# ── RELAX (6 channels) ────────────────────────────────────────────────────────

SPA_MUSIC = Channel(
    slug="spa-music",
    name="Spa Relaxation Music",
    music_prompts=[
        "spa relaxation music, gentle water sounds, soft flute, peaceful sanctuary, no lyrics",
        "luxury spa ambient, warm synthesizer pads, gentle koto, zen sanctuary atmosphere, no lyrics",
        "spa meditation music, crystal singing bowls, soft nature sounds, total relaxation, no lyrics",
        "day spa music, gentle harp, flowing water, light breeze, pure relaxation, no lyrics",
        "wellness spa ambient, soft piano, bamboo flute, tropical bird sounds, peaceful retreat, no lyrics",
    ],
    art_prompts=[
        "luxury spa interior, stones, candles, orchids, warm water, serene and elegant photography",
        "zen garden with bamboo fountain, morning mist, mossy stones, soft light, Japan aesthetic",
        "massage room with candles and flowers, warm golden light, luxury spa, peaceful photography",
        "infinity pool overlooking tropical forest, misty morning, luxury wellness resort photography",
        "hot spring with flower petals, steam, natural stone, peaceful sanctuary, warm photography",
    ],
    title_templates=[
        "Spa Music – 1 Hour Relaxing Music for Massage & Wellness",
        "Luxury Spa Relaxation – 1 Hour Peaceful Ambient Music",
        "Spa & Wellness Music – 1 Hour Calming Background Music",
        "1 Hour Spa Music – Relaxation, Massage & Healing",
        "Zen Spa Music – 1 Hour Peaceful Sanctuary Sounds",
    ],
    description_template="""{title}

Transform your space into a luxury spa. This calming music is perfect for massage, facials, meditation, yoga, or simply unwinding after a long day.

♫ 1 hour of luxury spa ambient music
♫ Gentle water, flute & nature sounds
♫ Perfect for massage, yoga & self-care

🔔 Subscribe for new spa music weekly

#SpaMusic #RelaxingMusic #MassageMusic #WellnessMusic #ZenMusic #AmbientMusic
""",
    tags=["spa music", "relaxing music", "massage music", "wellness music", "zen music",
          "ambient music", "meditation music", "spa relaxation", "healing music", "peaceful music"],
)

YOGA_FLOW = Channel(
    slug="yoga-flow",
    name="Yoga Flow Music",
    music_prompts=[
        "yoga flow music, slow world music fusion, Indian tabla and sitar, fluid movement, no lyrics",
        "vinyasa yoga music, gentle electronic ambient, flowing rhythm, movement and breath, no lyrics",
        "yoga and meditation music, Tibetan instruments, slow and grounding, body awareness, no lyrics",
        "yin yoga music, slow ambient, deep drones, long-hold stretch music, no lyrics",
        "sunrise yoga music, gentle acoustic, bird sounds, awakening energy, peaceful movement, no lyrics",
    ],
    art_prompts=[
        "woman doing yoga at sunrise on mountain, silhouette, golden sky, spiritual and athletic",
        "yoga studio with morning light through windows, plants, wooden floor, peaceful photography",
        "overhead view of person in child's pose on colorful mat, minimalist, peaceful photography",
        "yoga on beach at sunset, silhouette, orange and purple sky, freedom and peace, photography",
        "Indian temple interior with yoga practitioner, morning light, spiritual atmosphere, photography",
    ],
    title_templates=[
        "Yoga Music – 1 Hour Flow Music for Practice & Meditation",
        "Yoga Flow – 1 Hour Relaxing Music for Vinyasa & Yin",
        "Yoga & Meditation Music – 1 Hour Peaceful Background",
        "1 Hour Yoga Music – Sunrise Flow & Relaxation",
        "Yoga Flow Music – 1 Hour Grounding Ambient for Practice",
    ],
    description_template="""{title}

Music crafted for your yoga practice. Whether you're flowing through vinyasa or melting into yin poses, these sounds support your movement and breath.

♫ 1 hour of yoga flow music
♫ World music, ambient & Tibetan sounds
♫ Perfect for vinyasa, yin & yoga nidra

🔔 Subscribe for new yoga music weekly

#YogaMusic #YogaFlow #YogaAmbient #VinyasaMusic #YinYoga #MeditationMusic
""",
    tags=["yoga music", "yoga flow", "vinyasa music", "yin yoga", "meditation music",
          "yoga ambient", "yoga practice music", "yoga soundtrack", "flow music", "mindful movement"],
)

ANXIETY_RELIEF = Channel(
    slug="anxiety-relief",
    name="Anxiety Relief Music",
    music_prompts=[
        "anxiety relief music, slow calming piano, grounding bass, nervous system regulation, no lyrics",
        "stress relief music, gentle orchestral, slow 60bpm, parasympathetic nervous system, no lyrics",
        "anxiety music therapy, slow ambient, warm tones, safety and calm, no lyrics",
        "panic relief music, very slow piano, deep breathing rhythm, calming, grounding, no lyrics",
        "anxiety and stress music, soft acoustic guitar, slow tempo, emotional safety, no lyrics",
    ],
    art_prompts=[
        "peaceful meadow at golden hour, soft light on grass and wildflowers, calming, photography",
        "person sitting calmly by calm lake, warm light, nature, peace and safety, soft photography",
        "breathing visualization, expanding and contracting circle, soft blues and greens, calming art",
        "safe cozy corner with blanket and soft light, warm and grounding, calm photography",
        "misty morning forest path, soft light through trees, peaceful and safe, nature photography",
    ],
    title_templates=[
        "Anxiety Relief Music – 1 Hour Calming Music for Stress",
        "Music for Anxiety – 1 Hour Calming Sounds for Relief",
        "Stress & Anxiety Relief – 1 Hour Soothing Calm Music",
        "1 Hour Anxiety Relief – Calming Music for Nervous System",
        "Calm Anxiety Music – 1 Hour Grounding Sounds for Peace",
    ],
    description_template="""{title}

Specifically designed to calm the nervous system and provide relief from anxiety and stress. Slow tempos and grounding tones to help you feel safe and present.

♫ 1 hour of anxiety relief music
♫ Slow 60bpm — nervous system regulation
♫ Grounding tones for stress & anxiety

🔔 Subscribe for new calming music weekly

#AnxietyRelief #AnxietyMusic #StressRelief #CalmingMusic #MentalHealth #RelaxingMusic
""",
    tags=["anxiety relief", "anxiety music", "stress relief", "calming music", "mental health music",
          "relaxing music", "nervous system", "grounding music", "panic relief", "calm music"],
)

NATURE_SOUNDS = Channel(
    slug="nature-sounds",
    name="Nature Sounds",
    music_prompts=[
        "forest nature soundscape, birds, gentle stream, wind in trees, pure nature, no music just ambient",
        "ocean waves nature sounds, seagulls, coastal breeze, peaceful beach, pure nature ambient",
        "mountain stream nature sounds, flowing water, birds, distant wind, pure nature recording",
        "rainforest soundscape, tropical birds, gentle rain, insects, lush nature ambient",
        "campfire nature sounds, crackling fire, night crickets, owl, peaceful outdoor night",
    ],
    art_prompts=[
        "ancient redwood forest, morning mist, golden light beams, moss-covered ground, photography",
        "wild ocean coastline, waves crashing, dramatic cliffs, sea spray, powerful nature photography",
        "alpine mountain meadow with wildflowers, crystal stream, snow peaks, summer, landscape photography",
        "tropical rainforest waterfall, lush green, mist, vibrant nature, landscape photography",
        "peaceful lake at dawn, mist on water, pine forest reflection, golden hour photography",
    ],
    title_templates=[
        "Nature Sounds – 1 Hour Forest & Birds for Relaxation",
        "Relaxing Nature Sounds – 1 Hour Ocean, Rain & Forest",
        "Nature Sounds for Sleep – 1 Hour Peaceful Outdoor Ambience",
        "1 Hour Nature Sounds – Birds, Stream & Forest Ambience",
        "Pure Nature Sounds – 1 Hour Relaxing Outdoor Soundscape",
    ],
    description_template="""{title}

Pure, unprocessed nature sounds for relaxation, sleep, focus, and stress relief. No music — just the natural world at its most peaceful.

♫ 1 hour of pure nature sounds
♫ No music — 100% natural ambience
♫ Perfect for sleep, relaxation & focus

🔔 Subscribe for new nature sounds weekly

#NatureSounds #RelaxingNature #ForestSounds #OceanSounds #BirdSounds #SleepSounds
""",
    tags=["nature sounds", "relaxing nature", "forest sounds", "ocean sounds", "bird sounds",
          "rain sounds", "sleep sounds", "nature ambience", "outdoor sounds", "white noise"],
)

MEDITATION = Channel(
    slug="meditation",
    name="Meditation Music",
    music_prompts=[
        "mindfulness meditation music, gentle Tibetan singing bowl, slow ambient, present moment awareness, no lyrics",
        "zen meditation music, Japanese koto, soft drone, emptiness and peace, no lyrics",
        "vipassana meditation music, silent ambient, very slow tones, insight and clarity, no lyrics",
        "loving kindness meditation music, warm gentle tones, open heart, compassion and peace, no lyrics",
        "transcendental meditation music, mantra-like ambient tones, deep stillness, no lyrics",
    ],
    art_prompts=[
        "Buddha statue in peaceful garden, morning dew, lotus flowers, soft morning light, photography",
        "Zen stone meditation garden, raked sand, balanced rocks, minimalist, soft light, photography",
        "person meditating at sunrise on beach, silhouette, golden light, inner peace, photography",
        "ancient temple meditation room, incense smoke, candles, golden artifacts, spiritual photography",
        "close-up of hands in mudra position, soft natural light, peaceful meditation, photography",
    ],
    title_templates=[
        "Meditation Music – 1 Hour Mindfulness & Inner Peace",
        "Mindfulness Meditation – 1 Hour Calming Music for Practice",
        "Meditation Music – 1 Hour Tibetan & Zen Sounds",
        "1 Hour Meditation – Peaceful Music for Mindfulness",
        "Zen Meditation Music – 1 Hour Stillness & Clarity",
    ],
    description_template="""{title}

Peaceful music to deepen your meditation practice. Whether you're a beginner or experienced meditator, these sounds support presence, clarity, and inner stillness.

♫ 1 hour of meditation music
♫ Tibetan bowls, Zen & mindfulness tones
♫ Supports all meditation styles

🔔 Subscribe for new meditation music

#MeditationMusic #Mindfulness #ZenMusic #TibetanBowls #MeditationAmbient #InnerPeace
""",
    tags=["meditation music", "mindfulness", "zen music", "tibetan bowls", "meditation ambient",
          "inner peace", "mindfulness music", "calming meditation", "spiritual music", "vipassana"],
)

REIKI_HEALING = Channel(
    slug="reiki-healing",
    name="Reiki Healing Music",
    music_prompts=[
        "reiki healing music, crystal singing bowls, energy flow, chakra balancing tones, no lyrics",
        "energy healing music, 528hz love frequency, warm overtones, chakra alignment, no lyrics",
        "reiki session music, soft ambient healing, auric field cleansing, light body activation, no lyrics",
        "chakra healing music, seven chakra tones, rainbow frequency, energy center alignment, no lyrics",
        "quantum healing music, scalar wave tones, DNA activation frequency, cellular regeneration, no lyrics",
    ],
    art_prompts=[
        "human body with glowing chakra energy centers, rainbow light, dark background, spiritual digital art",
        "hands performing reiki healing, golden light energy flowing, spiritual art, warm tones",
        "crystal singing bowl with sound wave visualization, light and energy, mystical photography",
        "aura photography style portrait, rainbow energy field, spiritual, colorful digital art",
        "sacred geometry mandala with chakra colors, glowing, dark space, healing energy art",
    ],
    title_templates=[
        "Reiki Music – 1 Hour Healing Energy & Chakra Balance",
        "Chakra Healing Music – 1 Hour Energy Balance & Reiki",
        "Reiki Healing – 1 Hour 528Hz & Chakra Alignment Music",
        "1 Hour Reiki Music – Energy Healing & Chakra Cleansing",
        "Healing Energy Music – 1 Hour Reiki & Chakra Balance",
    ],
    description_template="""{title}

Music attuned to healing frequencies for Reiki sessions, chakra balancing, and energy work. Use during self-treatment, sessions with clients, or personal healing practice.

♫ 1 hour of reiki healing music
♫ Crystal bowls, 528Hz & chakra tones
♫ Supports energy work & chakra balance

🔔 Subscribe for new healing music

#ReikiMusic #ChakraHealing #HealingMusic #528Hz #EnergyHealing #ChakraMusic
""",
    tags=["reiki music", "chakra healing", "healing music", "528hz", "energy healing",
          "chakra music", "crystal bowls", "reiki healing", "chakra balance", "spiritual healing"],
)


# ── MOOD (7 channels) ─────────────────────────────────────────────────────────

HAPPY_MORNING = Channel(
    slug="happy-morning",
    name="Happy Morning Music",
    music_prompts=[
        "happy morning music, upbeat acoustic guitar, cheerful piano, positive energy, sunrise vibes, no lyrics",
        "morning motivation music, bright and uplifting, light jazz, energetic start to the day, no lyrics",
        "positive morning ambient, happy piano, acoustic guitar strumming, fresh and alive, no lyrics",
        "sunrise music, optimistic acoustic, warm and bright, awakening and joyful, no lyrics",
        "morning coffee music, cheerful bossa nova, light percussion, happy productive day, no lyrics",
    ],
    art_prompts=[
        "sunrise over golden field, warm morning light, dew drops, birds flying, beautiful morning",
        "cup of coffee by sunny window, fresh flowers, morning newspaper, warm happy morning scene",
        "mountain sunrise with orange and pink sky, hiker at peak, victorious happy morning, photography",
        "beach sunrise, golden light on waves, footprints in sand, peaceful happy morning photography",
        "city skyline at sunrise, golden hour, fresh day beginning, optimistic warm tones photography",
    ],
    title_templates=[
        "Happy Morning Music – 1 Hour Uplifting Music to Start Your Day",
        "Morning Music – 1 Hour Happy & Positive Vibes",
        "Good Morning Music – 1 Hour Upbeat Acoustic for a Great Day",
        "1 Hour Happy Morning Music – Positive Energy & Good Vibes",
        "Morning Motivation Music – 1 Hour Uplifting Start to Your Day",
    ],
    description_template="""{title}

Start your day on the right note. Uplifting, positive music to energize your morning routine, boost your mood, and set the tone for an amazing day.

♫ 1 hour of happy morning music
♫ Uplifting acoustic, piano & jazz
♫ Perfect for morning routines & breakfast

🔔 Subscribe for new morning music weekly

#MorningMusic #HappyMusic #UpliftingMusic #GoodMorning #PositiveVibes #MorningMotivation
""",
    tags=["morning music", "happy music", "uplifting music", "good morning", "positive vibes",
          "morning motivation", "cheerful music", "sunrise music", "acoustic morning", "happy morning"],
)

SAD_RAINY_DAY = Channel(
    slug="sad-rainy-day",
    name="Sad Rainy Day Music",
    music_prompts=[
        "sad rainy day music, melancholic piano, slow tempo, emotional and reflective, no lyrics",
        "melancholic ambient music, sad strings, rain sounds, introspective and emotional, no lyrics",
        "sad indie piano, emotional slow melody, rainy day reflection, bittersweet, no lyrics",
        "melancholy ambient, slow cello, distant piano, gray sky feeling, emotional depth, no lyrics",
        "sad beautiful music, slow orchestral strings, rain, nostalgia and longing, no lyrics",
    ],
    art_prompts=[
        "person looking out rain-covered window, moody gray light, reflective and melancholic, photography",
        "empty park bench in autumn rain, fallen leaves, gray sky, melancholic, photography",
        "foggy coastal cliff, dramatic gray ocean, lone figure, emotional landscape photography",
        "old polaroid photographs scattered on dark floor, memories, melancholic still life",
        "autumn forest in rain, orange leaves, gray mist, beautiful melancholy, landscape photography",
    ],
    title_templates=[
        "Sad Music – 1 Hour Melancholic Piano for Rainy Days",
        "Rainy Day Music – 1 Hour Sad & Beautiful Ambient",
        "Melancholic Music – 1 Hour Sad Piano & Strings",
        "1 Hour Sad Rainy Day Music – Emotional & Reflective",
        "Sad Piano Music – 1 Hour Beautiful Melancholy",
    ],
    description_template="""{title}

Sometimes you need music that understands. Beautiful, melancholic music for rainy days, reflection, and those moments when you need to feel your feelings.

♫ 1 hour of melancholic ambient music
♫ Sad piano, strings & rain sounds
♫ For reflection, healing & emotional release

🔔 Subscribe for more emotional music

#SadMusic #MelancholicMusic #RainyDayMusic #SadPiano #EmotionalMusic #MelancholyAmbient
""",
    tags=["sad music", "melancholic music", "rainy day music", "sad piano", "emotional music",
          "melancholy ambient", "sad strings", "reflective music", "beautiful sad music", "crying music"],
)

ROMANTIC_JAZZ = Channel(
    slug="romantic-jazz",
    name="Romantic Jazz Music",
    music_prompts=[
        "romantic jazz, soft saxophone, warm piano, evening candlelight dinner, intimate, no lyrics",
        "love jazz music, gentle guitar, brushed drums, romantic Paris atmosphere, no lyrics",
        "romantic ballad jazz, slow piano trio, intimate and warm, special evening, no lyrics",
        "date night jazz, smooth trumpet, soft bass, evening romance, sophisticated, no lyrics",
        "romantic bossa nova, acoustic guitar, soft percussion, Brazilian love atmosphere, no lyrics",
    ],
    art_prompts=[
        "romantic candlelit dinner for two, Paris restaurant, warm light, wine, roses, photography",
        "couple dancing in dimly lit jazz club, warm amber tones, romantic atmosphere, photography",
        "rain-soaked Paris street at night, couple under umbrella, romantic lights, oil painting style",
        "champagne and roses on balcony with city lights, romantic evening, warm tones, photography",
        "vintage record player with rose and candlelight, romantic home evening, warm photography",
    ],
    title_templates=[
        "Romantic Jazz – 1 Hour Love Songs & Dinner Music",
        "Jazz for Romance – 1 Hour Intimate Evening Music",
        "Romantic Dinner Jazz – 1 Hour Smooth Background Music",
        "1 Hour Romantic Jazz – Love & Candlelight Atmosphere",
        "Date Night Jazz – 1 Hour Romantic Smooth Jazz",
    ],
    description_template="""{title}

Set the mood for romance. Soft, intimate jazz perfect for dinner dates, anniversaries, Valentine's Day, or any special evening with someone you love.

♫ 1 hour of romantic jazz music
♫ Soft saxophone, piano & guitar
♫ Perfect for dinner, dates & romance

🔔 Subscribe for more romantic jazz

#RomanticJazz #DinnerJazz #DateNightMusic #RomanceMusic #SmoothJazz #LoveMusic
""",
    tags=["romantic jazz", "dinner jazz", "date night music", "romance music", "smooth jazz",
          "love music", "valentines music", "dinner music", "intimate jazz", "romantic music"],
)

CHRISTMAS_AMBIENT = Channel(
    slug="christmas-ambient",
    name="Christmas Ambient Music",
    music_prompts=[
        "ambient Christmas music, soft piano, sleigh bells, warm and magical, holiday spirit, no lyrics",
        "Christmas ambient, orchestral sleigh bells, soft choir pads, cozy winter holiday, no lyrics",
        "Christmas Eve music, gentle piano carols, fireplace warmth, magical winter night, no lyrics",
        "winter holiday ambient, soft music box, bells, snow falling atmosphere, magical, no lyrics",
        "Christmas morning music, warm and gentle, piano and strings, holiday wonder, no lyrics",
    ],
    art_prompts=[
        "cozy living room with Christmas tree, fireplace, snow outside, warm magical holiday photography",
        "snowy village at night, Christmas lights, warm windows, magical winter wonderland illustration",
        "Christmas ornaments on tree with bokeh lights, warm tones, magical holiday photography",
        "snow-covered forest path with lantern, magical winter night, Christmas atmosphere, photography",
        "Christmas morning gifts under tree, warm fireplace, snow at window, cozy holiday photography",
    ],
    title_templates=[
        "Christmas Music – 1 Hour Ambient Holiday Music for Christmas",
        "Christmas Ambient – 1 Hour Peaceful Holiday Background Music",
        "Cozy Christmas Music – 1 Hour Soft Holiday Atmosphere",
        "1 Hour Christmas Music – Ambient & Relaxing Holiday Sounds",
        "Christmas Eve Music – 1 Hour Magical Holiday Ambience",
    ],
    description_template="""{title}

Fill your home with the magical spirit of Christmas. Peaceful, ambient holiday music perfect for decorating, gift wrapping, or simply enjoying the season.

♫ 1 hour of ambient Christmas music
♫ Soft piano, bells & orchestral holiday sounds
♫ Perfect for decorating & holiday gatherings

🔔 Subscribe for more Christmas music

#ChristmasMusic #HolidayMusic #ChristmasAmbient #ChristmasSongs #CozyChristmas #WinterMusic
""",
    tags=["christmas music", "holiday music", "christmas ambient", "christmas songs", "cozy christmas",
          "winter music", "christmas eve", "holiday ambient", "christmas carols", "christmas background"],
)

WORSHIP_INSTRUMENTAL = Channel(
    slug="worship-instrumental",
    name="Worship Instrumental Music",
    music_prompts=[
        "worship instrumental music, soft piano and strings, reverent and holy, spiritual devotion, no lyrics",
        "Christian ambient worship, gentle guitar, soft pads, prayerful atmosphere, no lyrics",
        "worship meditation music, piano and gentle orchestra, sacred and uplifting, no lyrics",
        "soaking worship music, sustained piano chords, Holy Spirit atmosphere, deep reverence, no lyrics",
        "instrumental praise music, gentle acoustic guitar, heartfelt worship, spiritual peace, no lyrics",
    ],
    art_prompts=[
        "sunlight streaming through cathedral stained glass, rainbow light, sacred and beautiful photography",
        "empty chapel at dawn, candles, wooden pews, golden morning light, peaceful sacred space",
        "cross on hilltop at sunset, golden sky, peaceful and sacred, landscape photography",
        "person in prayer silhouette against sunrise, spiritual and reverent, photography",
        "open Bible with morning light and flowers, devotional peaceful still life, photography",
    ],
    title_templates=[
        "Worship Music – 1 Hour Instrumental Praise & Worship",
        "Christian Worship – 1 Hour Peaceful Instrumental Music",
        "Instrumental Worship – 1 Hour Soaking in God's Presence",
        "1 Hour Worship Music – Prayer & Devotion Instrumental",
        "Soaking Worship – 1 Hour Peaceful Christian Instrumental",
    ],
    description_template="""{title}

Peaceful instrumental worship music for prayer, devotion, Bible study, and spending time in God's presence. No lyrics — pure worship atmosphere.

♫ 1 hour of instrumental worship music
♫ No lyrics — soaking & devotional
♫ Perfect for prayer, Bible study & worship

🔔 Subscribe for new worship music weekly

#WorshipMusic #ChristianMusic #InstrumentalWorship #PraiseAndWorship #SoakingWorship #PrayerMusic
""",
    tags=["worship music", "christian music", "instrumental worship", "praise and worship",
          "soaking worship", "prayer music", "devotional music", "christian ambient", "worship instrumental"],
)

AFRICAN_MEDITATION = Channel(
    slug="african-meditation",
    name="African Meditation Music",
    music_prompts=[
        "African meditation music, djembe drums, kora harp, slow tribal ambient, spiritual Africa, no lyrics",
        "African healing music, slow ceremonial drums, mbira thumb piano, ancestral spirits, no lyrics",
        "West African meditation, balafon xylophone, gentle drums, earth connection, no lyrics",
        "African nature sounds music, savanna birds, distant drums, sunset Africa, no lyrics",
        "Ubuntu healing music, African chant-inspired ambient, community spirit, no vocals",
    ],
    art_prompts=[
        "African sunset over savanna, acacia tree silhouette, orange and gold sky, stunning photography",
        "tribal meditation circle with fire at night, stars, African village, spiritual photography",
        "Maasai elder in traditional dress, dramatic African landscape, portrait photography",
        "ancient baobab tree at sunset, vast African plains, spiritual landscape photography",
        "African river with hippos at golden hour, wild nature, dramatic Africa photography",
    ],
    title_templates=[
        "African Meditation Music – 1 Hour Tribal Drums & Healing",
        "African Healing Music – 1 Hour Drums, Kora & Meditation",
        "African Ambient – 1 Hour Tribal Meditation & Spiritual Music",
        "1 Hour African Meditation – Healing Drums & Kora",
        "Tribal Meditation Music – 1 Hour African Healing Sounds",
    ],
    description_template="""{title}

Ancient African healing music drawing from the rich spiritual traditions of the continent. Djembe rhythms, kora melodies, and mbira tones for meditation and inner journey.

♫ 1 hour of African meditation music
♫ Djembe, kora & mbira instruments
♫ Ancient healing traditions for modern life

🔔 Subscribe for more world meditation music

#AfricanMusic #TribalMusic #AfricanMeditation #DjembeMusic #HealingMusic #WorldMusic
""",
    tags=["african music", "tribal music", "african meditation", "djembe music", "healing music",
          "world music", "kora music", "african drums", "tribal meditation", "mbira"],
)

JAPANESE_LOFI = Channel(
    slug="japanese-lofi",
    name="Japanese Lo-Fi Music",
    music_prompts=[
        "Japanese lo-fi music, koto and piano, cherry blossom vibes, slow and serene, no lyrics",
        "Japanese study music, shakuhachi flute lo-fi, gentle rain, zen focus, no lyrics",
        "Tokyo cafe lo-fi, jazz influenced Japan, gentle shamisen, city nostalgia, no lyrics",
        "Japanese ambient lo-fi, biwa and piano, quiet contemplation, wabi-sabi aesthetic, no lyrics",
        "anime study lo-fi Japan, soft piano, distant city sounds, Japanese coziness, no lyrics",
    ],
    art_prompts=[
        "Tokyo rainy street at night, neon reflections, Japanese signs, lo-fi anime aesthetic, illustration",
        "Japanese temple garden in cherry blossom season, pink petals falling, peaceful photography",
        "cozy Japanese room, tatami mat, shoji screen, moonlight, wabi-sabi aesthetic, illustration",
        "Mt Fuji reflection in lake at sunrise, cherry blossoms, perfect Japan landscape photography",
        "Tokyo train window view at night, blurred city lights, Japanese urban lo-fi aesthetic, illustration",
    ],
    title_templates=[
        "Japanese Lo-Fi – 1 Hour Japan Aesthetic Study Music",
        "Tokyo Lo-Fi – 1 Hour Japanese Chill Study Beats",
        "Japanese Study Music – 1 Hour Lo-Fi Japan Vibes",
        "1 Hour Japanese Lo-Fi – Koto, Rain & Tokyo Nights",
        "Japan Lo-Fi – 1 Hour Cherry Blossom Study Music",
    ],
    description_template="""{title}

Study and chill with the calming aesthetic of Japan. Koto melodies, gentle rain, and the peaceful spirit of wabi-sabi in every beat.

♫ 1 hour of Japanese lo-fi music
♫ Koto, shakuhachi & piano beats
♫ Perfect for studying & relaxing

🔔 Subscribe for new Japanese lo-fi weekly

#JapaneseLoFi #JapanMusic #TokyoLoFi #StudyMusic #JapaneseMusic #CherryBlossom
""",
    tags=["japanese lo-fi", "japan music", "tokyo lo-fi", "study music", "japanese music",
          "koto music", "cherry blossom", "japanese chill", "anime music", "wabi-sabi"],
)


# ── REGISTRY ──────────────────────────────────────────────────────────────────

ALL_CHANNELS = {
    # Sleep
    "deep-sleep":        DEEP_SLEEP,
    "baby-sleep":        BABY_SLEEP,
    "sleep-meditation":  SLEEP_MEDITATION,
    "rain-sleep":        RAIN_SLEEP,
    "432hz-sleep":       HZ432_SLEEP,
    "binaural-sleep":    BINAURAL_SLEEP,
    # Focus
    "lofi-study":        LOFI_STUDY,
    "deep-work-jazz":    DEEP_WORK_JAZZ,
    "coding-music":      CODING_MUSIC,
    "coffee-shop-beats": COFFEE_SHOP_BEATS,
    "classical-study":   CLASSICAL_STUDY,
    "piano-focus":       PIANO_FOCUS,
    # Relax
    "spa-music":         SPA_MUSIC,
    "yoga-flow":         YOGA_FLOW,
    "anxiety-relief":    ANXIETY_RELIEF,
    "nature-sounds":     NATURE_SOUNDS,
    "meditation":        MEDITATION,
    "reiki-healing":     REIKI_HEALING,
    # Mood
    "happy-morning":     HAPPY_MORNING,
    "sad-rainy-day":     SAD_RAINY_DAY,
    "romantic-jazz":     ROMANTIC_JAZZ,
    "christmas-ambient": CHRISTMAS_AMBIENT,
    "worship-instrumental": WORSHIP_INSTRUMENTAL,
    "african-meditation": AFRICAN_MEDITATION,
    "japanese-lofi":     JAPANESE_LOFI,
}

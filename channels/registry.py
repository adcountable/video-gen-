"""
All 25 channel definitions.
Format inspired by @safeplaceinhere — spinning vinyl, casual titles, chapter timestamps.
"""

from channels.base import Channel

DESC = """{title}

{chapters}

put this on, close your eyes, and let go :)

🔔 new music every week — subscribe if this helps

#{tags}
"""

# ── SLEEP ─────────────────────────────────────────────────────────────────────

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
    vinyl_doodles=[
        "sleeping crescent moon with tiny stars around it",
        "little cloud with a sleeping face, zzz floating above",
        "crescent moon in a hammock between two stars",
        "small bear sleeping curled up, moon above",
        "night sky with one big sleeping star",
    ],
    title_templates=[
        "can't sleep? this one's for you :)",
        "put this on and drift away :)",
        "for when your brain won't shut up at night :)",
        "you need this tonight. trust me :)",
        "the sleep music that actually works :)",
        "close your eyes. you're safe here :)",
    ],
    description_template=DESC,
    tags=["deep sleep", "sleep music", "fall asleep fast", "ambient music", "insomnia relief",
          "delta waves", "relaxing music", "sleep aid", "calm music", "no lyrics"],
    chapters=["🌙 drift", "💤 settle", "🌊 deep rest", "✨ gone"],
    music_generator="sleep",
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
    vinyl_doodles=[
        "tiny sleeping bunny curled up in a ball",
        "little duck sleeping with a bow on its head",
        "sleeping baby bear with a star blanket",
        "crescent moon cradling a tiny baby",
        "small cloud rocking a star to sleep",
    ],
    title_templates=[
        "shh... little one :)",
        "for the tiny humans who won't sleep :)",
        "gentle enough for the littlest ones :)",
        "mama, put this on. it works :)",
        "sweet dreams, little one :)",
    ],
    description_template=DESC,
    tags=["baby sleep music", "lullaby", "newborn sleep", "infant sleep", "toddler sleep",
          "gentle music", "nursery music", "baby lullaby", "sleep baby", "baby calm"],
    chapters=["🌙 lullaby", "🐣 gentle", "💤 drifting", "✨ dreaming"],
    music_generator="sleep",
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
    vinyl_doodles=[
        "simple lotus flower with tiny stars",
        "meditation figure sitting cross-legged with moon above",
        "tibetan singing bowl with sound waves",
        "eye with stars inside, third eye symbol, simple",
        "small flame with spiraling smoke, peaceful",
    ],
    title_templates=[
        "let your body melt into the bed :)",
        "for when you need to actually rest :)",
        "a little meditation before sleep :)",
        "breathe out. you did enough today :)",
        "this will quiet your mind :)",
    ],
    description_template=DESC,
    tags=["sleep meditation", "meditation music", "yoga nidra", "tibetan bowls", "healing music",
          "deep sleep", "relaxation", "theta waves", "mindful sleep", "432hz"],
    chapters=["🧘 arrive", "🌬 breathe", "💫 release", "🌊 rest"],
    music_generator="sleep",
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
    vinyl_doodles=[
        "little rain cloud with drops falling",
        "umbrella with raindrops around it",
        "window with rain drops on the glass",
        "cozy house in rain, smoke from chimney",
        "frog sitting happily in rain, simple sketch",
    ],
    title_templates=[
        "rainy night. exactly what you needed :)",
        "fall asleep to the rain :)",
        "cozy rain for when you can't sleep :)",
        "the rain is here. you can rest now :)",
        "let the rain take you under :)",
    ],
    description_template=DESC,
    tags=["rain sounds", "rain sleep", "sleep music", "rain ambience", "nature sounds",
          "rainy night", "cozy rain", "sleep sounds", "rain and piano", "rain for sleep"],
    chapters=["🌧 falling", "💧 settle", "🌊 deep", "🌙 gone"],
    music_generator="sleep",
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
    vinyl_doodles=[
        "sound wave frequency spiral, simple geometric",
        "tuning fork with vibration lines",
        "DNA helix simple sketch, small",
        "golden ratio spiral, clean lines",
        "atom with orbiting electrons, simple doodle",
    ],
    title_templates=[
        "432hz. let your body heal while you sleep :)",
        "the frequency that actually helps :)",
        "tune in, drift off :)",
        "healing while you rest :)",
        "your body knows what to do with this :)",
    ],
    description_template=DESC,
    tags=["432hz", "healing frequency", "sleep music", "solfeggio", "healing sleep",
          "frequency healing", "deep sleep", "432hz music", "432hz sleep", "dna repair"],
    chapters=["🔮 tune", "💫 align", "🌊 heal", "✨ restore"],
    music_generator="sleep",
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
    vinyl_doodles=[
        "two circles overlapping creating sound waves between them",
        "left and right arrows pointing to a brain, simple",
        "headphones with wave lines coming out, minimal",
        "brain with delta wave lines, sketch style",
        "two ears with a wave connecting them",
    ],
    title_templates=[
        "⚠️ headphones on. brain off :)",
        "delta waves for your deepest sleep :)",
        "your brain will thank you tomorrow :)",
        "wear headphones. this one hits different :)",
        "binaural beats for when nothing else works :)",
    ],
    description_template=DESC,
    tags=["binaural beats", "delta waves", "binaural sleep", "brain entrainment", "sleep music",
          "delta wave sleep", "insomnia", "deep sleep", "headphones", "binaural beats sleep"],
    chapters=["🎧 sync", "🧠 calm", "💤 delta", "🌊 deep"],
    music_generator="sleep",
)

# ── FOCUS ─────────────────────────────────────────────────────────────────────

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
    vinyl_doodles=[
        "cozy bedroom desk at night, warm lamp light, open laptop, rain on window, lo-fi aesthetic",
        "small Tokyo apartment study nook, city lights outside, books stacked, late evening",
        "college dorm room, string lights, open textbooks, coffee cup steaming, golden lamp glow",
        "cafe window seat, rainy street outside, headphones on table, warm latte, autumn leaves",
        "library corner, afternoon sun through tall windows, dust motes, stacked books, peaceful",
    ],
    video_format="scene",
    title_templates=[
        "lock in. this one hits different :)",
        "the study playlist that actually keeps you focused :)",
        "put this on and get to work :)",
        "for the deep work session you keep putting off :)",
        "your brain will thank you :)",
        "flow state loading... :)",
    ],
    description_template=DESC,
    tags=["lo-fi", "study music", "lo-fi hip hop", "chill beats", "focus music",
          "homework music", "lo-fi study", "work music", "chill music", "no lyrics"],
    chapters=["☕ warm up", "📚 flow", "🎧 zone in", "⚡ locked"],
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
    vinyl_doodles=[
        "dimly lit jazz bar, warm amber light, empty stage with upright bass and piano, evening",
        "New York loft office, exposed brick, evening city view, desk lamp, warm and focused",
        "classic speakeasy interior, low lighting, mahogany bar, velvet booths, intimate",
        "rooftop at sunset, city skyline, a lone saxophone case open on a chair, golden hour",
        "Parisian cafe evening, candles on tables, rain outside, warm interior light, sophisticated",
    ],
    video_format="scene",
    title_templates=[
        "smooth jazz for when you need to actually get things done :)",
        "the jazz that puts you in the zone :)",
        "work smarter. jazz harder :)",
        "for the deep work session :)",
        "your office just got a lot cooler :)",
    ],
    description_template=DESC,
    tags=["deep work jazz", "smooth jazz", "work music", "jazz instrumental", "focus music",
          "productivity music", "office music", "jazz focus", "background jazz", "concentration"],
    chapters=["🎷 ease in", "☕ settle", "🎵 flow", "⚡ deep work"],
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
    vinyl_doodles=[
        "computer monitor with code lines on screen, tiny doodle",
        "keyboard with a small lightning bolt above it",
        "terminal cursor blinking, minimal sketch",
        "coffee cup next to a circuit board, simple",
        "brackets { } with a tiny star inside",
    ],
    title_templates=[
        "for the 2am coding session :)",
        "ship it. this will help :)",
        "in the zone. do not disturb :)",
        "100 lines of code incoming :)",
        "the playlist that makes you a better dev :)",
    ],
    description_template=DESC,
    tags=["coding music", "programmer music", "focus music", "electronic music", "flow state",
          "deep work", "programming music", "coder music", "music for coding", "techno focus"],
    chapters=["💻 boot up", "⚡ flow", "🔥 locked in", "🚀 ship it"],
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
    vinyl_doodles=[
        "coastal cafe kitchen, morning light through large windows, ocean view, coffee steaming, warm",
        "independent coffee shop, brick walls, hanging plants, morning sun, people working quietly",
        "Parisian sidewalk cafe, cobblestones wet from rain, espresso on table, morning newspaper",
        "Japanese minimalist cafe, wooden counter, pour-over coffee, soft light, calm atmosphere",
        "mountain cabin kitchen, coffee brewing, snow outside the window, fireplace glow, peaceful",
    ],
    video_format="scene",
    title_templates=[
        "bring the coffee shop to you :)",
        "wfh just got way better :)",
        "pretend you're in a paris cafe :)",
        "the vibe you didn't know you needed :)",
        "cozy coffee shop. no small talk :)",
    ],
    description_template=DESC,
    tags=["coffee shop music", "cafe music", "work music", "study music", "cozy music",
          "background music", "cafe ambience", "acoustic music", "morning music", "wfh music"],
    chapters=["☕ first sip", "📖 settle in", "✍️ flow", "🌟 peak focus"],
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
    vinyl_doodles=[
        "grand piano, small simple sketch",
        "musical staff with notes, clean lines",
        "violin bow across strings, elegant minimal",
        "quill pen writing musical notes",
        "sheet music rolling out, small doodle",
    ],
    title_templates=[
        "classical music for your big brain energy :)",
        "study like it's the renaissance :)",
        "turn this on and actually read the book :)",
        "for the essay due tomorrow :)",
        "big focus. big brain. classical music :)",
    ],
    description_template=DESC,
    tags=["classical music", "study music", "classical piano", "focus music", "Bach",
          "Mozart", "study classical", "instrumental classical", "academic music", "chamber music"],
    chapters=["🎼 prelude", "📚 allegro", "✍️ andante", "🏆 finale"],
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
    vinyl_doodles=[
        "single piano key pressed, sound waves coming out",
        "hands on piano keys, minimal sketch",
        "piano from above, just the keys",
        "music note with small heart, simple",
        "piano bench with a small star above it",
    ],
    title_templates=[
        "just you, a piano, and the work :)",
        "piano music for deep focus :)",
        "the playlist that silences everything else :)",
        "put this on. get in the zone :)",
        "solo piano for your best thinking :)",
    ],
    description_template=DESC,
    tags=["piano music", "focus music", "solo piano", "study music", "ambient piano",
          "work music", "piano focus", "instrumental piano", "relaxing piano", "neo-classical"],
    chapters=["🎹 open", "💭 think", "✨ flow", "🌟 clarity"],
)

# ── RELAX ─────────────────────────────────────────────────────────────────────

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
    vinyl_doodles=[
        "small candle flame with gentle smoke curl",
        "lotus flower floating on water, minimal",
        "bamboo stalks, two or three, simple sketch",
        "river stone stack, zen balance",
        "orchid flower, one stem, elegant minimal",
    ],
    title_templates=[
        "your spa day is right here :)",
        "you deserve this. take a moment :)",
        "turn your bathroom into a spa :)",
        "relax. you've earned it :)",
        "spa music for a very deserved rest :)",
    ],
    description_template=DESC,
    tags=["spa music", "relaxing music", "massage music", "wellness music", "zen music",
          "ambient music", "meditation music", "spa relaxation", "healing music", "peaceful music"],
    chapters=["🌸 arrive", "💆 unwind", "🌿 release", "✨ restored"],
    music_generator="sleep",
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
    vinyl_doodles=[
        "person in tree pose, simple silhouette sketch",
        "lotus position figure, minimal lines",
        "sun salutation sequence, tiny stick figures",
        "yoga mat rolled up with a flower on it",
        "hands in prayer position, namaste",
    ],
    title_templates=[
        "flow with this. your mat is waiting :)",
        "morning yoga. you've got this :)",
        "move your body. clear your mind :)",
        "for the slow flow you need today :)",
        "breathe in. breathe out. flow :)",
    ],
    description_template=DESC,
    tags=["yoga music", "yoga flow", "vinyasa music", "yin yoga", "meditation music",
          "yoga ambient", "yoga practice music", "flow music", "mindful movement", "yoga soundtrack"],
    chapters=["🌅 ground", "🌬 breathe", "🌊 flow", "🙏 rest"],
    music_generator="sleep",
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
    vinyl_doodles=[
        "small heart with a tiny bandage on it",
        "breathing circle expanding, simple animation doodle",
        "little sun peeking out from behind a cloud",
        "hands cupped holding a small star",
        "wave that starts choppy and becomes smooth",
    ],
    title_templates=[
        "hey. you're okay. breathe :)",
        "for when anxiety shows up uninvited :)",
        "this will help. promise :)",
        "you are safe. you are here :)",
        "calm is closer than you think :)",
        "for the hard days :)",
    ],
    description_template=DESC,
    tags=["anxiety relief", "anxiety music", "stress relief", "calming music", "mental health",
          "relaxing music", "nervous system", "grounding music", "calm music", "panic relief"],
    chapters=["💙 arrive", "🌬 breathe", "🌱 ground", "☀️ safe"],
    music_generator="sleep",
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
    vinyl_doodles=[
        "small tree with birds sitting on branches",
        "ocean wave, simple curved lines",
        "campfire with small sparks, cozy sketch",
        "mountain with small birds flying over it",
        "leaf with a dewdrop on it, minimal",
    ],
    title_templates=[
        "nature called. it says rest :)",
        "close your eyes. you're outside now :)",
        "the great outdoors. from your couch :)",
        "forest sounds for your overstimulated brain :)",
        "let nature do the work :)",
    ],
    description_template=DESC,
    tags=["nature sounds", "relaxing nature", "forest sounds", "ocean sounds", "bird sounds",
          "rain sounds", "sleep sounds", "nature ambience", "outdoor sounds", "white noise"],
    chapters=["🌿 arrive", "🐦 settle", "🌊 drift", "🌙 rest"],
    music_generator="sleep",
)

MEDITATION = Channel(
    slug="meditation",
    name="Meditation Music",
    music_prompts=[
        "mindfulness meditation music, gentle Tibetan singing bowl, slow ambient, present moment, no lyrics",
        "zen meditation music, Japanese koto, soft drone, emptiness and peace, no lyrics",
        "vipassana meditation music, silent ambient, very slow tones, insight and clarity, no lyrics",
        "loving kindness meditation music, warm gentle tones, open heart, compassion and peace, no lyrics",
        "transcendental meditation music, mantra-like ambient tones, deep stillness, no lyrics",
    ],
    vinyl_doodles=[
        "simple spiral going inward, meditation symbol",
        "single candle flame, peaceful and still",
        "om symbol, clean minimal lines",
        "eye with lotus inside, third eye minimal",
        "infinity symbol with small stars on it",
    ],
    title_templates=[
        "5 minutes or 60. either way, this helps :)",
        "quiet your mind. the world can wait :)",
        "for the meditation you keep skipping :)",
        "just breathe. that's all :)",
        "stillness is here :)",
    ],
    description_template=DESC,
    tags=["meditation music", "mindfulness", "zen music", "tibetan bowls", "meditation ambient",
          "inner peace", "mindfulness music", "calming meditation", "spiritual music", "vipassana"],
    chapters=["🧘 arrive", "🌬 settle", "💫 deepen", "🌙 still"],
    music_generator="sleep",
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
    vinyl_doodles=[
        "seven dots in a line going up, chakra symbols minimal",
        "hands with energy lines radiating from palms",
        "crystal with light rays, simple geometric",
        "flower of life sacred geometry, minimal lines",
        "spiral with small dots, energy field sketch",
    ],
    title_templates=[
        "let the energy do what it needs to :)",
        "healing is happening. even now :)",
        "chakra reset. you needed this :)",
        "reiki vibes for your tired soul :)",
        "your energy is being restored :)",
    ],
    description_template=DESC,
    tags=["reiki music", "chakra healing", "healing music", "528hz", "energy healing",
          "chakra music", "crystal bowls", "reiki healing", "chakra balance", "spiritual healing"],
    chapters=["✨ open", "💫 align", "🌊 flow", "🌸 restored"],
    music_generator="sleep",
)

# ── MOOD ──────────────────────────────────────────────────────────────────────

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
    vinyl_doodles=[
        "sun rising over small hills, rays of light",
        "rooster crowing, cheerful simple doodle",
        "cup of coffee with a sunshine face on it",
        "bird singing on a branch, morning light",
        "alarm clock with a smiling face, morning vibes",
    ],
    title_templates=[
        "good morning. today is yours :)",
        "rise and actually shine :)",
        "morning music that doesn't make you want to sleep more :)",
        "for a genuinely good morning :)",
        "start here. today is gonna be good :)",
    ],
    description_template=DESC,
    tags=["morning music", "happy music", "uplifting music", "good morning", "positive vibes",
          "morning motivation", "cheerful music", "sunrise music", "acoustic morning", "happy morning"],
    chapters=["🌅 rise", "☕ sip", "✨ energize", "🚀 go"],
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
    vinyl_doodles=[
        "apartment window streaming with rain, blurred city lights outside, gray afternoon, melancholic",
        "empty bench in a park, autumn leaves falling, soft rain, overcast sky, quiet and still",
        "train window with heavy rain, blurred passing landscape, moody light, introspective mood",
        "old wooden pier in fog, still water, muted colors, quiet rain, solitary and beautiful",
        "attic room with skylight, rain pattering on glass, single reading lamp, books, nostalgic",
    ],
    video_format="scene",
    title_templates=[
        "it's okay to feel this :)",
        "for the gray days :)",
        "sad music for when you need to feel it :)",
        "let it out. that's what this is for :)",
        "beautiful sadness. you're not alone :)",
    ],
    description_template=DESC,
    tags=["sad music", "melancholic music", "rainy day music", "sad piano", "emotional music",
          "melancholy ambient", "sad strings", "reflective music", "beautiful sad music", "crying music"],
    chapters=["🌧 feel", "💧 release", "🌊 sit with it", "🌱 breathe"],
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
    vinyl_doodles=[
        "candlelit restaurant table for two, warm glow, wine glasses, rose, Parisian evening",
        "rooftop dinner overlooking Paris at night, Eiffel Tower glowing, candles, intimate",
        "jazz lounge with low lighting, couples at tables, saxophonist on stage, warm amber",
        "coastal terrace at sunset, champagne on table, ocean view, golden hour, romantic",
        "penthouse window view of city at night, wine glasses, candles, elegant and intimate",
    ],
    video_format="scene",
    title_templates=[
        "set the mood. you know what to do :)",
        "jazz for the ones you love :)",
        "dinner for two. jazz for the night :)",
        "romance is in the air and this playlist :)",
        "the only jazz playlist you need tonight :)",
    ],
    description_template=DESC,
    tags=["romantic jazz", "dinner jazz", "date night music", "romance music", "smooth jazz",
          "love music", "valentines music", "dinner music", "intimate jazz", "romantic music"],
    chapters=["🕯 arrive", "🥂 toast", "🎷 settle", "💕 tonight"],
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
    vinyl_doodles=[
        "small christmas tree with star on top",
        "snowflake, intricate but small",
        "candy cane with a bow",
        "gift box with ribbon, simple",
        "reindeer head with antlers, cute sketch",
    ],
    title_templates=[
        "it's the most wonderful time :)",
        "cozy christmas vibes, no ads :)",
        "all the christmas feels :)",
        "wrap presents to this :)",
        "christmas magic. right here :)",
    ],
    description_template=DESC,
    tags=["christmas music", "holiday music", "christmas ambient", "christmas songs", "cozy christmas",
          "winter music", "christmas eve", "holiday ambient", "christmas carols", "christmas background"],
    chapters=["⛄ arrive", "🎁 cozy", "🕯 magic", "⭐ wonder"],
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
    vinyl_doodles=[
        "small cross with light rays, simple and clean",
        "dove in flight, minimal sketch",
        "open hands facing up, receiving",
        "single candle with light rays",
        "simple church window arch shape",
    ],
    title_templates=[
        "soak in his presence :)",
        "worship music for your quiet time :)",
        "just you and God. no distractions :)",
        "for prayer, study, and rest :)",
        "holy and still :)",
    ],
    description_template=DESC,
    tags=["worship music", "christian music", "instrumental worship", "praise and worship",
          "soaking worship", "prayer music", "devotional music", "christian ambient", "worship instrumental"],
    chapters=["🙏 enter", "✝️ abide", "🕊 soak", "💫 rest"],
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
    vinyl_doodles=[
        "djembe drum, simple sketch",
        "acacia tree silhouette, minimal",
        "baobab tree with small animals below",
        "kora instrument, elegant minimal drawing",
        "sun setting behind savanna hills, line drawing",
    ],
    title_templates=[
        "ancient rhythms for modern healing :)",
        "africa is calling. this is it :)",
        "drum medicine for your soul :)",
        "roots. rhythm. rest :)",
        "healing that goes back thousands of years :)",
    ],
    description_template=DESC,
    tags=["african music", "tribal music", "african meditation", "djembe music", "healing music",
          "world music", "kora music", "african drums", "tribal meditation", "mbira"],
    chapters=["🌍 ground", "🥁 rhythm", "🌿 heal", "🌅 restore"],
    music_generator="sleep",
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
    vinyl_doodles=[
        "Tokyo alley at night, paper lanterns glowing, light rain on cobblestones, warm and nostalgic",
        "Japanese tea house garden, cherry blossoms falling, stone path, soft morning mist",
        "Tokyo train window, passing city lights at night, reflections, lo-fi aesthetic",
        "minimalist Japanese study room, shoji screen, warm lamp, books, cherry blossom outside",
        "rainy Tokyo street at dusk, neon signs reflected in puddles, cozy ramen shop window",
    ],
    video_format="scene",
    title_templates=[
        "japanese lo-fi for your soul :)",
        "tokyo nights from your room :)",
        "wabi-sabi study session :)",
        "cherry blossoms and deadlines :)",
        "the japan vibe you needed :)",
    ],
    description_template=DESC,
    tags=["japanese lo-fi", "japan music", "tokyo lo-fi", "study music", "japanese music",
          "koto music", "cherry blossom", "japanese chill", "anime music", "wabi-sabi"],
    chapters=["🌸 bloom", "🎋 settle", "🗼 flow", "🌙 still"],
)


# ── REGISTRY ──────────────────────────────────────────────────────────────────

ALL_CHANNELS = {
    "deep-sleep":           DEEP_SLEEP,
    "baby-sleep":           BABY_SLEEP,
    "sleep-meditation":     SLEEP_MEDITATION,
    "rain-sleep":           RAIN_SLEEP,
    "432hz-sleep":          HZ432_SLEEP,
    "binaural-sleep":       BINAURAL_SLEEP,
    "lofi-study":           LOFI_STUDY,
    "deep-work-jazz":       DEEP_WORK_JAZZ,
    "coding-music":         CODING_MUSIC,
    "coffee-shop-beats":    COFFEE_SHOP_BEATS,
    "classical-study":      CLASSICAL_STUDY,
    "piano-focus":          PIANO_FOCUS,
    "spa-music":            SPA_MUSIC,
    "yoga-flow":            YOGA_FLOW,
    "anxiety-relief":       ANXIETY_RELIEF,
    "nature-sounds":        NATURE_SOUNDS,
    "meditation":           MEDITATION,
    "reiki-healing":        REIKI_HEALING,
    "happy-morning":        HAPPY_MORNING,
    "sad-rainy-day":        SAD_RAINY_DAY,
    "romantic-jazz":        ROMANTIC_JAZZ,
    "christmas-ambient":    CHRISTMAS_AMBIENT,
    "worship-instrumental": WORSHIP_INSTRUMENTAL,
    "african-meditation":   AFRICAN_MEDITATION,
    "japanese-lofi":        JAPANESE_LOFI,
}

"""
YouTube ATO — Local Admin Dashboard
Run with: streamlit run dashboard.py
"""

import os
import json
import time
import subprocess
import glob
from datetime import datetime
from typing import Optional

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ── Page config ────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="YouTube ATO",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Load channels ──────────────────────────────────────────────────────────────

import sys
sys.path.insert(0, os.path.dirname(__file__))

from channels.registry import ALL_CHANNELS
from config import OUTPUT_DIR

# ── Sidebar nav ───────────────────────────────────────────────────────────────

st.sidebar.title("🎵 YouTube ATO")
st.sidebar.caption("Local Admin Dashboard")
st.sidebar.divider()

page = st.sidebar.radio("", [
    "📊 Overview",
    "🚀 Launch Video",
    "📺 Output Library",
    "📡 Channels",
    "➕ Add Channel",
], label_visibility="collapsed")

st.sidebar.divider()

def _estimate_spend() -> float:
    """Estimate total Replicate spend based on output files."""
    minimax_slugs = [s for s, c in ALL_CHANNELS.items() if c.music_generator == "minimax"]
    sleep_slugs   = [s for s, c in ALL_CHANNELS.items() if c.music_generator == "sleep"]
    minimax_vids = sum(
        len(glob.glob(os.path.join(OUTPUT_DIR, slug, "*", "video.mp4")))
        for slug in minimax_slugs
    )
    sleep_vids = sum(
        len(glob.glob(os.path.join(OUTPUT_DIR, slug, "*", "video.mp4")))
        for slug in sleep_slugs
    )
    return minimax_vids * 0.19 + sleep_vids * 0.04  # music + FLUX


# Quick stats in sidebar
total_videos = len(glob.glob(os.path.join(OUTPUT_DIR, "**", "video.mp4"), recursive=True))
st.sidebar.metric("Videos Generated", total_videos)
st.sidebar.metric("Est. API Spend", f"${_estimate_spend():.2f}")
st.sidebar.metric("Channels", len(ALL_CHANNELS))


# ── Overview ──────────────────────────────────────────────────────────────────

if page == "📊 Overview":
    st.title("📊 Overview")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Videos", total_videos)
    col2.metric("Channels", len(ALL_CHANNELS))
    col3.metric("Est. Spend", f"${_estimate_spend():.2f}")
    col4.metric("Est. Cost/Video", "$0.11 avg")

    st.divider()

    # Channel breakdown
    st.subheader("Channels by generator")
    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("**🎵 MiniMax Music (~$0.15/video)**")
        for slug, ch in ALL_CHANNELS.items():
            if ch.music_generator == "minimax":
                vids = len(glob.glob(os.path.join(OUTPUT_DIR, slug, "*", "video.mp4")))
                fmt  = "🎨" if ch.video_format == "scene" else "💿"
                st.markdown(f"  {fmt} `{slug}` — {vids} videos")

    with col_b:
        st.markdown("**😴 Procedural Sleep (free)**")
        for slug, ch in ALL_CHANNELS.items():
            if ch.music_generator == "sleep":
                vids = len(glob.glob(os.path.join(OUTPUT_DIR, slug, "*", "video.mp4")))
                st.markdown(f"  💿 `{slug}` — {vids} videos")

    st.divider()

    # Recent outputs
    st.subheader("Recent videos")
    all_videos = sorted(
        glob.glob(os.path.join(OUTPUT_DIR, "**", "video.mp4"), recursive=True),
        key=os.path.getmtime, reverse=True
    )[:10]

    if all_videos:
        for vp in all_videos:
            parts = vp.split(os.sep)
            slug  = parts[-3]
            run_id = parts[-2]
            ts    = datetime.fromtimestamp(int(run_id)).strftime("%b %d %H:%M") if run_id.isdigit() else run_id
            size  = os.path.getsize(vp) / 1024 / 1024
            ch    = ALL_CHANNELS.get(slug)
            name  = ch.name if ch else slug
            thumb = vp.replace("video.mp4", "vinyl.jpg")
            cols  = st.columns([1, 4, 2, 1])
            if os.path.exists(thumb):
                cols[0].image(thumb, width=60)
            cols[1].markdown(f"**{name}**  \n`{ts}`")
            cols[2].caption(f"{size:.0f} MB")
            cols[3].markdown(f"[open]({vp})")
    else:
        st.info("No videos generated yet. Head to 🚀 Launch Video to create your first one.")


# ── Launch Video ──────────────────────────────────────────────────────────────

elif page == "🚀 Launch Video":
    st.title("🚀 Launch Video")

    col1, col2 = st.columns([2, 1])

    with col1:
        channel_slug = st.selectbox(
            "Channel",
            options=list(ALL_CHANNELS.keys()),
            format_func=lambda s: f"{ALL_CHANNELS[s].name} ({s})",
        )
        ch = ALL_CHANNELS[channel_slug]

        dry_run = st.checkbox("Dry run (build video, skip YouTube upload)", value=True)

        audio_file = st.text_input(
            "Custom audio file (optional)",
            placeholder="/path/to/suno_track.mp3 — leave empty to generate",
        )

    with col2:
        st.markdown("**Channel info**")
        st.caption(f"Format: `{ch.video_format}`")
        st.caption(f"Music: `{ch.music_generator}`")
        cost = "$0.15 + $0.04" if ch.music_generator == "minimax" else "$0.04 (free audio)"
        st.caption(f"Est. cost: {cost}")
        st.caption(f"Tags: {len(ch.tags)}")

    st.divider()

    if st.button("▶ Run Pipeline", type="primary", use_container_width=True):
        cmd = ["python3", "run.py", channel_slug]
        if dry_run:
            cmd.append("--dry-run")
        if audio_file.strip():
            cmd += ["--audio", audio_file.strip()]

        st.info(f"Running: `{' '.join(cmd)}`")

        log_box = st.empty()
        lines   = []

        with st.spinner("Pipeline running..."):
            proc = subprocess.Popen(
                cmd,
                cwd=os.path.dirname(__file__),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
            for line in proc.stdout:
                line = line.rstrip()
                if line and "Warning" not in line and "FutureWarning" not in line:
                    lines.append(line)
                    log_box.code("\n".join(lines[-30:]), language=None)
            proc.wait()

        if proc.returncode == 0:
            st.success("✅ Pipeline complete!")
            # Show thumbnail if it was generated
            latest = sorted(
                glob.glob(os.path.join(OUTPUT_DIR, channel_slug, "*", "vinyl.jpg")),
                key=os.path.getmtime, reverse=True
            )
            if latest:
                st.image(latest[0], caption="Generated artwork", width=300)
        else:
            st.error("❌ Pipeline failed — check the log above")


# ── Output Library ────────────────────────────────────────────────────────────

elif page == "📺 Output Library":
    st.title("📺 Output Library")

    filter_slug = st.selectbox(
        "Filter by channel",
        ["All channels"] + list(ALL_CHANNELS.keys()),
        format_func=lambda s: s if s == "All channels" else f"{ALL_CHANNELS[s].name} ({s})",
    )

    pattern = os.path.join(OUTPUT_DIR, "**", "video.mp4") if filter_slug == "All channels" \
              else os.path.join(OUTPUT_DIR, filter_slug, "*", "video.mp4")

    all_videos = sorted(glob.glob(pattern, recursive=True), key=os.path.getmtime, reverse=True)

    st.caption(f"{len(all_videos)} videos found")
    st.divider()

    for vp in all_videos:
        parts   = vp.split(os.sep)
        slug    = parts[-3]
        run_id  = parts[-2]
        ts      = datetime.fromtimestamp(int(run_id)).strftime("%b %d %Y %H:%M") if run_id.isdigit() else run_id
        size_mb = os.path.getsize(vp) / 1024 / 1024
        ch      = ALL_CHANNELS.get(slug)
        name    = ch.name if ch else slug
        thumb   = vp.replace("video.mp4", "vinyl.jpg")
        audio   = vp.replace("video.mp4", "track.mp3")

        with st.expander(f"{name} — {ts}"):
            c1, c2 = st.columns([1, 3])
            if os.path.exists(thumb):
                c1.image(thumb, width=140)
            with c2:
                st.markdown(f"**{name}**")
                st.caption(f"Run: `{run_id}` · {size_mb:.0f} MB")
                st.caption(f"Path: `{vp}`")
                if os.path.exists(audio):
                    st.audio(audio)
                cols = st.columns(2)
                cols[0].button("📂 Open folder", key=f"open_{run_id}",
                               on_click=lambda p=vp: subprocess.run(["open", os.path.dirname(p)]))


# ── Channels ──────────────────────────────────────────────────────────────────

elif page == "📡 Channels":
    st.title("📡 Channels")

    search = st.text_input("Search channels", placeholder="jazz, sleep, lofi...")

    for slug, ch in ALL_CHANNELS.items():
        if search and search.lower() not in slug and search.lower() not in ch.name.lower():
            continue

        fmt_badge  = "🎨 Scene" if ch.video_format == "scene" else "💿 Vinyl"
        gen_badge  = "🎵 MiniMax" if ch.music_generator == "minimax" else "😴 Sleep"
        vids_count = len(glob.glob(os.path.join(OUTPUT_DIR, slug, "*", "video.mp4")))

        with st.expander(f"**{ch.name}** `{slug}`  ·  {fmt_badge}  ·  {gen_badge}  ·  {vids_count} videos"):
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**Music prompts**")
                for p in ch.music_prompts:
                    st.caption(f"• {p[:80]}")
                st.markdown("**Title templates**")
                for t in ch.title_templates:
                    st.caption(f"• {t}")
            with c2:
                st.markdown("**Doodles / scenes**")
                for d in ch.vinyl_doodles:
                    st.caption(f"• {d[:70]}")
                st.markdown("**Tags**")
                st.caption(", ".join(ch.tags[:6]))
                st.markdown("**Chapters**")
                st.caption(" · ".join(ch.chapters))


# ── Add Channel ───────────────────────────────────────────────────────────────

elif page == "➕ Add Channel":
    st.title("➕ Add Channel")
    st.info("Fill in the details and the channel will be added to registry.py automatically.")

    col1, col2 = st.columns(2)

    with col1:
        new_slug  = st.text_input("Slug (URL-safe)", placeholder="ambient-piano")
        new_name  = st.text_input("Channel name", placeholder="Ambient Piano Music")
        new_format = st.radio("Video format", ["vinyl", "scene"])
        new_gen    = st.radio("Music generator", ["minimax", "sleep"])

    with col2:
        new_prompts = st.text_area(
            "Music prompts (one per line)",
            height=120,
            placeholder="ambient piano, slow arpeggios, peaceful, no lyrics\n..."
        )
        new_doodles = st.text_area(
            "Doodles / scenes (one per line)",
            height=120,
            placeholder="single candle on a rainy windowsill\n..."
        )
        new_titles = st.text_area(
            "Title templates (one per line)",
            height=80,
            placeholder="piano music for deep focus :)\n..."
        )
        new_tags = st.text_input("Tags (comma separated)",
                                  placeholder="ambient piano, focus music, piano music")
        new_chapters = st.text_input("Chapter names (comma separated)",
                                      placeholder="🎹 open, 💭 think, ✨ flow, 🌟 clarity")

    if st.button("Add Channel", type="primary"):
        if not new_slug or not new_name:
            st.error("Slug and name are required.")
        else:
            _append_channel(
                slug=new_slug, name=new_name,
                video_format=new_format, music_generator=new_gen,
                prompts=[p.strip() for p in new_prompts.strip().split("\n") if p.strip()],
                doodles=[d.strip() for d in new_doodles.strip().split("\n") if d.strip()],
                titles=[t.strip() for t in new_titles.strip().split("\n") if t.strip()],
                tags=[t.strip() for t in new_tags.split(",") if t.strip()],
                chapters=[c.strip() for c in new_chapters.split(",") if c.strip()],
            )
            st.success(f"✅ Channel `{new_slug}` added! Restart the app to see it.")


# ── Helpers ───────────────────────────────────────────────────────────────────

def _append_channel(slug, name, video_format, music_generator,
                    prompts, doodles, titles, tags, chapters):
    """Append a new Channel definition to registry.py."""
    var_name = slug.upper().replace("-", "_")
    indent   = "    "
    def fmt_list(items, indent):
        inner = f",\n{indent}        ".join(f'"{i}"' for i in items)
        return f"[\n{indent}        {inner},\n{indent}    ]"

    block = f"""
{var_name} = Channel(
    slug="{slug}",
    name="{name}",
    music_prompts={fmt_list(prompts, indent)},
    vinyl_doodles={fmt_list(doodles, indent)},
    title_templates={fmt_list(titles, indent)},
    description_template=DESC,
    tags={fmt_list(tags, indent)},
    chapters={fmt_list(chapters, indent)},
    video_format="{video_format}",
    music_generator="{music_generator}",
)
"""
    registry_path = os.path.join(os.path.dirname(__file__), "channels", "registry.py")
    with open(registry_path, "r") as f:
        content = f.read()

    # Insert before ALL_CHANNELS dict
    insert_before = "\n# ── REGISTRY"
    content = content.replace(insert_before, block + insert_before)

    # Add to ALL_CHANNELS dict
    content = content.replace(
        "}\n",
        f'    "{slug}":{" " * max(1, 22 - len(slug))}{var_name},\n}}\n',
        1
    )

    with open(registry_path, "w") as f:
        f.write(content)

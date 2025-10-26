import streamlit as st
from yt_dlp import YoutubeDL
import os
import re
import requests
from io import BytesIO

# Ensure downloads folder exists
if not os.path.exists("downloads"):
    os.makedirs("downloads")

st.title("🎬 YouTube Downloader")

url = st.text_input("Enter YouTube URL (video only)")

download_type = st.radio("Select type:", ["Video", "Audio"])

formats_dict = {}
thumbnail_url = None
video_title = None

if url:
    # Fetch video info
    with YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)
        video_title = info.get('title')
        thumbnail_url = info.get('thumbnail')
        formats = info.get('formats', [])

        if download_type == "Video":
            resolutions = {}
            for f in formats:
                if f.get('vcodec') != 'none':
                    height = f.get('height')
                    if height:
                        filesize_bytes = f.get('filesize_approx') or 0
                        resolutions[height] = (f.get('format_id'), round(filesize_bytes / (1024*1024), 2))

            available_resolutions = sorted(resolutions.keys(), reverse=True)
            formats_dict = {str(h): resolutions[h] for h in available_resolutions}

# Show thumbnail
if thumbnail_url:
    response = requests.get(thumbnail_url)
    st.image(BytesIO(response.content), caption=video_title, use_container_width=True)

# Select quality
if download_type == "Video" and formats_dict:
    quality = st.selectbox("Select video quality:", list(formats_dict.keys()))
    size_mb = formats_dict[quality][1]
    st.info(f"Approximate file size: {size_mb} MB")
else:
    quality = None

# Create a single progress bar placeholder
progress_bar = st.progress(0)
status_text = st.empty()  # Placeholder for text updates

def progress_hook(d):
    if d['status'] == 'downloading':
        percent_str = d.get('_percent_str', '0.0%').strip()
        # Remove ANSI color codes
        percent_str = re.sub(r'\x1b\[[0-9;]*m', '', percent_str)
        try:
            percent = float(percent_str.replace('%',''))
        except:
            percent = 0
        progress_bar.progress(percent / 100)
        speed = d.get('_speed_str', '')
        status_text.text(f"Downloading: {percent_str} at {speed}")

if st.button("Download"):
    if not url:
        st.warning("Enter a valid URL.")
    else:
        st.info("Starting download...")

        try:
            options = {}

            if download_type == "Audio":
                options = {
                    'format': 'bestaudio/best',
                    'outtmpl': 'downloads/%(title)s.%(ext)s',
                    'progress_hooks': [progress_hook],
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
            else:
                if quality is None:
                    st.warning("No video formats found.")
                    st.stop()
                format_id = formats_dict[quality][0]
                options = {
                    'format': format_id + '+bestaudio/best',
                    'outtmpl': 'downloads/%(title)s.%(ext)s',
                    'merge_output_format': 'mp4',
                    'progress_hooks': [progress_hook],
                }

            with YoutubeDL(options) as ydl:
                ydl.download([url])

            st.success("✅ Download completed! Check the 'downloads' folder.")

        except Exception as e:
            st.error(f"Error: {e}")

import streamlit as st
import os
from utils import download_youtube_video, extract_audio
from transcriber import transcribe_audio
from summarizer import summarize_text

st.set_page_config(page_title="AI Video Summarizer", layout="centered")

st.title("🎞️ AI Video Summarizer")
st.write("Paste a YouTube video link to generate transcript and summary.")

youtube_link = st.text_input("📺 YouTube Video URL")

if youtube_link:
    try:
        st.info("📥 Downloading video...")
        video_path = download_youtube_video(youtube_link)

        st.success("✅ Video downloaded!")
        st.video(video_path)

        audio_path = "audio.wav"

        if st.button("Generate Summary"):
            st.info("🔊 Extracting audio...")
            extract_audio(video_path, audio_path)

            st.info("🧠 Transcribing...")
            transcript = transcribe_audio(audio_path)

            st.subheader("📝 Transcript")
            st.write(transcript)

            st.info("✍️ Summarizing...")
            summary = summarize_text(transcript)

            st.subheader("📌 Summary")
            st.write(summary)

            os.remove(video_path)
            os.remove(audio_path)

    except Exception as e:
        st.error(f"❌ Error: {e}")

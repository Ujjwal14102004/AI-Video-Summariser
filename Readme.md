# YouTube Downloader Enhanced

An advanced YouTube downloader built with Streamlit and yt-dlp. Features:

- Download video, audio, or playlists
- Dynamic video quality selection (up to 4K)
- Video thumbnail preview
- Download progress bar and approximate file size
- Merges video + audio automatically
- Saves all downloads in `downloads/` folder

## Setup

```bash
pip install streamlit yt-dlp requests
streamlit run app.py

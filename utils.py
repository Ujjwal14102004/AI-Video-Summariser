import yt_dlp
import os
import uuid
from moviepy import VideoFileClip

def download_youtube_video(url, output_folder="downloads"):
    os.makedirs(output_folder, exist_ok=True)
    video_id = str(uuid.uuid4())
    output_path = os.path.join(output_folder, f"{video_id}.mp4")

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': output_path,
        'quiet': True,
        'merge_output_format': 'mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return output_path

def extract_audio(video_path, output_audio_path):
    video = VideoFileClip(video_path)
    if video.audio:
        video.audio.write_audiofile(output_audio_path, codec='pcm_s16le')

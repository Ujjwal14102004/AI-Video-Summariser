# AI-Video-Summariser


# 🎮 AI Video Summarizer

A locally hosted AI app that takes a **YouTube video URL**, downloads it, extracts audio, transcribes it using **Whisper**, and summarizes the transcript using **state-of-the-art transformer models** (T5 or BART).

---

## 🚀 Features

- 🔗 Input YouTube URL (no need to upload files)
- 🧠 Uses OpenAI Whisper for transcription
- 📝 Summarizes long transcripts using HuggingFace models (T5/BART)
- 💽 Built with Streamlit for a clean local interface
- 🔐 No API keys or cloud services required

---

## 🛠️ Tech Stack

| Component           | Tool/Framework               |
|---------------------|------------------------------|
| UI / Frontend       | Streamlit                    |
| Video Download      | yt-dlp                       |
| Audio Extraction    | FFmpeg                       |
| Transcription       | Whisper (via PyTorch)        |
| Summarization       | T5-base or BART-large-cnn    |
| Model Storage       | safetensors                  |
| Core Framework      | PyTorch                      |

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-video-summarizer.git
   cd ai-video-summarizer
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install FFmpeg**
   - Download from: https://ffmpeg.org/download.html
   - Or install using Chocolatey (Windows):
     ```bash
     choco install ffmpeg -y
     ```

---

## ▶️ Running the App

```bash
python -m streamlit run main.py
```

Make sure `ffmpeg` is accessible in your system's PATH.

---

## 🧠 Models Used

- **Whisper (tiny/base)** — for accurate and multilingual transcription.
- **T5-base / BART-large-cnn** — transformer models for high-quality summarization.
- All models are loaded using **`safetensors`** for secure and fast inference.

---

## 📅 Example Usage

1. Paste a YouTube URL in the app.
2. The app:
   - Downloads the video
   - Extracts audio
   - Transcribes speech to text
   - Summarizes the transcript
3. Displays both transcript and summary in the browser.

---

## 🧹 Troubleshooting

- **yt-dlp timeout**
  ```bash
  yt-dlp --retries 10 --fragment-retries 10 "<YouTube URL>"
  ```

- **FFmpeg not found?**
  Make sure it's installed and added to your system PATH.

- **Partial downloads?**
  Use the `-c` flag to resume:
  ```bash
  yt-dlp -c "<YouTube URL>"
  ```

---

## 📌 To-Do / Future Features

- Multi-language support
- PDF/Doc export for summaries
- Batch video processing
- Visual summary generation

---

## 📄 License

MIT License


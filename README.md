
---


# 🎧 YouTube Downloader CLI (MP3/MP4)

A simple command-line tool to download YouTube videos as MP4 or extract audio as MP3 — with interactive prompts and conversion magic. Built using `pytubefix`, `moviepy`, and `InquirerPy`.

---

## Features

- 📥 Download YouTube videos in selected resolutions (highest, 480p, 360p)
- 🎵 Extract and convert audio to MP3
- 📂 Auto-creates download directory if missing
- 🧠 Interactive CLI using InquirerPy
- 🛡️ Error handling so it doesn't freak out

---

## 📦 Requirements

- Python 3.7+
- `pytubefix`
- `moviepy`
- `InquirerPy`

---

## 🔧 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/yt-downloader-cli.git
   cd yt-downloader-cli
```

2. Create and activate a virtual environment (optional but recommended):
    
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```
    
3. Install dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```
    

---

## 🧠 Usage

```bash
python downloader.py
```

Then follow the on-screen prompts:

- Paste a YouTube URL
    
- Choose format: MP3 or MP4
    
- (If MP4) Pick your desired resolution
    

---

## 🛠 Configuration

By default, files are saved in a folder defined by:

```python
default_path = "YOUR_PATH_HERE"
```

👉 Replace `"YOUR_PATH_HERE"` with your desired path or modify the code to dynamically ask for it.

---

## Troubleshooting

- `moviepy` uses `ffmpeg`. If you run into issues, install `ffmpeg` and ensure it's in your system path.
---


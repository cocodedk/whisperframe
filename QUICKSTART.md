# 🚀 Quick Start Guide

## For Impatient Users

Want to start transcribing videos immediately? Follow these steps:

### 1. Install Everything (2 minutes)

```bash
# Download and run the installer
chmod +x install_manually.sh
./install_manually.sh
```

This will:
- ✅ Create a virtual environment
- ✅ Install PyTorch and Whisper
- ✅ Test that everything works

### 2. Transcribe Your First Video

```bash
# Use Python from the virtual environment
env/bin/python video_transcriber.py your_video.mp4
```

**That's it!** The script will:
1. Extract audio from your video
2. Transcribe it using AI
3. Create 4 output files (txt, vtt, srt, json)

---

## 📂 What You Get

After transcription, you'll find these files:

```
your_video.txt     # Plain text transcript
your_video.vtt     # WebVTT subtitles (for web players)
your_video.srt     # SubRip subtitles (for video players)
your_video.json    # Detailed data with timestamps
```

---

## ⚡ Common Use Cases

### Persian/Farsi Videos
```bash
env/bin/python video_transcriber.py persian_video.mp4 --language Persian
```

### High Quality Transcription
```bash
env/bin/python video_transcriber.py important_meeting.mp4 --model large
```

### Multiple Files
```bash
for video in *.mp4; do
    env/bin/python video_transcriber.py "$video"
done
```

### Custom Output Location
```bash
env/bin/python video_transcriber.py video.mp4 --output-dir ./transcripts
```

---

## 🛠️ Troubleshooting

**Script not found?** Make sure you're in the right directory:
```bash
ls -la video_transcriber.py
```

**Permission denied?** Make scripts executable:
```bash
chmod +x *.sh
```

**No virtual environment?** Run the installer:
```bash
./install_manually.sh
```

**FFmpeg not found?** Install it:
```bash
sudo apt update && sudo apt install ffmpeg
```

---

## 🎯 Pro Tips

1. **Start with `small` model** - good balance of speed and accuracy
2. **Use `tiny` for quick tests** - fastest but lower quality
3. **Use `large` for important content** - best quality but slowest
4. **Specify language when known** - `--language Persian` is faster than auto-detection
5. **Keep audio files for debugging** - use `--keep-audio` flag

---

Need more details? Check the full [README.md](README.md)

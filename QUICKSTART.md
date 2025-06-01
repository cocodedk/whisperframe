# 🚀 Quick Start Guide

## For Impatient Users

Want to start processing videos immediately? This guide covers both transcription and frame extraction:

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

### 2. Process Your First Video

#### 🎤 Transcribe a Video
```bash
# Use Python from the virtual environment
env/bin/python video_transcriber.py your_video.mp4
```

**That's it!** The script will:
1. Extract audio from your video
2. Transcribe it using AI
3. Create 4 output files (txt, vtt, srt, json)

#### 📸 Extract Frames from Video
```bash
# Extract 1 frame per second (default)
env/bin/python video_frame_extractor.py your_video.mp4
```

**That's it!** The script will:
1. Extract frames at 1 fps (configurable)
2. Save them as numbered image files
3. Create organized output directory

---

## 📂 What You Get

### 🎤 After Transcription
```
your_video.txt        # Plain text transcript
your_video.vtt        # WebVTT subtitles (for web players)
your_video.srt        # SubRip subtitles (for video players)
your_video.json       # Detailed data with timestamps
your_video_audio.wav  # Extracted audio (kept by default)
```

### 📸 After Frame Extraction
```
output/                             # Default output directory (git ignored)
└── your_video_frames/             # Video-specific subdirectory
    ├── your_video_frame_0001.jpg  # First frame (includes video name)
    ├── your_video_frame_0002.jpg  # Second frame
    ├── your_video_frame_0003.jpg  # Third frame
    ├── ...                        # More frames
    └── contact_sheet_your_video.jpg  # Optional contact sheet
```

---

## ⚡ Common Use Cases

### 🎤 Transcription Use Cases

#### Persian/Farsi Videos
```bash
env/bin/python video_transcriber.py persian_video.mp4 --language Persian
```

#### High Quality Transcription
```bash
env/bin/python video_transcriber.py important_meeting.mp4 --model large
```

#### Custom Output Location
```bash
env/bin/python video_transcriber.py video.mp4 --output-dir ./transcripts
```

### 📸 Frame Extraction Use Cases

#### Fast Frame Extraction (2 fps)
```bash
env/bin/python video_frame_extractor.py video.mp4 --fps 2
```

#### Time-lapse Style (1 frame every 5 seconds)
```bash
env/bin/python video_frame_extractor.py video.mp4 --fps 0.2
```

#### High Quality PNG with Contact Sheet
```bash
env/bin/python video_frame_extractor.py video.mp4 --format png --quality 1 --contact-sheet
```

### 🔄 Batch Processing
```bash
# Process multiple files
for video in *.mp4; do
    env/bin/python video_transcriber.py "$video"
    env/bin/python video_frame_extractor.py "$video" --fps 1
done
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

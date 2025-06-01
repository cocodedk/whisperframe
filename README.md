# Video Transcriber with Whisper

A Python script that extracts audio from video files and transcribes them using OpenAI's Whisper AI model.

## ✨ Features

- **Audio Extraction**: Automatically extracts audio from video files using FFmpeg
- **AI Transcription**: Uses OpenAI's Whisper for accurate speech-to-text conversion
- **Multiple Output Formats**: Generates `.txt`, `.vtt`, `.srt`, and `.json` files
- **Language Support**: Auto-detection or manual language specification
- **Model Selection**: Choose from different Whisper model sizes
- **Subtitle Generation**: Creates subtitle files with timestamps
- **Clean Interface**: Beautiful command-line interface with progress indicators

## 🔧 Prerequisites

- **Python 3.8+**
- **FFmpeg** (for audio extraction)
- **Sufficient disk space** for model downloads (models range from ~40MB to ~3GB)

## 🚀 Quick Start

### 1. Install Dependencies

**Recommended method (handles virtual environments automatically):**

```bash
chmod +x install_manually.sh
./install_manually.sh
```

**Alternative method:**

```bash
# Make setup script executable and run it
chmod +x setup.sh
./setup.sh
```

**Manual installation:**

```bash
# Install FFmpeg (Ubuntu/Debian)
sudo apt update && sudo apt install ffmpeg

# Create virtual environment
python3 -m venv env

# Activate virtual environment
# For Bash/Zsh:
source env/bin/activate
# For Fish shell:
source activate_env.fish

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Transcription

**If using virtual environment, activate it first:**

```bash
# For Bash/Zsh:
source env/bin/activate

# For Fish shell:
source activate_env.fish

# Or use Python directly from virtual environment:
env/bin/python video_transcriber.py your_video.mp4
```

**Usage examples:**

```bash
# Basic usage
python video_transcriber.py your_video.mp4

# Specify language and model
python video_transcriber.py video.mp4 --language Persian --model medium

# Custom output directory
python video_transcriber.py video.mp4 --output-dir ./transcripts

# Keep extracted audio file
python video_transcriber.py video.mp4 --keep-audio
```

## 📖 Usage Examples

### Basic Transcription
```bash
python video_transcriber.py lecture.mp4
```

### Persian/Farsi Content
```bash
python video_transcriber.py persian_video.mp4 --language Persian --model small
```

### High-Quality Transcription
```bash
python video_transcriber.py interview.mp4 --model large --output-dir ./results
```

### Batch Processing
```bash
# Process multiple files
for video in *.mp4; do
    python video_transcriber.py "$video" --language auto --model medium
done
```

## ⚙️ Command Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--language` | `-l` | Language code or 'auto' for detection | `auto` |
| `--model` | `-m` | Whisper model size | `small` |
| `--output-dir` | `-o` | Output directory | Same as video |
| `--keep-audio` | `-k` | Keep extracted audio file | `false` |

### Model Sizes

| Model    | Size   | VRAM   | Speed   | Accuracy |
|----------|--------|--------|---------|----------|
| `tiny`   | ~40MB  | Low    | Fastest | Basic    |
| `base`   | ~150MB | Low    | Fast    | Good     |
| `small`  | ~500MB | Medium | Medium  | Better   |
| `medium` | ~1.5GB | Medium | Slower  | High     |
| `large`  | ~3GB   | High   | Slowest | Best     |

## 📁 Output Files

The script generates multiple output formats:

```
video_name.txt       # Plain text transcription
video_name.vtt       # WebVTT subtitles
video_name.srt       # SubRip subtitles
video_name.json      # Detailed JSON with timestamps
video_name_audio.wav # Extracted audio (if --keep-audio)
```

## 🌍 Supported Languages

Whisper supports 99+ languages including:
- English, Spanish, French, German, Italian
- Persian/Farsi, Arabic, Hebrew
- Chinese, Japanese, Korean
- Russian, Portuguese, Dutch
- And many more...

Use `--language auto` for automatic detection or specify like `--language Persian`.

## 🔧 Troubleshooting

### FFmpeg Not Found
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

### Out of Memory Error
Try a smaller model:
```bash
python video_transcriber.py video.mp4 --model tiny
```

### Slow Transcription
Use GPU acceleration (if available):
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Permission Error
Make sure you have write permissions in the output directory.

## 📊 Performance Tips

1. **Model Selection**: Use `small` for balanced speed/accuracy
2. **GPU Support**: Install CUDA-enabled PyTorch for faster processing
3. **Audio Quality**: Higher quality audio = better transcription
4. **File Size**: Large files may take significant time and memory

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📄 License

This project is open source. Whisper is released under MIT license by OpenAI.

## 🙏 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for the amazing AI transcription
- [FFmpeg](https://ffmpeg.org/) for audio/video processing
- The open-source community for inspiration and tools

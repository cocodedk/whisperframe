# Video Processing Tools

A collection of Python scripts for video processing: transcription using OpenAI's Whisper and frame extraction using FFmpeg.

## ✨ Features

### 🎤 Video Transcriber (`video_transcriber.py`)
- **Audio Extraction**: Automatically extracts audio from video files using FFmpeg
- **AI Transcription**: Uses OpenAI's Whisper for accurate speech-to-text conversion
- **Multiple Output Formats**: Generates `.txt`, `.vtt`, `.srt`, and `.json` files
- **Language Support**: Auto-detection or manual language specification
- **Model Selection**: Choose from different Whisper model sizes
- **Subtitle Generation**: Creates subtitle files with timestamps

### 📸 Frame Extractor (`video_frame_extractor.py`)
- **Configurable Frame Rate**: Extract 1 frame per second (default) or any custom rate
- **Multiple Image Formats**: Output as JPG, PNG, BMP, TIFF, or WebP
- **Quality Control**: Adjustable image quality settings
- **Smart Output**: Organized frame directories with custom naming
- **Contact Sheets**: Optional creation of contact sheet/montage
- **Video Analysis**: Shows duration, resolution, and estimated frame count

### 🎨 Common Features
- **Clean Interface**: Beautiful command-line interface with progress indicators
- **Error Handling**: Comprehensive validation and helpful error messages
- **Cross-platform**: Works on Linux, macOS, and Windows

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

### 🎤 Video Transcription
```bash
# Basic transcription
python video_transcriber.py your_video.mp4

# Specify language and model
python video_transcriber.py video.mp4 --language Persian --model medium

# Custom output directory
python video_transcriber.py video.mp4 --output-dir ./transcripts

# Delete audio after transcription (audio kept by default)
python video_transcriber.py video.mp4 --delete-audio
```

### 📸 Frame Extraction
```bash
# Basic extraction (1 frame per second)
python video_frame_extractor.py your_video.mp4

# Extract 2 frames per second in PNG format
python video_frame_extractor.py video.mp4 --fps 2 --format png

# Extract every 2 seconds (0.5 fps) with contact sheet
python video_frame_extractor.py video.mp4 --fps 0.5 --contact-sheet

# High quality extraction with custom prefix
python video_frame_extractor.py video.mp4 --fps 1 --quality 1 --prefix scene
```

## 📖 Usage Examples

### 🎤 Transcription Examples

#### Basic Transcription
```bash
python video_transcriber.py lecture.mp4
```

#### Persian/Farsi Content
```bash
python video_transcriber.py persian_video.mp4 --language Persian --model small
```

#### High-Quality Transcription
```bash
python video_transcriber.py interview.mp4 --model large --output-dir ./results
```

### 📸 Frame Extraction Examples

#### Time-lapse Frames
```bash
# Extract 1 frame every 10 seconds
python video_frame_extractor.py timelapse.mp4 --fps 0.1
```

#### Scene Analysis
```bash
# Extract 4 frames per second for detailed analysis
python video_frame_extractor.py movie.mp4 --fps 4 --format png --contact-sheet
```

#### Thumbnail Generation
```bash
# Extract key frames with custom naming
python video_frame_extractor.py presentation.mp4 --fps 0.5 --prefix thumbnail --quality 1
# Output: output/presentation_frames/presentation_thumbnail_0001.jpg, etc.
```

### 🔄 Batch Processing
```bash
# Process multiple files for transcription
for video in *.mp4; do
    python video_transcriber.py "$video" --language auto --model medium
done

# Extract frames from multiple videos
for video in *.mp4; do
    python video_frame_extractor.py "$video" --fps 1 --contact-sheet
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

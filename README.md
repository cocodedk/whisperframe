# 🎬 WhisperFrame - AI-Powered Video Processing Toolkit

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-Required-orange.svg)](https://ffmpeg.org/)

> **WhisperFrame** is a comprehensive Python toolkit that combines OpenAI's Whisper AI transcription with advanced video frame extraction capabilities. Perfect for content creators, researchers, and developers who need to process video content for analysis, transcription, or archival purposes.

## ✨ Features

### 🎤 **AI Video Transcription** (`video_transcriber.py`)
- **🎵 Audio Extraction**: Automatically extracts audio from video files using FFmpeg
- **🤖 AI Transcription**: Uses OpenAI's Whisper for accurate speech-to-text conversion
- **📝 Multiple Output Formats**: Generates `.txt`, `.vtt`, `.srt`, and `.json` files
- **🌍 Language Support**: Auto-detection or manual language specification (99+ languages)
- **⚡ Model Selection**: Choose from different Whisper model sizes (tiny to large)
- **🎬 Subtitle Generation**: Creates subtitle files with precise timestamps

### 📸 **Smart Frame Extraction** (`video_frame_extractor.py`)
- **⚙️ Configurable Frame Rate**: Extract 1 frame per second (default) or any custom rate
- **🖼️ Multiple Image Formats**: Output as JPG, PNG, BMP, TIFF, or WebP
- **🎯 Quality Control**: Adjustable image quality settings
- **📁 Smart Output**: Organized frame directories with custom naming
- **🖼️ Contact Sheets**: Optional creation of contact sheet/montage
- **📊 Video Analysis**: Shows duration, resolution, and estimated frame count

### 🎨 **Common Features**
- **✨ Clean Interface**: Beautiful command-line interface with progress indicators
- **🛡️ Error Handling**: Comprehensive validation and helpful error messages
- **🔄 Cross-platform**: Works on Linux, macOS, and Windows
- **🚀 Performance Optimized**: Efficient processing with minimal memory usage

## 🚀 Quick Start

### 1. **Install Dependencies**

**🚀 Recommended method (handles virtual environments automatically):**

```bash
chmod +x install_manually.sh
./install_manually.sh
```

**🔧 Alternative method:**

```bash
# Make setup script executable and run it
chmod +x setup.sh
./setup.sh
```

**📦 Manual installation:**

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

### 2. **Run Transcription**

**If using virtual environment, activate it first:**

```bash
# For Bash/Zsh:
source env/bin/activate

# For Fish shell:
source activate_env.fish

# Or use Python directly from virtual environment:
env/bin/python video_transcriber.py your_video.mp4
```

## 📖 Usage Examples

### 🎤 **Video Transcription Examples**

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

### 📸 **Frame Extraction Examples**

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

### 🔄 **Batch Processing**
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

### Video Transcriber Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--language` | `-l` | Language code or 'auto' for detection | `auto` |
| `--model` | `-m` | Whisper model size | `small` |
| `--output-dir` | `-o` | Output directory | Same as video |
| `--keep-audio` | `-k` | Keep extracted audio file | `true` |
| `--delete-audio` | | Delete audio after transcription | `false` |

### Frame Extractor Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--fps` | `-f` | Frames per second to extract | `1.0` |
| `--format` | | Output image format | `jpg` |
| `--quality` | `-q` | Image quality (1-31, lower=better) | `2` |
| `--prefix` | `-p` | Frame filename prefix | `frame` |
| `--contact-sheet` | | Generate contact sheet | `false` |
| `--output-dir` | `-o` | Output directory | `output/video_frames` |

### Model Sizes

| Model    | Size   | VRAM   | Speed   | Accuracy |
|----------|--------|--------|---------|----------|
| `tiny`   | ~40MB  | Low    | Fastest | Basic    |
| `base`   | ~150MB | Low    | Fast    | Good     |
| `small`  | ~500MB | Medium | Medium  | Better   |
| `medium` | ~1.5GB | Medium | Slower  | High     |
| `large`  | ~3GB   | High   | Slowest | Best     |

## 📁 Output Structure

The toolkit generates organized output files:

```
output/
├── video_name.txt          # Plain text transcription
├── video_name.vtt          # WebVTT subtitles
├── video_name.srt          # SubRip subtitles
├── video_name.json         # Detailed JSON with timestamps
├── video_name_audio.wav    # Extracted audio (if kept)
└── video_name_frames/      # Extracted frames directory
    ├── frame_0001.jpg
    ├── frame_0002.jpg
    └── ...
```

## 🌍 Supported Languages

Whisper supports 99+ languages including:
- **European**: English, Spanish, French, German, Italian, Dutch, Portuguese
- **Middle Eastern**: Persian/Farsi, Arabic, Hebrew, Turkish
- **Asian**: Chinese, Japanese, Korean, Hindi, Thai, Vietnamese
- **Slavic**: Russian, Polish, Czech, Ukrainian
- **And many more...**

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

1. **🎯 Model Selection**: Use `small` for balanced speed/accuracy
2. **🚀 GPU Support**: Install CUDA-enabled PyTorch for faster processing
3. **🎵 Audio Quality**: Higher quality audio = better transcription
4. **💾 File Size**: Large files may take significant time and memory
5. **🔄 Batch Processing**: Process multiple files sequentially for efficiency

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🐛 Report Bugs**: Open an issue with detailed bug reports
2. **💡 Suggest Features**: Share your ideas for improvements
3. **🔧 Submit PRs**: Fork the repository and submit pull requests
4. **📚 Improve Docs**: Help enhance documentation and examples

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/yourusername/whisperframe.git
cd whisperframe

# Create virtual environment
python3 -m venv env
source env/bin/activate  # or source activate_env.fish

# Install development dependencies
pip install -r requirements.txt

# Make your changes and test
python video_transcriber.py --help
python video_frame_extractor.py --help
```

## 📄 License

This project is licensed under the **Apache License 2.0** - see the [LICENSE](LICENSE) file for details.

**Copyright 2024 [COCODE.DK](https://cocode.dk)**

## 🙏 Acknowledgments

- **[OpenAI Whisper](https://github.com/openai/whisper)** for the amazing AI transcription technology
- **[FFmpeg](https://ffmpeg.org/)** for robust audio/video processing capabilities
- **The open-source community** for inspiration, tools, and continuous support

## 🌟 Star History

If you find this project useful, please consider giving it a ⭐️ on GitHub!

---

**Made with ❤️ by [COCODE.DK](https://cocode.dk)**

*Empowering developers with AI-powered video processing tools*

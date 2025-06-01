#!/bin/bash

echo "🎬 Video Transcriber Setup"
echo "=========================="

# Check if we're in a virtual environment
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "✅ Virtual environment detected: $VIRTUAL_ENV"
else
    echo "⚠️  No virtual environment detected."
    echo "Creating virtual environment automatically..."

    # Create virtual environment
    python3 -m venv env
    if [ $? -ne 0 ]; then
        echo "❌ Failed to create virtual environment"
        echo "Please install python3-venv package:"
        echo "  sudo apt install python3-venv python3-full"
        exit 1
    fi

    echo "✅ Virtual environment created: ./env"
    echo ""
    echo "🔧 To activate manually in the future, run:"
    echo "   source env/bin/activate"
    echo ""

    # Activate the virtual environment for this script
    source env/bin/activate
    echo "✅ Virtual environment activated for setup"
fi

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8 or newer."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Check for ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ ffmpeg not found in PATH"
    echo "Please install ffmpeg:"
    echo ""
    echo "Ubuntu/Debian:"
    echo "  sudo apt update && sudo apt install ffmpeg"
    echo ""
    echo "macOS:"
    echo "  brew install ffmpeg"
    echo ""
    echo "Windows:"
    echo "  Download from https://ffmpeg.org/download.html"
    echo ""
    read -p "Continue without ffmpeg? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo "✅ ffmpeg found: $(ffmpeg -version | head -n1)"
fi

# Install Python dependencies
echo ""
echo "📦 Installing Python dependencies..."

# Use pip from virtual environment if available
if [[ "$VIRTUAL_ENV" != "" ]]; then
    pip install -r requirements.txt
else
    # Fallback to system pip with user install
    echo "Installing in user space..."
    pip3 install --user -r requirements.txt
fi

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Setup completed successfully!"
    echo ""
    if [[ "$VIRTUAL_ENV" != "" ]]; then
        echo "💡 Virtual environment is active. Usage examples:"
        echo "  python video_transcriber.py video.mp4"
        echo "  python video_transcriber.py video.mp4 --language Persian --model medium"
        echo "  python video_transcriber.py --help"
        echo ""
        echo "⚠️  Remember to activate the virtual environment before using:"
        echo "  source env/bin/activate"
    else
        echo "Usage examples:"
        echo "  python3 video_transcriber.py video.mp4"
        echo "  python3 video_transcriber.py video.mp4 --language Persian --model medium"
        echo "  python3 video_transcriber.py --help"
    fi
else
    echo ""
    echo "❌ Installation failed. Please check the error messages above."
    exit 1
fi

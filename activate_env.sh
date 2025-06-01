#!/bin/bash

# Simple script to activate the virtual environment

if [ ! -d "env" ]; then
    echo "❌ Virtual environment not found!"
    echo "Run ./setup.sh first to create it."
    exit 1
fi

echo "🔧 Activating virtual environment..."
source env/bin/activate

echo "✅ Virtual environment activated!"
echo ""
echo "Now you can run:"
echo "  python video_transcriber.py your_video.mp4"
echo ""
echo "To deactivate when done, run:"
echo "  deactivate"

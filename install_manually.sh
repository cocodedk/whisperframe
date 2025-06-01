#!/bin/bash

echo "🔧 Manual Installation Guide"
echo "============================="
echo ""

# Activate virtual environment if it exists
if [ -d "env" ]; then
    echo "✅ Activating existing virtual environment..."
    source env/bin/activate
else
    echo "📦 Creating virtual environment..."
    python3 -m venv env
    source env/bin/activate
    echo "✅ Virtual environment created and activated"
fi

echo ""
echo "🚀 Installing dependencies step by step..."
echo ""

# Install PyTorch first
echo "1️⃣ Installing PyTorch..."
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu

if [ $? -ne 0 ]; then
    echo "❌ PyTorch installation failed. Trying alternative..."
    pip install torch torchaudio
fi

echo ""
echo "2️⃣ Installing Whisper..."

# Try different Whisper installation methods
echo "Trying method 1: pip install openai-whisper..."
pip install openai-whisper

if [ $? -ne 0 ]; then
    echo "❌ Method 1 failed. Trying method 2: git install..."
    pip install git+https://github.com/openai/whisper.git

    if [ $? -ne 0 ]; then
        echo "❌ Method 2 failed. Trying method 3: specific version..."
        pip install openai-whisper==20240930

        if [ $? -ne 0 ]; then
            echo "❌ All methods failed. Manual installation required."
            echo ""
            echo "Please try these commands manually:"
            echo "1. source env/bin/activate"
            echo "2. pip install --upgrade pip setuptools wheel"
            echo "3. pip install torch torchaudio"
            echo "4. pip install openai-whisper"
            exit 1
        fi
    fi
fi

echo ""
echo "3️⃣ Testing installation..."
python -c "import whisper; print('✅ Whisper imported successfully')" 2>/dev/null

if [ $? -eq 0 ]; then
    echo "🎉 Installation completed successfully!"
    echo ""
    echo "Usage:"
    echo "  source env/bin/activate  # (if not already active)"
    echo "  python video_transcriber.py your_video.mp4"
else
    echo "⚠️ Installation completed but Whisper import failed."
    echo "Please check for any error messages above."
fi

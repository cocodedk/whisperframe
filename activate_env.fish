#!/usr/bin/env fish

# Fish shell compatible activation script

if not test -d "env"
    echo "❌ Virtual environment not found!"
    echo "Run ./install_manually.sh first to create it."
    exit 1
end

echo "🔧 Activating virtual environment for Fish shell..."

# Set environment variables for Fish
set -gx VIRTUAL_ENV (realpath env)
set -gx PATH $VIRTUAL_ENV/bin $PATH

# Remove PYTHONHOME if set
if set -q PYTHONHOME
    set -e PYTHONHOME
end

echo "✅ Virtual environment activated!"
echo ""
echo "Now you can run:"
echo "  python video_transcriber.py your_video.mp4"
echo ""
echo "To deactivate when done, run:"
echo "  deactivate"

# Define deactivate function
function deactivate -d "Deactivate the virtual environment"
    if set -q VIRTUAL_ENV
        set -e VIRTUAL_ENV
        if set -q _OLD_VIRTUAL_PATH
            set -gx PATH $_OLD_VIRTUAL_PATH
            set -e _OLD_VIRTUAL_PATH
        else
            # Remove the virtual env path
            set -l index (contains -i $VIRTUAL_ENV/bin $PATH)
            if test $index
                set -e PATH[$index]
            end
        end
        if set -q _OLD_VIRTUAL_PYTHONHOME
            set -gx PYTHONHOME $_OLD_VIRTUAL_PYTHONHOME
            set -e _OLD_VIRTUAL_PYTHONHOME
        end
        functions -e deactivate
        echo "Virtual environment deactivated"
    end
end

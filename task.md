# I wan to extract audio from a video file and transcribe it using whisper by a python script

Need your help to create a python script which does it.
---

### 🧰 What you need to do:

#### **Step 1: Extract audio from your video file**

Use `ffmpeg`:

```bash
ffmpeg -i your_video.mp4 -ar 16000 -ac 1 -c:a pcm_s16le output.wav
```

This:

* Converts audio to 16kHz, mono channel — perfect for Whisper
* Saves it as `output.wav`

---

#### **Step 2: Transcribe using Whisper**

```bash
whisper output.wav --language Persian --model small
```

This will create:

* `output.txt` – plain transcript
* `output.vtt` / `output.srt` – for subtitles
* `output.json` – with word timestamps (optional for syncing)

---

Let me know if you want a bash script that loops over multiple videos automatically.


### 🧰 Prerequisites:

* Python 3.8 or newer
* `ffmpeg` installed and available in your system path
* A working terminal (Linux, macOS, or Windows PowerShell)

---

### ✅ Step-by-Step Installation

#### **1. Create and activate a virtual environment** (optional but recommended)

```bash
python -m venv env
source env/bin/activate.fish
```

#### **2. Install ffmpeg**

* **Ubuntu/Debian:**

  ```bash
  sudo apt update && sudo apt install ffmpeg
  ```

#### **3. Install Whisper**

```bash
pip install git+https://github.com/openai/whisper.git
```

Optional: If you don’t have PyTorch installed:

```bash
pip install torch torchvision torchaudio
```

(use `pip install torch==<version>` if needed for your CUDA version)

---

### 🚀 Usage Example:

Transcribe a Persian audio file:

```bash
whisper /path/to/audio.wav --language Persian --model small
```

That will generate `.txt`, `.vtt`, `.srt`, and `.json` files with the transcript.

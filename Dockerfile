# WhisperFrame — CLI toolkit image (Whisper transcription + FFmpeg frame extraction)
FROM python:3.12-slim

# ffmpeg for audio/video; git because requirements.txt pulls Whisper from GitHub
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY video_transcriber.py video_frame_extractor.py ./

# Process media mounted at /data, e.g.:
#   docker run --rm -v "$PWD:/data" ghcr.io/cocodedk/whisperframe video_transcriber.py /data/clip.mp4 -l Persian
WORKDIR /data
ENTRYPOINT ["python", "/app/video_transcriber.py"]
CMD ["--help"]

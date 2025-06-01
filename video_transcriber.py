#!/usr/bin/env python3
"""
Video Transcriber using FFmpeg and Whisper
==========================================

This script extracts audio from video files and transcribes them using OpenAI's Whisper.

Usage:
    python video_transcriber.py <video_file> [options]

Example:
    python video_transcriber.py video.mp4 --language Persian --model small
"""

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Optional

try:
    import whisper
except ImportError:
    print("❌ Whisper not installed. Install it with:")
    print("pip install git+https://github.com/openai/whisper.git")
    sys.exit(1)


class VideoTranscriber:
    """Main class for video transcription workflow."""

    def __init__(self, video_path: str, language: str = "auto", model: str = "small",
                 output_dir: Optional[str] = None, keep_audio: bool = True):
        self.video_path = Path(video_path)
        self.language = language
        self.model = model
        self.output_dir = Path(output_dir) if output_dir else self.video_path.parent
        self.keep_audio = keep_audio

        # Validate input file
        if not self.video_path.exists():
            raise FileNotFoundError(f"Video file not found: {self.video_path}")

        # Create output directory if it doesn't exist
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Set output audio path
        self.audio_path = self.output_dir / f"{self.video_path.stem}_audio.wav"

    def check_ffmpeg(self) -> bool:
        """Check if ffmpeg is available in system PATH."""
        try:
            subprocess.run(["ffmpeg", "-version"],
                         capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    def extract_audio(self) -> str:
        """Extract audio from video file using ffmpeg."""
        print(f"🎵 Extracting audio from: {self.video_path.name}")

        if not self.check_ffmpeg():
            raise RuntimeError("❌ ffmpeg not found. Please install ffmpeg first.")

        # FFmpeg command to extract audio optimized for Whisper
        cmd = [
            "ffmpeg",
            "-i", str(self.video_path),
            "-ar", "16000",  # 16kHz sample rate (Whisper's preferred)
            "-ac", "1",      # Mono channel
            "-c:a", "pcm_s16le",  # PCM 16-bit little-endian
            "-y",            # Overwrite output file
            str(self.audio_path)
        ]

        try:
            # Run ffmpeg with minimal output
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"✅ Audio extracted to: {self.audio_path}")
            return str(self.audio_path)

        except subprocess.CalledProcessError as e:
            print(f"❌ FFmpeg error: {e.stderr}")
            raise RuntimeError(f"Failed to extract audio: {e}")

    def transcribe_audio(self, audio_path: str) -> dict:
        """Transcribe audio using Whisper."""
        print(f"🎤 Loading Whisper model: {self.model}")

        try:
            # Load Whisper model
            model = whisper.load_model(self.model)

            print(f"🔄 Transcribing audio...")

            # Transcribe with language detection or specified language
            if self.language.lower() == "auto":
                result = model.transcribe(audio_path)
                detected_lang = result.get("language", "unknown")
                print(f"🌍 Detected language: {detected_lang}")
            else:
                result = model.transcribe(audio_path, language=self.language)
                print(f"🌍 Using language: {self.language}")

            print("✅ Transcription completed!")
            return result

        except Exception as e:
            raise RuntimeError(f"Failed to transcribe audio: {e}")

    def save_results(self, result: dict) -> dict:
        """Save transcription results in multiple formats."""
        base_name = self.output_dir / self.video_path.stem
        output_files = {}

        print("💾 Saving transcription results...")

        # Save plain text
        txt_path = f"{base_name}.txt"
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(result["text"].strip())
        output_files["txt"] = txt_path
        print(f"📄 Text saved: {txt_path}")

        # Save VTT (WebVTT subtitle format)
        vtt_path = f"{base_name}.vtt"
        with open(vtt_path, "w", encoding="utf-8") as f:
            self._write_vtt(f, result["segments"])
        output_files["vtt"] = vtt_path
        print(f"📺 VTT subtitles saved: {vtt_path}")

        # Save SRT (SubRip subtitle format)
        srt_path = f"{base_name}.srt"
        with open(srt_path, "w", encoding="utf-8") as f:
            self._write_srt(f, result["segments"])
        output_files["srt"] = srt_path
        print(f"🎬 SRT subtitles saved: {srt_path}")

        # Save JSON with detailed information
        import json
        json_path = f"{base_name}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        output_files["json"] = json_path
        print(f"📊 JSON data saved: {json_path}")

        return output_files

    def _write_vtt(self, file, segments):
        """Write VTT subtitle format."""
        file.write("WEBVTT\n\n")
        for segment in segments:
            start = self._format_timestamp(segment["start"])
            end = self._format_timestamp(segment["end"])
            file.write(f"{start} --> {end}\n")
            file.write(f"{segment['text'].strip()}\n\n")

    def _write_srt(self, file, segments):
        """Write SRT subtitle format."""
        for i, segment in enumerate(segments, 1):
            start = self._format_timestamp(segment["start"], srt_format=True)
            end = self._format_timestamp(segment["end"], srt_format=True)
            file.write(f"{i}\n")
            file.write(f"{start} --> {end}\n")
            file.write(f"{segment['text'].strip()}\n\n")

    def _format_timestamp(self, seconds, srt_format=False):
        """Format timestamp for subtitle files."""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        milliseconds = int((seconds % 1) * 1000)

        if srt_format:
            return f"{hours:02d}:{minutes:02d}:{secs:02d},{milliseconds:03d}"
        else:
            return f"{hours:02d}:{minutes:02d}:{secs:02d}.{milliseconds:03d}"

    def cleanup(self):
        """Clean up temporary audio file when explicitly requested."""
        if self.audio_path.exists():
            self.audio_path.unlink()
            print(f"🗑️  Cleaned up: {self.audio_path}")

    def run(self) -> dict:
        """Execute the complete transcription workflow."""
        try:
            # Extract audio
            audio_path = self.extract_audio()

            # Transcribe
            result = self.transcribe_audio(audio_path)

            # Save results
            output_files = self.save_results(result)

            # Cleanup (only if specifically requested)
            if not self.keep_audio:
                self.cleanup()

            return {
                "success": True,
                "video_file": str(self.video_path),
                "audio_file": str(self.audio_path) if self.keep_audio else None,
                "output_files": output_files,
                "transcription": result["text"].strip()
            }

        except Exception as e:
            print(f"❌ Error: {e}")
            return {
                "success": False,
                "error": str(e)
            }


def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(
        description="Extract audio from video and transcribe using Whisper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python video_transcriber.py video.mp4
  python video_transcriber.py video.mp4 --language Persian --model medium
  python video_transcriber.py video.mp4 --output-dir ./transcripts --delete-audio
        """
    )

    parser.add_argument("video_file", help="Path to video file")
    parser.add_argument("--language", "-l", default="auto",
                       help="Language code (e.g., 'Persian', 'English') or 'auto' for detection")
    parser.add_argument("--model", "-m", default="small",
                       choices=["tiny", "base", "small", "medium", "large"],
                       help="Whisper model size (default: small)")
    parser.add_argument("--output-dir", "-o",
                       help="Output directory (default: same as video file)")
    parser.add_argument("--delete-audio", "-d", action="store_true",
                       help="Delete extracted audio file after transcription")
    parser.add_argument("--keep-audio", "-k", action="store_true",
                       help="Keep extracted audio file (default behavior)")

    args = parser.parse_args()

    print("🎬 Video Transcriber with Whisper")
    print("=" * 40)

    try:
        # Determine whether to keep audio (default True, unless --delete-audio is specified)
        keep_audio = not args.delete_audio if args.delete_audio else True

        transcriber = VideoTranscriber(
            video_path=args.video_file,
            language=args.language,
            model=args.model,
            output_dir=args.output_dir,
            keep_audio=keep_audio
        )

        result = transcriber.run()

        if result["success"]:
            print("\n🎉 Transcription completed successfully!")
            print(f"📁 Output files: {len(result['output_files'])} files created")
            print("\n📝 Transcription preview:")
            print("-" * 40)
            preview = result["transcription"][:200]
            print(f"{preview}{'...' if len(result['transcription']) > 200 else ''}")
        else:
            print(f"\n💥 Failed: {result['error']}")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n⏸️  Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

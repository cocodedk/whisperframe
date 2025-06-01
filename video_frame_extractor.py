#!/usr/bin/env python3
"""
Video Frame Extractor using FFmpeg
==================================

This script extracts frames/images from video files at configurable intervals.

Usage:
    python video_frame_extractor.py <video_file> [options]

Example:
    python video_frame_extractor.py video.mp4 --fps 2 --format png
"""

import argparse
import os
import subprocess
import sys
import math
from pathlib import Path
from typing import Optional


class VideoFrameExtractor:
    """Main class for video frame extraction workflow."""

    def __init__(self, video_path: str, fps: float = 1.0, output_dir: Optional[str] = None,
                 format: str = "jpg", quality: int = 2, prefix: str = "frame"):
        self.video_path = Path(video_path)
        self.fps = fps
        self.format = format.lower()
        self.quality = quality
        self.prefix = prefix

        # Validate input file
        if not self.video_path.exists():
            raise FileNotFoundError(f"Video file not found: {self.video_path}")

        # Set output directory
        if output_dir:
            self.output_dir = Path(output_dir)
        else:
            # Use 'output' directory (already in .gitignore) with video name subdirectory
            base_output = Path("output")
            self.output_dir = base_output / f"{self.video_path.stem}_frames"

        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Validate format
        supported_formats = ['jpg', 'jpeg', 'png', 'bmp', 'tiff', 'webp']
        if self.format not in supported_formats:
            raise ValueError(f"Unsupported format: {self.format}. Supported: {supported_formats}")

    def check_ffmpeg(self) -> bool:
        """Check if ffmpeg is available in system PATH."""
        try:
            subprocess.run(["ffmpeg", "-version"],
                         capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    def get_video_info(self) -> dict:
        """Get video information using ffprobe."""
        if not self.check_ffmpeg():
            raise RuntimeError("❌ ffmpeg not found. Please install ffmpeg first.")

        try:
            # Use ffprobe to get video duration and fps
            cmd = [
                "ffprobe", "-v", "quiet", "-print_format", "json",
                "-show_format", "-show_streams", str(self.video_path)
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            # Parse the JSON output manually for basic info
            import json
            info = json.loads(result.stdout)

            # Find video stream
            video_stream = None
            for stream in info.get('streams', []):
                if stream.get('codec_type') == 'video':
                    video_stream = stream
                    break

            if not video_stream:
                raise RuntimeError("No video stream found in file")

            # Extract basic info
            duration = float(info.get('format', {}).get('duration', 0))
            width = int(video_stream.get('width', 0))
            height = int(video_stream.get('height', 0))

            return {
                'duration': duration,
                'width': width,
                'height': height,
                'estimated_frames': math.ceil(duration * self.fps)
            }

        except subprocess.CalledProcessError as e:
            print(f"❌ FFprobe error: {e.stderr}")
            raise RuntimeError(f"Failed to get video info: {e}")
        except json.JSONDecodeError:
            # Fallback: estimate duration manually
            return {
                'duration': 0,
                'width': 0,
                'height': 0,
                'estimated_frames': 0
            }

    def extract_frames(self) -> dict:
        """Extract frames from video using ffmpeg."""
        print(f"🎬 Extracting frames from: {self.video_path.name}")
        print(f"📊 Rate: {self.fps} frames per second")
        print(f"📁 Output: {self.output_dir}")

        if not self.check_ffmpeg():
            raise RuntimeError("❌ ffmpeg not found. Please install ffmpeg first.")

        # Get video info first
        try:
            video_info = self.get_video_info()
            if video_info['duration'] > 0:
                print(f"⏱️  Video duration: {video_info['duration']:.1f} seconds")
                print(f"📸 Estimated frames: ~{video_info['estimated_frames']}")
                if video_info['width'] > 0:
                    print(f"📐 Resolution: {video_info['width']}x{video_info['height']}")
        except Exception as e:
            print(f"⚠️  Could not get video info: {e}")
            video_info = {'estimated_frames': 0}

        # Build output filename pattern with video name included
        video_name = self.video_path.stem
        output_pattern = self.output_dir / f"{video_name}_{self.prefix}_%04d.{self.format}"

        # Build FFmpeg command for frame extraction
        cmd = [
            "ffmpeg",
            "-i", str(self.video_path),
            "-vf", f"fps={self.fps}",  # Extract at specified fps
            "-y",  # Overwrite existing files
        ]

        # Add quality settings based on format
        if self.format in ['jpg', 'jpeg']:
            # JPEG quality: 1 (best) to 31 (worst)
            cmd.extend(["-q:v", str(self.quality)])
        elif self.format == 'png':
            # PNG compression: 0 (no compression) to 9 (max compression)
            cmd.extend(["-compression_level", str(min(9, self.quality * 3))])

        cmd.append(str(output_pattern))

        try:
            print("🔄 Extracting frames...")
            # Run ffmpeg with progress
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            # Count extracted frames
            video_name = self.video_path.stem
            extracted_files = list(self.output_dir.glob(f"{video_name}_{self.prefix}_*.{self.format}"))
            extracted_count = len(extracted_files)

            print(f"✅ Extracted {extracted_count} frames")
            print(f"📁 Saved to: {self.output_dir}")

            return {
                'success': True,
                'frames_extracted': extracted_count,
                'output_directory': str(self.output_dir),
                'format': self.format,
                'fps': self.fps,
                'files': [str(f) for f in extracted_files[:5]]  # Show first 5 files
            }

        except subprocess.CalledProcessError as e:
            print(f"❌ FFmpeg error: {e.stderr}")
            raise RuntimeError(f"Failed to extract frames: {e}")

    def create_contact_sheet(self, columns: int = 4) -> Optional[str]:
        """Create a contact sheet/montage of extracted frames."""
        video_name = self.video_path.stem
        extracted_files = list(self.output_dir.glob(f"{video_name}_{self.prefix}_*.{self.format}"))

        if len(extracted_files) < 2:
            print("⚠️  Need at least 2 frames to create contact sheet")
            return None

        print(f"📋 Creating contact sheet with {len(extracted_files)} frames...")

        # Sort files by name to maintain order
        extracted_files.sort()

        # Calculate rows needed
        rows = math.ceil(len(extracted_files) / columns)

        contact_sheet_path = self.output_dir / f"contact_sheet_{self.video_path.stem}.{self.format}"

        # Build montage command
        cmd = [
            "ffmpeg",
            "-y",  # Overwrite
            "-pattern_type", "glob",
            "-i", str(self.output_dir / f"{video_name}_{self.prefix}_*.{self.format}"),
            "-filter_complex", f"tile={columns}x{rows}:margin=10:padding=5",
            str(contact_sheet_path)
        ]

        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"📋 Contact sheet created: {contact_sheet_path}")
            return str(contact_sheet_path)
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Could not create contact sheet: {e.stderr}")
            return None

    def run(self, create_contact: bool = False) -> dict:
        """Execute the complete frame extraction workflow."""
        try:
            # Extract frames
            result = self.extract_frames()

            # Create contact sheet if requested
            if create_contact and result['frames_extracted'] > 1:
                contact_sheet = self.create_contact_sheet()
                result['contact_sheet'] = contact_sheet

            return result

        except Exception as e:
            print(f"❌ Error: {e}")
            return {
                'success': False,
                'error': str(e)
            }


def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(
        description="Extract frames from video files using FFmpeg",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python video_frame_extractor.py video.mp4
  python video_frame_extractor.py video.mp4 --fps 2 --format png
  python video_frame_extractor.py video.mp4 --fps 0.5 --output-dir ./frames --contact-sheet
  python video_frame_extractor.py video.mp4 --fps 1 --quality 1 --prefix scene
        """
    )

    parser.add_argument("video_file", help="Path to video file")
    parser.add_argument("--fps", "-f", type=float, default=1.0,
                       help="Frames per second to extract (default: 1.0)")
    parser.add_argument("--format", "-fmt", default="jpg",
                       choices=["jpg", "jpeg", "png", "bmp", "tiff", "webp"],
                       help="Output image format (default: jpg)")
    parser.add_argument("--quality", "-q", type=int, default=2,
                       help="Image quality: 1 (best) to 5 (fastest) for JPEG (default: 2)")
    parser.add_argument("--output-dir", "-o",
                       help="Output directory (default: output/<video_name>_frames)")
    parser.add_argument("--prefix", "-p", default="frame",
                       help="Filename prefix for extracted frames (default: frame)")
    parser.add_argument("--contact-sheet", "-c", action="store_true",
                       help="Create a contact sheet/montage of all frames")

    args = parser.parse_args()

    # Validate fps
    if args.fps <= 0:
        print("❌ FPS must be greater than 0")
        sys.exit(1)

    # Validate quality
    if not 1 <= args.quality <= 10:
        print("❌ Quality must be between 1 and 10")
        sys.exit(1)

    print("🎬 Video Frame Extractor")
    print("=" * 40)

    try:
        extractor = VideoFrameExtractor(
            video_path=args.video_file,
            fps=args.fps,
            output_dir=args.output_dir,
            format=args.format,
            quality=args.quality,
            prefix=args.prefix
        )

        result = extractor.run(create_contact=args.contact_sheet)

        if result['success']:
            print("\n🎉 Frame extraction completed successfully!")
            print(f"📸 Frames extracted: {result['frames_extracted']}")
            print(f"📁 Output directory: {result['output_directory']}")

            if result['frames_extracted'] > 0:
                print("\n📋 Sample files:")
                for file in result.get('files', [])[:3]:
                    print(f"  • {Path(file).name}")
                if result['frames_extracted'] > 3:
                    print(f"  • ... and {result['frames_extracted'] - 3} more")

            if 'contact_sheet' in result:
                print(f"📋 Contact sheet: {Path(result['contact_sheet']).name}")
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

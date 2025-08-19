#!/usr/bin/env python3
"""
Setup script for WhisperFrame - AI-Powered Video Processing Toolkit
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Read requirements
requirements = []
if (this_directory / "requirements.txt").exists():
    with open(this_directory / "requirements.txt", "r", encoding="utf-8") as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="whisperframe",
    version="1.0.0",
    author="COCODE.DK",
    author_email="info@cocode.dk",
    description="AI-Powered Video Processing Toolkit with Whisper transcription and frame extraction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cocode-dk/whisperframe",
    project_urls={
        "Bug Reports": "https://github.com/cocode-dk/whisperframe/issues",
        "Source": "https://github.com/cocode-dk/whisperframe",
        "Documentation": "https://github.com/cocode-dk/whisperframe#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Video",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "whisperframe=whisperframe.cli:main",
            "whisper-transcribe=whisperframe.video_transcriber:main",
            "whisper-extract=whisperframe.video_frame_extractor:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="video, transcription, whisper, ai, ffmpeg, frame-extraction, speech-to-text",
    platforms=["Linux", "macOS", "Windows"],
)

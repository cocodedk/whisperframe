"""Smoke tests: both CLI entry points build their parsers and respond to --help.

These give CI a fast, dependency-light signal that the scripts are importable and
their argparse configuration is valid, without processing any real media.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _run_help(script: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / script), "--help"],
        capture_output=True,
        text=True,
    )


def test_transcriber_help_exits_clean():
    result = _run_help("video_transcriber.py")
    assert result.returncode == 0
    assert "usage" in result.stdout.lower()


def test_frame_extractor_help_exits_clean():
    result = _run_help("video_frame_extractor.py")
    assert result.returncode == 0
    assert "usage" in result.stdout.lower()

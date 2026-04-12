# CLAUDE.md — WhisperFrame

## Project Overview

WhisperFrame is an AI-powered video processing toolkit that uses OpenAI Whisper for speech transcription and extracts video frames at key moments. It supports batch processing of video files.

- **Language / Runtime**: Python 3.12
- **Framework**: setuptools / pyproject.toml
- **Architecture**: CLI scripts + processing pipeline
- **Package / Namespace**: `whisperframe`

---

## Required Skills — ALWAYS Invoke These

| Situation | Skill |
|-----------|-------|
| Before any new feature or screen | `superpowers:brainstorming` |
| Planning multi-step changes | `superpowers:writing-plans` |
| Writing or fixing core logic | `superpowers:test-driven-development` |
| First sign of a bug or failure | `superpowers:systematic-debugging` |
| Before completing a feature branch | `superpowers:requesting-code-review` |
| Before claiming any task done | `superpowers:verification-before-completion` |
| Working on UI / frontend | `frontend-design:frontend-design` |
| After implementing — reviewing quality | `simplify` |

---

## Architecture

```
whisper/
├── video_transcriber.py     ← Whisper-based transcription
├── video_frame_extractor.py ← Frame extraction logic
├── requirements.txt         ← Runtime dependencies
├── requirements-dev.txt     ← Dev dependencies
└── output/                  ← Processing output
```

---

## Coding Conventions

- [ ] All functions typed with Python type hints
- [ ] No hardcoded strings
- [ ] `ruff` enforced via pre-commit hook

---

## Engineering Principles

### File Size
- **200-line maximum per file**

### DRY · SOLID · KISS · YAGNI
- Single Responsibility per function

### TDD
- Write failing test first

### Commit hygiene
- Conventional Commits enforced by commit-msg hook

---

## Build Commands

```bash
pip install -r requirements.txt    # Install dependencies
pip install -r requirements-dev.txt  # Dev deps
ruff check .                       # Lint
pytest --tb=short                  # Run tests
```

---

## Key Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | This file |
| `version.txt` | Semantic version |
| `.github/workflows/` | CI, release, Pages |
| `scripts/install-hooks.sh` | Hook installer |

---

## Starting a New Session

1. Read this file
2. Run `ruff check . && pytest --tb=short`
3. Invoke `superpowers:brainstorming` before new features

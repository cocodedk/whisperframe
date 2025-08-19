# 🤝 Contributing to WhisperFrame

Thank you for your interest in contributing to WhisperFrame! This document provides guidelines and information for contributors.

## 🚀 Quick Start

1. **Fork** the repository
2. **Clone** your fork locally
3. **Create** a feature branch
4. **Make** your changes
5. **Test** your changes
6. **Commit** with clear messages
7. **Push** to your fork
8. **Submit** a Pull Request

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Release Process](#release-process)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

### Our Standards

- **Be respectful** and inclusive
- **Be collaborative** and constructive
- **Be professional** in all interactions
- **Be helpful** to newcomers

## 🎯 How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check the existing issues. When creating a bug report, include:

- **Clear title** describing the issue
- **Detailed description** of the problem
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Environment details** (OS, Python version, etc.)
- **Screenshots/logs** if applicable

**Bug Report Template:**
```markdown
## Bug Description
Brief description of the bug

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: [e.g., Ubuntu 22.04]
- Python: [e.g., 3.9.7]
- FFmpeg: [e.g., 4.4.2]
- WhisperFrame: [e.g., commit hash]

## Additional Information
Any other context, logs, or screenshots
```

### 💡 Suggesting Enhancements

We welcome feature requests! When suggesting enhancements:

- **Describe the problem** you're trying to solve
- **Explain why** this feature would be useful
- **Provide examples** of how it would work
- **Consider alternatives** and trade-offs

**Enhancement Template:**
```markdown
## Problem Statement
What problem are you trying to solve?

## Proposed Solution
Describe your proposed solution

## Alternative Solutions
What other approaches have you considered?

## Additional Context
Any other information that might be helpful
```

### 🔧 Pull Requests

We love pull requests! Here's how to make them:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Make** your changes
4. **Test** your changes thoroughly
5. **Commit** with clear messages
6. **Push** to your branch (`git push origin feature/amazing-feature`)
7. **Open** a Pull Request

## 🛠️ Development Setup

### Prerequisites

- Python 3.8+
- FFmpeg
- Git

### Local Setup

```bash
# Fork and clone the repository
git clone https://github.com/yourusername/whisperframe.git
cd whisperframe

# Add upstream remote
git remote add upstream https://github.com/cocode-dk/whisperframe.git

# Create virtual environment
python3 -m venv env

# Activate virtual environment
# On Linux/macOS:
source env/bin/activate
# On Windows:
env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt  # if available
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run tests with coverage
python -m pytest --cov=.

# Run specific test file
python -m pytest tests/test_video_transcriber.py

# Run tests with verbose output
python -m pytest -v
```

## 📝 Coding Standards

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

- **Line length**: 88 characters (Black formatter default)
- **Docstrings**: Google style
- **Type hints**: Required for public functions
- **Imports**: Grouped and sorted

### Code Formatting

We use [Black](https://black.readthedocs.io/) for code formatting:

```bash
# Install Black
pip install black

# Format code
black .

# Check formatting
black --check .
```

### Import Sorting

We use [isort](https://pycqa.github.io/isort/) for import sorting:

```bash
# Install isort
pip install isort

# Sort imports
isort .

# Check import sorting
isort --check-only .
```

### Linting

We use [flake8](https://flake8.pycqa.org/) for linting:

```bash
# Install flake8
pip install flake8

# Run linting
flake8 .
```

## 🧪 Testing Guidelines

### Test Structure

```
tests/
├── test_video_transcriber.py
├── test_video_frame_extractor.py
├── test_utils.py
└── conftest.py
```

### Writing Tests

- **Test one thing** per test function
- **Use descriptive names** for test functions
- **Test both success and failure** cases
- **Use fixtures** for common setup
- **Mock external dependencies**

**Example Test:**
```python
import pytest
from pathlib import Path
from video_transcriber import VideoTranscriber

def test_video_transcriber_initialization():
    """Test VideoTranscriber initialization with valid video file."""
    video_path = "tests/fixtures/sample_video.mp4"
    transcriber = VideoTranscriber(video_path)

    assert transcriber.video_path == Path(video_path)
    assert transcriber.language == "auto"
    assert transcriber.model == "small"

def test_video_transcriber_invalid_file():
    """Test VideoTranscriber initialization with invalid file."""
    with pytest.raises(FileNotFoundError):
        VideoTranscriber("nonexistent_file.mp4")
```

### Test Fixtures

Create reusable test data in `conftest.py`:

```python
import pytest
from pathlib import Path

@pytest.fixture
def sample_video_path():
    """Provide path to sample video file."""
    return Path("tests/fixtures/sample_video.mp4")

@pytest.fixture
def temp_output_dir(tmp_path):
    """Provide temporary output directory."""
    return tmp_path / "output"
```

## 🔄 Pull Request Process

### Before Submitting

- [ ] **Tests pass** locally
- [ ] **Code is formatted** with Black
- [ ] **Imports are sorted** with isort
- [ ] **Linting passes** with flake8
- [ ] **Documentation is updated**
- [ ] **Changelog is updated** (if applicable)

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] All existing tests pass

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes

## Additional Notes
Any additional information or context
```

### Review Process

1. **Automated checks** must pass
2. **Code review** by maintainers
3. **Address feedback** and make changes
4. **Maintainer approval** required
5. **Merge** when ready

## 🚀 Release Process

### Versioning

We use [Semantic Versioning](https://semver.org/):

- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Checklist

- [ ] **Update version** in relevant files
- [ ] **Update changelog** with new features/fixes
- [ ] **Create release tag**
- [ ] **Update documentation**
- [ ] **Announce release**

## 📚 Additional Resources

- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Python Testing Best Practices](https://realpython.com/python-testing/)
- [Open Source Guide](https://opensource.guide/)

## 🆘 Getting Help

If you need help:

1. **Check existing issues** and documentation
2. **Ask in discussions** or issues
3. **Join our community** (if available)
4. **Contact maintainers** directly

## 🙏 Thank You

Thank you for contributing to WhisperFrame! Your contributions help make this project better for everyone.

---

**Questions?** Open an issue or contact us at [cocode.dk](https://cocode.dk)

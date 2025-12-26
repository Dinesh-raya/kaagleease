# KaggleEase Deployment Guide

This guide provides detailed instructions for deploying the KaggleEase package to PyPI and GitHub.

## Package Overview

KaggleEase is a production-ready Python package that provides the fastest, notebook-first way to load Kaggle datasets into pandas with one line. The package includes:
- Thread-safe authentication with proper locking
- Structured logging framework
- Retry logic with exponential backoff
- Progress indication for large downloads
- CLI and magic command interfaces
- Comprehensive error handling

## Package Contents

The production-ready package includes:
- `kaggleease/` - Main package with all modules
- `setup.py` - Setup configuration
- `pyproject.toml` - Modern Python packaging configuration
- `README.md` - Complete documentation
- `LICENSE` - MIT License
- `CONTRIBUTING.md` - Contribution guidelines

## Deployment to PyPI

### Prerequisites

1. **Python Packaging Tools**: Install required tools
   ```bash
   pip install --upgrade pip setuptools wheel build twine
   ```

2. **PyPI Account**: Create an account at [pypi.org](https://pypi.org) if you don't have one

3. **API Token**: Generate an API token from your PyPI account settings (Account Settings > API Tokens)

### Step-by-Step Deployment Process

#### 1. Verify Package Contents
```bash
cd kaggleease-prod
ls -la
```

Ensure you see:
- `kaggleease/` directory with all modules
- `setup.py`, `pyproject.toml`, `README.md`, `LICENSE`, `CONTRIBUTING.md`

#### 2. Update Package Version (if needed)
Edit `pyproject.toml` to ensure the version is correct:
```toml
version = "1.0.0"  # Update as needed
```

#### 3. Build the Package
```bash
python -m build
```

This creates `dist/` directory with:
- `kaggleease-1.0.0-py3-none-any.whl` (wheel distribution)
- `kaggleease-1.0.0.tar.gz` (source distribution)

#### 4. Verify the Build
```bash
twine check dist/*
```

#### 5. Test in Virtual Environment (Optional but Recommended)
```bash
# Create and activate a new virtual environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install the built package
pip install dist/kaggleease-*.whl

# Test basic functionality
python -c "import kaggleease; print('Package imports successfully')"
python -c "from kaggleease import load; print('Load function available')"

# Deactivate
deactivate
```

#### 6. Upload to TestPyPI (Optional but Recommended)
```bash
# Upload to TestPyPI first
twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ kaggleease
```

#### 7. Upload to PyPI
```bash
# Upload to production PyPI
twine upload dist/*
```

When prompted, use `__token__` as the username and your API token as the password, or create a `.pypirc` file.

### Creating .pypirc file (Optional)
Create `~/.pypirc` file:
```
[pypi]
username = __token__
password = your-api-token-here

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = your-testpypi-api-token
```

## Deployment to GitHub

### 1. Create GitHub Repository
1. Go to GitHub and create a new repository named `kaggleease`
2. Initialize with a README (optional, as we have our own)
3. Do not add .gitignore or license as we have these files

### 2. Initialize Git in Package Directory
```bash
cd kaggleease-prod
git init
git add .
git commit -m "Initial commit: KaggleEase v1.0.0"
```

### 3. Connect to GitHub Repository
```bash
git remote add origin https://github.com/your-username/kaggleease.git
git branch -M main
git push -u origin main
```

### 4. Create Git Tags for Versioning
```bash
git tag -a v1.0.0 -m "KaggleEase v1.0.0"
git push origin v1.0.0
```

### 5. Create GitHub Release
1. Go to your repository on GitHub
2. Click "Releases" > "Draft a new release"
3. Choose the tag you just created
4. Add release title and description
5. Upload the built distributions from the `dist/` folder
6. Publish the release

## Authentication Requirements

### PyPI Authentication
- **Username**: `__token__` (for API token authentication)
- **Password**: Your PyPI API token
- **Security**: Never commit tokens to source code

### GitHub Authentication
- **Username/Password**: Your GitHub credentials
- **Or SSH Key**: For SSH-based authentication
- **Or Personal Access Token**: For token-based authentication

## Verification Steps

### 1. PyPI Installation Test
After deployment, verify installation from PyPI:
```bash
# Create fresh virtual environment
python -m venv verify_env
source verify_env/bin/activate  # On Windows: verify_env\Scripts\activate

# Install from PyPI
pip install kaggleease

# Test functionality
python -c "import kaggleease; print('✓ Package imports successfully')"
python -c "from kaggleease import load, search; print('✓ Core functions available')"

# Test CLI
kaggleease --help

# Test progress functionality
python -c "from kaggleease.progress import ProgressBar; print('✓ Progress functionality available')"

deactivate
```

### 2. GitHub Repository Verification
- Ensure all files are present in the repository
- Verify the README.md renders correctly
- Check that the release contains distribution files
- Test cloning and installation from GitHub:
```bash
pip install git+https://github.com/your-username/kaggleease.git
```

## Post-Deployment Tasks

### 1. Update pyproject.toml for GitHub
Update the URLs in `pyproject.toml`:
```toml
[project.urls]
Homepage = "https://github.com/your-username/kaggleease"
Repository = "https://github.com/your-username/kaggleease"
Documentation = "https://github.com/your-username/kaggleease#readme"
```

### 2. Announce Release
- Update project documentation
- Announce on relevant channels
- Add to your portfolio/website if applicable

## Troubleshooting

### Common PyPI Issues
- **403 Forbidden**: Check API token permissions
- **Invalid package**: Run `twine check` to validate
- **Version conflicts**: Ensure version number is incremented

### Common GitHub Issues
- **Permission denied**: Check SSH keys or personal access tokens
- **Large files**: Use git-lfs for large binary files
- **Merge conflicts**: Resolve before pushing

## Security Considerations

- Never commit credentials or API keys
- Use secure protocols (HTTPS/SSH) for Git operations
- Regularly rotate API tokens
- Keep dependencies updated

## Versioning Strategy

Follow semantic versioning:
- **MAJOR.MINOR.PATCH** (e.g., 1.0.0)
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)
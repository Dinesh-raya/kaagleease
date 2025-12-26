# KaggleEase v1.3.0: Deployment Guide

I have prepared the code for deployment in the `dist_pkg` folder. 
The distribution files have been built and are located in `dist_pkg/dist`.

## 1. Push to GitHub

To push the new version to GitHub, run the following commands from your terminal in the project root:

```bash
# Initialize git if needed or just add the new files
git add dist_pkg/
git commit -m "chore: prepare v1.3.0 release distribution"

# Tag the release
git tag -a v1.3.0 -m "Release v1.3.0: The Intelligent Loader"

# Push to your repository
git push origin main --tags
```

## 2. Push to PyPI

The package is built and ready in `dist_pkg/dist`. To upload it to PyPI, use `twine`:

```bash
# Upload the built distribution files
twine upload dist_pkg/dist/*
```
*Note: You will need your PyPI API token or credentials.*

## 3. Deployment Summary
- **Version**: 1.3.0
- **Package Name**: `kaggleease`
- **Core Improvements**:
    - Intelligent Handle Resolution (Fuzzy matching).
    - Lightweight architecture (Removed `kaggle` legacy dependency).
    - Proactive Memory Guarding (`psutil`).
    - Beautiful IPython Magic error blocks.

**The folder `dist_pkg` is your "Golden Copy" for this release.**

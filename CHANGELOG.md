# Changelog

All notable changes to **KaggleEase** will be documented in this file.

## [1.3.10] - 2025-12-27
### 🚀 Major Improvements
*   **Bulletproof Release**: Clean separation of secrets from git history.
*   **Testing Infrastructure**: Added `pytest` framework with strict offline mocking.
*   **Documentation**: Added `KaggleEase_Masterclass.ipynb` and `TECHNICAL_REFERENCE.md`.

### 🐛 Bug Fixes
*   Fixed `AttributeError` in `%kaggle` magic registration logic.
*   Fixed circular dependency in `__init__.py`.
*   Corrected SQLite dataset handles in documentation.
*   Resolved Shadowing issues in test mocks.

### 📦 Dependencies
*   Added `openpyxl` for native Excel support.
*   Added `pytest` and `pytest-cov` for dev environment.

## [1.3.9] - 2025-12-27
### Added
*   **Universal Resilience**: Late-resolution logic for fuzzy matching.
*   **Competition Support**: Unified `load()` API for datasets and competitions.

## [1.3.0] - Initial Release
*   Basic `load()` function.
*   Search capabilities.

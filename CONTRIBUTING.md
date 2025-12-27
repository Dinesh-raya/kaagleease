# Contributing to KaggleEase

Thank you for your interest in contributing to **KaggleEase**! 🚀

## 🛠️ Development Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Dinesh-raya/kaagleease.git
    cd kaagleease
    ```

2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -e .[dev]
    ```

## 🧪 Running Tests

We use `pytest` for testing. Using the intelligent mocks in `tests/conftest.py`, you can run the full suite without internet access.

```bash
pytest tests/ -v
```

## 📝 Style Guide

*   Use **Black** for formatting.
*   Follow **PEP 8**.
*   Write docstrings for all public functions.

## 🚀 Pull Request Process

1.  Fork the repo and create your branch from `main`.
2.  Add tests for any new features.
3.  Ensure `pytest` passes.
4.  Update `CHANGELOG.md`.

Thank you for making data science easier for everyone! 💙
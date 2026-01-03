# Contributing to KaggleEase

Thank you for your interest in contributing to KaggleEase! This document provides guidelines and information to help you contribute effectively.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Be respectful, inclusive, and constructive in all interactions.

## How to Contribute

### Reporting Bugs

Before submitting a bug report:
1. Check if the issue has already been reported
2. Try to reproduce the issue with the latest version

When submitting a bug report, please include:
- A clear and descriptive title
- Steps to reproduce the issue
- Expected vs. actual behavior
- Your environment information (OS, Python version, etc.)
- Any relevant error messages or logs

### Suggesting Enhancements

Feature requests are welcome! Please include:
- A clear explanation of the proposed feature
- Use cases that would benefit from this feature
- Any implementation ideas you might have

### Code Contributions

#### Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/kaggle-ease.git
   cd kaggle-ease
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -e .
   ```

#### Coding Standards

- Follow PEP 8 style guidelines
- Write clear, descriptive docstrings for all functions
- Include type hints where appropriate
- Keep functions focused and modular
- Write tests for new functionality

#### Testing

Run the test suite before submitting changes:
```bash
pytest tests/
```

#### Submitting Changes

1. Create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes
3. Add tests if applicable
4. Ensure all tests pass
5. Commit your changes with a clear, descriptive message
6. Push to your fork
7. Open a pull request

## Pull Request Process

1. Ensure your code follows the project's coding standards
2. Include tests for any new functionality
3. Update documentation as needed
4. Describe your changes clearly in the pull request
5. Reference any related issues

## Style Guide

### Python Code

- Use 4 spaces for indentation (no tabs)
- Limit lines to 88 characters (PEP 8 recommends 79, but 88 is acceptable)
- Use descriptive variable and function names
- Follow PEP 8 naming conventions:
  - `snake_case` for functions and variables
  - `PascalCase` for classes
  - `UPPER_CASE` for constants

### Documentation

- Use Markdown for documentation files
- Write in clear, concise English
- Use code blocks for examples
- Include expected outputs where helpful

### Git Commits

- Write clear, concise commit messages
- Use present tense ("Add feature" not "Added feature")
- Keep commits focused on a single change
- Reference issues when applicable ("Fixes #123")

## Getting Help

If you need help or have questions:
- Check existing issues and pull requests
- Open a new issue for discussion
- Be patient - maintainers work on this in their spare time

Thank you for contributing to KaggleEase!
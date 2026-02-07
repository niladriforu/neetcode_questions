# Contributing Guidelines

Thank you for considering contributing to this project! Here's how you can help:

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/neetcode_questions.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes
6. Commit: `git commit -m 'Add some feature'`
7. Push: `git push origin feature/your-feature-name`
8. Create a Pull Request

## Development Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e ".[dev]"
   ```

2. Run tests:
   ```bash
   pytest tests/
   ```

3. Format code:
   ```bash
   black src/ tests/
   ```

4. Run linter:
   ```bash
   flake8 src/ tests/
   ```

## Code Style

- Follow PEP 8
- Use Black for formatting (line length: 100)
- Add docstrings to all functions and classes
- Write unit tests for new functionality

## Pull Request Process

1. Update documentation if needed
2. Add tests for new features
3. Ensure all tests pass
4. Update the README.md if needed
5. Request review from maintainers

## Reporting Issues

When reporting issues, please include:
- Python version
- Databricks Runtime version (if applicable)
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error messages/stack traces

## Questions?

Feel free to open an issue for discussion!

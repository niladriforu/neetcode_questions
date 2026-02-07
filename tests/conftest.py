"""Conftest for pytest configuration."""

import pytest
import logging

# Setup logging for tests
logging.basicConfig(level=logging.INFO)


def pytest_configure(config):
    """Configure pytest."""
    config.addinivalue_line(
        "markers", "integration: mark test as integration test"
    )
    config.addinivalue_line(
        "markers", "unit: mark test as unit test"
    )

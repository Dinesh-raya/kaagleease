import pytest
import sys
import os
from unittest.mock import MagicMock

# Ensure the package is importable
# sys.path hacking removed; relying on pip install -e .

@pytest.fixture
def mock_kagglehub(monkeypatch):
    """
    Mock the kagglehub module to prevent actual Internet calls during tests.
    """
    mock = MagicMock()
    mock.dataset_download.return_value = "/tmp/mock/dataset"
    mock.competition_download.return_value = "/tmp/mock/competition"
    # Fix for shadowing: Import the actual module object
    import sys
    # Ensure we get the module, not the function from __init__
    if 'kaggleease.load' not in sys.modules:
        import kaggleease.load
    
    load_module = sys.modules['kaggleease.load']
    
    monkeypatch.setattr(load_module, "kagglehub", mock)
    return mock

@pytest.fixture
def mock_auth(monkeypatch):
    """
    Mock authentication to always succeed.
    """
    mock = MagicMock()
    # We need to patch where it is imported in load.py
    import sys
    if 'kaggleease.load' not in sys.modules:
        import kaggleease.load
    load_module = sys.modules['kaggleease.load']
    
    monkeypatch.setattr(load_module, "setup_auth", mock)
    return mock

@pytest.fixture
def mock_metadata(monkeypatch):
    """
    Mock the metadata resolution to avoid network calls.
    """
    mock = MagicMock()
    # files, total_size, res_type, resolved_handle
    mock.return_value = ([], 0, "dataset", "test/dataset")
    
    import sys
    if 'kaggleease.load' not in sys.modules:
        import kaggleease.load
    load_module = sys.modules['kaggleease.load']
    
    monkeypatch.setattr(load_module, "_get_dataset_files", mock)
    return mock

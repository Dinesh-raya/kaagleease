import pytest
import sys
import os
from unittest.mock import MagicMock

# Ensure the package is importable
# sys.path hacking removed; relying on pip install -e .

@pytest.fixture
def mock_kagglehub(monkeypatch):
    """
    Mock the kagglehub module globally by replacing it in sys.modules.
    """
    mock = MagicMock()
    mock.dataset_download.return_value = "/tmp/mock/dataset"
    mock.competition_download.return_value = "/tmp/mock/competition"
    
    # Nuclear Option: Patch sys.modules directly so ANY import gets the mock
    monkeypatch.setitem(sys.modules, "kagglehub", mock)
    return mock

@pytest.fixture
def mock_auth(monkeypatch):
    """
    Mock authentication to always succeed.
    """
    mock = MagicMock()
    # Since load.py now does 'from . import auth' and calls 'auth.setup_auth()',
    # patching 'kaggleease.auth.setup_auth' works globally!
    import kaggleease.auth
    monkeypatch.setattr(kaggleease.auth, "setup_auth", mock)
    return mock

@pytest.fixture
def mock_client(monkeypatch):
    """
    Mock the KaggleClient class via attribute patching.
    """
    mock = MagicMock()
    mock.return_value.list_files.return_value = [
        {"name": "train.csv", "size": 1024, "type": "dataset"}
    ]
    
    # Import the module so we can patch the class attribute on it
    import kaggleease.client
    monkeypatch.setattr(kaggleease.client, "KaggleClient", mock)
    return mock

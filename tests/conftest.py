import pytest
import sys
import os
from unittest.mock import MagicMock

# --- EXTREME ISOLATION: Mock dependencies before any collection ---

# 1. Mock requests
mock_resp = MagicMock()
mock_resp.status_code = 200
mock_resp.json.return_value = {"currentVersionNumber": 1, "files": []}
mock_resp.text = '{"currentVersionNumber": 1, "files": []}'
mock_resp.url = "https://www.kaggle.com/test/dataset"
mock_resp.headers.get.return_value = "1.0.0"
mock_resp.__enter__.return_value = mock_resp

mock_requests_lib = MagicMock()
mock_requests_lib.get.return_value = mock_resp
mock_requests_lib.post.return_value = mock_resp
sys.modules["requests"] = mock_requests_lib

# 2. Mock kagglehub
mock_kh = MagicMock()
mock_kh.dataset_download.return_value = "/tmp/mock/dataset"
mock_kh.competition_download.return_value = "/tmp/mock/competition"
sys.modules["kagglehub"] = mock_kh

# 3. Mock psutil
mock_ps = MagicMock()
mock_ps.virtual_memory.return_value.available = 8 * 1024**3
sys.modules["psutil"] = mock_ps

# --- Fixtures for test-level control ---

@pytest.fixture(autouse=True)
def mock_kagglehub():
    return sys.modules["kagglehub"]

@pytest.fixture(autouse=True)
def mock_requests():
    return sys.modules["requests"]

@pytest.fixture(autouse=True)
def mock_auth(monkeypatch):
    """
    Mock authentication to always succeed.
    """
    mock = MagicMock()
    # We patch the auth module directly
    import kaggleease.auth
    monkeypatch.setattr(kaggleease.auth, "setup_auth", mock)
    return mock

@pytest.fixture(autouse=True)
def mock_client(monkeypatch):
    """
    Mock the KaggleClient class via attribute patching.
    """
    mock_instance = MagicMock()
    mock_instance.list_files.return_value = [
        {"name": "train.csv", "size": 1024, "type": "dataset"}
    ]
    mock_instance.search_datasets.return_value = [
        {"handle": "test/dataset", "title": "Test Dataset", "size": 1024, "votes": 10}
    ]
    
    import kaggleease.client
    monkeypatch.setattr(kaggleease.client, "KaggleClient", lambda: mock_instance)
    return mock_instance

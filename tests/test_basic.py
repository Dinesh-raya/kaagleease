import pytest
import kaggleease
from kaggleease import load
from kaggleease.errors import DatasetNotFoundError

def test_version_exposure():
    """Verify that version is exposed correctly."""
    assert kaggleease.__version__ is not None

def test_load_import():
    """Verify that load is importable."""
    from kaggleease import load
    assert callable(load)

def test_mocked_download(mock_kagglehub, mock_auth, mock_metadata):
    """Test that download calls the mock instead of real internet."""
    # This should NOT crash even without internet if mocks work
    try:
        # We expect it to eventually fail on file finding since /tmp/mock/dataset doesn't exist
        # But the key is verifying it CALLED the mock
        load("test/dataset")
    except Exception:
        pass 
    
    mock_kagglehub.dataset_download.assert_called_with("test/dataset")

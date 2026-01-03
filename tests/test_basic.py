import pytest

def test_mocked_download(mock_kagglehub, mock_auth, mock_client):
    """Test that download calls the mock instead of real internet."""
    from kaggleease import load
    load("test/dataset")
    
    mock_kagglehub.dataset_download.assert_called_with("test/dataset")

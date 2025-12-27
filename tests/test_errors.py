import pytest
from kaggleease.errors import (
    KaggleEaseError,
    DatasetNotFoundError,
    AuthError,
    DataFormatError,
    MultipleFilesError,
    UnsupportedFormatError,
    NetworkError
)

def test_hierarchy():
    """Verify that specific errors are caught by the base class."""
    try:
        raise DatasetNotFoundError("Test error")
    except KaggleEaseError:
        assert True
    except:
        assert False, "DatasetNotFoundError should inherit from KaggleEaseError"

def test_data_format_hierarchy():
    """Verify logical grouping of format errors."""
    # MultipleFilesError should be a DataFormatError
    try:
        raise MultipleFilesError("Ambiguous files")
    except DataFormatError:
        assert True
    except:
        assert False, "MultipleFilesError should inherit from DataFormatError"

def test_error_message_formatting():
    """Verify the nice '💡 Fix Suggestion' formatting."""
    err = AuthError("Login failed", fix_suggestion="Check kaggle.json")
    msg = str(err)
    assert "Login failed" in msg
    assert "💡 Suggestion: Check kaggle.json" in msg
    assert "🔗 Docs" in msg

def test_network_error():
    """Verify the new NetworkError."""
    err = NetworkError("Connection timed out")
    assert isinstance(err, KaggleEaseError)

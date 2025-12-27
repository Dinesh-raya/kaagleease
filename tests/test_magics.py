import pytest
from unittest.mock import MagicMock
from kaggleease.magics import KaggleController
import pandas as pd
from kaggleease.errors import KaggleEaseError

def test_controller_help():
    """Verify (no args) returns help."""
    ctrl = KaggleController()
    res = ctrl.handle_command("")
    assert res['type'] == 'help'
    assert 'usage:' in res['content'].lower()

def test_controller_load():
    """Verify 'load titanic' calls load function and updates namespace."""
    mock_load = MagicMock(return_value=pd.DataFrame({'a': [1, 2, 3]}))
    ns = {}
    ctrl = KaggleController(load_fn=mock_load, user_ns=ns)
    
    res = ctrl.handle_command("load titanic --as my_df")
    
    # Assertions
    mock_load.assert_called_with("titanic", file=None, timeout=300)
    assert res['type'] == 'df'
    assert 'my_df' in ns
    assert isinstance(ns['my_df'], pd.DataFrame)

def test_controller_search():
    """Verify 'search query' calls search function."""
    mock_search = MagicMock(return_value=[{'handle': 'foo/bar', 'title': 'Bar', 'size': '1MB', 'votes': 10}])
    ctrl = KaggleController(search_fn=mock_search)
    
    res = ctrl.handle_command("search 'machine learning' --top 10")
    
    mock_search.assert_called_with("machine learning", top=10, timeout=30)
    assert res['type'] == 'search_results'
    assert len(res['content']) == 1
    assert res['content'][0]['handle'] == 'foo/bar'

def test_controller_error():
    """Verify exceptions are caught and returned as error type."""
    def error_load(*args, **kwargs):
        raise KaggleEaseError("Mock failure")
        
    ctrl = KaggleController(load_fn=error_load)
    res = ctrl.handle_command("load fail")
    
    assert res['type'] == 'error'
    assert isinstance(res['content'], KaggleEaseError)
    assert res['content'].message == "Mock failure"

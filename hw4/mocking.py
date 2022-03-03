from unittest.mock import Mock, patch
from hw4 import getInfo

@patch('getInfo.requests.get')
def test_getting_commits(mock_get):
    commits = '[{"name":"name1"},{"name":"name2"}]'

    mock_get.return_value = commits

@patch('getInfo.input')
def test_getting_input(mock_get):
    mock_get.return_value = "adriang11"
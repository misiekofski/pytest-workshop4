from unittest import mock

from remover import rm

@mock.patch('remover.os')
def test_remover_with_mocks(mock_os):
    rm("any path 123")
    mock_os.remove.assert_called_with("any path 123")

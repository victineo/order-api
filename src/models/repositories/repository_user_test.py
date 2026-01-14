from .repository_user import UserRepository
from ..settings.db_connection_handler import db_connection_handler
from unittest.mock import Mock
import pytest

class MockCursor:
    def __init__(self):
        self.execute = Mock()
        self.fetchone = Mock()

class MockConnection:
    def __init__(self):
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()

def test_create_user():
    mock_connection = MockConnection()
    repository = UserRepository(mock_connection)

    username = "testCreateNewUser"
    password = "testCreateNewUserPassword"

    repository.create_user(username, password)

    cursor = mock_connection.cursor.return_value
    assert 'INSERT INTO users' in cursor.execute.call_args[0][0]
    assert '(username, password)' in cursor.execute.call_args[0][0]
    assert 'VALUES' in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password)
    mock_connection.commit.assert_called_once()

def test_create_user_with_existing_username():
    with pytest.raises(Exception):
        connection = db_connection_handler.get_connection()
        repository = UserRepository(connection)

        username = "testCreateUser"
        password = "testCreateUserPassword"

        repository.create_user(username, password)

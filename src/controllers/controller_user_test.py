from sqlite3 import connect
from .controller_user import UserController
from src.models.repositories.repository_user import UserRepository
from src.models.settings.db_connection_handler import DBConnectionHandler, db_connection_handler
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

@pytest.mark.skip(reason="Interacts with real database")
def test_create_user_on_db():
    db_connection_handler.connect()

    connection = db_connection_handler.get_connection()
    repository = UserRepository(connection)
    controller = UserController(repository)

    username = "testCreateUser"
    password = "testCreateUser"

    controller.create_user(username, password)

def test_create_user_with_invalid_username():
    with pytest.raises(Exception):
        db_connection_handler.connect()

        connection = db_connection_handler.get_connection()
        repository = UserRepository(connection)
        controller = UserController(repository)

        username = ""
        password = "testPassword"

        controller.create_user(username, password)

        assert Exception == "Invalid username"

def test_create_user_with_invalid_password():
    with pytest.raises(Exception):
        db_connection_handler.connect()

        connection = db_connection_handler.get_connection()
        repository = UserRepository(connection)
        controller = UserController(repository)

        username = "testCreateUser"
        password = ""

        controller.create_user(username, password)

        assert Exception == "Invalid password"

def test_create_user_with_existing_username():
    with pytest.raises(Exception):
        db_connection_handler.connect()

        connection = db_connection_handler.get_connection()
        repository = UserRepository(connection)
        controller = UserController(repository)

        username = "testCreateUser"
        password = "testCreateUser"

        controller.create_user(username, password)
        controller.create_user(username, password)

        assert Exception == "Username already exists"

def test_get_user():
    db_connection_handler.connect()

    connection = db_connection_handler.get_connection()
    repository = UserRepository(connection)
    controller = UserController(repository)

    username = "testCreateUser"

    user = controller.get_user(username)

    assert user is not None
    assert user[1] == username

def test_get_user_with_nonexistent_username():
    with pytest.raises(Exception):
        db_connection_handler.connect()

        connection = db_connection_handler.get_connection()
        repository = UserRepository(connection)
        controller = UserController(repository)

        username = "testFindUserNonexistent"

        user = controller.get_user(username)

        assert user is None
        assert Exception == "User not found"

def test_create_login():
    db_connection_handler.connect()

    connection = db_connection_handler.get_connection()
    repository = UserRepository(connection)
    controller = UserController(repository)

    username = "testCreateUser"
    password = "testCreateUser"

    token = controller.create_login(username, password)
    print(token)

    assert token is not None
    assert token != ""

def test_login_with_invalid_credentials():
    with pytest.raises(Exception):
        db_connection_handler.connect()

        connection = db_connection_handler.get_connection()
        repository = UserRepository(connection)
        controller = UserController(repository)

        username = "testCreateUser"
        password = "testCreateUserInvalid"

        token = controller.create_login(username, password)

        assert token is None
        assert Exception == "Invalid credentials"

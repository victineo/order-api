from sqlite3 import connect

from src.models.repositories import repository_order
from .controller_order import OrderController
from src.models.repositories.repository_order import OrderRepository
from src.models.settings.db_connection_handler import db_connection_handler
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

def test_create_order():
    mock_connection = MockConnection()
    repository = OrderRepository(mock_connection)
    controller = OrderController(repository)

    user_id = 1
    description = "testCreateOrder"

    controller.create_order(user_id, description)

    cursor = mock_connection.cursor.return_value
    assert 'INSERT INTO orders' in cursor.execute.call_args[0][0]
    assert '(user_id, description)' in cursor.execute.call_args[0][0]
    assert 'VALUES' in cursor.execute.call_args[0][0]
    # assert cursor.execute.call_args[0][1] == (user_id, description)
    mock_connection.commit.assert_called_once()

@pytest.mark.skip(reason="Interacts with real database")
def test_create_order_on_db():
    db_connection_handler.connect()

    connection = db_connection_handler.get_connection()
    repository = OrderRepository(connection)
    controller = OrderController(repository)

    user_id = 1
    description = "testCreateOrderOnDB"

    controller.create_order(user_id, description)

def test_create_order_with_invalid_description():
    with pytest.raises(Exception):
        db_connection_handler.connect()

        connection = db_connection_handler.get_connection()
        repository = OrderRepository(connection)
        controller = OrderController(repository)

        user_id = 1
        description = ""

        controller.create_order(user_id, description)

def test_get_orders():
    db_connection_handler.connect()

    connection = db_connection_handler.get_connection()
    repository = OrderRepository(connection)
    controller = OrderController(repository)

    user_id = 1

    orders = controller.get_orders(user_id)
    print(orders)

    assert orders is not None
    assert isinstance(orders, list)
    assert all(isinstance(order, tuple) for order in orders)
    assert all(len(order) == 4 for order in orders)

def test_update_order():
    db_connection_handler.connect()

    connection = db_connection_handler.get_connection()
    repository = OrderRepository(connection)
    controller = OrderController(repository)

    user_id = 1
    order_id = 1
    new_description = "testUpdateOrder"

    controller.update_order(user_id, order_id, new_description)

def test_update_order_with_invalid_user_id():
    with pytest.raises(Exception):
        db_connection_handler.connect()

        connection = db_connection_handler.get_connection()
        repository = OrderRepository(connection)
        controller = OrderController(repository)

        user_id = 2
        order_id = 1
        new_description = "testUpdateOrderWithInvalidUserId"

        controller.update_order(user_id, order_id, new_description)

def test_update_with_invalid_description():
    with pytest.raises(Exception):
        db_connection_handler.connect()

        connection = db_connection_handler.get_connection()
        repository = OrderRepository(connection)
        controller = OrderController(repository)

        user_id = 1
        order_id = 1
        new_description = ""

        controller.update_order(user_id, order_id, new_description)

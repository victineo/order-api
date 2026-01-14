from .repository_order import OrderRepository
from ..settings.db_connection_handler import DBConnectionHandler, db_connection_handler
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

    user_id = 1
    description = "testCreateOrderDescription"

    repository.create_order(user_id, description)

    cursor = mock_connection.cursor.return_value
    assert 'INSERT INTO orders' in cursor.execute.call_args[0][0]
    assert '(user_id, description)' in cursor.execute.call_args[0][0]
    assert 'VALUES' in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (user_id, description)
    mock_connection.commit.assert_called_once()

def test_list_orders():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repository = OrderRepository(conn)

    user_id = 1

    orders = repository.get_orders_by_user_id(user_id)
    print(orders)

# MOVER PARA TESTE DE INTEGRACAO NOS CONTROLLERS, FUTURAMENTE
# def test_create_order_with_invalid_user_id():
#     with pytest.raises(Exception):
#         db_connection_handler.connect()
#         # mock_connection = MockConnection()
#         conn = db_connection_handler.get_connection()
#         repository = OrderRepository(conn)

#         user_id = 0
#         description = "testCreateOrderDescription"

#         repository.create_order(user_id, description)

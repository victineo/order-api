from sqlite3 import Connection
from .interfaces.repository_order_interface import OrderRepositoryInterface

class OrderRepository(OrderRepositoryInterface):
    def __init__(self, connection: Connection) -> None:
        self.__connection = connection
    
    def create_order(self, user_id: int, description: str) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            INSERT INTO orders
                (user_id, description)
            VALUES
                (?, ?)
            ''', (user_id, description)
        )
        self.__connection.commit()

    def get_orders_by_user_id(self, user_id: int) -> list:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            SELECT * FROM orders
            WHERE user_id = ?
            ''', (user_id,)
        )
        return cursor.fetchall()

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

    def get_orders_by_user_id(self, user_id: int) -> list[tuple[int, int, str, str]]:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            SELECT *
            FROM orders
            WHERE user_id = ?
            ''', (user_id,)
        )
        return cursor.fetchall()

    def get_order_by_id(self, order_id: int) -> tuple[int, int, str, str]:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            SELECT *
            FROM orders
            WHERE id = ?
            ''', (order_id,)
        )
        return cursor.fetchone()

    def update_order(self, user_id: int, order_id: int, new_description: str) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            UPDATE orders
            SET description = ?
            WHERE id = ? AND user_id = ?
            ''', (new_description, order_id, user_id)
        )
        self.__connection.commit()

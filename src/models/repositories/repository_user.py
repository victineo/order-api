from sqlite3 import Connection
from .interfaces.repository_user_interface import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):
    def __init__(self, connection: Connection) -> None:
        self.__connection = connection

    def create_user(self, username: str, password: str) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            INSERT INTO users 
                (username, password) 
            VALUES
                (?, ?)
            ''', (username, password)
        )
        self.__connection.commit()

    def get_user_by_username(self, username: str) -> tuple[int, str, str] | None:
        cursor = self.__connection.cursor()
        cursor.execute(
            '''
            SELECT *
            FROM users
            WHERE username = ?
            ''', (username,)
        )
        return cursor.fetchone()

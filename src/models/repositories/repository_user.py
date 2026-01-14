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

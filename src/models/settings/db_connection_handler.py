import sqlite3
from sqlite3 import Connection

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"
        self.__connection = None

    def connect(self) -> None:
        if self.__connection is None:
            self.__connection = sqlite3.connect(self.__connection_string)

    def get_connection(self) -> Connection:
        return self.__connection

db_connection_handler = DBConnectionHandler()

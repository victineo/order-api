from src.models.repositories.interfaces.repository_user_interface import UserRepositoryInterface
from src.drivers.password_handler import PasswordHandler
from src.drivers.jwt_handler import JWTHandler
from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.types.http_bad_request import HttpBadRequestError
from .interfaces.controller_user_interface import UserControllerInterface

class UserController(UserControllerInterface):
    def __init__(self, repository: UserRepositoryInterface) -> None:
        self.__repository = repository
        self.__password_handler = PasswordHandler()
        self.__jwt_handler = JWTHandler()

    def create_user(self, username: str, password: str) -> None:
        self.__verify_valid_username(username)
        self.__verify_valid_password(password)

        hashed_password = self.__create_hash_password(password)
        self.__register_new_user(username, hashed_password)

    def get_user(self, username: str) -> tuple[int, str, str]:
        return self.__find_user(username)

    def create_login(self, username: str, password: str) -> str:
        user = self.__find_user(username)
        user_id = user[0]
        username = user[1]
        hashed_password = user[2]

        self.__verify_correct_password(password, hashed_password)
        return self.__create_token(user_id, username)

    def __create_hash_password(self, password: str) -> str:
        return self.__password_handler.encrypt_password(password)

    def __register_new_user(self, username: str, password: str) -> None:
        return self.__repository.create_user(username, password)

    def __find_user(self, username: str) -> tuple[int, str, str]:
        user = self.__repository.get_user_by_username(username)
        if not user:
            raise HttpNotFoundError("User not found")

        return user

    def __verify_valid_username(self, username: str) -> None:
        if not username or len(username) < 3:
            raise HttpBadRequestError("Invalid username")

    def __verify_valid_password(self, password: str) -> None:
        if not password or len(password) < 6:
            raise HttpBadRequestError("Invalid password")

    def __verify_correct_password(self, password: str, user_password: str) -> None:
        password_correct = self.__password_handler.verify_password(password, user_password)
        if not password_correct:
            raise HttpBadRequestError("Invalid credentials")

    def __create_token(self, user_id: int, username: str) -> str:
        payload = {
            "user_id": user_id,
            "username": username
        }
        token = self.__jwt_handler.create_jwt_token(payload)
        return token

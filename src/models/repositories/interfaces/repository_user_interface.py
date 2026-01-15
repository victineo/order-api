from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    @abstractmethod
    def create_user(self, username: str, password: str) -> None:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> tuple[int, str, str] | None:
        pass

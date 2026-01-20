from abc import ABC, abstractmethod

class UserControllerInterface(ABC):
    @abstractmethod
    def create_user(self, username: str, password: str) -> None:
        pass

    @abstractmethod
    def get_user(self, username: str) -> tuple[int, str, str]:
        pass

    @abstractmethod
    def create_login(self, username: str, password: str) -> str:
        pass

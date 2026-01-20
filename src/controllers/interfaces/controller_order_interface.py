from abc import ABC, abstractmethod

class OrderControllerInterface(ABC):
    @abstractmethod
    def create_order(self, user_id: int, description: str) -> None:
        pass

    @abstractmethod
    def get_orders(self, user_id: int) -> list[tuple[int, int, str, str]]:
        pass

    @abstractmethod
    def get_order(self, order_id: int) -> tuple[int, int, str, str]:
        pass

    @abstractmethod
    def update_order(self, user_id: int, order_id: int, new_description: str) -> None:
        pass

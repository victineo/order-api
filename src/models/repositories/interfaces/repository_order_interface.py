from abc import ABC, abstractmethod

class OrderRepositoryInterface(ABC):
    @abstractmethod
    def create_order(self, user_id: int, description: str) -> None:
        pass

    @abstractmethod
    def get_orders_by_user_id(self, user_id: int) -> list[tuple[int, int, str, str]]:
        pass

    @abstractmethod
    def get_order_by_id(self, order_id: int) -> tuple[int, int, str, str]:
        pass

    @abstractmethod
    def update_order(self, user_id: int, order_id: int, new_description: str) -> None:
        pass

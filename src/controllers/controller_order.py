from src.models.repositories.interfaces.repository_order_interface import OrderRepositoryInterface
from .interfaces.controller_order_interface import OrderControllerInterface

class OrderController(OrderControllerInterface):
    def __init__(self, repository: OrderRepositoryInterface) -> None:
        self.__repository = repository

    def create_order(self, user_id: int, description: str) -> None:
        self.__verify_valid_description(description)
        self.__repository.create_order(user_id, description)

    def get_orders(self, user_id: int) -> list[tuple[int, int, str, str]]:
        return self.__repository.get_orders_by_user_id(user_id)
    
    def get_order(self, order_id: int) -> tuple[int, int, str, str]:
        return self.__repository.get_order_by_id(order_id)
    
    def update_order(self, user_id: int, order_id: int, new_description: str) -> None:
        order = self.get_order(order_id)
        order_user_id = order[1]
        if order_user_id != user_id:
            raise Exception("Unauthorized")

        self.__verify_valid_description(new_description)
        self.__repository.update_order(user_id, order_id, new_description)

    def __verify_valid_description(self, description: str) -> None:
        if not description or len(description) < 3:
            raise Exception("Invalid description")

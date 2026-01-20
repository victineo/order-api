from src.controllers.interfaces.controller_order_interface import OrderControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_order_interface import OrderViewInterface

class OrderView(OrderViewInterface):
    def __init__(self, controller: OrderControllerInterface) -> None:
        self.__controller = controller

    def handle_create_order(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.params.get("user_id")
        header_user_id = http_request.headers.get("uid")
        description = http_request.body.get("description")

        self.__validate_inputs("create_order", {
            "user_id": user_id,
            "header_user_id": header_user_id,
            "description": description
        })

        self.__controller.create_order(user_id, description)
        return HttpResponse({"message": "Order created"}, 201)

    def handle_get_orders(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.params.get("user_id")
        header_user_id = http_request.headers.get("uid")

        self.__validate_inputs("get_orders", {
            "user_id": user_id,
            "header_user_id": header_user_id
        })

        orders = self.__controller.get_orders(user_id)
        return HttpResponse({"orders": orders}, 200)

    def handle_get_order(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.params.get("user_id")
        header_user_id = http_request.headers.get("uid")
        order_id = http_request.body.get("order_id")

        self.__validate_inputs("get_order", {
            "user_id": user_id,
            "header_user_id": header_user_id,
            "order_id": order_id
        })

        order = self.__controller.get_order(order_id)
        return HttpResponse({"order": order}, 200)

    def handle_update_order(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.params.get("user_id")
        header_user_id = http_request.headers.get("uid")
        order_id = http_request.body.get("order_id")
        new_description = http_request.body.get("new_description")

        self.__validate_inputs("update_order", {
            "user_id": user_id,
            "header_user_id": header_user_id,
            "order_id": order_id,
            "new_description": new_description
        })

        self.__controller.update_order(user_id, order_id, new_description)
        return HttpResponse({"message": "Order updated"}, 200)

    def __validate_inputs(self, body_type: str, body: dict) -> None:
        if (
            not body
            or not isinstance(body, dict)
        ): raise Exception("Invalid input")

        if body_type == "create_order":
            if (
                not body.get("user_id")
                or not body.get("header_user_id")
                or not body.get("description")
                or not isinstance(body.get("description"), str)
                or int(body.get("header_user_id")) != int(body.get("user_id"))
            ): raise Exception("Invalid input")

        elif body_type == "get_orders":
            if (
                not body.get("user_id")
                or not body.get("header_user_id")
                or int(body.get("header_user_id")) != int(body.get("user_id"))
            ): raise Exception("Invalid input")

        elif body_type == "get_order":
            if (
                not body.get("user_id")
                or not body.get("header_user_id")
                or not body.get("order_id")
                or int(body.get("header_user_id")) != int(body.get("user_id"))
            ): raise Exception("Invalid input")

        elif body_type == "update_order":
            if (
                not body.get("user_id")
                or not body.get("header_user_id")
                or not body.get("order_id")
                or not body.get("new_description")
                or not isinstance(body.get("new_description"), str)
                or int(body.get("header_user_id")) != int(body.get("user_id"))
            ): raise Exception("Invalid input")

        else:
            raise Exception("Invalid input")

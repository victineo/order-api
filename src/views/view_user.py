from src.controllers.interfaces.controller_user_interface import UserControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_user_interface import UserViewInterface

class UserView(UserViewInterface):
    def __init__(self, controller: UserControllerInterface) -> None:
        self.__controller = controller

    def handle_create_user(self, http_request: HttpRequest) -> HttpResponse:
        self.__validate_inputs("create_user", http_request.body)
        username = http_request.body.get("username")
        password = http_request.body.get("password")

        self.__controller.create_user(username, password)
        return HttpResponse({"message": "User created"}, 201)
    
    def handle_get_user(self, http_request: HttpRequest) -> HttpResponse:
        self.__validate_inputs("get_user", http_request.params)
        username = http_request.params.get("username")
        user = self.__controller.get_user(username)
        return HttpResponse({"user": user}, 200)
    
    def handle_create_login(self, http_request: HttpRequest) -> HttpResponse:
        self.__validate_inputs("create_login", http_request.body)
        username = http_request.body.get("username")
        password = http_request.body.get("password")

        token = self.__controller.create_login(username, password)
        return HttpResponse({"token": token}, 200)

    def __validate_inputs(self, body_type: str, body: dict) -> None:
        if (
            not body
            or not isinstance(body, dict)
        ): raise Exception("Invalid input")

        if body_type == "create_user" or body_type == "create_login":
            if (
                not body.get("username")
                or not body.get("password")
                or not isinstance(body.get("username"), str)
                or not isinstance(body.get("password"), str)
            ): raise Exception("Invalid input")

        elif body_type == "get_user":
            if (
                not body.get("username")
                or not isinstance(body.get("username"), str)
            ): raise Exception("Invalid input")

        else:
            raise Exception("Invalid input")

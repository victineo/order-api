from abc import ABC, abstractmethod
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class UserViewInterface(ABC):
    @abstractmethod
    def handle_create_user(self, http_request: HttpRequest) -> HttpResponse: pass

    @abstractmethod
    def handle_get_user(self, http_request: HttpRequest) -> HttpResponse: pass

    @abstractmethod
    def handle_create_login(self, http_request: HttpRequest) -> HttpResponse: pass

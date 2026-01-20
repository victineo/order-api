from abc import ABC, abstractmethod
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class OrderViewInterface(ABC):
    @abstractmethod
    def handle_create_order(self, http_request: HttpRequest) -> HttpResponse: pass

    @abstractmethod
    def handle_get_orders(self, http_request: HttpRequest) -> HttpResponse: pass

    @abstractmethod
    def handle_get_order(self, http_request: HttpRequest) -> HttpResponse: pass

    @abstractmethod
    def handle_update_order(self, http_request: HttpRequest) -> HttpResponse: pass

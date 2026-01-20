from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .view_order import OrderView
import pytest

class MockController:
    def create_order(self, user_id, description) -> None:
        pass

    def get_orders(self, user_id) -> list[tuple[int, int, str, str]]:
        return [
            (1, 1, "mockDescription", "mockDatetime"),
            (2, 1, "mockDescription", "mockDatetime")
        ]

    def get_order(self, order_id) -> tuple[int, int, str, str]:
        return (1, 1, "mockDescription", "mockDatetime")

    def update_order(self, user_id, order_id, new_description) -> None:
        pass

def test_handle_create_order():
    body = {
        "user_id": 1,
        "description": "mockDescription"
    }
    request = HttpRequest(
        body=body,
        params={ "user_id": 1 },
        headers={ "uid": 1 }
    )

    mock_controller = MockController()
    view = OrderView(mock_controller)

    response = view.handle_create_order(request)

    assert isinstance(response, HttpResponse)
    assert isinstance(response.body, dict)
    assert response.body == { "message": "Order created" }
    assert response.status_code == 201

def test_handle_create_order_with_invalid_input():
    with pytest.raises(Exception):
        body = { "description": "mockDescription" }
        request = HttpRequest(
            body=body,
            params={ "user_id": 1 },
            headers={ "uid": 1 }
        )

        mock_controller = MockController()
        view = OrderView(mock_controller)

        view.handle_create_order(request)

        assert Exception == "Invalid input"

def test_handle_create_order_with_unauthorized_user():
    with pytest.raises(Exception):
        body = { "description": "mockDescription" }
        request = HttpRequest(
            body=body,
            params={ "user_id": 2 },
            headers={ "uid": 1 }
        )

        mock_controller = MockController()
        view = OrderView(mock_controller)

        view.handle_create_order(request)

        assert Exception == "Unauthorized"

def test_handle_get_orders():
    request = HttpRequest(
        params={ "user_id": 1 },
        headers={ "uid": 1 }
    )

    mock_controller = MockController()
    view = OrderView(mock_controller)

    response = view.handle_get_orders(request)

    assert isinstance(response, HttpResponse)
    assert isinstance(response.body, dict)
    assert response.body == { "orders": [
        (1, 1, "mockDescription", "mockDatetime"),
        (2, 1, "mockDescription", "mockDatetime")
    ] }
    assert response.status_code == 200

def test_handle_get_orders_with_invalid_input():
    with pytest.raises(Exception):
        request = HttpRequest(
            params={},
            headers={ "uid": 1 }
        )

        mock_controller = MockController()
        view = OrderView(mock_controller)

        view.handle_get_orders(request)

        assert Exception == "Invalid input"

def test_handle_get_orders_with_unauthorized_user():
    with pytest.raises(Exception):
        request = HttpRequest(
            params={ "user_id": 2 },
            headers={ "uid": 1 }
        )

        mock_controller = MockController()
        view = OrderView(mock_controller)

        view.handle_get_orders(request)

        assert Exception == "Unauthorized"

def test_handle_get_order():
    body = { "order_id": 1 }
    request = HttpRequest(
        body=body,
        params={ "user_id": 1 },
        headers={ "uid": 1 }
    )

    mock_controller = MockController()
    view = OrderView(mock_controller)

    response = view.handle_get_order(request)

    assert isinstance(response, HttpResponse)
    assert isinstance(response.body, dict)
    assert response.body == { "order": (1, 1, "mockDescription", "mockDatetime") }
    assert response.status_code == 200

def test_handle_get_order_with_invalid_input():
    with pytest.raises(Exception):
        request = HttpRequest(
            body={ "order_id": "1" },
            params={ "user_id": 1 },
            headers={ "uid": 1 }
        )

        mock_controller = MockController()
        view = OrderView(mock_controller)

        view.handle_get_order(request)

        assert Exception == "Invalid input"

def test_handle_get_order_with_unauthorized_user():
    with pytest.raises(Exception):
        request = HttpRequest(
            body={ "order_id": 1 },
            params={ "user_id": 2 },
            headers={ "uid": 1 }
        )

        mock_controller = MockController()
        view = OrderView(mock_controller)

        view.handle_get_order(request)

        assert Exception == "Unauthorized"

def test_handle_update_order():
    body = {
        "order_id": 1,
        "new_description": "mockUpdateDescription"
    }
    request = HttpRequest(
        body=body,
        params={ "user_id": 1 },
        headers={ "uid": 1 }
    )

    mock_controller = MockController()
    view = OrderView(mock_controller)

    response = view.handle_update_order(request)

    assert isinstance(response, HttpResponse)
    assert isinstance(response.body, dict)
    assert response.body == { "message": "Order updated" }
    assert response.status_code == 200

def test_handle_update_order_with_invalid_input():
    with pytest.raises(Exception):
        request = HttpRequest(
            body={ "order_id": 1 },
            params={ "user_id": 1 },
            headers={ "uid": 1 }
        )

        mock_controller = MockController()
        view = OrderView(mock_controller)

        view.handle_update_order(request)

        assert Exception == "Invalid input"

def test_handle_update_order_with_unauthorized_user():
    with pytest.raises(Exception):
        body = {
            "order_id": 1,
            "new_description": "mockUpdateDescription"
        }
        request = HttpRequest(
            body=body,
            params={ "user_id": 2 },
            headers={ "uid": 1 }
        )

        mock_controller = MockController()
        view = OrderView(mock_controller)

        view.handle_update_order(request)

        assert Exception == "Unauthorized"

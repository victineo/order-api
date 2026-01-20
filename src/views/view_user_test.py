from unittest.mock import Mock
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .view_user import UserView
import pytest

class MockController:
    def create_user(self, username, password) -> None:
        pass

    def get_user(self, username) -> tuple[int, str, str]:
        return {
            "id": 1,
            "username": username,
            "password": "mockPassword"
        }

    def create_login(self, username, password) -> str:
        return "mockToken"

def test_handle_create_user():
    body = {
        "username": "mockUsername",
        "password": "mockPassword"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    view = UserView(mock_controller)

    response = view.handle_create_user(request)

    assert isinstance(response, HttpResponse)
    assert isinstance(response.body, dict)
    assert response.body == { "message": "User created" }
    assert response.status_code == 201

def test_handle_create_user_with_invalid_input():
    with pytest.raises(Exception):
        body = {
            "username": "mockUsername"
        }
        request = HttpRequest(body=body)

        mock_controller = MockController()
        view = UserView(mock_controller)

        view.handle_create_user(request)

        assert Exception == "Invalid input"

def test_handle_get_user():
    body = {
        "username": "mockUsername"
    }
    request = HttpRequest(params=body)

    mock_controller = MockController()
    view = UserView(mock_controller)

    response = view.handle_get_user(request)

    assert isinstance(response, HttpResponse)
    assert isinstance(response.body, dict)
    assert response.body == {
        "user": {
            "id": 1,
            "username": "mockUsername",
            "password": "mockPassword"
        }
    }
    assert response.status_code == 200

def test_handle_get_user_with_invalid_input():
    with pytest.raises(Exception):
        body = {
            "password": "mockPassword"
        }
        request = HttpRequest(params=body)

        mock_controller = MockController()
        view = UserView(mock_controller)

        view.handle_get_user(request)

        assert Exception == "Invalid input"

def test_handle_create_login():
    body = {
        "username": "mockUsername",
        "password": "mockPassword"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    view = UserView(mock_controller)

    response = view.handle_create_login(request)

    assert isinstance(response, HttpResponse)
    assert isinstance(response.body, dict)
    assert response.body == { "token": "mockToken" }
    assert response.status_code == 200

def test_handle_create_login_with_invalid_input():
    with pytest.raises(Exception):
        body = {
            "username": "mockUsername"
        }
        request = HttpRequest(body=body)

        mock_controller = MockController()
        view = UserView(mock_controller)

        view.handle_create_login(request)

        assert Exception == "Invalid input"

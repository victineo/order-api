from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.user_composer import user_composer
from src.errors.error_handler import handle_errors

users_bp = Blueprint("users", __name__)

@users_bp.route("/user/register", methods=["POST"])
def create_user():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = user_composer().handle_create_user(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        http_response = handle_errors(e)
        return jsonify(http_response.body), http_response.status_code

@users_bp.route("/user/login", methods=["POST"])
def login_user():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = user_composer().handle_create_login(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        http_response = handle_errors(e)
        return jsonify(http_response.body), http_response.status_code

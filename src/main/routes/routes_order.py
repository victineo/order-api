from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.order_composer import order_composer
from src.main.middlewares.auth_jwt import auth_jwt_verify
from src.errors.error_handler import handle_errors

orders_bp = Blueprint("user", __name__)

@orders_bp.route("/orders", methods=["POST"])
def create_order():
    try:
        token_information = auth_jwt_verify()
        http_request = HttpRequest(
            body=request.json,
            params=request.args,
            headers=request.headers,
            token_infos=token_information
        )
        http_response = order_composer().handle_create_order(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        http_response = handle_errors(e)
        return jsonify(http_response.body), http_response.status_code

# FIX
@orders_bp.route("/orders/<int:user_id>", methods=["GET"])
def get_orders(user_id):
    try:
        token_information = auth_jwt_verify()
        http_request = HttpRequest(
            body=request.json,
            params={ "user_id": user_id },
            headers=request.headers,
            token_infos=token_information
        )
        http_response = order_composer().handle_get_orders(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        http_response = handle_errors(e)
        return jsonify(http_response.body), http_response.status_code

@orders_bp.route("/orders/<int:order_id>", methods=["PATCH"])
def update_order(order_id):
    try:
        token_information = auth_jwt_verify()
        http_request = HttpRequest(
            body=request.json,
            params={ "order_id": order_id },
            headers=request.headers,
            token_infos=token_information
        )
        http_response = order_composer().handle_update_order(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        http_response = handle_errors(e)
        return jsonify(http_response.body), http_response.status_code

from .jwt_handler import JWTHandler

def test_jwt_handler():
    jwt_handler = JWTHandler()
    body = {
        "user_id": 1,
        "username": "testuser"
    }
    token = jwt_handler.create_jwt_token(body)
    token_info = jwt_handler.decode_jwt_token(token)

    assert token is not None
    assert isinstance(token, str)
    assert token_info['user_id'] == body['user_id']
    assert token_info['username'] == body['username']

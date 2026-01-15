from .password_handler import PasswordHandler

def test_encrypt():
    password_handler = PasswordHandler()
    password = "testPassword"

    hashed_password = password_handler.encrypt_password(password)
    password_checked = password_handler.verify_password(password, hashed_password)

    assert password_checked

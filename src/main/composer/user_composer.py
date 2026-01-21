from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.repository_user import UserRepository
from src.controllers.controller_user import UserController
from src.views.view_user import UserView

def user_composer():
    connection = db_connection_handler.get_connection()
    user_repository = UserRepository(connection)
    user_controller = UserController(user_repository)
    user_view = UserView(user_controller)

    return user_view

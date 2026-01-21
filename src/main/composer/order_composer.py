from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.repository_order import OrderRepository
from src.controllers.controller_order import OrderController
from src.views.view_order import OrderView

def order_composer():
    connection = db_connection_handler.get_connection()
    order_repository = OrderRepository(connection)
    order_controller = OrderController(order_repository)
    order_view = OrderView(order_controller)

    return order_view

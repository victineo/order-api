from flask import Flask
from src.models.settings.db_connection_handler import db_connection_handler
from ..routes.routes_user import users_bp
from ..routes.routes_order import orders_bp

db_connection_handler.connect()

app = Flask(__name__)

app.register_blueprint(users_bp)
app.register_blueprint(orders_bp)

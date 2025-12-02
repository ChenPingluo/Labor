from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

from . import items, inventory, stock, auth, finance


def register_blueprints(app):
    app.register_blueprint(api_v1)
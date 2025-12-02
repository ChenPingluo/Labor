from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db, migrate, jwt
from .api import register_blueprints

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    register_blueprints(app)

    return app
import os

from flasgger import Swagger
from flask import Flask

from app.routes import register_blueprints


def create_app():
    app = Flask(__name__)
    swagger = Swagger(app)

    app.config["ENV"] = os.getenv("FLASK_ENV", "production")
    app.config["DEBUG"] = os.getenv("DEBUG", "false").lower() == "true"
    app.config["APP_NAME"] = os.getenv("APP_NAME", "DefaultApp")

    register_blueprints(app)

    @app.route("/")
    def index():
        return f"Welcome to {app.config['APP_NAME']} (env: {app.config['ENV']})"

    return app

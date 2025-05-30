import os

from flasgger import Swagger
from flask import Flask
from libversion import version

from app.routes import register_blueprints


def create_app():
    app = Flask(__name__)

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "App Service",
            "description": "Backend service to communicate with the model",
            "version": version.VersionUtil.get_version(),
        },
        "basePath": "/app",
        "schemes": ["http"],
        "consumes": ["application/json"],
        "produces": ["application/json"],
    }

    swagger = Swagger(app, template=swagger_template)

    app.config["ENV"] = os.getenv("FLASK_ENV", "production")
    app.config["DEBUG"] = os.getenv("DEBUG", "false").lower() == "true"
    app.config["APP_NAME"] = os.getenv("APP_NAME", "DefaultApp")

    register_blueprints(app)

    @app.route("/")
    def index():
        return f"Welcome to {app.config['APP_NAME']} (env: {app.config['ENV']})"

    return app

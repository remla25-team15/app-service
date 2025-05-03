import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["ENV"] = os.getenv("FLASK_ENV", "production")
    app.config["DEBUG"] = os.getenv("DEBUG", "false").lower() == "true"
    app.config["APP_NAME"] = os.getenv("APP_NAME", "DefaultApp")

    @app.route("/")
    def index():
        return f"Welcome to {app.config['APP_NAME']} (env: {app.config['ENV']})"

    return app

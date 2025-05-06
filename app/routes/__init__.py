from flask import Flask

from app.routes.feedback import feedback_bp
from app.routes.predict import predict_bp
from app.routes.version import version_bp


def register_blueprints(app: Flask):
    app.register_blueprint(version_bp)
    app.register_blueprint(predict_bp)
    app.register_blueprint(feedback_bp)

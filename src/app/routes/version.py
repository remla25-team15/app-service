import requests
from flask import Blueprint, current_app, jsonify

version_bp = Blueprint("version", __name__)


@version_bp.route("/version", methods=["GET"])
def get_versions():
    model_url = current_app.config["MODEL_SERVICE_URL"]
    try:
        response = requests.get(f"{model_url}/version", timeout=2)
        model_version = response.json().get("model_version", "unknown")
    except Exception:
        model_version = "unreachable"

    return jsonify(
        {
            "app_version": 0,  # Use lib-version for doing this
            "model_service_version": model_version,
        }
    )

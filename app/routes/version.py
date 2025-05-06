import requests
from flask import Blueprint, current_app, jsonify
from libversion import version

from app.config import MODEL_SERVICE_URL

version_bp = Blueprint("version", __name__, url_prefix="/api")


@version_bp.route("/version", methods=["GET"])
def get_versions():
    """
    Get application and model service versions
    ---
    responses:
      200:
        description: Version information
        schema:
          type: object
          properties:
            app_version:
              type: string
              example: "v1.0.0"
            model_service_version:
              type: string
              example: "v1.0.0"
    """
    try:
        response = requests.get(f"{MODEL_SERVICE_URL}/version", timeout=2)
        model_version = response.json().get("version", "unknown")
    except Exception:
        model_version = "unreachable"

    return jsonify(
        {
            "app_version": version.VersionUtil.get_version(),  # Use lib-version for doing this
            "model_service_version": model_version,
        }
    )

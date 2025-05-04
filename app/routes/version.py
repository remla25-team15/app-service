import requests
from flask import Blueprint, current_app, jsonify

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
              type: integer
              example: 0
            model_service_version:
              type: string
              example: "1.0.0"
    """
    model_url = ""
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

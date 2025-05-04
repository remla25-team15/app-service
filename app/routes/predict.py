import requests
from flask import Blueprint, current_app, jsonify, request

from app.config import MODEL_SERVICE_URL

predict_bp = Blueprint("predict", __name__, url_prefix="/api")


@predict_bp.route("/predict", methods=["POST"])
def predict():
    """
    Make a prediction using the model service
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          example: {"data": "your input data here"}
    responses:
      200:
        description: Successful prediction
      503:
        description: Service unavailable
    """
    try:
        response = requests.post(
            f"{MODEL_SERVICE_URL}/predict", json=request.json, timeout=5
        )
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return (
            jsonify({"error": "Failed to contact model-service", "details": str(e)}),
            503,
        )

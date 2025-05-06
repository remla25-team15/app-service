import requests
from flask import Blueprint, current_app, jsonify, request

feedback_bp = Blueprint("feedback", __name__, url_prefix="/api")


@feedback_bp.route("/feedback", methods=["POST"])
def predict():
    """
    Provide Feedback on the sentiment
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          example: {"text": "your input data here"}
    responses:
      200:
        description: Successful something
      503:
        description: Service unavailable
    """
    try:
        print(f"Data: {request.json}")
        return jsonify({"response": "received"}), 200
    except Exception as e:
        return (
            jsonify({"error": "Failed to contact model-service", "details": str(e)}),
            503,
        )

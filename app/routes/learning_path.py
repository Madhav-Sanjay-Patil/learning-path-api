from flask import Blueprint, jsonify
from ..services.learning_path_service import get_eligible_topics

# Define a Blueprint for the learning path routes
learning_path_bp = Blueprint('learning_path', __name__)

@learning_path_bp.route('/<int:learner_id>', methods=['GET'])
def get_learning_path(learner_id):
    """
    GET endpoint to fetch eligible learning topics for a given learner ID.

    ---
    Swagger documentation:
    parameters:
      - in: path
        name: learner_id
        required: true
        schema:
          type: integer
        description: ID of the learner

    responses:
      200:
        description: List of eligible topics or message if all are completed
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  title:
                    type: string
                  prerequisites:
                    type: string
                    nullable: true
      404:
        description: Invalid learner ID
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
    """

    # Call service logic to fetch topics eligible for the learner
    topics = get_eligible_topics(learner_id)

    # If learner_id is invalid or has no progress, return 404
    if topics is None:
        return jsonify({"error": "Invalid learner ID entered"}), 404

    # Return the list of eligible topics
    return jsonify(topics), 200

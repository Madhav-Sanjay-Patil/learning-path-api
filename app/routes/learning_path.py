from flask import Blueprint, jsonify
from ..services.learning_path_service import get_eligible_topics


learning_path_bp = Blueprint('learning_path', __name__)

@learning_path_bp.route('/<int:learner_id>', methods=['GET'])
def get_learning_path(learner_id):
    """
    Get eligible topics for a learner
    ---
    parameters:
      - in: path
        name: learner_id
        required: true
        schema:
          type: integer
        description: ID of the learner
    responses:
      200:
        description: List of eligible topics or message if all completed
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
    topics = get_eligible_topics(learner_id)
    if topics is None:
        return jsonify({"error": "Invalid learner ID entered"}), 404

    return jsonify(topics), 200

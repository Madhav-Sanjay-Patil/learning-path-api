#This file contains the core logic to determine which topics a learner is ready for, based on their progress and each topic’s prerequisites.

from ..models.models import Topic, LearnerProgress
from ..extensions import db

def get_eligible_topics(learner_id):
    # Fetch all progress records for the given learner
    learner_progress_entries = LearnerProgress.query.filter_by(learner_id=learner_id).all()

    # If no records are found, the learner_id may be invalid
    if not learner_progress_entries:
        return None  # Caller can handle this as "invalid learner"

    # Create a lookup for the learner's current progress: {topic_id: status}
    progress = {entry.topic_id: entry.status for entry in learner_progress_entries}

    # Fetch all topics and create a quick lookup by topic ID
    all_topics = Topic.query.all()
    topic_dict = {topic.id: topic for topic in all_topics}

    eligible_topics = []

    for topic in all_topics:
        # Skip topics the learner has already completed or started
        if progress.get(topic.id) in ['Completed', 'In Progress']:
            continue

        # Fetch list of prerequisite topic IDs for this topic
        prerequisite_ids = topic.get_prerequisites()

        # Check if all prerequisites are completed
        if all(progress.get(pid) == 'Completed' for pid in prerequisite_ids):
            prerequisites = []
            for pid in prerequisite_ids:
                prereq_topic = topic_dict.get(pid)
                if prereq_topic:
                    prerequisites.append({
                        "id": prereq_topic.id,
                        "title": prereq_topic.title
                    })

            # Add the topic to the eligible list with its prerequisite info
            eligible_topics.append({
                "id": topic.id,
                "title": topic.title,
                "prerequisites": prerequisites
            })

    return eligible_topics

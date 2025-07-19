from ..models.models import Topic, LearnerProgress
from ..extensions import db

def get_eligible_topics(learner_id):
    learner_progress_entries = LearnerProgress.query.filter_by(learner_id=learner_id).all()

    # Explicit check for invalid learner_id
    if not learner_progress_entries:
        return None  # Flag that learner_id is invalid

    progress = {entry.topic_id: entry.status for entry in learner_progress_entries}

    all_topics = Topic.query.all()
    topic_dict = {topic.id: topic for topic in all_topics}

    eligible_topics = []

    for topic in all_topics:
        if progress.get(topic.id) in ['Completed', 'In Progress']:
            continue

        prerequisite_ids = topic.get_prerequisites()

        if all(progress.get(pid) == 'Completed' for pid in prerequisite_ids):
            prerequisites = []
            for pid in prerequisite_ids:
                prereq_topic = topic_dict.get(pid)
                if prereq_topic:
                    prerequisites.append({
                        "id": prereq_topic.id,
                        "title": prereq_topic.title
                    })

            eligible_topics.append({
                "id": topic.id,
                "title": topic.title,
                "prerequisites": prerequisites
            })

    return eligible_topics

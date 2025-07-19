from app import create_app
from app.extensions import db
from app.models.models import Topic, LearnerProgress

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # ----- Create Topics -----
    topics = [
        Topic(id=1, title='HTML Basics', prerequisite_ids=''),
        Topic(id=2, title='CSS Fundamentals', prerequisite_ids='1'),
        Topic(id=3, title='JavaScript Essentials', prerequisite_ids='1,2'),
        Topic(id=4, title='DOM Manipulation', prerequisite_ids='3'),
        Topic(id=5, title='React Basics', prerequisite_ids='3'),
        Topic(id=6, title='Redux & State Management', prerequisite_ids='5'),
        Topic(id=7, title='Flask Basics', prerequisite_ids=''),
        Topic(id=8, title='Flask REST APIs', prerequisite_ids='7'),
        Topic(id=9, title='SQLAlchemy ORM', prerequisite_ids='7'),
        Topic(id=10, title='Full Stack Integration', prerequisite_ids='6,8,9'),
    ]

    db.session.bulk_save_objects(topics)
    db.session.commit()

    # ----- Create Learner Progress -----
    learner_progress = [
        # Learner 1 has finished frontend basics
        LearnerProgress(learner_id=1, topic_id=1, status='Completed', score=95),
        LearnerProgress(learner_id=1, topic_id=2, status='Completed', score=88),
        LearnerProgress(learner_id=1, topic_id=3, status='Completed', score=80),

        # Learner 2 is backend focused
        LearnerProgress(learner_id=2, topic_id=7, status='Completed', score=90),
        LearnerProgress(learner_id=2, topic_id=9, status='In Progress', score=40),

        # Learner 3 is just getting started
        LearnerProgress(learner_id=3, topic_id=1, status='Completed', score=70),

        # Learner 4 has completed everything except the final topic
        *[
            LearnerProgress(learner_id=4, topic_id=i, status='Completed', score=85)
            for i in range(1, 10)
        ]
    ]

    db.session.bulk_save_objects(learner_progress)
    db.session.commit()

    print("Database created with topics and learner progress.")

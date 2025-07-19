from app.extensions import db  
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

class Topic(db.Model):
    __tablename__ = 'topics'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    prerequisite_ids = Column(String)  # comma-separated ids like "1,2"

    def get_prerequisites(self):
        return [int(pid) for pid in self.prerequisite_ids.split(',')] if self.prerequisite_ids else []

class LearnerProgress(db.Model):
    __tablename__ = 'learner_progress'

    id = Column(Integer, primary_key=True)
    learner_id = Column(Integer, nullable=False)
    topic_id = Column(Integer, ForeignKey('topics.id'), nullable=False)
    status = Column(Enum('Not Started', 'In Progress', 'Completed'), nullable=False)
    score = Column(Integer)

    topic = relationship('Topic')

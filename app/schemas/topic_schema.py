# Import Marshmallow instance (ma) and Topic model
from ..extensions import ma
from ..models.models import Topic

# Schema for serializing and deserializing Topic model instances
class TopicSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # Associate schema with Topic model
        model = Topic

        # Enable deserialization to model instances (i.e., model objects on load)
        load_instance = True

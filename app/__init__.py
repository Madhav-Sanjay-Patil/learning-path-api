from flask import Flask
from app.config import Config
from app.extensions import db, ma
from app.routes.learning_path import learning_path_bp

# Application factory function
def create_app():
    app = Flask(__name__)

    # Load configuration from Config class
    app.config.from_object(Config)

    # Initialize extensions with app context
    db.init_app(app)
    ma.init_app(app)

    # Register blueprint for learning path routes
    app.register_blueprint(learning_path_bp, url_prefix='/api/learning-path')

    # Health check route
    @app.route("/ping")
    def ping():
        return "App is working!"

    return app

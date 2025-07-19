from flask import Flask
from app.config import Config
from app.extensions import db, ma
from app.routes.learning_path import learning_path_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(learning_path_bp, url_prefix='/api/learning-path')

    @app.route("/ping")
    def ping():
        return "App is working!"


    return app

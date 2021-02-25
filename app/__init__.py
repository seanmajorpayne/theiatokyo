from flask import Flask
from flask_caching import Cache
from flask_bootstrap import Bootstrap

from config import DevelopmentConfig

cache = Cache()
bootstrap = Bootstrap()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    cache.init_app(app)
    bootstrap.init_app(app)

    with app.app_context():
        from app.client import bp as eyexplore_bp
        app.register_blueprint(eyexplore_bp)

    return app

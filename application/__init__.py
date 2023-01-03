"""
Main Flask Application Initialization
"""
import os

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

from application.context_processors import utility_text_processors
from application.database import db, User
import config
from application.bp.homepage import bp_homepage
from application.bp.authentication import authentication
from flask_login import LoginManager

migrate = Migrate()
csrf = CSRFProtect()
login_manager = LoginManager()


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    if os.getenv('DEPLOYMENT', "development"):
        app.config.from_object(config.DevelopmentConfig)
    elif os.getenv('DEPLOYMENT', "production"):
        app.config.from_object(config.ProductionConfig)
    else:
        app.config.from_object(config.TestingConfig)

    csrf.init_app(app)
    bootstrap = Bootstrap5(app)
    app.context_processor(utility_text_processors)
    login_manager.login_view = "authentication.login"
    login_manager.init_app(app)

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        blueprints = [bp_homepage, authentication]
        # Register Blueprints
        for blueprint in blueprints:
            app.register_blueprint(blueprint)
        return app


@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.query.get(user_id)
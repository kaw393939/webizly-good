"""Configuration Class for Flask"""
import os
import secrets


class Config(object):
    """Default Config Settings"""
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SECRET_KEY = secrets.token_urlsafe(16)
    DEPLOYMENT = os.getenv('DEPLOYMENT', "development-default")
    TESTING = False


class ProductionConfig(Config):
    """Default Config Settings"""
    FLASK_DEBUG = False


class DevelopmentConfig(Config):
    FLASK_DEBUG = True


class TestingConfig(Config):
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    WTF_CSRF_ENABLED = False

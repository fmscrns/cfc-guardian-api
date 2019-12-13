import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fmscrns')
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:18345@localhost:5432/cfc-guardian'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:18345@localhost:5432/cfc-guardian-testing'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    SQLALCHEMY_DATABASE_URI = ''


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
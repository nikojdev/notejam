import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'notejam-flask-secret-key'
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'notejam-flask-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+ os.environ['DBUSER'] +':' + os.environ['DBPASS'] + '@' + os.environ['DBENDPOINT'] + '/notejamdb?charset=utf8mb4'


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

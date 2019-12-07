import os


basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    SECRET_KEY = "SO_SECURE"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = '..database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
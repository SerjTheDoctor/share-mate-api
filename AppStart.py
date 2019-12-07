from flask import Flask
import os

from flask_sqlalchemy import SQLAlchemy
from config_file import BaseConfig
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from api.Data.models import db

from .api import  create_app,app
if __name__ == '__main__':
    app1 = create_app(app)
    app1.run(host='127.0.0.1', threaded=True, debug=True)


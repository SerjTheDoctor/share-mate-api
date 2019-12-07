from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from config_file import BaseConfig


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)

    from api.Views.views import view

    cors = CORS(app, resources={
        r'/api/*': {
            'origins': BaseConfig.ORIGINS
        }
    })

    app.url_map.strict_slashes = False

    app.register_blueprint(view,url_prefix="/api")
    return app
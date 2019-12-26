from flask import Flask
from config_file import BaseConfig
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from api.Data.models import db
import os


def create_app():
    app = Flask(__name__, static_folder='./static', template_folder='./static/public')
    static_folder_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "client")
    app.config.from_object(BaseConfig)
    bcrypt = Bcrypt(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Data/database.db'
    with app.app_context():
        db.init_app(app)

    from api.Views.views import view
    app.register_blueprint(view)
    return app

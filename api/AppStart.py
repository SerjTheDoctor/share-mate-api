from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from api.config_file import BaseConfig
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)



main = Blueprint('main', __name__)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(host='127.0.0.1', threaded=True, debug=True)
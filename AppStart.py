from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config_file import BaseConfig
from flask_bcrypt import Bcrypt
from api import create_app

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)




@app.route('/home', methods=['GET'])
def index():
    return "Hello home!"

if __name__ == '__main__':
    app = create_app(BaseConfig)
    app.run(host='127.0.0.1', threaded=True, debug=True)


from flask import Blueprint, jsonify, request
from . import db
from .models import Users,Movie

main = Blueprint('main', __name__)

@main.route('/login', methods=['GET'])
def user_login():
    users_list = Users.query.all()
    users = []

    for user in users_list:
        users.append({'mail' : user.mail, 'password' : user.password})

    return jsonify({'users' : users})

@main.route('/users', methods=['GET'])
def profile():
    users_list = Users.query.all();
    users = []

    for user in users_list:
        users.append({'last name' : user.last_name, 'first_name' : user.first_name ,'shareCoins' : user.shareCoins , 'password' : user.password,'mail' : user.mail, 'location' : user.location, 'age':user.age ,'image': user.image })

    return jsonify({'users' : users})


@main.route('/register', methods=['POST'])
def add_user():
    user_data = request.get_json()

    new_user = Users(last_name=user_data['last_name'],first_name=user_data['first_name'],shareCoins=user_data['shareCoins'],password=user_data['password'],
                     mail=user_data['mail'],location=user_data['location'],age=user_data['age'],image=user_data['image'])

    db.session.add(new_user)
    db.session.commit()

    return "Added"+user_data['last_name']+"\n", 201
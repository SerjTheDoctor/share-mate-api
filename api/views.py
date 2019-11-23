from flask import Blueprint, jsonify, request
from . import db
from .models import Users,UserTag

main = Blueprint('main', __name__)

@main.route('/login', methods=['GET'])
def user_login():
    users_list = Users.query.all()
    users = []

    for user in users_list:
        users.append({'mail' : user.mail, 'password' : user.password})

    return jsonify({'users' : users})

@main.route('/checker_login', methods=['GET'])
def check_login():
    users_list = Users.query.all()
    data = request.get_json()
    mail = data['mail']
    password = data['password']
    for user in users_list:
        if user.mail==mail and user.password==password:
            return 0;
    return 1;

@main.route('/givetags',methods=['GET'])
def giveTags():
    tag=['math','machine learning','football','italian dishes','tango','web development','react','css','carpenting','english']
    users_with_tag_list = UserTag.query.all()
    #for tagger in users_with_tag_list:
      #if tagger.tag not in tag:
       #     tag.append(tagger.tag)
    return jsonify(tag)

@main.route('/filter', methods=['GET'])
def filter():
    data = request.get_json()
    tagger = data['tag']
    users_with_tag_list = UserTag.query.filter_by(tag=tagger)
    users_list = Users.query.all()
    users = []
    users_with_tag =[]

    for user in users_with_tag_list:
        users.append(user.mail)

    for user_with_tag in users_list:
        if user_with_tag.mail in users:
            users_with_tag.append(user_with_tag)

    return jsonify(users_with_tag)

@main.route('/addTag', methods=['POST'])
def add_tags():

    data = request.get_json()
    mail=data['mail']
    tags=data['tags']

    for tag in tags:
        new_tag = UserTag(mail,tag)
        db.session.add(new_tag)
        db.session.commit()



@main.route('/users', methods=['GET'])
def profile():
    users_list = Users.query.all()
    users = []

    for user in users_list:
        users.append({'last name' : user.last_name, 'first_name' : user.first_name ,'shareCoins' : user.shareCoins , 'password' : user.password,'mail' : user.mail, 'location' : user.location, 'age':user.age ,'image': user.image })

    return jsonify(users)


@main.route('/register', methods=['POST'])
def add_user():
    user_data = request.get_json()

    new_user = Users(last_name=user_data['last_name'],first_name=user_data['first_name'],shareCoins=user_data['shareCoins'],password=user_data['password'],
                     mail=user_data['mail'],location=user_data['location'],age=user_data['age'],image=user_data['image'])

    db.session.add(new_user)
    db.session.commit()

    return "Added"+user_data['last_name']+"\n", 201
from flask import Blueprint, jsonify, request
from . import db
from .models import Users,UserTag,ExternalLinks,Message


main = Blueprint('main', __name__)


@main.route('/login', methods=['POST'])
def check_login():
    users_list = Users.query.all()
    data = request.get_json()
    mail = data['mail']
    password = data['password']
    for user in users_list:
        if user.mail == mail and user.password == password:
            return {"ok" :"true"}
    return {"ok" :"false"}

@main.route('/givetags',methods=['GET'])
def giveTags():
    tag=['math','machine learning','football','italian dishes','tango','web development','react','css','carpenting','english']
    users_with_tag_list = UserTag.query.all()
    for tagger in users_with_tag_list:
      if tagger.tag not in tag:
            tag.append(tagger.tag)
    return jsonify(tag)

@main.route('/add_external_links',methods=['POST'])
def addLinks():
    links_data = request.get_json()
    links_list = ExternalLinks.query.all()
    print("links {}".format(links_list))
    ok=0
    for user in links_list:
        if user.mail == links_data['mail']:
            user.linkedin=links_data['linkedin']
            user.github=links_data['github']
            db.session.commit()
            return {"ok":"modified"}

    new_user = ExternalLinks(mail=links_data['mail'],linkedin=links_data['linkedin'],github=links_data['github'])
    db.session.add(new_user)
    db.session.commit()
    links_list = ExternalLinks.query.all()
    return {"ok":"added"}

@main.route('/filter', methods=['POST'])
def filter():
    data = request.get_json()
    tagger = data['tag']
    users_with_tag_list = UserTag.query.filter(UserTag.tag.contains(tagger))
    user_tag=UserTag.query.all()


    users_list = Users.query.all()
    users = []
    print(users_with_tag_list)
    for user in users_list:
        tags = []
        ok=0
        for tag in user_tag:
            if tag.mail == user.mail:
                ok=1
                tags.append({"name":tag.tag,"rating":tag.rating})
        if ok==1:
            users.append({'last_name': user.last_name, 'first_name': user.first_name, 'location': user.location,
                  'age': user.age, 'image': user.image,'tags':tags,'mail':user.mail})

    return jsonify(users)

@main.route('/addTag', methods=['POST'])
def add_tags():

    data = request.get_json()
    mail=data['mail']
    tags=data['tag']
    rating=data['rating']
    new_tag = UserTag(mail=mail,tag=tags,rating=rating)
    db.session.add(new_tag)
    db.session.commit()

    return "Added tag"
@main.route('/getUser',methods=['POST'])
def GetUser():
    data = request.get_json();
    mail = data['mail']
    user = Users.query.filter(UserTag.tag.contains(mail))
    user_tag = UserTag.query.all()

    tags = []
    for tag in user_tag:
        if tag.mail == user.mail:
            tags.append({"name": tag.tag, "rating": tag.rating})
    return {'last_name': user.last_name, 'first_name': user.first_name,'phone':user.phone_number,
            'location': user.location, 'age': user.age, 'image': user.image, 'tags': tags, 'mail': user.mail};


@main.route('/getMessage', methods=['POST'])
def get_messages():
    message_data = request.get_json()
    sender=message_data["sender"]
    receiver=message_data["receiver"]
    message_list = Message.query.filter((Message.mail_user1.contains(sender) & Message.mail_user2.contains(receiver)) | (Message.mail_user1.contains(receiver) & Message.mail_user2.contains(sender)))
    Messages = []
    for message in message_list:
        Messages.append({'id':message.id,'mail1':message.mail_user1,'mail2':message.mail_user2,'who':message.sender,'text':message.message})
    return jsonify(Messages)

@main.route('/addMessage', methods=['POST'])
def add_message():
    message_data = request.get_json()

    new_message = Message(id=message_data["id"],mail_user1=message_data["mail1"],mail_user2=message_data["mail2"],sender=message_data["who"],message=message_data["message"])

    db.session.add(new_message)
    db.session.commit()

    return "ADDED"
@main.route('/users', methods=['GET'])
def profile():
    users_list = Users.query.all()
    users = []
    users_with_tag_list = UserTag.query.all()
    print(users_with_tag_list)
    for user in users_list:
        tags=[]
        for tag in users_with_tag_list:
            if tag.mail == user.mail:
                tags.append({"name":tag.tag,"rating":tag.rating})
        users.append({'last_name' : user.last_name, 'first_name' : user.first_name ,'shareCoins' : user.shareCoins , 'password' : user.password,'tags':tags,'mail' : user.mail, 'location' : user.location, 'age':user.age ,'image': user.image })

    return jsonify(users)

@main.route('/tagsman',methods=['POST'])
def tags():
    users_list = UserTag.query.all()
    users = []
    tags=[]
    for tag in users_list:
            #if tag.mail == user.mail:
        tags.append({tag.tag:tag.rating})
    users.append({'tags' : tags })

    return jsonify(users)

@main.route('/register', methods=['POST'])
def add_user():
    user_data = request.get_json()

    new_user = Users(last_name=user_data['last_name'],first_name=user_data['first_name'],shareCoins=0,password=user_data['password'],
                     mail=user_data['mail'],phone_number=user_data['phone'],location=user_data['location'],age=user_data['age'],image=user_data['image'])

    db.session.add(new_user)
    db.session.commit()

    return "Added"+user_data['last_name']+"\n";
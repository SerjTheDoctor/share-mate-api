from . import db



class Users(db.Model):
    last_name=db.Column(db.String(45))
    first_name=db.Column(db.String(45))
    shareCoins=db.Column(db.Integer)
    password=db.Column(db.String(40))
    mail=db.Column(db.String(40), primary_key=True)
    phone_number=db.Column(db.String(15))
    location=db.Column(db.String(50))
    age=db.Column(db.Integer)
    image=db.Column(db.String(255))

class UserTag(db.Model):
    mail=db.Column(db.String(40),primary_key=True)
    tag=db.Column(db.String(20),primary_key=True)
    rating=db.Column(db.Integer)

class ExternalLinks(db.Model):
    mail=db.Column(db.String(40),primary_key=True)
    linkedin=db.Column(db.String(120))
    github=db.Column(db.String(120))

class Message(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    mail_user1=db.Column(db.String(40))
    mail_user2=db.Column(db.String(40))
    sender=db.Column(db.Integer)
    message=db.Column(db.String(300))







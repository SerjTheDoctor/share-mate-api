from . import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    rating = db.Column(db.Integer)


class Users(db.Model):
    last_name=db.Column(db.String(45))
    first_name=db.Column(db.String(45))
    shareCoins=db.Column(db.Integer)
    password=db.Column(db.String(25))
    mail=db.Column(db.String(40), primary_key=True)
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







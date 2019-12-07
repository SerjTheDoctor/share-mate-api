from . import db, bcrypt

class Client(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    mail = db.Column(db.String(255), unique = True) # = had size 40
    password = db.Column(db.string(40))
    __tablename__= 'Client'


    def __init__(self, mail, password):
        self.mail = mail
        self.active = True
        self.password = Client.hashed_password(password)

    @staticmethod
    def hashed_password(password):
        return bcrypt.generate_password_hash(password).decode("utf-8")

    @staticmethod
    def get_client_with_mail_and_password(mail, password):
        client = Client.query.filter_by(mail = mail).first()
        if client and db.Modelbcrypt.check_password_hash(user.password, password):
            return client
        else:
            return None

class Users(Client):
    #this class inherits from client
    #preffered to make this change to avoid adding a foreign key in order not to duplicate some fields
    last_name=db.Column(db.String(45))
    first_name=db.Column(db.String(45))
    shareCoins=db.Column(db.Integer)
    phone_number=db.Column(db.String(15), unique = True)
    location=db.Column(db.String(50))
    age=db.Column(db.Integer)
    image=db.Column(db.String(255))
    __tablename__ = 'Users'

    def __init__(self, mail, password, last_name, first_name, phone_number, location, age):
        super(Users, self).__init__(mail, password)
        self.last_name = last_name
        self.first_name = first_name
        self.shareCoins = 0
        self.phone_number = phone_number
        self.location = location
        self.age = age


class Tags(db.Model):
    #contains all tags, each tag has a id and nae
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(20), unique = True)
    __tablename__ = 'Tags'

    def __init__(self, name):
        self.name = name


class UserTag(db.Model):
    #changed this table from keeping multiple tags that could be duplicated in the db
    #to keep a foreign key to the tag id
    tagId=db.Column(db.Integer, ForeignKey('Tags.id', ondelete='CASCADE'), nullable=False)
    rating=db.Column(db.Integer)
    mail = db.Column(db.String(255), ForeignKey('Users.mail', ondelete='CASCADE'), nullable=False)
    user = relationship('Users', backref='UserTag')
    tag = relationship('Tags', backref = 'UserTag')
    __tablename = 'UserTag'

    def __init__(self, tagId, rating, mail):
        self.tagId = tagId
        self.rating = rating
        self.mail = mail
        self.user = Users.query.filter_by(mail = mail).first()
        self.tag = Tags.query.filter_by(id = tag)

class ExternalLinks(db.Model):
    mail=db.Column(db.String(255),ForeignKey('Users.mail', ondelete = 'CASCADE'), nullable = False)
    user = relationship('Users', backref='ExternalLinks')
    linkedin=db.Column(db.String(120))
    github=db.Column(db.String(120))
    __tablename__ = 'ExternalLinks'

    def __init__(self, mail, linkedin, github):
        self.mail = mail
        self.linkedin = linkedin
        self.github = github
        self.user = Users.query.filter_by(mail = mail).first()

class Message(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    mail_user1=db.Column(db.String(40),ForeignKey('Users.mail', ondelete = 'CASCADE'), nullable = False)
    mail_user2=db.Column(db.String(40),ForeignKey('Users.mail', ondelete = 'CASCADE'), nullable = False)
    user1 = relationship('Users', backref='ExternalLinks')
    user2 = relationship('Users', backref='ExternalLinks')
    sender=db.Column(db.Integer)
    message=db.Column(db.String(300))
    __tablename__ = 'Message'


    def __init__(self, id, mail1, mail2, sender, message):
        if mail1 == mail2:
            return None

        self.id = id
        self.mail_user1 = mail1
        self.mail_user2 = mail2
        self.sender = sender
        self.message = message
        self.user1 = Users.query.filter_by(mail = mail1).first()
        self.user2 = Users.query.filter_by(mail = mail2).first()
        return self






import sqlite3
from db import db

class UserModel(db.Model): #create mapping between the database and these object
    __tablename__ = 'users'
    #tell it create mapping between the database and these object

    id = db.Column(db.Integer, primary_key=True) # primary_key unique
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self) #this object that we're currently dealing with is self
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

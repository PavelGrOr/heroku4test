from db import db

class StoreModel(db.Model): #create mapping between the database and these object
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)  #non u
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic') #list of items... lazy='dynamic' - don't create object to each item

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]} #query builder that has the ability
                            # to look into the items table, then we can use .all to retrieve all of the items in that table.

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #.query it's something that comes from db.Model
                                                    # SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self) #this object that we're currently dealing with is self
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


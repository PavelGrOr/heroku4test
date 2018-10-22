from db import db

class ItemModel(db.Model): #create mapping between the database and these object
    __tablename__ = 'items'
    #tell it create mapping between the database and these object

    id = db.Column(db.Integer, primary_key=True)  #non u
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2)) #precision - num after decimal point

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name' : self.name, 'price' : self.price}

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


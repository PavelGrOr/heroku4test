from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #is gonna live at the root folder of our project
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # disable flask sqlalchemy tracker to use it from sqlalchemy .
                                        # So this is only changing the extensions behaviours and not the underlying SQLAlchemy behaviour.
app.secret_key = 'jose'
api = Api(app)

'''
    When we initialise the JWT object
    and that is going to use our app,
    the authenticate and the identity functions together
    to allow for authentication of the users.
'''

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

#from db import db  # circular import
#db.init_app(app)
#print('run it')
if __name__ == '__main__':
    print('run it')
    from db import db #circular import
    db.init_app(app) #It links together your Flask app with SQLAlchemy.
    app.run(port=5000, debug=True)

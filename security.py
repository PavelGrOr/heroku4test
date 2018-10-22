from models.user import UserModel
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password): #safe_str_cmp - safe compare, decide different problems with diff text encoding (askii, unicode)
        return user


def identity(payload): #payload - JWT
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
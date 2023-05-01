from sys import path
from os.path import join
from os import getenv

path.append(join(getenv('APP_PATH')))

from src.api.rest.model.user import User

class UserController:
    def get(self, id):
        print(type(id))
        if type(id) == int:
            print(id)
            return User().get(id)
        
        return User().me()

    def getAll(self):
        return User().all()

    def create(self, user):
        return User().create(user)
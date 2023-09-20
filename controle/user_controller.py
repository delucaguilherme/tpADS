from modelo.user import User
from persistencia.user_persistence import User_persistence

class User_controller:
    #def __init__(self): #controller precisa do construtor?

    def checkPassword(password, confirmed_password):
        if (password == confirmed_password):
            return 1
        return 0
    
    def searchEmail(email, userList):
        for user in userList:
            if user.email == email:
                return 0
        return 1
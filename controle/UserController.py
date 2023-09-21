from .modelo.user import User

# from persistencia.user_persistence import User_persistence
"""
class User_controller:
    #def __init__(self): #controller precisa do construtor?

    def checkPassword(password, confirmed_password):
        if (password == confirmed_password):
            return 1
        return 0
    
    def checkEmail(email, userList):
        for user in userList:
            if user.email == email:
                return 0
        return 1
"""

class UserController:
    def registerUser(self, name, email, password, password_confirm):
        self.checkPassword(password, password_confirm)
        # self.checkEmail(), sem classe persistência é impossível verificar a existência
        user = User(name, email, password)
        print(user)
        # Persistencia.persistirUsuario(), sem classe persistência é impossivel persistir usuário

    def logUser(self, email, password):
        # consultar a existência do usuário e dar acesso as suas informações 
        print(done)

    def checkPassword():

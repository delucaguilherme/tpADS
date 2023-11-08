class User:
    def __init__(self, email="", senha="", tipo=0):
        self.email = email
        self.senha = senha
        self.tipo = tipo

    def __str__(self):
        return self.email + " " + self.senha + " " + str(self.tipo)
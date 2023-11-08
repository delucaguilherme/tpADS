class User:
    def __init__(self, email="", password="", type=0):
        self.email = email
        self.password = password
        self.type = type

    def __str__(self):
        return self.email + " " + self.senha + " " + str(self.tipo)
class User:
    def __init__(self, name, email, password, address, permission = 0):
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.permission = permission

    def __str__(self):
        return f"{self.name}, {self.email}, {self.password}, {self.address}"

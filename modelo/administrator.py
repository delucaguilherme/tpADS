import user

class Administrator(user.User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.permission = 1

    def __str__(self):
        return f"{self.username}, {self.password}, {self.permission}"
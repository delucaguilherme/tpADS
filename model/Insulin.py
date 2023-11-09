class Insulin:
    def __init__(self, quantity, type, date, time, meal_type, meal_time, usuario):
        self.quantity = quantity
        self.type = type
        self.date = date
        self.time = time
        self.meal_type = meal_type
        self.meal_time = meal_time
        self.usuario = usuario

    def __str__(self):
        return str(self.quantity) + " " + self.type + " " + self.date + " " + self.time + " " + self.meal_type + " " + self.meal_time + " " + self.usuario
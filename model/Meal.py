class Meal:
    def __init__(self, carbohydrates, date, time, meal_type, usuario):
        self.carbohydrates = carbohydrates
        self.date = date
        self.time = time
        self.meal_type = meal_type
        self.usuario = usuario

    def __str__(self):
        return self.carbohydrates+ " " + self.date + " " + self.time + " " + self.meal_type + " " + self.usuario
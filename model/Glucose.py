class Glucose:
    def __init__(self, sugar_level, date, time, meal_type, meal_time):
        self.sugar_level = sugar_level
        self.date = date
        self.time = time
        self.meal_type = meal_type
        self.meal_time = meal_time

    def __str__(self):
        return str(self.sugar_level) + " " + self.date + " " + self.time + " " + self.meal_tipe + " " + self.meal_time
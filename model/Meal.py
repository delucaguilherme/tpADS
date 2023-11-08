class Meal:
    def __init__(self, carboidrates, date, time, meal):
        self.carboidrates = carboidrates
        self.date = date
        self.time = time
        self.meal = meal

    def __str__(self):
        return self.carboidrates+ " " + self.date + " " + self.time + " " + self.meal
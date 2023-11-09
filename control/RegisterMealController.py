from model.Meal import Meal
from persistance.MealPersistance import MealPersistance

class RegisterMealController:
    @classmethod
    def register_meal(self, screen, email):
        carbohydrates = screen.carbohydrates.get()
        date = screen.date.get()
        time = screen.time.get()
        meal_type = screen.meal_type.get()

        new_meal = Meal(carbohydrates, date, time, meal_type, email)

        return MealPersistance.insert_meal(new_meal)
from view.RegisterGlucoseScreen import RegisterGlucoseScreen
from view.RegisterMealScreen import RegisterMealScreen

class UserScreenController:
    @classmethod
    def open_register_glucose_screen(self, ):
        RegisterGlucoseScreen()

    @classmethod
    def open_register_meal_screen(self):
        RegisterMealScreen()
    
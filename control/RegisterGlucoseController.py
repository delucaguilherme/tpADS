from model.Glucose import Glucose
from persistance.GlucosePersistance import GlucosePersistance


class RegisterGlucoseController:
    @classmethod
    def register_glucose(self, screen):
        root = screen.get_root()

        sugar_level = screen.sugar_level.get()
        date = screen.date.get()
        time = screen.time.get()
        meal_type = screen.meal_type.get()
        meal_time = screen.radio_var.get()

        new_gluscose = Glucose(sugar_level, date, time, meal_type, meal_time)
        
        return  GlucosePersistance.insert_glucose(new_gluscose)

        
from customtkinter import *
from model.Glucose import Glucose
from persistance.GlucosePersistance import GlucosePersistance

class RegisterGlucoseController:
    @classmethod
    def register_glucose(self, screen, email):
        root = screen.get_root()
        
        sugar_level = screen.sugar_level.get()
        date = screen.date.get()
        time = screen.time.get()
        meal_type = screen.meal_type.get()
        meal_time = screen.radio_var.get()

        new_glucose = Glucose(sugar_level, date, time, meal_type, meal_time, email)
        result = GlucosePersistance.insertGlucose(new_glucose)

        if result == "Índice glicêmico registrado com sucesso!":
            success = CTkLabel(
                master=root,
                text="Índice glicêmico registrado com sucesso!",
                text_color="green",
                font=("Segeo UI", 16, "bold")
            )
            success.place(relx=0.5, rely=0.62, anchor=CENTER)
        else:
            error = CTkLabel(
                master=root,
                text= f'Erro ao registrar índice glicêmico:\n{result}',
                text_color="red",
                font=("Segeo UI", 16, "bold")
            )
            error.place(relx=0.5, rely=0.62, anchor=CENTER)
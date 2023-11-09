from customtkinter import *
from model.Insulin import Insulin
from persistance.InsulinPersistance import InsulinPersistance

class RegisterInsulinController:
    @classmethod
    def register_insulin(self, screen, email):
        root = screen.get_root()
        
        quantity = screen.quantity.get()
        type = screen.type.get()
        date = screen.date.get()
        time = screen.time.get()
        meal_type = screen.meal_type.get()
        meal_time = screen.radio_var.get()

        new_insulin = Insulin(quantity, type, date, time, meal_type, meal_time, email)
        result = InsulinPersistance.insertInsulin(new_insulin)

        if result == "Aplicação de insulina registrada com sucesso!":
            success = CTkLabel(
                master=root,
                text="Aplicação de insulina registrada com sucesso!",
                text_color="green",
                font=("Segeo UI", 16, "bold")
            )
            success.place(relx=0.5, rely=0.68, anchor=CENTER)
        else:
            error = CTkLabel(
                master=root,
                text= f'Erro ao registrar aplicação de insulina:\n{result}',
                text_color="red",
                font=("Segeo UI", 16, "bold")
            )
            error.place(relx=0.5, rely=0.68, anchor=CENTER)
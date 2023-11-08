from customtkinter import *
from control.UserScreenController import UserScreenController as Controller

class UserScreen:
    def __init__(self):
        
        #configuração da janela
        root = CTk()
        root.title("Menu de Usuário")
        root.geometry("800x600")
        root.resizable(False, False)
        set_appearance_mode("light")

        glucose_bttn = CTkButton(master=root,
                                  text='Cadastrar Glicose', 
                                  font=('Segeo UI', 16),
                                  width=210, height=60,
                                  command=lambda: [Controller.open_register_glucose_screen()])
        glucose_bttn.place(relx=0.5, rely=0.20, anchor=CENTER)

        meal_bttn = CTkButton(master=root,
                                  text='Cadastrar Meal', 
                                  font=('Segeo UI', 16),
                                  width=210, height=60,
                                  command=lambda: [Controller.open_register_meal_screen()])
        meal_bttn.place(relx=0.5, rely=0.35, anchor=CENTER)

        root.mainloop()
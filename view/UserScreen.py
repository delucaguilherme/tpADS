from customtkinter import *
from control.UserScreenController import UserScreenController as Controller

class UserScreen:
    def __init__(self, email):
        
        #configuração da janela
        self.root = CTk()
        self.root.title("Menu de Usuário")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        set_appearance_mode("light")

        heading = CTkLabel(
            master=self.root, 
            text='Menu do Usuário', 
            font=('Segoe UI', 26, 'bold')
        )
        heading.place(relx=0.5, rely=0.20, anchor=CENTER)

        register_glucose_bttn = CTkButton(
            master=self.root, 
            text='Registrar Índice Glicêmico',
            font=('Segoe UI', 16),
            width=210, height=30, 
            command=lambda: [Controller.open_register_glucose(email)]
        )
        register_glucose_bttn.place(relx=0.5, rely=0.34, anchor=CENTER)

        list_glucose_bttn = CTkButton(
            master=self.root, 
            text='Listar Índice Glicêmico',
            font=('Segoe UI', 16),
            width=210, height=30, 
            command=lambda: [Controller.open_list_glucose(email)]
        )
        list_glucose_bttn.place(relx=0.5, rely=0.40, anchor=CENTER)

        register_insulin_bttn = CTkButton(
            master=self.root, 
            text='Registrar Aplicação de Insulina',
            font=('Segoe UI', 16),
            width=210, height=30, 
            command=lambda: [Controller.open_register_insulin(email)]
        )
        register_insulin_bttn.place(relx=0.5, rely=0.46, anchor=CENTER)

        register_meal_bttn = CTkButton(
            master=self.root, 
            text='Registrar Refeição',
            font=('Segoe UI', 16),
            width=210, height=30, 
            command=lambda: [Controller.open_register_meal(email)]
        )
        register_meal_bttn.place(relx=0.5, rely=0.52, anchor=CENTER)

        self.root.mainloop()
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

        signup_bttn = CTkButton(
            master=self.root, 
            text='Registrar Índice Glicêmico',
            font=('Segoe UI', 16),
            width=210, height=30, 
            command=lambda: [Controller.open_register_glucose(email)]
        )
        signup_bttn.place(relx=0.5, rely=0.34, anchor=CENTER)

        self.root.mainloop()
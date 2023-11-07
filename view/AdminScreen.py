from customtkinter import *
from control.AdminScreenController import AdminScreenController as Controller

class AdminScreen:
    def __init__(self):
        
        #configuração da janela
        root = CTk()
        root.title("Menu de Administrador")
        root.geometry("800x600")
        root.resizable(False, False)
        set_appearance_mode("light")

        register_bttn = CTkButton(master=root,
                                  text='Cadastrar Administrador', 
                                  font=('Segeo UI', 16),
                                  width=210, height=60,
                                  command=lambda: [Controller.open_register_admin_screen()])
        register_bttn.place(relx=0.5, rely=0.20, anchor=CENTER)

        delete_bttn = CTkButton(master=root, 
                                text='Excluir Usuário', 
                                font=('Segeo UI', 16),
                                width=210, height=60, 
                                command=lambda: [Controller.open_delete_screen()])
        delete_bttn.place(relx=0.5, rely=0.35, anchor=CENTER)

        root.mainloop()
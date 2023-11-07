from customtkinter import *
from tkinter import *
import os
from PIL import Image

from control.HomeScreenController import HomeScreenController as Controller

class HomeScreen: 
    def __init__(self):
        #configuração da janela
        self.root = CTk()
        self.root.title("GlicMed")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        set_appearance_mode("light")
    
        # logo da empresa
        icon_glicmed = PhotoImage(file=os.path.join(os.path.dirname(__file__), '../icons/GlicMed_icon.png'))
        text_glicmed = PhotoImage(file=os.path.join(os.path.dirname(__file__), '../icons/GlicMed_text.png'))

        glicmed_icon = CTkLabel(master=self.root, image=icon_glicmed, text="")
        glicmed_icon.place(relx=0.405, rely=0.215, anchor=CENTER)

        glicmed_label = CTkLabel(master=self.root, image=text_glicmed, text="")
        glicmed_label.place(relx=0.555, rely=0.23, anchor=CENTER)

        # caixas de texto
        self.email = CTkEntry(
            master=self.root, 
            width=210, height=30,
            placeholder_text='e-mail',
            corner_radius=9
        )
        self.email.place(relx=0.5, rely=0.39, anchor=CENTER)

        self.password = CTkEntry(
            master=self.root,
            width=210, height=30,
            placeholder_text='senha',
            show='*',
            corner_radius=6
        )
        self.password.place(relx=0.5, rely=0.45, anchor=CENTER)

        # botões
        signin_bttn = CTkButton(master=self.root, 
                                text='Entre', 
                                font=('Segeo UI', 16),
                                width=210, height=30,
                                command=lambda: [Controller.signin_user(self)]) #esperando tela de usuário
        signin_bttn.place(relx=0.5, rely=0.53, anchor=CENTER)

        alternative = CTkLabel(master=self.root, text="ou", font=('Segoe UI', 17))
        alternative.place(relx=0.5, rely=0.579, anchor=CENTER)

        signup_bttn = CTkButton(master=self.root,
                                text='Cadastre-se',
                                font=('Segoe UI', 16),
                                width=210, height=30, 
                                command=lambda: [Controller.open_register_user_screen()])
        signup_bttn.place(relx=0.50, rely=0.63, anchor=CENTER)
        
        self.root.mainloop()

    def get_root(self):
        return self.root
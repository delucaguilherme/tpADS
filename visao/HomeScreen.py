import customtkinter as ctk
from tkinter import *
from .RegisterUser import *
from .UserSignin import UserSignin
import os
from PIL import Image

ctk.set_appearance_mode("Light") # Other: "Light", "System" (only macOS)

class HomeScreen:
    def __init__(self, root=None):
        self.root = root
        self.root.title('GlicMed')
        self.root.geometry('800x600')
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)
    
        
        icon_glicmed = PhotoImage(file=os.path.join(os.path.dirname(__file__), '../icons/GlicMed_icon.png'))
        text_glicmed = PhotoImage(file=os.path.join(os.path.dirname(__file__), '../icons/GlicMed_text.png'))
        
        glicmed_icon = ctk.CTkLabel(root, image=icon_glicmed, text="")
        glicmed_icon.place(relx=0.41, rely=0.2, anchor=ctk.CENTER)

        glicmed_label = ctk.CTkLabel(root, image=text_glicmed, text="")
        glicmed_label.place(relx=0.56, rely=0.23, anchor=ctk.CENTER)

        email = ctk.CTkEntry(master=root,
                               width=210,
                               height=26,
                               placeholder_text='E-mail',
                               corner_radius=9)
        email.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

        password = ctk.CTkEntry(master=root,
                               width=210,
                               height=26,
                               placeholder_text='Senha',
                               show='*',
                               corner_radius=9)
        password.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        userBttn = ctk.CTkButton(root,
                                 text='Login',
                                 font=('Segoe UI', 16), 
                                 width=210, height=60,)
        userBttn.place(relx=0.5, rely=0.63, anchor=ctk.CENTER)

        loginBttn = ctk.CTkButton(root,
                                  text='Cadastrar Usuário',
                                  font=('Segoe UI', 16),
                                  width=210, height=60,
                                  command=lambda: [HomeScreen.show_register_user(self)])
        loginBttn.place(relx=0.5, rely=0.76, anchor=ctk.CENTER)

    def show_register_user(self):
        RegisterUser()

    def show_login(self):
        UserSignin(self.root)

    def show_home_screen(self):
        self.root.mainloop()

    def close_window(self):
        self.root.after(5000,  self.root.destroy())
       

if __name__ == "__main__":
    home_screen = HomeScreen()
    home_screen.show_home_screen()

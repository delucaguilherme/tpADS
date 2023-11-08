import customtkinter
from tkinter import *
from .RegisterUser import *
from .UserSignin import UserSignin
from .AdmScreen import AdmScreen
import os


ctk.set_appearance_mode("Light")  # Other: "Light", "System" (only macOS)

class HomeScreen:
    def __init__(self, root=None):
        self.root = customtkinter.CTk()

        icon_glicmed = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), '../icons/GlicMed_icon.png'))
        text_glicmed = PhotoImage(file=os.path.join(
            os.path.dirname(__file__), '../icons/GlicMed_text.png'))

        glicmed_icon = ctk.CTkLabel(root, image=icon_glicmed, text="")
        glicmed_icon.place(relx=0.41, rely=0.2, anchor=ctk.CENTER)

        glicmed_label = ctk.CTkLabel(root, image=text_glicmed, text="")
        glicmed_label.place(relx=0.56, rely=0.23, anchor=ctk.CENTER)

        self.email = ctk.CTkEntry(master=root,
                                  width=210,
                                  height=26,
                                  placeholder_text='E-mail',
                                  corner_radius=9)
        self.email.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

        self.password = ctk.CTkEntry(master=root,
                                     width=210,
                                     height=26,
                                     placeholder_text='Senha',
                                     show='*',
                                     corner_radius=9)
        self.password.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        userBttn = ctk.CTkButton(root,
                                 text='Login',
                                 font=('Segoe UI', 16),
                                 width=210, height=60,
                                 command=lambda: [HomeScreen.userSignin(self)])
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
        self.root.after(5000, self.root.destroy())

    def userSignin(self):
        user = Usuarios()
        email = self.email.get()
        password = self.password.get()
        resultado = user.selectUser(email, password)

        if resultado == 0:
            UserSignin()
        elif resultado == 1:
            AdmScreen()
        elif resultado == "Usuário ou senha incorretos.":
            wrong = ctk.CTkLabel(self.root, text=f'Usuário ou senha incorretos!', text_color='red', font=('Segoe UI', 16, 'bold'))
            wrong.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)
        else: 
            error = ctk.CTkLabel(self.root, text= f'Erro ao logar: \n{resultado}', text_color='red', font=('Segoe UI', 16, 'bold'))
            error.place(relx=0.5, rely=0.52, anchor=ctk.CENTER)

if __name__ == "__main__":
    home_screen = HomeScreen()
    home_screen.show_home_screen()

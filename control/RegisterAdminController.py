from customtkinter import *
from model.User import User
from persistance.UserPersistance import UserPersistance

class RegisterAdminController:
    @classmethod
    def register_user(self, screen):
        email = screen.email.get()
        password = screen.password.get()
        password_confirm = screen.password_confirm.get()

        if password == password_confirm:
            new_user = User(email, password, 1)
            result = UserPersistance.insertUser(new_user)

            if result == "Usuário cadastrado com sucesso!":
                sucess = CTkLabel(
                    master=screen.root,
                    text="Administrador cadastrado com sucesso!",
                    text_color="green", 
                    font=("Segeo UI", 16, "bold")
                )
                sucess.place(relx=0.5, rely=0.65, anchor=CENTER)
            else:
                error = CTkLabel(
                    master=screen.root, 
                    text= f'Erro ao cadastrar administrador:\n{result}', 
                    text_color='red', 
                    font=('Segoe UI', 16, 'bold')
                )
                error.place(relx=0.5, rely=0.65, anchor=CENTER)
        else:
            mismatch = CTkLabel(master=screen.root, text= f'As senhas não coincidem.', text_color='red', font=('Segoe UI', 16, 'bold'))
            mismatch.place(relx=0.5, rely=0.52, anchor=CENTER)
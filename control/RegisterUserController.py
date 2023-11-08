from customtkinter import *
from model.User import User
from persistance.UserPersistance import UserPersistance

class RegisterUserController:
    @classmethod
    def register_user(self, screen):
        root = screen.get_root()
        
        email = screen.email.get()
        password = screen.password.get()
        password_confirm = screen.password_confirm.get()

        if password == password_confirm:
            new_user = User(email, password)
            result = UserPersistance.insertUser(new_user)

            if result == "Usuário cadastrado com sucesso!":
                sucess = CTkLabel(
                    master=root,
                    text="Usuário cadastrado com sucesso!",
                    text_color="green", 
                    font=("Segeo UI", 16, "bold")
                )
                sucess.place(relx=0.5, rely=0.5, anchor=CENTER)
            else:
                error = CTkLabel(
                    master=root, 
                    text= f'Erro ao cadastrar usuário:\n{result}', 
                    text_color='red', 
                    font=('Segoe UI', 16, 'bold')
                )
                error.place(relx=0.5, rely=0.5, anchor=CENTER)
        else:
            mismatch = CTkLabel(master=root, text= f'As senhas não coincidem.', text_color='red', font=('Segoe UI', 16, 'bold'))
            mismatch.place(relx=0.5, rely=0.52, anchor=CENTER)
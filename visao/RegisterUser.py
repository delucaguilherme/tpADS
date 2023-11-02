from tkinter import Tk, Entry, Label, Button, StringVar
import customtkinter as ctk
from .User import Usuarios

class RegisterUser:
    def __init__(self):
        
        self.root = Tk()
        self.root.title('GlicMed')
        self.root.geometry('800x600')
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)
        
        heading = ctk.CTkLabel(self.root, text='Preencha as informações', text_color='#57a1f8', font=('Segoe UI', 26, 'bold'))
        heading.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

        self.email = ctk.CTkEntry(self.root, placeholder_text="Email")
        self.email.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

        self.password = ctk.CTkEntry(self.root, show="*", placeholder_text="Senha")
        self.password.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

        self.password_confirm = ctk.CTkEntry(self.root, show="*", placeholder_text="Confirmar Senha")
        self.password_confirm.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

        loginBttn = ctk.CTkButton(self.root,
                                  text='Cadastrar Usuário',
                                  font=('Segoe UI', 16),
                                  width=210, height=60,
                                  command=lambda: [self.userSignup()])
        loginBttn.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)
        
        returnBttn = ctk.CTkButton(self.root,
                                   text='Voltar para Login',
                                   font=('Segoe UI', 12),
                                   width=100, height=40,
                                   command=self.root.destroy)
        returnBttn.place(relx=0.2, rely=0.9, anchor=ctk.CENTER)

    def userSignup(self):
        email = self.email.get() 
        password = self.password.get()
        password_confirm = self.password_confirm.get()

        if password == password_confirm:
            novo_usuario = Usuarios(email=email, senha=password)  
            resultado = novo_usuario.insertUser()
            
            if resultado == "Usuário cadastrado com sucesso!":
                sucess = ctk.CTkLabel(self.root, text='Usuário cadastrado com sucesso!', text_color='green', font=('Segoe UI', 16, 'bold'))
                sucess.place(relx=0.5, rely=0.52, anchor=ctk.CENTER)
                print("Usuário cadastrado com sucesso!")
            else:
                error = ctk.CTkLabel(self.root, text= f'Erro ao cadastrar usuário:\n{resultado}', text_color='red', font=('Segoe UI', 16, 'bold'))
                error.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        else:
            wrong = ctk.CTkLabel(self.root, text= f'As senhas não coincidem.', text_color='red', font=('Segoe UI', 16, 'bold'))
            wrong.place(relx=0.5, rely=0.52, anchor=ctk.CENTER)

class UserSignin:
    def __init__(self, root):
        
        print(f"{self.email}, {self.password}")


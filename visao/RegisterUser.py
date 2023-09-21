from tkinter import *
from visao.PlaceholderEntry import PlaceholderEntry
from .User import Usuarios

class RegisterUser:
    def __init__(self):
        root = Tk()
        root.title('GlicMed')
        root.geometry('800x600')
        root.configure(bg="#fff")
        root.resizable(False, False)

        heading = Label(root, text='Preencha as informações', fg='#57a1f8', bg='white', font=('Segoe UI', 16, 'bold'))
        heading.place(x=250, y=10)

        self.name = PlaceholderEntry(root, fg='black', border=1, placeholder="Nome Completo")
        self.name.place(x=250, y=50, width=300, height=30)

        self.email = PlaceholderEntry(root, fg='black', border=1, placeholder="Email")
        self.email.place(x=250, y=100, width=300, height=30)

        self.usuario = PlaceholderEntry(root, fg='black', border=1, placeholder="Nome de Usuário")  # Corrigi o texto do placeholder
        self.usuario.place(x=250, y=150, width=300, height=30)

        self.password = PlaceholderEntry(root, password=1, fg='black', border=1, placeholder="Senha")
        self.password.place(x=250, y=200, width=300, height=30)

        self.password_confirm = PlaceholderEntry(root, password=1, fg='black', border=1, placeholder="Confirmar Senha")
        self.password_confirm.place(x=250, y=250, width=300, height=30)

        cmmnUserBttn = Button(root, text='Cadastrar', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 14, 'bold'), command=lambda :[self.userSignup(), root.destroy()])
        cmmnUserBttn.place(x=250, y=320, width=300, height=60)

    def userSignup(self):
        name = self.name.get()
        email = self.email.get()
        usuario = self.usuario.get()  # Usei a variável 'usuario' para obter o nome de usuário
        password = self.password.get()
        password_confirm = self.password_confirm.get()

        if password == password_confirm:
            # Crie uma instância de Usuarios com as informações inseridas pelo usuário
            novo_usuario = Usuarios(nome=name, email=email, usuario=usuario, senha=password)  # Corrigi o uso de 'usuario'

            # Insira o novo usuário no banco de dados
            resultado = novo_usuario.insertUser()
            
            if resultado == "Usuário cadastrado com sucesso!":
                print("Usuário cadastrado com sucesso!")
            else:
                print("Erro ao cadastrar usuário:", resultado)
        else:
            print("As senhas não coincidem.")        
from tkinter import *
from visao.PlaceholderEntry import PlaceholderEntry

class RegisterUser:
    def __init__(self, parent=None):
        frame = Frame(parent, width=400, height=400, bg='white')
        frame.place(x=200, y=100)

        heading = Label(frame, text='Preencha as informações', fg='#57a1f8', bg='white', font=('Segoe UI', 16, 'bold'))
        heading.place(x=50, y = 10)

        name = PlaceholderEntry(frame, fg='black', border=1, placeholder= "Nome Completo")
        name.place(x=50, y=50, width=300, height=30)

        email = PlaceholderEntry(frame, fg='black', border=1, placeholder= "Email")
        email.place(x=50, y=100, width=300, height=30)

        password = PlaceholderEntry(frame, password=1, fg='black', border=1, placeholder="Senha") 
        password.place(x=50, y=150, width=300, height=30)

        password_confirm = PlaceholderEntry(frame, password=1, fg='black', border=1, placeholder="Confirmar Senha") 
        password_confirm.place(x=50, y=200, width=300, height=30)

        cmmnUserBttn = Button(frame, text='Entrar', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 14, 'bold'), command=lambda: [frame.destroy(), self.userSignup(parent)])
        cmmnUserBttn.place(x = 50, y=280, width=300, height=60)

    def userSignup(self, parent):
        print("done")

from tkinter import *
from visao.PlaceholderEntry import PlaceholderEntry

class UserSignin:
    def __init__(self, parent=None):
        frame = Frame(parent, width=400, height=400, bg='white')
        frame.place(x=200, y=100)

        heading = Label(frame, text='Entre como Administrador', fg='#57a1f8', bg='white', font=('Segoe UI', 16, 'bold'))
        heading.place(x=50, y = 10)

        username = PlaceholderEntry(frame, fg='black', border=1, placeholder="Nome de Usuário") 
        username.place(x=50, y=50, width=300, height=60)
        
        password = PlaceholderEntry(frame, fg='black', border=1, placeholder="Senha") 
        password.place(x=50, y=140, width=300, height=60)

        cmmnUserBttn = Button(frame, text='Entrar', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 14, 'bold'), command=lambda: [frame.destroy(), self.userSignin(parent)])
        cmmnUserBttn.place(x = 50, y=220, width=300, height=60)

    def userSignin(self, parent):
        print("done")
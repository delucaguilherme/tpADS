from tkinter import *
from visao.PlaceholderEntry import PlaceholderEntry

class UserSignin:
    def __init__(self, parent=None):
        frame = Frame(parent, width=400, height=400, bg='white')
        frame.place(x=200, y=100)

        heading = Label(frame, text='Entrar', fg='#57a1f8', bg='white', font=('Segoe UI', 16, 'bold'))
        heading.place(x=50, y = 10)

        email = PlaceholderEntry(frame, fg='black', border=1, placeholder="e-mail") 
        email.place(x=50, y=50, width=300, height=60)
        
        password = PlaceholderEntry(frame, fg='black', border=1, placeholder="senha") 
        password.place(x=50, y=140, width=300, height=60)

        cmmnUserBttn = Button(frame, text='Entrar', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 14, 'bold'), command=lambda: [self.userSignin(parent, email.get(), password.get()), frame.destroy()])
        cmmnUserBttn.place(x = 50, y=220, width=300, height=60)

    def userSignin(self, parent, email, password):
        print(f"{email}, {password}")
        print("done")
from tkinter import *
from .userMenu import *
from .adminMenu import *

class UserType:
    def __init__(self, parent):
        frame = Frame(parent, width=800, height=400, bg='white')
        frame.place(x=200, y=100)

        userBttn = Button(frame, text='Usuário', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 13, 'bold'), command=lambda: [frame.destroy(), self.userMenu(parent)])
        userBttn.place(x = 50, y=50, width=300, height=60)

        adminBttn = Button(frame, text='Administrador', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 13, 'bold'), command=lambda: [frame.destroy(), self.adminMenu(parent)])
        adminBttn.place(x=50, y=130, width=300, height=60)

    def userMenu(self, parent):
        UserMenu(parent)

    def adminMenu(self, parent):
        AdminMenu(parent)
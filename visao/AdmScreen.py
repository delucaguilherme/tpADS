from tkinter import *
from .RemoveUser import *

class AdmScreen:
    def __init__(self, parent):
        frame = Frame(parent, width=400, height=400, bg='red')
        frame.place(x=200, y=100)

        userBttn = Button(frame, text='Excluir Usuário', bg='#57a1f8', fg='white', border=0, font=('Segoe UI', 13, 'bold'), command=lambda: [frame.destroy(), self.removeUser(parent)])
        userBttn.place(x = 50, y=100, width=300, height=60)

    def removeUser(self, parent):
        RemoveUser(parent)